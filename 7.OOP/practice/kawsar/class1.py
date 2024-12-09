class parent:
    def func1(self):
        print("This is a parent class.")


class child (parent):
    def func2(self):
        print("This is a child class.")

object = child()
object.func1()
object.func2()