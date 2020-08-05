class CalorieMate:
    def __init__(self):
        self.natrients = [
            "PROTEIN",
            "FAT",
            "CARBOHYDRATE",
            "VITAMIN",
            "MINERAL"
        ]

    def __str__(self):
        return "カロリーメイト リキッド"


class Human:
    def drink(self, calorie_mate: CalorieMate):
        print("{}には".format(calorie_mate))
        print("{}大栄養素が含まれています。".format(len(calorie_mate.natrients)))
        print("ぜひ飲んでください。")


if __name__ == "__main__":
    calorie_mate = CalorieMate()
    human = Human()
    
    human.drink(calorie_mate)
