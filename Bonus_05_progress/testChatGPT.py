from PyQt6.QtWidgets import QApplication, QMainWindow

from Bonus_05_progress.mainwindowChatGPTExt import mainwindowChatGPTExt


app=QApplication([])
main=QMainWindow()
my_window=mainwindowChatGPTExt()
my_window.setupUi(main)
my_window.showWindow()
app.exec()