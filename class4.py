class Mobile:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        price = p
        print("Model : ", self.model, "Price : ", price)


realme = Mobile('RealMe X')
realme.show_model(1000)
