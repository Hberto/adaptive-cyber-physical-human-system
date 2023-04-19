from powergrid.base.consumer import BaseConsumer
from powergrid.trade_objects import Order


class Team04Consumer(BaseConsumer):
    """
    Simple Team04 Consumer implementation
    """

    def __init__(self, agent_id: int):
        super().__init__(agent_id)

    def get_demand(self) -> Order:
        return None

    def calc_demand(self) -> None:
        pass

    def pay(self) -> None:
        pass