from PyQt6.QtWidgets import QApplication, QMainWindow

from HousePrediction.qt.MainWindowExt import MainWindowExt

app = QApplication([])
loginWindow = MainWindowExt()
loginWindow.setupUi(QMainWindow())
loginWindow.showWindow()
app.exec()