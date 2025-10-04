import sqlite3
import pandas as pd

def top_invoices_in_range(conn, a, b, n):
    query = f"""
        SELECT InvoiceId, CustomerId, Total
        FROM Invoice
        WHERE Total BETWEEN {a} AND {b}
        ORDER BY Total DESC
        LIMIT {n};
    """
    return pd.read_sql_query(query, conn)

def top_customers_by_invoice_count(conn, n):
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName,
               COUNT(i.InvoiceId) AS InvoiceCount
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY InvoiceCount DESC
        LIMIT {n};
    """
    return pd.read_sql_query(query, conn)

def top_customers_by_invoice_total(conn, n):
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName,
               SUM(i.Total) AS TotalAmount
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY TotalAmount DESC
        LIMIT {n};
    """
    return pd.read_sql_query(query, conn)


try:
    sqliteConnection = sqlite3.connect("../databases/Chinook_Sqlite.sqlite")
    print("DB Init")

    print("\nTOP 5 Invoice trong khoảng 5 -> 15:")
    print(top_invoices_in_range(sqliteConnection, 5, 15, 5))

    print("\nTOP 5 khách hàng có nhiều Invoice nhất:")
    print(top_customers_by_invoice_count(sqliteConnection, 5))

    print("\nTOP 5 khách hàng có tổng Invoice cao nhất:")
    print(top_customers_by_invoice_total(sqliteConnection, 5))

except sqlite3.Error as error:
    print("Error occurred -", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite Connection closed")
