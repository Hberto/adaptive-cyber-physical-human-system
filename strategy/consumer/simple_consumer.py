import random

import agent

class Simple_consumer(agent.Consumer):
    """Class for simple consumer agent"""

    def __init__(self, demand=12.0, unit_price=10.0):
        super().__init__(demand=demand, unit_price=unit_price)
        self._unit_price = 2

    def announce_bid(self):
        self._bid = agent.Bid(amount=self.demand, unit_price=self._unit_price)


    def pay(self):
        costs = 0
        for element in self._orders:
            costs += element.amount * element.price
            self.demand -= element.amount
        if self.demand < 12:
            self.demand = 12
        self._balance -= costs
