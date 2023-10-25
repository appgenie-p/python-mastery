class Parent:
    def spam(self):
        print("Parent")


class A(Parent):
    def spam(self):
        print("A")
        # super().spam()


class B(Parent):
    def spam(self):
        print("B")
        # super().spam()


class Child(A, B):
    pass


c = Child()
c.spam()
