def disp():
    def pri():
        print("This is inner function")
    print("This is outer function")
    pri()


disp()
