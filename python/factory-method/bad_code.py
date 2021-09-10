"""
Problems:
1. `Truck` and `Boat` are not scalable as they are both Vehicles, but
    the whole realization is different => It is better to create the
    interface for this Vehicles
2. `Logistic` class should better be divided onto several specific
    Logistics for every type of Vehicles. That will give us the 
    opportunity to create specific business logic for every type of 
    Logistic.
3. Create `Factory-Method` to avoide hard-code creation of Vehicles. 
"""

from typing import Union


class Truck:
    
    def prepare_truck(self):
        print("Truck is prepared!")

    def deliver(self):
        print("Delivered by truck")

class Boat:

    def prepare_boat(self):
        print("Boat is prepared!")

    def deliver(self):
        print("Delivered by truck")

class Logistic:

    def do_some_business_logic(self, transport: Union[Truck, Boat]):
        """
        If we will add more types of transport, we will have a huge
        code that is not scaleable.
        """
        if isinstance(transport, Truck):
            transport.prepare_truck()
        elif isinstance(transport, Boat):
            transport.prepare_boat()
        else:
            raise Exception("Transport not found")
        
        transport.deliver()

if __name__ == "__main__":
    boat = Boat()
    truck = Truck()

    massive_logistic = Logistic()
    massive_logistic.do_some_business_logic(truck)
    massive_logistic.do_some_business_logic(boat)