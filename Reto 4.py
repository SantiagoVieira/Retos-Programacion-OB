import matplotlib.pyplot as plt
from datetime import date


class User():
    def __init__(self,id,user_name,balance):
        self.id=int(id)
        self.user_name=str(user_name)
        self.balance=float(balance)
        
        self.order_list=[]
        self.car=[]
    
    def add_product_to_car(self,product):
        self.car.append(product)

    
    def consolidate_order(self,order_id):

        for i in self.car:
            order_id.total+=i.price
        if order_id.total>self.balance:
            print(f" NO TIENE SALDO SUFICIENTE \n El valor total de su compra es de {order_id.total} y su saldo es de {self.balance}$ ")
        else:
            print(f" La orden se ha realizado con exito.\nEl valor a pagar es de {order_id.total}")
            order_id.product_list.append(self.car)
            self.order_list.append(order_id)
            order_id.status=True
    

    
    def add_to_balance(self,amount):
        if type(amount)==int:
            self.balance+=amount
        else:
            print("digite un número valido")

    
    def plot_order_history(self,product):
        x=[]
        y=[]
        plt.style.use(['dark_background'])
        for i in product.price_history:
            x.append(i)
            y.append(product.price_history[i])

        if len(product.price_history)>1:
            plt.plot(x,y,linestyle="--",color="g",label=product.name)

        else:
            plt.bar(x,y,linestyle="--",color="g",label=product.name)

        plt.legend()
        plt.xlabel("Tiempo")
        plt.ylabel("Precio")
        plt.title(f"Cambio del precio de la {product.name}")
        plt.show()


        

class Order():
    def __init__(self,id,date,status=False,total=0):
        self.id=int(id)
        self.product_list=[]
        self.date=date
        self.status=status
        self.total=total
        
class Product():
    def __init__(self, id, name, price, dict):
        self.id=int(id)
        self.name=str(name)
        self.price=float(price)
        self.price_history=dict

    def update_price(self,date,price):
        self.price=float(price)
        self.price_history[date]=price

Arroz=Product(1,"Arroz",123,{date(2022,1,12):123.7})
Frijoles=Product(2,"Frijoles",12,{date(2022,1,19):12})
Lentejas=Product(3,"Lentejas",34,{date(2022,1,2):34})
Chocolate=Product(4,"Chocolate",42,{date(2022,1,5):42})
Galletas=Product(5,"Galletas",54,{date(2022,1,4):54})

papa.update_price(date(2022,3,12),2.2)

Santiago=User(1,"Santiago VIeira",13.12)
Santiago.add_product_to_car(Frijoles)
Santiago.add_product_to_car(Lentejas)
Santiago.add_product_to_car(Chocolate)

mercado=Order(1,date(2022,1,2))
Santiago.consolidate_order(mercado)

Santiago.add_to_balance(3123123)
mercado=Order(1,date(2022,1,2))
Santiago.consolidate_order(mercado)

Santiago.plot_order_history(Arroz)
Santiago.plot_order_history(Frijoles)