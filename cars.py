import logging

logging.basicConfig(level=logging.INFO)


class EnvironmentalError(Exception):
    pass


class TankCapacityError(Exception):
    pass


class RangeError(Exception):
    pass


class Car:
    def __init__(self, brand, tank_capacity, tanked_fuel, engine_type):
        self.brand = brand
        self.tank_capacity = tank_capacity
        self.tanked_fuel = tanked_fuel
        self.engine_type = self._is_valid_engine_type(engine_type)

        logging.info(
            f'New car of brand {self.brand}, with tank full in {round(100 * self.tanked_fuel/self.tank_capacity, 1)}%')

    def __repr__(self):
        return f'Car object at {hex(id(self))} registered under the {self.brand} brand, with tank full in {round(100 * self.tanked_fuel/self.tank_capacity, 1)}%'

    def _is_valid_engine_type(self, engine_type):
        if engine_type != 'Diesel' and engine_type != 'Gasoline':
            raise ValueError(
                'Value for engine type should be Diesel or Gasoline')
        return engine_type

    def fill_tank(self, liters=None):
        if liters != None and type(liters) != float and type(liters) != int:
            raise TypeError('Value should be a number')

        if self.engine_type == 'Diesel':
            raise EnvironmentalError(
                'ON fuel not available, because of environmental restrictions. Change engine as soon, as possible.')

        if liters == None:
            tanked_liters = self.tank_capacity - self.tanked_fuel
            self.tanked_fuel += tanked_liters
            return tanked_liters
        else:
            if liters > self.tank_capacity - self.tanked_fuel:
                raise TankCapacityError(
                    'Tank capacity is too small for this amount of fuel.')

            self.tanked_fuel += liters

            return liters

    def empty_tank(self, limit):
        if type(limit) != float and type(limit) != int:
            raise TypeError('Value should be a number')

        if limit < 0 or limit > 1:
            raise RangeError('The number should be in range between 0 and 1')

        emptied_liters = self.tanked_fuel * (1 - limit)
        self.tanked_fuel -= emptied_liters

        return emptied_liters
