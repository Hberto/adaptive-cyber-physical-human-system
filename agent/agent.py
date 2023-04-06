from agent.bid import Bid
from agent.order import Order


class Agent(object):
    """Base class agent for the whole system"""
    pass


class Participant(Agent):
    """Base class for all agents that can participate in the market.
    This includes all consumers and producers."""

    def __init__(self):
        self._orders = []
        self._bid = None

    def announce_bid(self) -> Bid:
        raise NotImplementedError  # ToDo: Impl

    def add_order(self, order: Order):
        self._orders.append(order)

    def bid(self) -> Bid:
        return self._bid
