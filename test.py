class Dog:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = "Woof"

    def say(self):
        return self.sound


class Cat:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = "Meow"

    def say(self):
        return self.sound


def create_pet(nickname, pet="dog"):
    pets = dict(dog=Dog(nickname=nickname), cat=Cat(nickname=nickname))
    return pets.get(pet)


if __name__ == "__main__":
    d = create_pet("Bobik")
    print(d.say())

    c = create_pet("Murzic", pet="cat")
    print(c.say())



