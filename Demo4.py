class Test:
    eye=2
    def __init__(self):
        print(Test.eye)
        self.a=100
        #del Test.eye
        print(Test.eye)
t=Test()