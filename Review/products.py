class ListProduct:
    def __init__(self):
        self.products=[]
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def price_desc(self):
        self.products = sorted(self.products, key=lambda x: x.price, reverse=True)
        for dp in self.products:
            print(dp)
    def sort_price_desc(self):
        for i in range(0,len(self.products)):
            for j in range(i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price<pj.price:
                    self.products[i]=pj
                    self.products[j]=pi
                if pi.quantity<pj.quantity:
                    self.products[i] = pj
                    self.products[j] = pi

