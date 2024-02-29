class Mobile:
    fp = 'Yes'

    def __init__(self):
        self.model = 'RealMe X'

    def show_model(self):
        print("Model:",self.model)

    @classmethod
    def is_fp(cls):
        print("Finger Print:",cls.fp)

realme = Mobile()
realme.show_model()
Mobile.is_fp()