def disp():
    def show():
        return "Show Function"
    print("Disp Functionn")
    return show


r_sh = disp()
print(r_sh())
