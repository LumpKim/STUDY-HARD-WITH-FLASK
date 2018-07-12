lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer("Rolf")
player_one.numbers =(1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

#print(player_one.numbers == player_two.numbers)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(marks) / len(marks)

    @staticmethod
    def go_to_school(cls):
        print("I'm going to school")
        print("I'm a {}".format(cls))

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
anna.marks.append(71)
Student.go_to_school()