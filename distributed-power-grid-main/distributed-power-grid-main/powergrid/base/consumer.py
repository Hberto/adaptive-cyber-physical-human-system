from powergrid.base.agent import Agent
from powergrid.trade_objects import MarketResponse, Order


class BaseConsumer(Agent):
    """
    Base Consumer class, inherits from agent to be part of the network.
    Has to be implemented by all the other groups, following the naming scheme:
    'TeamXXConsumer'
    """
    def __init__(self, agent_id: int):
        """
        Constructor
        :param agent_id: Unique ID of this consumer
        """
        super().__init__(agent_id)

    def get_demand(self) -> Order:
        """
        Returns the current order (demand) for the simulation round
        :return: Current order of this consumer
        """
        ...

    def calc_demand(self) -> None:
        """
        Calculates the demand of this consumer in the simulation round.
        This is the place where the individual strategies are applied.
        :return: None
        """
        ...

    def pay(self) -> None:
        """
        Reduces the balance of the consumer based on the market response from the simulation round.
        :return: None
        """
        ...
