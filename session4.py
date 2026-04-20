# Session 4 - ASTR 19 Code Journal

class Animal:
    def __init__(self, arms, leg_length, eyes, has_tail, is_furry):
        self.arms = arms
        self.leg_length = leg_length
        self.eyes = eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        print("Animal description:")
        print("Arms:", self.arms)
        print("Leg length:", self.leg_length)
        print("Eyes:", self.eyes)
        print("Has tail:", self.has_tail)
        print("Is furry:", self.is_furry)


def main():
    my_animal = Animal(0.0, 1.0, 2, True, True)
    my_animal.describe()


if __name__ == "__main__":
    main()