class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}"

    def __add__(self, other):
        height = (self.height + other.height) // 2
        danger = self.danger if self.danger >= other.danger else other.danger
        color = self.color if self.color <= other.color else other.color
        return Dragon(height, danger, color)

    def __lt__(self, other):
        return self.height < other.height and self.danger < other.danger and self.color < other.color

    def __le__(self, other):
        return self.height <= other.height and self.danger <= other.danger and self.color <= other.color

    def __gt__(self, other):
        return self.height > other.height and self.danger > other.danger and self.color > other.color

    def __ge__(self, other):
        return self.height >= other.height and self.danger >= other.danger and self.color >= other.color

    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color

    def __ne__(self, other):
        return self.height != other.height or self.danger != other.danger or self.color != other.color

    def change_color(self, color):
        self.color = color
        return self.color

    def __isub__(self, value):
        self.height -= self.height // value
        self.danger += self.danger % value
        return self

    def __repr__(self):
        return f'Dragon ({self.height}, {self.danger}, {self.color})'

    def __call__(self, string):
        return string * self.danger

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")


dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")
print(dr("Welcome"))
print(repr(dr))
