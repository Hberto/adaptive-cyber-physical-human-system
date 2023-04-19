import numpy as np

from powergrid.base.consumer import BaseConsumer
from powergrid.base.producer import BaseProducer
from powergrid.trade_objects import MarketResponse, Order


class Market:
    """
    Implements the market in the simulation of the distributed power grid
    """
    def __init__(self, consumers: list[BaseConsumer], producers: list[BaseProducer]):
        """
        Constructor
        :param consumers: All consumers in the simulation
        :param producers: All producers in the simulation
        """
        self.consumers: list[BaseConsumer] = consumers
        self.producers: list[BaseProducer] = producers
        self.buy_orders: list[Order] = []
        self.sell_orders: list[Order] = []

    def _collect_all_orders(self) -> None:
        """
        Collects all orders from the agents and stores them according to buying or selling orders
        :return:
        """
        self.buy_orders = [c.get_demand() for c in self.consumers]
        self.sell_orders = [p.get_bid() for p in self.producers]

    def clear(self) -> None:
        """
        Main function of the market.
        Collects all order, calculates a clearing price and notifies all participating agents
        on the results
        :return: None
        """
        self._collect_all_orders()  # collect all orders

        # TODO: Implement merit order principle to calculate a clearing price
        clearing_price = np.random.randint(1, 150)
        calculated_fee = np.random.randint(1, 15)

        for c in self.consumers:
            dummy_market_response = MarketResponse(c.get_demand(),
                                                   np.random.randint(0, 50),
                                                   clearing_price, calculated_fee)
            c.set_market_response(dummy_market_response)

        for p in self.producers:
            dummy_market_response = MarketResponse(p.get_bid(),
                                                   np.random.randint(0, 300),
                                                   clearing_price, calculated_fee)
            p.set_market_response(dummy_market_response)

