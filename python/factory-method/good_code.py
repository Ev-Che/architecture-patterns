from abc import ABC, abstractmethod

# Vehicles
class AbstractVehicle(ABC):
    """ Abstract class for all of the Vehicles. """

    @abstractmethod
    def deliver(self) -> None:
        pass

    @abstractmethod
    def prepare_vehicle(self) -> None:
        pass

## Certain vehicles
class Boat(AbstractVehicle):
    
    def deliver(self) -> None:
        print("Delivered by Boat")

    def prepare_vehicle(self) -> None:
        print("Boat is prepared!")

class Truck(AbstractVehicle):
    
    def deliver(self) -> None:
        print("Delivered by Truck")

    def prepare_vehicle(self) -> None:
        print("Truck is prepared!")


# Logistics
class BaseLogistic(ABC):
    
    @abstractmethod
    def create_vehicle(self) -> AbstractVehicle:
        """ 
        Factory method, that needs to be overwritten by 
        specific logistic class.
        """
        pass

    def do_some_business_logic(self) -> None:
        vehicle = self.create_vehicle()
        vehicle.prepare_vehicle()
        vehicle.deliver()

## Certain Logistics
class LandLogistic(BaseLogistic):

    def create_vehicle(self) -> AbstractVehicle:
        return Truck()

class SeaLogistic(BaseLogistic):

    def create_vehicle(self) -> AbstractVehicle:
        return Boat()


if __name__ == "__main__":
    LandLogistic().do_some_business_logic()
    SeaLogistic().do_some_business_logic()