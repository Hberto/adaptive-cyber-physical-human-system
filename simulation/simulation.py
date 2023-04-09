import random

from agent import Market
from simulation.statistics import Statistics


class Simulation(object):
    def __init__(self,
                 market: Market,
                 rounds=5,
                 consume_distribution=10.0
                 ):
        self._rounds = rounds
        self._consume_distribution = consume_distribution
        self._market = market

    def run(self) -> Statistics:
        consumers = self._market.network().consumers()
        producers = self._market.network().producers()
        for t in range(self._rounds):
            for consumer in consumers:
                consumer._demand = consumer.demand + random.uniform(0, self._consume_distribution)

            for participant in consumers + producers:
                participant.announce_bid()

            self._market.clear()

            for consumer in consumers:
                consumer.pay()

            for producer in producers:
                producer.process_orders()
                producer.compute_cost_and_update_profit()
                producer.adjust_production()

            for i, consumer in enumerate(self._market.network().consumers()):
                print("Consumer " + str(i) + " Balance: " + str(consumer.getBalance()))

            for i, producer in enumerate(self._market.network().producers()):
                print("Producer " + str(i) + " Balance: " + str(producer.getBalance()))

        return self._calculate_statistics()

    def _calculate_statistics(self) -> Statistics:
        #for i, consumer in enumerate(self._market.network().consumers()):
         #   print("Consumer " + str(i) + " Balance: " + str(consumer.getBalance()))

        #for i, producer in enumerate(self._market.network().producers()):
           # print("Producer " + str(i) + " Balance: " + str(producer.getBalance()))
        return Statistics(self._rounds, self._consume_distribution)
