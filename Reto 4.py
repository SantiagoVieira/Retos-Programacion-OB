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
            print(f" Actualmente no tienes suficiente saldo y El valor  de su compra es de {order_id.total} y su saldo actual es de {self.balance}$ ")
        else:
            print(f" Su orden a sido exitosa.\n Valor a pagar es  {order_id.total}")
            order_id.product_list.append(self.car)
            self.order_list.append(order_id)
            order_id.status=True
    

    def add_to_balance(self,amount):
        if type(amount)==int:
            self.balance+=amount
        else:
            print("Nuevamente ingrese un numero valido")
    
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
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.title(f"Cambio del {product.name}")
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

Arroz=Product(1,"Arroz",123,{date(2022,1,11):156.7})
Frijoles=Product(2,"Frijoles",12,{date(2022,1,18):18})
Lentejas=Product(3,"Lentejas",34,{date(2022,1,33):37})
Chocolate=Product(4,"Chocolate",42,{date(2022,1,55):49})
Galletas=Product(5,"Galletas",54,{date(2022,1,44):52})

Arroz.update_price(date(2022,3,12),2.5)

Santiago=User(1,"Santiago VIeira",13.12)
Santiago.add_product_to_car(Frijoles)
Santiago.add_product_to_car(Lentejas)
Santiago.add_product_to_car(Chocolate)

mercado=Order(1,date(2022,2,2))
Santiago.consolidate_order(mercado)

Santiago.add_to_balance(3214569)
mercado=Order(1,date(2022,2,2))
Santiago.consolidate_order(mercado)

Santiago.plot_order_history(Arroz)
Santiago.plot_order_history(Frijoles)
