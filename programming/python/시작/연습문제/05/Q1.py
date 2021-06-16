class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class po(Calculator):
    def minus(self, val):
        self.value -=val

l = po()
l.add(10)
l.minus(7)
print(l.value)