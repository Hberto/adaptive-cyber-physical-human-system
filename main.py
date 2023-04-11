import random

import networkx as nx
import agent
import market_network
from strategy.consumer import simple_cons
from strategy.producer import simple_prod

PARTICIPANTS = 10
P_PROD = 0.5
N_EPISODES = 1


def get_network_configuration():
    n_producers = int(PARTICIPANTS * P_PROD)
    n_consumers = PARTICIPANTS - n_producers
    num_edges = n_producers * n_consumers
    weights = [random.uniform(0, 1) for _ in range(num_edges)]
    return n_consumers, n_producers, weights


def create_network(n_producers, n_consumers, weights) -> market_network.MarketNetwork:
    producers = [simple_prod for _ in range(n_producers)]
    consumers = [simple_cons for _ in range(n_consumers)]
    g: nx.Graph = nx.complete_bipartite_graph(producers, consumers)
    for (u, v, w), weight in zip(g.edges(data=True), weights):
        w['weight'] = weight
    return market_network.MarketNetwork(graph=g)


def main():
    n_consumers, n_producers, weights = get_network_configuration()

    for i in range(N_EPISODES):
        network = create_network(n_producers, n_consumers, weights)

        simulation = simulation.Simulation(market=agent.Market(network))
        stats = simulation.run()
        stats.print()


if __name__ == '__main__':
    main()
