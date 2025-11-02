import os
from datetime import datetime
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QMessageBox, QFileDialog, QTableWidgetItem
)
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LinearRegression

from HousePrediction.DatasetViewer import DataSetViewer
from HousePrediction.FileUtil import FileUtil
from HousePrediction.qt.MainWindow import Ui_TranThiBichNga_HousePrediction


class MainWindowExt(Ui_TranThiBichNga_HousePrediction):
    def __init__(self):
        # Chỉ khởi tạo dữ liệu và biến nền
        self.df = None
        self.lm = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.fileName = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.setWindowTitle("House Pricing Prediction - Tran Thi Bich Nga 🏡")

        # Gắn sự kiện cho các nút
        self.buttonPickDataset.clicked.connect(self.do_pick_data)
        self.buttonViewDataset.clicked.connect(self.do_view_dataset)
        self.buttonTrainModel.clicked.connect(self.do_train)
        self.buttonEvaluateModel.clicked.connect(self.do_evaluation)
        self.buttonSaveModel.clicked.connect(self.do_save_model)
        self.buttonPredictPrice.clicked.connect(self.do_prediction)


        self.lblEvalStatus.setText("Waiting for evaluation...")
        self.lblEvalStatus.setStyleSheet("background-color:#E8F8F5; color:#117A65; font-weight:bold;")
        self.Dataset.setAlternatingRowColors(True)

    def showWindow(self):
        self.MainWindow.show()



    def do_pick_data(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self.MainWindow, "Select Dataset", "", "CSV Files (*.csv);;All Files (*)"
        )
        if file_name:
            self.fileName = file_name
            QMessageBox.information(self.MainWindow, "Dataset Selected", f"You selected:\n{file_name}")
        else:
            QMessageBox.warning(self.MainWindow, "Warning", "No file selected!")

    def do_view_dataset(self):
        if not self.fileName:
            QMessageBox.warning(self.MainWindow, "Warning", "Please pick a dataset first!")
            return
        viewer = DataSetViewer()
        viewer.create_ui()
        viewer.show_data_listview(self.fileName)
        viewer.show_ui()

    def do_train(self):
        if not self.fileName:
            QMessageBox.warning(self.MainWindow, "Warning", "Please select a dataset first!")
            return
        try:
            self.df = pd.read_csv(self.fileName)
            X = self.df[['Avg. Area Income', 'Avg. Area House Age',
                         'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms',
                         'Area Population']]
            y = self.df['Price']

            self.X_train, self.X_test, self.y_train, self.y_test = (
                train_test_split(X, y, test_size=0.2, random_state=101)
            )
            self.lm = LinearRegression()
            self.lm.fit(self.X_train, self.y_train)
            QMessageBox.information(self.MainWindow, "Training", "Model training completed!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Training failed:\n{str(e)}")

    def do_evaluation(self):
        if self.lm is None:
            QMessageBox.warning(self.MainWindow, "Warning", "Please train the model first!")
            return
        try:
            predictions = self.lm.predict(self.X_test)
            self.Dataset.setRowCount(len(self.X_test))

            for i in range(len(self.X_test)):
                row_data = [
                    self.X_test.iloc[i, 0], self.X_test.iloc[i, 1],
                    self.X_test.iloc[i, 2], self.X_test.iloc[i, 3],
                    self.X_test.iloc[i, 4],
                    self.y_test.iloc[i], predictions[i]
                ]
                for j, val in enumerate(row_data):
                    self.Dataset.setItem(i, j, QTableWidgetItem(str(round(val, 2))))

            coeff_df = pd.DataFrame(self.lm.coef_, self.X_train.columns, columns=['Coefficient'])
            self.Coefficients.setText(str(coeff_df))

            mae = metrics.mean_absolute_error(self.y_test, predictions)
            mse = metrics.mean_squared_error(self.y_test, predictions)
            rmse = np.sqrt(mse)

            self.labelMAE.setText(f"{mae:.2f}")
            self.labelMSE.setText(f"{mse:.2f}")
            self.labelRMSE.setText(f"{rmse:.2f}")

            self.lblEvalStatus.setText("Evaluation is finished")
            self.lblEvalStatus.setStyleSheet("background-color:#D5F5E3; color:#145A32; font-weight:bold;")

            QMessageBox.information(self.MainWindow, "Evaluation", "Model evaluation completed successfully!")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Evaluation failed:\n{str(e)}")

    def do_save_model(self):
        if self.lm is None:
            QMessageBox.warning(self.MainWindow, "Warning", "Train a model first before saving.")
            return
        try:
            filename = f"housingmodel_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.zip"
            os.makedirs("model", exist_ok=True)
            FileUtil.savemodel(self.lm, os.path.join("model", filename))
            QMessageBox.information(self.MainWindow, "Save Model", f"Model saved as {filename}")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Failed to save model:\n{str(e)}")

    def do_prediction(self):
        try:
            if self.lm is None:
                QMessageBox.warning(self.MainWindow, "Warning", "You must train or load a model first!")
                return

            vals = [
                float(self.labelIncome.text()),
                float(self.labelHouseAge.text()),
                float(self.labelRooms.text()),
                float(self.labelBedrooms.text()),
                float(self.labelPopulation.text())
            ]
            result = self.lm.predict([vals])[0]
            self.labelPrediction.setText(f"{result:,.2f}")
            QMessageBox.information(self.MainWindow, "Prediction", f" Predicted House Price: {result:,.2f}")
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Error", f"Prediction failed:\n{str(e)}")
