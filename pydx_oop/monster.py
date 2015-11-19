class Monster:
    sound = "Raarrr!"

    def __init__(self, sount=None):
        self.sound = sound or self.sound

    # weird; makes python behave like JS; ymmv
    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except KeyError as err:
            raise err

    def attack(self):
        print("The monster cries '{}' and attacks!".format(self.sound))

    def give_up(self):
        print("the monster throws down its weapons and runs away.")

class Troll(Monster):
    bridge = False
    sound = "Well, actually..."

    def attack(self):
        print("The troll says something mean about you.")
        super(Troll, self).attack()

class Dungeon:
    trouble = []

    def __init__(self, monsters=None):
        if monsters:
            self.trouble.extend(monsters)

    # Generator
    def __iter__(self):
        random.shuffle(self.trouble)
        return (m for m in self.trouble)

m1 = Monster()
m2 = Monster(sound="Urk!")
t1 = Troll()
t2 = Troll(sound="Discrimination is a fairy tale!")

dungeon = Dungeon(monsters=[m1, m2, t1, t2])
print(list(dungeon))
