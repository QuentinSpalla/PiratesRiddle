
class Pirate():
    def __init__(self, order, reward, last_reward):
        """
        Initialize a pirate
        :param order: order of the pirate in the hierarchy
        :param reward: current reward in the captain tactic
        :param last_reward: future reward if the captain is killed (new captain having the same tactic than the former)
        """
        self.order = order
        self.reward = reward
        self.last_step_reward = last_reward

    def vote_captain(self):
        """
        :return: is the pirate voting for the captain's survival
        """
        return self.reward >= self.last_step_reward
