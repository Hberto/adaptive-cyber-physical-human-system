from agent.producer import Producer
from agent.bid import Bid
from agent.market import Market

OUR_OPERATING_COST = 40
FULL_CAPACITY = 100
MINIMUM_CAPACITY = 30
EMPTY_STORAGE = 0


class SimpleStrategy(Producer):
    # 1. Gewinnmage an Speicherkapazität anpassen

    # 2. kein voller Speicher

    # 3. (Strategie bzgl. Nach Erhalt der Informationen vom Markt) Anpassung des Verkaufspreises

    # 4. Schwellenwert: 40 Betriebskosten ≤ Verkaufspreis

    # 5. Aussetzen (Beachte: Speicher und Marktpreis (Angebot und Nachfrage)

    def __init__(self):
        super().__init__()
        self._operating_cost = OUR_OPERATING_COST
        self._start_cost = 2
        self._shutdown_cost = 2
        self._min_performance = 0
        self._max_performance = 100
        self._current_performance = 50
        self._storage_capacity = 100
        self._unit_price = 5

    def announce_bid(self):
        print("SimpleProducerStrategy: Announce Bid")
        target_profit = 41  # ToDo: Adapt Target Profit
        if (self._storage == self._storage_capacity) \
                or (self._storage == EMPTY_STORAGE) \
                or OUR_OPERATING_COST > target_profit:
            costs = self._get_total_costs()
            self._unit_price = costs + target_profit
            self._bid = Bid(self._storage + self._current_performance, self._unit_price)

    def process_orders(self):
        print("SimpleProducerStrategy: Process Orders")
        total_amount = self._calculate_total_amount()
        remaining_amount = total_amount - self._current_performance
        new_storage = self._storage - remaining_amount
        if new_storage > self._storage_capacity:
            self._storage = self._storage_capacity
        if new_storage < 0:
            self._storage = 0

        self._storage = new_storage

    def compute_cost_and_update_profit(self):
        print("SimpleProducerStrategy: Compute Cost and Update Profit")
        costs = self._get_total_costs()
        total_orders = self._unit_price * self._calculate_total_amount()
        self._profit = self._profit + (total_orders - costs)
        self._balance += self._profit

    def adjust_production(self):
        print("SimpleProducerStrategy: Adjust Production")
        pass

    def _get_total_costs(self):
        return self._start_cost + self._shutdown_cost + self._operating_cost + Market.MARKET_FEE

    def _calculate_total_amount(self):
        return sum([order.amount for order in self._orders])
