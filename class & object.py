class cat:
    attr1 = "man"
    attr2 = "cat"
    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
Rodger = cat()
print(Rodger.attr1)
Rodger.fun()