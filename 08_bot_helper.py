from AddrBook import *
import pickle


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "+rb") as f:
            restored_bk = pickle.load(f)
            cnt = len(restored_bk)
            print(f"{cnt} contacts in AddressBook loaded")
            return restored_bk
    except:
        return AddressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Command not Found."
        except KeyError:
            return "Name not Found."
        except NameError:
            return "Name not Found."
        except Exception as e:
            return f"Error: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(*args):
    if args[0] in book:
        record = book.find(args[0])
        record.add_phone(args[1])
    else:
        record = Record(args[0])
        record.add_phone(args[1])
        book.add_record(record)
    return record


@input_error
def change_contact(command, *args):
    record = book.find(args[0])
    record.edit_phone(args[1], args[2])
    return record


@input_error
def show_phone(*args):
    record = book.find(args[0])
    return record


@input_error
def show_all():
    return book


@input_error
def show_birthday(*args):
    record = book.find(args[0])
    return record.birthday


@input_error
def add_birthday(*args):
    record = book.find(args[0])
    record.add_birthday(args[1])
    return record


book = load_data()


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break
        elif command in ["hello"]:
            print("Hello how can I help you?")
        elif command in ["add"]:
            add = add_contact(*args)
            print(add)

        elif command in ["change"]:
            ch = change_contact(command, *args)
            print(ch)

        elif command in ["phone"]:
            p = show_phone(*args)
            print(p)

        elif command in ["all"]:
            all = show_all()
            print(all)

        elif command == "add-birthday":
            print(add_birthday(*args))

        elif command == "show-birthday":
            b_day = show_birthday(*args)
            print(b_day)

        elif command == "birthdays":
            congrats_list = book.get_birthdays(7)
            print(congrats_list)

        else:
            print("Invalid command")


if __name__ == "__main__":
    main()

#     test_cmd = """
# add jon 1234567890
# phone jon
# add bob 5555555555
# add sonia 9876543210
# change jon 1234567890 2222222228
# phone jon
# add-birthday jon 23.04.2000
# add-birthday sonia 05.03.2000
# show-birthday jon
# birthdays"""
#     a = test_cmd.split("\n")
#     print (a)
