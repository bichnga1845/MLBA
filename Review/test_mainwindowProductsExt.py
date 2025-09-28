from PyQt6.QtWidgets import QApplication, QMainWindow

from Review.mainwindowProductsExt import mainwindowProductsExt
from Review.product import Product
from Review.products import ListProduct

app=QApplication([])
main=QMainWindow()
my_window=mainwindowProductsExt()
my_window.setupUi(main)

#napdata
lp=ListProduct()
lp.add_product(Product("p1","Coca",7,17900))
lp.add_product(Product("p2","pepsi",14,26000))
lp.add_product(Product("p3", "sting",6,15000))
lp.add_product(Product("p4","fanta",8,17900))

my_window.load_products(lp)
my_window.showWindow()
app.exec()
