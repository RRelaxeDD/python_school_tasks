class Phone:

    def is_foldable(self): pass

class RegularPhone(Phone):

    def __init__(self, name) -> None:
        self.name = name

    def is_foldable(self):
        return False

class FoldablePhone(Phone):

    def __init__(self, name) -> None:
        self.name = name

    def is_foldable(self):
        return True

phones = [RegularPhone("regular phone"), FoldablePhone("foldable phone")]

for i in phones:
    print(i.is_foldable())