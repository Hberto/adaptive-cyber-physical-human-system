class Statistics(object):
    def __init__(self, rounds, consume_distribution):
        self.rounds = rounds
        self.consume_distribution = consume_distribution

    def print(self):
        print("=== Simulation Statistics ===")
        print("rounds:", self.rounds)
        print("consume distribution:", self.consume_distribution)
        print("=============================")
