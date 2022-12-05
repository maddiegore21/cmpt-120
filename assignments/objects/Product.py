class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def inStock(self):
        return self.quantity
    
    def getStock(self, quantity):
        return self.quantity < self.quantity

    def totalCost(self):
        return self.quantity * self.price

    def newStock(self, quantity):
        return self.quantity- quantity


p1 = Product ("Ultrasonic range finder", 2.50, 4)
p2 = Product ("Servo motor", 14.99, 10)
p3 = Product ("Servo controller", 44.95, 5)
p4 = Product ("Microcontroller Board", 34.95, 7)
p5 = Product ("Laser range finder", 149.99, 2)
p6 = Product ("Lithium polymer battery", 8.99, 8)