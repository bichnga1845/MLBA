from PyQt6.QtWidgets import QTableWidgetItem

from Review.mainwindowProducts import Ui_MainWindow


class mainwindowProductsExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def load_products(self,lp):
        self.tableWidgetProduct.setRowCount(0)
        for i in range(0,len(lp.products)):
            p=lp.products[i]
            number_row=self.tableWidgetProduct.rowCount()
            #insert new row
            self.tableWidgetProduct.insertRow(number_row)
            #fill all attributes of products
            self.tableWidgetProduct.setItem(number_row,0,QTableWidgetItem(p.id))
            self.tableWidgetProduct.setItem(number_row,1,QTableWidgetItem(p.name))
            self.tableWidgetProduct.setItem(number_row,2,QTableWidgetItem(str(p.quantity)))
            self.tableWidgetProduct.setItem(number_row,3,QTableWidgetItem(str(p.price)))


