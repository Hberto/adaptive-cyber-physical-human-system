from market import Market
from simulation import Simulation
from powergrid.team03.consumer import Team03Consumer
from powergrid.team03.producer import Team03Producer

ROUNDS = 5

if __name__ == "__main__":
    consumers = [Team03Consumer(i) for i in range(ROUNDS)]
    producers = [Team03Producer(i + 5) for i in range(ROUNDS)]
    market = Market(consumers, producers)
    Simulation.run(ROUNDS, consumers, producers, market)
