
class GotCharacter:
    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = is_alive

    def printname(self):
        print(self.first_name, self.is_alive)

#Ex1 = GotCharacter('Robert', 'true')
#print(f'({Ex1.first_name}, {Ex1.is_alive}))

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def printname(self):
        print(self.first_name, self.house_words, self.is_alive)

    def is_alive(self):
        if str(self.is_alive) == 'is_alive':
            print("is_alive")
        else:
            print("is dead")

X = Stark('Robert')
X.printname()
