import time
import os
timer = int(input("Set your time in minutes: "))
if timer == 1:
    a = 60
    while a != 0:
        a = a - 1
        os.system("clear")
        print(str(a) + " seconds left")
        time.sleep(1)
    os.system("firefox")
elif timer > 1:
    timer = timer - 1
    a = 60
    os.system("clear")
    print(str(timer) + " minutes " + str(a) + " seconds left")
    while timer != 0:
        while a != 0:
            a = a - 1
            os.system("clear")
            print(str(timer) + " minutes " + str(a) + " seconds left")
            time.sleep(1)
        while a == 0:
            a = 60
            timer = timer - 1
            os.system("clear")
            print(str(timer) + " minutes " + str(a) + " seconds left")
            time.sleep(1)
    if timer == 0:
        a = 60
        while a != 0:
            a = a - 1
            os.system("clear")
            print(str(a) + " seconds left")
            time.sleep(1)
        os.system("firefox")
