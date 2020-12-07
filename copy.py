import os
def copy():
    source=input("Enter path of source : ")
    destination=input("Enter path of destination : ")
    os.system("cp {} {}".format(source,destination))
    print("successfully copied ")
