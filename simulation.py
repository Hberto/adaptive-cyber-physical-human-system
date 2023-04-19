from powergrid.base.consumer import BaseConsumer
from powergrid.base.producer import BaseProducer


class Simulation:
    """
    Simulation class
    """
    @staticmethod
    def run(rounds, consumers: list[BaseConsumer], producers: list[BaseProducer], market) -> None:
        """
        Main method that runs the simulation of the distributed power grid
        :param rounds: Maximum number of rounds
        :param consumers: All participating consumers
        :param producers: All participating producers
        :param market: The market
        :return: None
        """
        for curr_round in range(1, rounds+1):
            # consumers calculate their demands
            for c in consumers:
                c.calc_demand()

            # producers announce their bids
            for p in producers:
                p.announce_bid()

            # market calculates clearing price and notifies all agents
            market.clear()

            for c in consumers:
                c.pay()
                c.update_storage()

            for p in producers:
                p.process_orders()
                p.compute_cost_and_update_profit()
                p.adjust_production()
                p.update_storage()

            print(f'Simulation round {curr_round}')
