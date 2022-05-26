import unittest
from main import Student
from main import Room


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student()

    def test_give_ban(self):
        self.student.give_ban()
        self.assertEqual(self.student.get_number_of_bans(), 1)

    def test_check_kick(self):
        for x in range(2):
            self.student.give_ban()
        self.assertTrue(self.student.check_kick())


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1)

    def test_get_number_of_room(self):
        self.assertEqual(self.room.get_number_of_room(), 1)

    def test_add_student(self):
        student = Student()
        self.room.add_student(student)
        self.assertEqual(self.room.get_number_of_students(), 1)
        self.assertEqual(self.room.get_students()[0], student)

    def test_add_neighbour_room(self):
        room = Room(1)
        self.room.add_neighbour_room(room)
        self.assertEqual(self.room.get_room_neighbours()[0], room)

    def test_noise_in_room(self):
        student = Student()
        self.room.add_student(student)
        self.assertFalse(self.room.get_is_source_of_noise())

    def test_move_out(self):
        student = Student()
        self.room.add_student(student)
        self.assertEqual(self.room.get_number_of_students(), 1)
        self.room.move_out(student)
        self.assertEqual(self.room.get_number_of_students(), 0)

    def test_kill_roach(self):
        self.room.set_roach(True)
        self.room.kill_roach()
        self.assertFalse(self.room.get_is_roach_in_room())


if __name__ == "__main__":
    unittest.main()
