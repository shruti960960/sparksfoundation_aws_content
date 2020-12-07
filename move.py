import os
def move():
    source=input("Enter path of source : ")
    destination=input("Enter path of destination : ")
    os.system("mv {} {}".format(source,destination))
    print("successfully moved")
