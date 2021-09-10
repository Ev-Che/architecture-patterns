from abc import ABC, abstractmethod

# Abstract furniture
"""
I am not mixing that 3 SAME interfaces in one,
because for that example we have small amount of 
fields in classes and for each type of furniture
they are the same. Speaking about expanding furniture
classes, their may appear some specific fields for 
each furniture type.

But due to Interface segregation principle, we can create
some small interfaces like 
`FurnitureWithLegs`, `SitableFurniture` that will have 
some of the fields.
"""

class AbstractChair(ABC):

    _legs: int = 4
    _material: str

    def can_sit_on_it(self) -> bool:
        return True

class AbstractSofa(ABC):

    _legs: int = 4
    _material: str

    def can_sit_on_it(self) -> bool:
        return True

class AbstractTable(ABC):

    _legs: int = 4
    _material: str

    def can_sit_on_it(self) -> bool:
        return False

## Certain furniture
class ModernChair(AbstractChair):
    _material: str = "Wood"

class ModernSofa(AbstractSofa):
    _material: str = "Wood"

class ModernTable(AbstractTable):
    _material: str = "Wood"

# Furniture sets
class AbstractFurnitureSet:
    """
    This is abstact factory that will validate,
    that all of the furniture are of the same
    type. So, then we don't need validation
    method to check, if they are of the same 
    style.
    """
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_sofa(self) -> AbstractSofa:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass

    def do_some_business_logic(self) -> None:
        for furniture in [
            self.create_chair(),
            self.create_sofa(),
            self.create_table()
        ]:
            print(f"There is {furniture.__class__.__name__}")

## Certain Furniture sets
class ModernFurnitureSet(AbstractFurnitureSet):
    
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_sofa(self) -> ModernSofa:
        return ModernSofa()

    def create_table(self) -> ModernTable:
        return ModernTable()

if __name__ == "__main__":
    ModernFurnitureSet().do_some_business_logic()