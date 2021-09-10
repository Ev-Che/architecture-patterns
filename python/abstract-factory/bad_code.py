"""
Problems:
1. `Chair`, `Sofa`, `Table` should have interfaces as their will be
    many types of that furniture.
2. `ModernFurniture` should have some sort of validator that will
    check if all of the furniture in the set is of the same type. 
"""

class Chair:

    _legs: int = 4
    _material: str = "Leather"
    
    @property
    def can_sit_on_it(self) -> bool:
        return True

class Sofa:

    _legs: int = 4
    _material: str = "Leather"

    @property
    def can_sit_on_it(self) -> bool:
        return True

class Table:

    _legs: int = 4
    _material: str = "Wood"

    @property
    def can_sit_on_it(self) -> bool:
        return False


class ModernChair(Chair):
    _material = "Wood"

class ModernSofa(Sofa):
    _material = "Wood"

class ModernTable(Table):
    _material = "Wood"


class ModernFurnitureSet:

    def __init__(
        self, 
        chair: ModernChair, 
        sofa: ModernSofa, 
        table: ModernTable
    ):
        self._chair = chair
        self._sofa = sofa
        self._table = table

    def is_same_style(self):
        return isinstance(self._chair, ModernChair) and \
            isinstance(self._sofa, ModernSofa) and \
                isinstance(self._table, ModernTable)

    def do_some_business_logic(self):
        for attr in self.__dict__.keys():
            print(f"There is {getattr(self, attr).__class__.__name__}")


if __name__ == "__main__":
    # We can easily switch any of that modern furnitures
    # to any other style furniture and our business logic
    # is not going to work.
    
    furniture_set = ModernFurnitureSet(
        ModernChair(),
        ModernSofa(),
        ModernTable()
    )

    if furniture_set.is_same_style():
        furniture_set.do_some_business_logic()