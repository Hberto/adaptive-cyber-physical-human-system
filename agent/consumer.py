from agent.agent import Participant


class Consumer(Participant):
    """Base class for all consumer agents"""

    def __init__(self, demand=0.0, storage=0.0):
        super().__init__()
        self._demand = demand
        self._storage = storage

    def announce_bid(self):
        pass

    def pay(self):
        self._orders = []

    # ToDo: update_storage()
    def update_storage(self):
        pass

    @property
    def storage(self):
        return self._storage

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, demand):
        if demand < 0:
            raise ValueError("demand cannot be negative")
        self._demand = demand

    @storage.setter
    def storage(self, storage):
        if storage < 0:
            raise ValueError("storage cannot be negative")
        self._storage = storage
