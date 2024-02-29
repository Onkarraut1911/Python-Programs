class Mobile:
    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        print("Model: ", self.model)


realme = Mobile()
realme.show_model()
print(realme.model)

realme.model = 'RealMe pro2'
print(realme.model)
