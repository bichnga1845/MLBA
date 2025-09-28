from Review.product import Product
from Review.products import ListProduct

lp=ListProduct()
lp.add_product(Product("p1","Coca",7,17900))
lp.add_product(Product("p2","pepsi",14,26000))
lp.add_product(Product("p3", "sting",6,15000))
lp.add_product(Product("p4","fanta",8,17900))
lp.print_products()
#lp.price_desc()
lp.sort_price_desc()
print("List products- Desc")
lp.print_products()
