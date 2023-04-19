from market import Market
from simulation import Simulation
from powergrid.team03.consumer import Team03Consumer
from powergrid.team03.producer import Team03Producer


if __name__ == "__main__":
    consumers = [Team03Consumer(i) for i in range(5)]
    producers = [Team03Producer(i + 5) for i in range(5)]
    market = Market(consumers, producers)
    Simulation.run(5, consumers, producers, market)
