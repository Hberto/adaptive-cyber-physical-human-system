import agent

class Simple_producer(agent.Producer):
    """A simple producer class that inherits from Producer"""

    def __init__(self, operating_cost=20, start_cost=2, shutdown_cost=2, min_performance=0, current_performance=10,
                 max_performance=100, storage_capacity=1):
        super().__init__(operating_cost=operating_cost, start_cost=start_cost, shutdown_cost=shutdown_cost,
                         min_performance=min_performance, current_performance=current_performance,
                         max_performance=max_performance, storage_capacity=storage_capacity)
        self._unit_price = 0

    def announce_bid(self):
        target_profit = 5
        costs = self._calculate_costs()
        self._unit_price = costs + target_profit
        self._bid = agent.Bid(self._storage + self._current_performance, self._unit_price)

    def process_orders(self):
        total_amount = self._calculate_total_amount()
        remaining_amount = total_amount - self._current_performance
        new_storage = self._storage - remaining_amount
        if new_storage > self._storage_capacity:
            self._storage = self._storage_capacity
        if new_storage < 0:
            self._storage = 0

        self._storage = new_storage
        self._orders = []

    def compute_cost_and_update_profit(self):
        self._balance = self._balance - self._calculate_costs() + self._unit_price * self._calculate_total_amount()

    def adjust_production(self):
        if self._current_performance < self._max_performance:
            self._current_performance += self._up_rate_limit

        if self._current_performance > self._max_performance:
            self._current_performance = self._up_rate_limit

        self._storage += self._current_performance
        pass

    def _calculate_costs(self):
        return self._start_cost + self._shutdown_cost + self._operating_cost + agent.Market.MARKET_FEE

    def _calculate_total_amount(self):
        return sum([order.amount for order in self._orders])

