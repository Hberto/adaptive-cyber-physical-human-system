from agent.agent import Agent
from agent.agent import Order
from market_network.market_network import MarketNetwork


class Market(Agent):
    """Example implementation class of a market agent"""

    MARKET_FEE = 1

    def __init__(self, network: MarketNetwork):
        self._network = network

    def network(self) -> MarketNetwork:
        return self._network

    def clear(self):
        consumers = self._network.consumers()
        producers = self._network.producers()
        p = producers[0]
        for c in consumers:
            bid = c.bid()
            c.add_order(Order(amount=bid.amount, unit_price=bid.unit_price))
            p.add_order(Order(amount=bid.amount, unit_price=bid.unit_price))
