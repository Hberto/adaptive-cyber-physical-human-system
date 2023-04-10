from typing import List
import networkx as nx  # ToDo: install package
from agent import Consumer, Producer


class MarketNetwork(object):
    def __init__(self, graph: nx.Graph):
        self._graph = graph
        self._consumers, self._producers = self._extract_participants()

    def graph(self):
        return self._graph

    def consumers(self) -> List[Consumer]:
        return self._consumers

    def producers(self) -> List[Producer]:
        return self._producers

    def _extract_participants(self):
        consumers: List[Consumer] = []
        producers: List[Producer] = []
        for n in self._graph.nodes():
            if issubclass(n.__class__, Producer):
                producers.append(n)
                continue
            if issubclass(n.__class__, Consumer):
                consumers.append(n)
                continue
            raise ValueError("Unsupported participant type!")
        return consumers, producers
