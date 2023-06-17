class intTime:
    def geti(self):
        return 18032000

class strTime:
    def gets(self):
        return "404"

class Adapter(intTime,strTime):
    def get1(self):
        return str(self.geti())
    def get2(self):
        return int(self.gets())

work = Adapter()
intwork=intTime()
strwork=strTime()
print("Итог:" + work.get1())
print(work.get2()+intwork.geti())
