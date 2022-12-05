class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self):
        return self.quantity

    def getStock(self, quantity):
        return quantity < self.quantity

    def totalCost(self):
        return self.quantity * self.price

    def newStock(self, quantity):
        return self.quantity - quantity


p1 = Product("Ultrasonic range finder", 2.50, 4)
p2 = Product("Servo motor", 14.99, 10)
p3 = Product("Servo controller", 44.95, 5)
p4 = Product("Microcontroller Board", 34.95, 7)
p5 = Product("Laser range finder", 149.99, 2)
p6 = Product("Lithium polymer battery", 8.99, 8)

products = [p1, p2, p3, p4, p5, p6]


def print_stock():
    print("\nAvailable Products")
    print("-----------------")


for i in range(0, len(products)):
    if products[i].quantity > 0:
        print(str(i) + ")", products[i].name, "$", products[i].price)
    print()


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input(
            "Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break

    prod_id = int(vals[0])
    count = int(vals[1])

    product = products[prod_id]

    if product.getStock(count):
        if cash >= product.totalCost():
            price = product.price * count
            cash -= price
            print("You purchased", count, product.name + ".")
            print("You have $", "{0:.2f}".format(cash), "remaining.")
        else:
            print("Sorry, you cannot afford that product.")
    else:
        print("Sorry, we are sold out of", product.name)


main()
