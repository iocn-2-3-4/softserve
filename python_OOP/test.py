class Vehicle(object):

    base_sale_price = 0
    wheels = 0

    def __init__(self, miles, make, model, year, sold_on):
        self.miles = miles
        self.make = make
        self.model = model
        self.year = year
        self.sold_on = sold_on

    def sale_price(self):
        """Return the sale price for this vehicle as a float amount."""
        if self.sold_on is not None:
            return 0.0  # Already sold
        return 5000.0 * self.wheels

    def purchase_price(self):
        """Return the price for which we would pay to purchase the vehicle."""
        if self.sold_on is None:
            return 0.0  # Not yet sold
        return self.base_sale_price - (.10 * self.miles)

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        pass

class Car(Vehicle):
    """A car for sale by Jeffco Car Dealership."""

    base_sale_price = 8000
    wheels = 4
    def __init__(self,miles, make, model, year, sold_on, effCoeff):
        super(Car, self).__init__(miles, make, model, year, sold_on)
        self.effCoeff = effCoeff
        self.miles = self.miles*effCoeff
    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'car'

class Truck(Vehicle):
    """A truck for sale by Jeffco Car Dealership."""

    base_sale_price = 10000
    wheels = 4

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'truck'

class Motorcycle(Vehicle):
    """A motorcycle for sale by Jeffco Car Dealership."""

    base_sale_price = 4000
    wheels = 2

    def vehicle_type(self):
        """"Return a string representing the type of vehicle this is."""
        return 'motorcycle'


c = Car(20,"f","f","r",None,1)
print c.vehicle_type()
print c.purchase_price()
print c.sale_price()
print c.miles
