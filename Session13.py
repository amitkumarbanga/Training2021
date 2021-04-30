"""
INHERITANCE
"""
class Parent():
    def __init__(self):
        print("Parent Object Constructed")

        self.frame = "Amit"
        self.lname = "Kumar"
        self.wealth = 100000

    def show(self):
        print("This is show of Parent")

class Child(Parent):
    def show(self):
        print("This is show of Child")

def main():
    print("Parent class Dictionary")
    print(Parent.__dict__)

    print("Child class Dictionary")
    print(Child.__dict__)

    cRef = Child()
    cRef.show()

if __name__ == '__main__':
    main()