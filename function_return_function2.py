def disp(sh):
    print("disp function ")
    return sh


def show():
    return "show function"


r_sh = disp(show)
print(r_sh())
