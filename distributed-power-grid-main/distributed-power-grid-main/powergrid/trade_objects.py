class Order:
    """
    Class that represents an order.
    Can be a bid by the consumers, or an offer by the producers.
    quantity == 0 => No Order
    """
    def __init__(self, agent_id: int = -1, quantity: int = 0, price: int = 0):
        """
        Constructor
        :param agent_id: ID of the agent that made the order.
        :param quantity: Amount of electricity units to be bought/sold.
        :param price: Price per unit.
        """
        self.agent_id = agent_id
        self.quantity = quantity
        self.price = price


class MarketResponse:
    """
    Class that represents a response from the market, after clearing.
    actual_quantity == 0 => No Response
    """
    def __init__(self, initial_order: Order = None, actual_quantity: int = 0, market_unit_price: int = 0, fee: int = 0):
        """
        Constructor
        :param initial_order: Initial order proposed to the market
        :param actual_quantity: Actual quantity of electricity units sold/bought.
        :param market_unit_price: Price per unit, calculated by the market.
        :param fee: Fee, that has to be paid to the market.
        """
        self.initial_order = initial_order
        self.actual_quantity = actual_quantity
        self.market_unit_price = market_unit_price
        self.fee = fee
