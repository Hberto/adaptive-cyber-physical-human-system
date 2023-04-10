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

        amount_needed = 0
        consumer_bid = []
        for c in consumers:
            consumer_bid.append((c.bid().amount, c.bid().unit_price, c))
            amount_needed += c.bid().amount

        consumer_bid.sort(key=lambda x: (x[1], x[0]))

        producer_bid = []
        for p in producers:
            producer_bid.append((p.bid().amount, p.bid().unit_price, p))

        producer_bid.sort(key=lambda x: (x[1], x[0]))

        amount = 0
        price = 0

        for i in range(0, len(producer_bid)):
            p_bid = producer_bid[i]
            while p_bid[1] > consumer_bid[0][1] and amount < amount_needed:
                amount_needed -= consumer_bid[0][0]
                consumer_bid.pop(0)

            if amount > amount_needed:

                i -= 1
                if i >= 0:
                    while (amount - producer_bid[i][0]) >= amount_needed:
                        amount -= producer_bid[i][0]
                        i -= 1
                        if i >= 0:
                            price = producer_bid[i][1]
                        else:
                            price = 0
                            amount = 0
                            break
                break
            else:
                amount += p_bid[0]
                price = p_bid[1]
                if amount > amount_needed:
                    break

        for c_bid in consumer_bid:
            c = c_bid[2]
            bid = c.bid()
            c.add_order(Order(amount=bid.amount, unit_price=price))

        amount_produced = 0
        for p_bid in producer_bid:
            if amount_produced + p_bid[0] < amount_needed:
                amount_produced += p_bid[0]
                p = p_bid[2]
                bid = p.bid()
                p.add_order(Order(amount=bid.amount, unit_price=price))
            elif amount_produced < amount_needed:
                p = p_bid[2]
                p.add_order(Order(amount=amount_needed - amount_produced, unit_price=price))
                amount_produced = amount_needed
