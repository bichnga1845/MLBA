from flask import Flask, render_template, request
from FileUtil import FileUtil  # module load model của bạn

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/doprediction", methods=["POST"])
def doprediction():
    # Lấy dữ liệu từ form
    area_income_value = float(request.form["area_income_value"])
    area_house_age_value = float(request.form["area_house_age_value"])
    area_number_of_rooms_value = float(request.form["area_number_of_rooms_value"])
    area_number_of_bedrooms_value = float(request.form["area_number_of_bedrooms_value"])
    area_population_value = float(request.form["area_population_value"])

    # Load mô hình
    trainedModel = FileUtil.loadmodel("housingmodel.zip")

    # Dự đoán
    result = trainedModel.predict([[
        area_income_value,
        area_house_age_value,
        area_number_of_rooms_value,
        area_number_of_bedrooms_value,
        area_population_value
    ]])

    # Trả về chuỗi kết quả
    return str(round(result[0], 2))

if __name__ == "__main__":
    app.run(host="localhost", port=9000, debug=True)
