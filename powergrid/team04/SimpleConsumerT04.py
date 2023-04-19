import random

from powergrid.base.consumer import BaseConsumer
from powergrid.trade_objects import Order


VOLATILE_PRICE = 1
class Team04Consumer(BaseConsumer):
    """
    Simple Team04 Consumer implementation
    """

    def __init__(self, agent_id: int, demand: int, consume_distribution: int, price: int):
        super().__init__(agent_id)
        self._consume_distribution = consume_distribution
        self.demand = demand
        self.price = price

    def get_demand(self) -> Order:
        self._current_order = Order(agent_id=self.agent_id, quantity=self.demand, price=self.price)
        return self._current_order

    def calc_demand(self) -> None:
        self.demand = self.demand + random.uniform(0, self._consume_distribution)

    def pay(self) -> None:
        if self._market_response.actual_quantity == 0:
            self.price += VOLATILE_PRICE
        else:
            self.price -= VOLATILE_PRICE
            self._balance = self._balance - self._market_response.fee + self._market_response.actual_quantity * \
                            self._market_response.market_unit_price

    def update_storage(self) -> None:
        if self._market_response.actual_quantity != 0:
            self._storage -= self._market_response.actual_quantity
        #Debug Here?
        print("Agent id: %s , Current demand: %s, Balance: %s" % (self.agent_id, self.demand, self._balance))
