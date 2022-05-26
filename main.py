import pickle


if __name__ == '__main__':
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
    our_dorm.print_field()
    while True:
        entry = input('Введите команду\n')
        split_entry = entry.split()
        if split_entry[0] == 'help':
            print('kill_roach \'номер\' - убить тараканов в комнате\n'
                  'print_info_room \'номер\' - вывод информации о комнате\n'
                  'print_info_dorm - вывод информации об общежитии\n'
                  'check_in \'номер\'- заселить студентов в комнату\n'
                  'print_map - вывод карты общежития'
                  'exit - выход')
        elif split_entry[0] == 'kill_roach':
            for x in range(1, len(split_entry)):
                try:
                    number_of_room = int(split_entry[x])
                    try:
                        room = our_dorm.get_room_by_number(number_of_room)
                        room.kill_roach()
                    except IndexError:
                        print('В общежитии 15 комнат, введите число от 1 до 15')
                except ValueError:
                    print('Ожидается номер комнаты для очистки')
        elif split_entry[0] == 'print_info_room':
            try:
                number_of_room = int(split_entry[1])
                try:
                    room = our_dorm.get_room_by_number(number_of_room)
                    room.print_info()
                except IndexError:
                    print('В общежитии 15 комнат, введите число от 1 до 15')
            except ValueError:
                print('Ожидается номер комнаты для вывода информации')
        elif split_entry[0] == 'print_info_dorm':
            our_dorm.print_info()
        elif split_entry[0] == 'check_in':
            for x in range(1, len(split_entry)):
                try:
                    number_of_room = int(split_entry[x])
                    try:
                        room = our_dorm.get_room_by_number(number_of_room)
                        our_dorm.check_in(room)
                    except IndexError:
                        print('В общежитии 15 комнат, введите число от 1 до 15')
                except ValueError:
                    print('Ожидается номер комнаты для заселения')
        elif split_entry[0] == 'print_map':
            our_dorm.print_field()
        elif split_entry[0] == 'exit':
            break
        else:
            print('Неверный ввод, введите \'help\' чтобы увидеть список команд')
    with open("saved_step.pickle", "wb") as write_file:
        pickle.dump(our_dorm, write_file)
    write_file.close()

    with open("saved_step_2.pickle", "wb") as write_file:
        pickle.dump(our_dorm.get_room_list(), write_file)
    write_file.close()

