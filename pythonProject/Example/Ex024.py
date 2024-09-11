class Member:
    def __init__(self, name, age):  # 생성자를 통해서 멤버변수를 만들었어요.
        self.name = name
        self.age = age
    def show_member(self):
        print(self.name, "\t", self.age)

member1 = Member(age = 40, name = "Karl")
member1.show_member()
#==========================================================================
# 연습문제 8-3. 생성자 이용한 성적 합계/평균
class Student :
    total = 0
    avg = 0.0
    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math= math
    def get_Sum(self) :
        self.total = self.kor + self.eng + self.math
        return self.total
    def get_Avg(self) :
        self.avg = self.total /3
        return self.avg

s1 = Student('홍지영', 90, 90, 100)
print('이름 : %s' % s1.name)
print('합계 : %d' % s1.get_Sum())
print('평균 : %.1f' % s1.get_Avg() )
#==========================================================================