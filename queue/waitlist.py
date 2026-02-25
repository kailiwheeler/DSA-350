import random
from q import *
class Student:
    def __init__(self,first_name = "",last_name =""):
        self.first_name = first_name
        self.last_name = last_name
        self.sid = random.randint(1000,9999)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ID: {self.sid}"

if __name__ == '__main__' :  
    k = Student("Kaili", "Wheeler")
    l = Student("Lea", "Lovelace")
    e = Student("Ella", "Hardy")
    print("\nTest Student")
    print(k)
    print(l)
    print(e)

    waitlist = Queue()
    waitlist.add("Kaili", "Wheeler")
    waitlist.add("Lea", "Lovelace")
    waitlist.add("Ella", "Hardy")
    print("\nTest Queue")
    for stud in waitlist:
        print(stud.data)
    print(waitlist)

    print("\nTest Pop")
    print(waitlist)
    waitlist.pop_left()
    print(waitlist)
    waitlist.pop_left()
    print(waitlist)
    waitlist.pop_left()
    print(waitlist)
    
