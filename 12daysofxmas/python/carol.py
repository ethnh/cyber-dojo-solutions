class Carol:
    start_of_carol = """On the {} day of Christmas
My true love gave to me:"""

    def __init__(self, *args, **kwargs):
        self._carol = (
            []
        )  # not 100% sure this will make a new empty list every time, python is weird 🙏
        self._day = 0

    def add_line(self, line: str):
        if self._day >= 12:
            raise ValueError("You may not add more than 12 days!")
        self._day += 1
        self._carol.append(line)

    def day_as_str(self):
        if self._day == 0:
            raise ValueError(
                "There is not 0th day of Christmas! Add a line to the carol first with add_line(line)"
            )
        day_repr = {
            1: "First",
            2: "Second",
            3: "Third",
            4: "Fourth",
            5: "Fifth",
            6: "Sixth",
            7: "Seventh",
            8: "Eigth",
            9: "Ninth",
            10: "Tenth",
            11: "Eleventh",
            12: "Twelveth",
        }
        return day_repr[self._day]

    def sing_carol(
        self,
    ):  # this function is incredibly simple, no testing needed for prints
        print(
            self.start_of_carol.replace(
                "{}", self.day_as_str()  # On the {} day of christmas
            )
        )  # Could be tested using a function that returns the start of carol w/ day_as_str pre-replaced
        print(
            "\n".join(  # Every line must have a line break
                self._carol[
                    ::-1
                ]  # Reverse days of the carol, it goes [1], [2, 1], [3, 2, 1] ...
            )
        )


if __name__ == "__main__":
    new_carol = Carol()
    lines = """My true love gave to me:
Twelve drummers drumming
Eleven pipers piping
Ten lords a-leaping
Nine ladies dancing
Eight maids a-milking
Seven swans a-swimming
Six geese a-laying
Five golden rings
Four calling birds
Three french hens
Two turtle doves
A partridge in a pear tree.""".split(
        "\n"
    )
    for line in lines:
        new_carol.add_line(line)
        new_carol.sing_carol()
