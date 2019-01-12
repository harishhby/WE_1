class Test:
    x=100#public-Accessed across all level
    _y=200#protected-Accessed in parent and child class
    __z=300#private-Accessed only in same class
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)
t=Test()
t.m1()
print("-------------")
print(Test.x)
print(Test._y)
print(Test.__z)
print(Test.__z)
