class Animal:
    name = "" # property == instance 변수 # public
    def sound(self, name):
        self.name = name
        print(f"{self.name}이 소리를 낸다.")

animal1 = Animal()
animal2 = Animal()
animal3 = Animal()
# animal.sound("고양이")
# print(animal.sound("고양이"))
#========================================================
class Fruit:
    name = '오렌지'
    color = '노란색'
    def taste(self):
        print('새콤하다.')
    def vitamin(self):
        print('비타민 C가 풍부하다.')
orange = Fruit()

print('과일명: %s' % orange.name)
print('색상: %s' % orange.color)
orange.taste()
orange.vitamin()