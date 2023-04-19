from powergrid.trade_objects import MarketResponse, Order


class Agent:
    """
    Base class that represents an agent in the network.
    Contains a unique ID, the balance of this agent, the current order placed on the market,
    the response from the market, after clearing and the storage of this agent
    """
    def __init__(self, agent_id: int):
        """
        Constructor
        :param agent_id: Unique ID of this agent
        """
        self.agent_id: int = agent_id
        self._balance: int = 0
        self._current_order: Order = Order()
        self._market_response: MarketResponse = MarketResponse()
        self._storage = 0

    def set_market_response(self, market_response: MarketResponse):
        """
        Gets called by the market to notify the agent about the result of the market clearance
        :param market_response: Personal response for this specific agent
        :return: None
        """
        self._market_response = market_response

    def update_storage(self) -> None:
        """
        Update the storage of this agent based on a strategy
        :return: None
        """
        ...
