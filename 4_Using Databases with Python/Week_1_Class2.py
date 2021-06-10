#Week_1_Class2.py
class PartyAnimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name,"constructed")

    def party(self): #method
        self.x=self.x+1
        print(self.name,"party count",self.x)

s=PartyAnimal("Sally")
s.party()

j=PartyAnimal("Jim")
j.party()
s.party()

#Sally constructed
#Sally party count 1
#Jim constructed
#Jim party count 1
#Sally party count 2
