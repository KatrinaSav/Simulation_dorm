import pickle
import click as click
from click_shell import shell
from Mentor import Mentor


@shell(prompt='Общежитие > ', intro='Запуск симуляции...')
def main():
    global our_dorm
    global mentor
    with open('saved_step.pickle', 'rb') as f:
        our_dorm = pickle.load(f)
    f.close()
    with open('saved_step_2.pickle', 'rb') as f:
        our_dorm.set_room_list(pickle.load(f))
    f.close()
    our_dorm.find_all_students()
    our_dorm.next_month()
    our_dorm.define_is_kitchen_okey()
    our_dorm.roach()
    our_dorm.noise_in_dorm()
    our_dorm.visit_every_room()
    our_dorm.change_duty()
    mentor = Mentor(our_dorm)
    mentor.check_room()
    our_dorm.save_to_file()
    our_dorm.print_field()

    @main.command(help='Травить тараканов в комнате №[1..15]')
    @click.argument('number')
    def kill_roach(number):
        try:
            room = our_dorm.get_room_by_number(int(number))
            room.kill_roach()
            our_dorm.save_to_file()
        except IndexError:
            print('В общежитии 15 комнат')

    @main.command(help='Вывести информацию о комнате №[1..15]')
    @click.argument('number')
    def print_info_room(number):
        try:
            room = our_dorm.get_room_by_number(int(number))
            room.print_info()
        except IndexError:
            print('В общежитии 15 комнат')

    @main.command(help='Заселить студента в комнату №[1..15]')
    @click.argument('number')
    def check_in(number):
        try:
            room = our_dorm.get_room_by_number(int(number))
            our_dorm.check_in(room)
            our_dorm.save_to_file()
        except IndexError:
            print('В общежитии 15 комнат')

    @main.command()
    def print_info_dorm():
        our_dorm.print_info()

    @main.command()
    def mentor_info():
        mentor.print_info()

    @main.command()
    def print_map():
        our_dorm.print_field()

if __name__ == '__main__':
    main()




