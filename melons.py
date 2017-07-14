"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == 'Christmas Melon':
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

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

        super(GovernmentMelonOrder, self).__init__(species, qty, 'government'
                                                      0)

        self.passed_inspection = False


    def mark_inspection(passed):
     
        self.passed_inspection = passed 