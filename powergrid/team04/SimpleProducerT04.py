from powergrid.base.producer import BaseProducer
from powergrid.trade_objects import Order

OPERATING_COST = 20
START_COST = 2
SHUTDOWN_COST = 2
MIN_PERFORMANCE = 0
MAX_PERFORMANCE = 100


class Team04Producer(BaseProducer):

    def __init__(self, agent_id: int, quantity: int, price: int, current_performance: int):
        super().__init__(agent_id)
        self._operating_cost = OPERATING_COST
        self._start_cost = START_COST
        self._shutdown_cost = SHUTDOWN_COST
        self._current_performance = current_performance
        self.quantity = quantity
        self.price = price

    def get_bid(self) -> Order:
        return self._current_order

    def announce_bid(self) -> None:
        # Notizen
        # Speicher einbauen
        # Auf den Market Response reagieren
        # Balance beachten

        # ToDo: adjust normal case and else - basic impl
        """
        1. Normal Case: Sell everything, must be one higher than our costs
        2. Storage is empty or we are broke -> can't sell anything
        """
        if self._balance >= 0 and self._storage > 0:
            self.price = self._calculate_costs() + 1
            self.quantity = self._storage + self._current_performance
            self._current_order = Order(agent_id=self.agent_id, quantity=self.quantity, price=self.price)

        if self._balance < 0 or self._storage == 0:
            self.price = 0
            self.quantity = 0
            self._current_order = Order(agent_id=self.agent_id, quantity=self.quantity, price=self.price)

        else:
            self.quantity = self._storage + self._current_performance
            self.price = 1  # low price, sell anyway -> CHANGE
            self._current_order = Order(agent_id=self.agent_id, quantity=self.quantity, price=self.price)

    def process_orders(self) -> None:
        new_storage = self._storage + self._current_performance - self._market_response.actual_quantity
        if new_storage < 0:
            self._storage = 0
        self._storage = new_storage

    def compute_cost_and_update_profit(self) -> None:
        self._balance += self._calculate_total_amount_my_sell() - self._calculate_costs()

    def adjust_production(self) -> None:
        """
        if self._current_performance < self._max_performance:
            self._current_performance += self._up_rate_limit

        if self._current_performance > self._max_performance:
            self._current_performance = self._up_rate_limit
        """
        pass

    def _calculate_costs(self) -> int:
        return self._start_cost + self._shutdown_cost + self._operating_cost + self._market_response.fee

    def _calculate_total_amount_my_sell(self) -> int:
        return self._market_response.actual_quantity * self._market_response.market_unit_price

    def update_storage(self) -> None:
        print("Producer Agent id: %s , Current storage: %s, Balance: %s" % (self.agent_id, self._storage, self._balance))
