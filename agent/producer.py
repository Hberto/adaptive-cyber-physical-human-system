import agent
class Producer(agent.agent.Participant):
    """Base class for all producer agents"""

    def __init__(self, operating_cost=1, start_cost=1, shutdown_cost=1, min_performance=1, current_performance=1,
                 max_performance=1, storage_capacity=100, down_rate_limit=5, up_rate_limit=5):
        super().__init__()
        self._operating_cost = operating_cost
        self._start_cost = start_cost
        self._shutdown_cost = shutdown_cost
        self._max_performance = max_performance
        self._current_performance = current_performance
        self._min_performance = min_performance
        self._storage = 0
        self._storage_capacity = storage_capacity
        self._down_rate_limit = down_rate_limit
        self._up_rate_limit = up_rate_limit


    def announce_bid(self):
        raise NotImplementedError # ToDo: Impl

    def process_orders(self):
        raise NotImplementedError # ToDo: Impl

    def compute_cost_and_update_profit(self):
        raise NotImplementedError # ToDo: Impl

    def adjust_production(self):
        raise NotImplementedError # ToDo: Impl
