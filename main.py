import os

from market import Market
from powergrid.team03.consumer import Team03Consumer
from powergrid.team03.producer import Team03Producer
from simulation import Simulation
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    num_agents = int(os.getenv('NUM_AGENTS'))
    num_producers = int(float(os.getenv('PRODUCER_PROB')) * num_agents)
    num_consumers = num_agents - num_producers

    consumers = [Team03Consumer(i) for i in range(num_consumers)]
    producers = [Team03Producer(i + 5) for i in range(num_producers)]
    market = Market(consumers, producers)
    Simulation.run(int(os.getenv('NUM_ROUNDS')), consumers, producers, market)
