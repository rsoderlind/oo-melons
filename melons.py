"""Classes for melon orders."""

from random import randint
from datetime import datetime

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!!!!")

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        """Calculate base price"""

        base_price = 0

        currenttime = datetime.now()

        if ((currenttime.hour > 8 and currenttime.hour < 11) and
            (currenttime.weekday() >= 0 and currenttime.weekday() <= 4)):
            base_price = 4
    

        base_price += randint(5, 9)
        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty,
                                                 "domestic",
                                                 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty,
                                                      "international",
                                                      0.17)

        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax, plus flat fee if less than 10"""

        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A Government Melon Order """

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(GovernmentMelonOrder, self).__init__(species, qty, 'government',
                                                   0)

        self.passed_inspection = False

    def mark_inspection(passed):
        """Mark the inspection as passed"""

        self.passed_inspection = passed


class TooManyMelonsError(ValueError):
    """Raises an error if there are too many melons"""

    pass
