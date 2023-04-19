from powergrid.base.producer import BaseProducer
from powergrid.trade_objects import Order


class Team04Producer(BaseProducer):

    def __init__(self, agent_id: int):
        super().__init__(agent_id)

    def get_bid(self) -> Order:
        """
        Returns the current order (bid) for the simulation round
        :return: Current order of this producer
        """
        ...

    def announce_bid(self) -> None:
        """
        Calculates the bid of this producer in the simulation round.
        This is the place where the individual strategies are applied.
        :return: None
        """
        ...

    def process_orders(self) -> None:
        """
        Processes the accepted orders from the consumers.
        :return:
        """
        ...

    def compute_cost_and_update_profit(self) -> None:
        """
        Compute costs and update profit margin
        :return:
        """
        ...

    def adjust_production(self) -> None:
        """
        Adjust production based on a strategy and market_response
        :return:
        """
        ...
