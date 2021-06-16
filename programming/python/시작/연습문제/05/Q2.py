class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class po (Calculator):
    def add(self, val):
        if (self.value + val) >= 100:
            print("tlqkf")
            self.value = 100
        else:
            self.value += val

c = po()
c.add(50)
c.add(60)
print(c.value) 