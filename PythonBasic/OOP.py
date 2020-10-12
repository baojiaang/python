class Student:
    def __init__(self):
        self.score = 99
        self.money = 100000000000

    def get_score(self):
        return self.score

    def get_money(self):
        return self.money

    def go(self):
        self.a = "run"
    def goo(self):
        print(self.money)
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('value must be int')
        if value<0 or value>100:
            raise ValueError("must be in 0-100")
        self.score = value


s = Student()
s.set_score(100)
s.goo()
print(s.get_score())
str="11222"
print(str[::-1])

