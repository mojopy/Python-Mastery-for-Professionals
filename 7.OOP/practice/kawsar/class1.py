class Id:
    name = ""
    roll = ""

    def __init__(self,name, roll):
        self.name = name
        self.roll = roll

    def myself(self):
        return f"my name is {self.name} and {self.roll}."
    

id = Id("kawsar",3)
print(id.myself())
