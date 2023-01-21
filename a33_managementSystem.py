# design a system that takes:
# 3 clients - harry, rohan, hammad
# what they eat and at what times
# in total 6 files: 3 for locking diet taken, 3 for exercises done by them

def getdate():
    import datetime
    return datetime.datetime.now()


def update():
    client = int(input("Enter \n1. Harry\n2. Rohan\n3. Hammad\n"))
    check = 1
    if client == 1:
        while check != 0:
            print("What do you want to update?")
            print("Press 1 for Diet\nPress 2 for Exercise")
            choice = int(input())
            if choice == 1:
                f = open("harry_diet.txt", "a")
                st = input("Enter the diet taken\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            elif choice == 2:
                f = open("harry_exercise.txt", "a")
                st = input("Enter the exercise done\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            check = int(input("Press 1 to log more\nPress 0 to leave\n"))
    if client == 2:
        while check != 0:
            print("What do you want to update?")
            print("Press 1 for Diet\nPress 2 for Exercise")
            choice = int(input())
            if choice == 1:
                f = open("Rohan_diet.txt", "a")
                st = input("Enter the diet taken\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            elif choice == 2:
                f = open("Rohan_exercise.txt", "a")
                st = input("Enter the exercise done\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            check = int(input("Press 1 to log more\nPress 0 to leave\n"))
    if client == 3:
        while check != 0:
            print("What do you want to update?")
            print("Press 1 for Diet\nPress 2 for Exercise")
            choice = int(input())
            if choice == 1:
                f = open("Hammad_diet.txt", "a")
                st = input("Enter the diet taken\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            elif choice == 2:
                f = open("Hammad_exercise.txt", "a")
                st = input("Enter the exercise done\n")
                x = str([str(getdate())])
                f.write("Time: " + x + " " + "Diet: ")
                f.write(st + "\n")
                f.close()
            check = int(input("Press 1 to log more\nPress 0 to leave\n"))


# retrieve
def retrieve():
    print("Whose details you want to retrieve?")
    name = int(input("0. None\n1. Harry\n2.Rohan\n3.Hammad\n"))
    choice = int(input("1. Diet Info\n2. Exercise Info\n"))
    if name == 0:
        print("Have a nice Day :)\n")
    if name == 1:
        if choice == 1:
            f = open("Harry_diet.txt")
            print(f.read())
        elif choice == 2:
            f = open("Harry_exercise.txt")
            print(f.read())
    elif name == 2:
        if choice == 1:
            f = open("Rohan_diet.txt")
            print(f.read())
        elif choice == 2:
            f = open("Rohan_exercise.txt")
            print(f.read())
    elif name == 3:
        if choice == 1:
            f = open("Hammad_diet.txt")
            print(f.read())
        elif choice == 2:
            f = open("Hammad_exercise.txt")
            print(f.read())
    print("Have a nice day:)")


print("Welcome to Health Management System!\n")
print("Do you want to:")
k = int(input("1.Retrieve\n2.Update\n"))
if k == 1:
    retrieve()
elif k == 2:
    update()
else:
    print("Wrong input :(")
