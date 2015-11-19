class Song:
    total_seconds = 0

    def __init__(self, time='00:00:00'):
        self.time = time
        self.__total_seconds = 0; # just in case; not strictly necessary
        self.total_seconds = time # MAGIC
        # self.total_seconds = self.__set_total_seconds(time)

    def __int__(self):
        return self.total_seconds

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other): # reflected add: 1+2 == 2+1
        return int(self) + other

    def __iadd__(self, other): # in-place add: x+=3
        pass

    @property
    def total_seconds(self):
        return self.__total_seconds

    # useful to reset after instantiated
    @total_seconds.setter # MAGIC
    def total_seconds(self, time):
        if time.count(':') != 2:
            raise ValueError('')
        seconds, minutes, hours = map(int, time.split(':')[::-1])
        seconds += minutes * 60
        seconds += hours * 3600
        self.__total_seconds = seconds

    # name-munging: __ "private"; makes method only callable from inside the class
    # fyi: _ = "this is my method; use if needed, but might change"
    # def __set_total_seconds(self, time):
    #     if time.count(':') != 2:
    #         raise ValueError('')
    #     seconds, minutes, hours = map(int, time.split(':')[::-1])
    #     seconds += minutes * 60
    #     seconds += hours * 3600
    #     return seconds

song1 = Song(time="00:00:10")
song2 = Song(time="00:01:00")
print(sont1+song2)
