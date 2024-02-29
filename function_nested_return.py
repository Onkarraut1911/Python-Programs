def disp():
    def show():
        return "show function"
    result = show() + " disp function"
    return result


a = disp()
print(a)
