from powergrid.base.producer import BaseProducer


class Team03Producer(BaseProducer):
    """
    Dummy and example Producer class for the market team.
    """
    def __init__(self, agent_id: int):
        super().__init__(agent_id)
