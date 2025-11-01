from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from scipy.cluster.hierarchy import centroid
from sklearn.cluster import KMeans
import numpy as np
from flask import Flask, render_template_string, send_file
from project_detail.connectors.connector import Connector


conn = Connector(database="sakila")
conn.connect()
app = Flask(__name__)

#cau1:==================================================================================================================
def get_customers_by_film():
    db = conn.connect()  # Lấy connection từ class Connector
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT 
        f.film_id,
        f.title AS film_title,
        COUNT(DISTINCT c.customer_id) AS total_customers,
        GROUP_CONCAT(DISTINCT CONCAT(c.first_name, ' ', c.last_name) SEPARATOR ', ') AS customers
    FROM film f
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    JOIN customer c ON c.customer_id = r.customer_id
    GROUP BY f.film_id, f.title
    ORDER BY total_customers DESC;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    df = pd.DataFrame(result)
    print(df.to_string(index=False))

    cursor.close()
    # Không close db để Flask còn dùng
    return df
#get_customers_by_film()

#cau2:==================================================================================================================
def get_customers_by_category():
    db = conn.connect()
    cursor = db.cursor(dictionary=True)

    query = """
    SELECT 
        cat.name AS category_name,
        COUNT(DISTINCT c.customer_id) AS total_customers,
        GROUP_CONCAT(DISTINCT CONCAT(c.first_name, ' ', c.last_name) SEPARATOR ', ') AS customers
    FROM category cat
    JOIN film_category fc ON cat.category_id = fc.category_id
    JOIN film f ON fc.film_id = f.film_id
    JOIN inventory i ON f.film_id = i.film_id
    JOIN rental r ON r.inventory_id = i.inventory_id
    JOIN customer c ON c.customer_id = r.customer_id
    GROUP BY cat.category_id, cat.name
    ORDER BY total_customers DESC;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    df = pd.DataFrame(result)
    print(df.to_string(index=False))

    cursor.close()
    return df
#get_customers_by_category()

#cau3:==================================================================================================================
def get_customer_features():
    db = conn.connect()
    cursor = db.cursor(dictionary=True)

    sql = """
    SELECT 
        c.customer_id,
        CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
        COUNT(r.rental_id) AS total_rentals,
        COUNT(DISTINCT i.film_id) AS unique_films,
        COUNT(DISTINCT fc.category_id) AS unique_categories,
        AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_duration,
        DATEDIFF(NOW(), MAX(r.rental_date)) AS recency_days
    FROM customer c
    JOIN rental r ON c.customer_id = r.customer_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film_category fc ON i.film_id = fc.film_id
    GROUP BY c.customer_id;
    """

    cursor.execute(sql)
    data = cursor.fetchall()
    df = pd.DataFrame(data).fillna(0)

    cursor.close()
    return df

df = get_customer_features()

features = [
    "total_rentals",
    "unique_films",
    "unique_categories",
    "avg_rental_duration",
    "recency_days"
]

def elbowMethod(df, features):
    X = df[features].values
    inertia = []
    for k in range(1, 11):
        model = KMeans(n_clusters=k, init="k-means++", max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)

    plt.plot(range(1, 11), inertia, "o-")
    plt.title("Elbow Method")
    plt.xlabel("Clusters")
    plt.ylabel("Inertia")
    plt.show()

# elbowMethod(df, features)

def runKMeans(df, features, k):
    X = df[features].values
    model = KMeans(n_clusters=k, init="k-means++", max_iter=500, random_state=42)
    labels = model.fit_predict(X)
    df["cluster"] = labels
    return df, model.cluster_centers_

cluster_num = 5     # đổi số cụm
df, centers = runKMeans(df, features, cluster_num)

def printCustomersPerCluster(df):
    for c in sorted(df["cluster"].unique()):
        print(f"\nCLUSTER {c}")
        print(df[df["cluster"] == c][["customer_name"] + features])

# printCustomersPerCluster(df)

def visualize2D(df):
    plt.figure(figsize=(8,6))
    plt.scatter(df["total_rentals"], df["unique_films"], c=df["cluster"], s=60)
    plt.title("Customer Clusters (2D)")
    plt.xlabel("Total Rentals")
    plt.ylabel("Unique Films Watched")

    for i in range(0, len(df), max(1, len(df)//40)):
        plt.annotate(df.iloc[i]["customer_name"],
                     (df.iloc[i]["total_rentals"], df.iloc[i]["unique_films"]),
                      fontsize=8)
    plt.show()

#visualize2D(df)

def visualize3D(df):
    fig = px.scatter_3d(
        df, x="total_rentals", y="unique_films", z="unique_categories",
        color="cluster", hover_data=["customer_name"]
    )
    fig.show()

#visualize3D(df)

@app.route("/")
def show_clusters():
    html = ""
    for c in sorted(df["cluster"].unique()):
        html += f"<h2>Cluster {c}</h2>"
        cluster_df = df[df["cluster"] == c]
        html += cluster_df.to_html(index=False, classes="table table-bordered")

    page = f"""
    <html>
    <head>
        <title>Sakila Customer Clustering</title>
        <link rel="stylesheet" 
        href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    </head>
    <body class="p-4">
        <h1>Sakila Customer Clustering (k = {cluster_num})</h1>
        {html}
        <a href="/download" class="btn btn-success mt-3">Download Excel</a>
    </body>
    </html>
    """
    return render_template_string(page)

@app.route("/download")
def download_excel():
    filename = "sakila_customer_clusters.xlsx"
    df.to_excel(filename, index=False)
    return send_file(filename, as_attachment=True)

#if __name__ == "__main__":
    #app.run(debug=True)