from PyQt6.QtWidgets import QApplication, QMainWindow

from CodingPythonAPI.mainwindowAPITranslateExt import mainwindowAPITranslateExt


app=QApplication([])
main=QMainWindow()
my_window=mainwindowAPITranslateExt()
my_window.setupUi(main)

my_window.showWindow()
app.exec()
