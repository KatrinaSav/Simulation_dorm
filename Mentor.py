import random
from Student import Student


class Mentor:
    __dirty_rate: int
    __favourite_students: list[Student] = []
    __number_of_room: int

    def __init__(self, dorm):
        self.__dirty_rate = random.randint(5, 15)
        self.dorm = dorm
        for x in range(5):
            self.__favourite_students.append(random.choice(dorm.get_student_list()))
        self.__number_of_room = random.randint(1, 15)

    def check_room(self):
        room = self.dorm.get_room_by_number(self.__number_of_room)
        print('Комнату №' + str(self.__number_of_room) + " посетил проверяющий")
        if room.get_dirty() >= self.__dirty_rate:
            for each_student in room.get_students():
                if each_student in self.__favourite_students:
                    continue
                else:
                    each_student.give_ban()
                    if each_student.check_kick():
                        self.dorm.kick_student(each_student)

    def print_info(self):
        print("Проверяемая комната: " + str(self.__number_of_room) + "\nПроверяемый уровень чистоты: " +
              str(self.__dirty_rate) + "\n__Студенты-любимчики__\n")
        for stud in self.__favourite_students:
            print('__Информация о студенте__')
            stud.print_info()

