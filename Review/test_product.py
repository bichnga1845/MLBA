from Review.product import Product

p1=Product("p1","coca","5","20000")
print(p1)

p2=Product() #luc nay cac thuoc tinh ko duoc gan gia tri
             # nen bi none --> ko sui dc
            #bat buoc ta phai lam thu cong
p2.id="p2"
p2.name="pepsi"
print(p2)