from agent.consumer import Consumer
from agent.bid import Bid
import random

OPERATING_COSTS = 40


class SimpleStrategy(Consumer):
    # 1. Speicherkapazität
    # darf nicht leer sein

    # 2. Anpassung des Einkaufspreises

    # 3. Schwellenwert der Betriebskosten

    # 4. (Aussetzen)

    def __int__(self):
        super().__init__()
        self._amount = self.demand
        self._unit_price = 0
        self._costs = 0

    def announce_bid(self):
        print("SimpleConsumerStrategy: Announce Bid")
        if self.storage <= 0.0:
            _amount = 100.0
            _unit_price = 100.0
            self._bid = Bid(amount=_amount, unit_price=_unit_price)
        else:
            _amount = random.uniform(0.0, 100.0)  # no logic yet
            _unit_price = random.uniform(0.0, 100.0)  # no logic yet
            self._bid = Bid(amount=_amount, unit_price=_unit_price)

    def pay(self):
        """consumers pay products and fees"""
        # ToDo: add fees: transport of product etc.
        print("SimpleConsumerStrategy: pay")
        for element in self._orders:
            self._costs += element.amount * element.unit_price
        self._balance -= self._costs

    def get_total_costs(self):
        return self._costs
