class getNprint():
    def __init__(self,str):
        self.str = str
    def getString(self):
        self.inst = input('Enter a String')
    def printStr(self):
        print(self.inst)

def test():
    getNprint.getString()
