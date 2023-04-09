from agent import Bid
from agent.agent import Participant


class Consumer(Participant):
    """Base class for all consumer agents"""

    def __init__(self, demand=12.0, unit_price=10.0):
        super().__init__()
        self._unit_price = unit_price
        self._demand = demand

    def announce_bid(self):
        raise NotImplementedError # ToDo: Impl

    def pay(self):
        self._orders = []

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, demand):
        if demand < 0:
            raise ValueError("demand cannot be negative")
        self._demand = demand
