from powergrid.base.consumer import BaseConsumer


class Team03Consumer(BaseConsumer):
    """
    Dummy and example Consumer class for the market team.
    """
    def __init__(self, agent_id: int):
        super().__init__(agent_id)
