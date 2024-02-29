class Mobial:
    def __init__(self):
        self.price = 50000

    def show_price(self):
        print(self.price)


realme = Mobial()
redmi = Mobial()
samsung = Mobial()

print(realme.price)
print(redmi.price)
print(samsung.price)

print()

redmi.price = 40000

print()
print(realme.price)
print(redmi.price)
print(samsung.price)
