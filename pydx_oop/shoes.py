class Shoe:
    # leave it here for clarity of design
    # size = 9.5
    # color = 'red'

    def __init__(self, size=9.5, color='red'):
        self.size = size #or self.size
        self.color = color #or self.color
        # ^^ more confusing, but if defaults are set to None, go get above

    def __str__(self):
        return "{}, size {}".format(self.color, self.size)

    def __repr__(self):
        pass

    def put_on(self):
        print("You put on your {} shoes.".format(self.color))

    @classmethod
    def create(cls, description):
        shoe = cls()
        size, color = description.split()
        shoe.size = float(size)
        shoe.color = color
        return shoe

    @staticmethod
    def shoe_rack(shoes):
        for shoe in shoes:
            yield Shoe.create(shoe)

closet = Shoe.shoe_rack(["10.5 green", "8 brown", "13 yellow"])
for shoe in closet:
    shoe.put_on()
