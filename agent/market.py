import numpy as np

from shapely.geometry import LineString
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

        i_amount = 0
        i_price = 1
        i_agent = 2
        i_total_amount = 3

        consumer_bid = []
        for c in consumers:
            consumer_bid.append([c.bid().amount, c.bid().unit_price, c, 0])

        consumer_bid.sort(key=lambda x: (x[i_price], x[i_amount]))
        consumer_bid.reverse()

        producer_bid = []
        for p in producers:
            producer_bid.append([p.bid().amount, p.bid().unit_price, p, 0])

        producer_bid.sort(key=lambda x: (x[i_price], x[i_amount]))

        total_amount = 0
        for c in consumer_bid:
            total_amount += c[i_amount]
            c[i_total_amount] = total_amount

        total_amount = 0
        for p in producer_bid:
            total_amount += p[i_amount]
            p[i_total_amount] = total_amount

        try:
            while consumer_bid[-1][i_total_amount] > producer_bid[-1][i_total_amount] or consumer_bid[-1][i_price] < \
                    producer_bid[-1][i_price]:
                while consumer_bid[-1][i_total_amount] > producer_bid[-1][i_total_amount]:
                    consumer_bid.pop()

                while consumer_bid[-1][i_total_amount] < producer_bid[-1][i_total_amount] - producer_bid[-1][i_amount]:
                    producer_bid.pop()

                while consumer_bid[-1][i_price] < producer_bid[-1][i_price]:
                    consumer_bid.pop()

                while consumer_bid[-1][i_total_amount] < producer_bid[-1][i_total_amount] - producer_bid[-1][i_amount]:
                    producer_bid.pop()
        except IndexError:
            consumer_bid = []
            producer_bid = []

        amount_needed = 0
        for c_bid in consumer_bid:
            c_bid[2].add_order(Order(amount=c_bid[i_amount], unit_price=producer_bid[-1][i_price]))
            amount_needed += c_bid[i_amount]

        amount_produced = 0
        for p_bid in producer_bid:
            if amount_produced + p_bid[i_amount] < amount_needed:
                amount_produced += p_bid[i_amount]
                p_bid[i_agent].add_order(Order(amount=p_bid[i_amount], unit_price=producer_bid[-1][i_price]))

            elif amount_produced < amount_needed:
                p_bid[i_agent].add_order(
                    Order(amount=amount_needed - amount_produced, unit_price=producer_bid[-1][i_price]))
