from collections import UserDict
import re
from datetime import datetime as dtdt
import datetime as dt


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
            super().__init__(value)
        else:
            pass


class Phone(Field):
    def __init__(self, number):
        if self.validate_number(number):
            super().__init__(number)
        else:
            raise ValueError

    def validate_number(self, number):
        if (len(number) == 10) and \
                (re.match(r"^\d+$", number)):
            return True
        else:
            raise ValueError

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Phone):
            return self.value == other.value
        else:
            return False

    def __str__(self):
        return super().__str__()


class Birthday(Field):
    def __init__(self, value: str) -> None:
        try:
            b_date = dtdt.strptime(value, "%d.%m.%Y").date()
            super().__init__(b_date)
        except:
            raise ValueError("please input date in correct format \
                              DD.MM.YYYY")


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.birthday = None
        self.phones = []

    def add_phone(self, phone_number):
        number = Phone(phone_number)
        if number:
            self.phones.append(number)

    def add_birthday(self, b_day):
        b_day = Birthday(b_day)
        if b_day:
            self.birthday = b_day

    def remove_phone(self, phone_number):
        phone_obj = Phone(phone_number)
        for obj in self.phones:
            if obj.value == phone_obj.value:
                self.phones.remove(obj)

    def edit_phone(self, old_number, new_number):
        self.find_phone(old_number)
        self.remove_phone(old_number)
        self.add_phone(new_number)

    def find_phone(self, phone_number):
        ph = Phone(phone_number)
        if ph in self.phones:
            return ph
        else:
            raise ValueError

    def __str__(self) -> str:
        all_phones_str = []
        for tel in self.phones:
            all_phones_str.append(str(tel))
        return f" Phones:{str(all_phones_str)} Birthday: {self.birthday}"


class AddressBook(UserDict):

    def add_record(self, record_item: "Record"):
        self.data[record_item.name.value] = record_item

    def find(self, key):
        return self[key]

    def delete(self, key):
        del self[key]

    def get_birthdays(self, for_the_period: 7):
        congrats_list = []
        bd_dict = {k: v.birthday.value for k, v in self.items() \
                   if v.birthday is not None}
        curr_date = dtdt.today().date()
        end_date = curr_date + dt.timedelta(for_the_period)
        for k, v in bd_dict.items():
            bd_date = v
            bd_date_this_year = dt.date(curr_date.year, bd_date.month, bd_date.day)
            if bd_date_this_year.weekday() == 6:
                bd_date_this_year = bd_date_this_year + dt.timedelta(1)
            if bd_date_this_year.weekday() == 5:
                bd_date_this_year = bd_date_this_year + dt.timedelta(2)

            if (bd_date_this_year <= end_date) and (bd_date_this_year >= curr_date):
                dct = {"name": k, "congratulation_date": bd_date_this_year.strftime("%Y.%m.%d")}
                congrats_list.append(dct)
        return congrats_list

    def __str__(self) -> str:
        dict = {}
        for k, v in self.items():
            dict[k] = str(v)
            result_str = "\n".join([f"{k}:{v}" for k, v in dict.items()])
        return str(result_str)

# if __name__ == "__main__":
#### -------for testing only 

#     def save_data(book, filename="addressbook.pkl"):
#         with open(filename, "wb") as f:
#             pickle.dump(book, f)

#     def load_data(filename="addressbook.pkl" ):
#         try:
#             with open(filename,"+rb") as f:
#                 return pickle.load(f)
#         except:
#             return AddressBook() 

#     book = load_data()
#     # book= AddressBook()

#     # jon = Record("jon")
#     # jon.add_phone("1234567890")
#     # jon.add_phone("2224567890")
#     # jon.add_birthday ("01.01.2023") 
#     # book.add_record(jon)

#     # bob = Record("bob")
#     # bob.add_phone("9876543210")
#     # bob.add_birthday ("01.02.2023") 
#     # book.add_record(bob)

#     # adam = Record("adam")
#     # adam.add_phone("9456654456")
#     # adam.add_birthday ("01.05.2023") 
#     # book.add_record(adam)

#     # bobi = Record("bobi")
#     # bobi.add_phone("9876543888")
#     # bobi.add_birthday ("01.03.2023") 
#     # book.add_record(bobi)

#     print(f"{book} restored")
#     save_data(book)
