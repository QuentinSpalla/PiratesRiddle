from pirate import Pirate
import math


class Game():
    def __init__(self, nbr_coins, nbr_pirates, output_file):
        """
        Initialize the game and check the game could proceed
        :param nbr_coins: number coins to distribute
        :param nbr_pirates: number of pirates voting
        :param output_file: file used to print results
        """

        self.msg_error = 'Success'
        self.is_error = False
        self.output_file = output_file

        if nbr_coins < 0:
            self.is_error = True
            self.msg_error = 'Negative number of coins. Change parameters'
        elif nbr_pirates < 0:
            self.is_error = True
            self.msg_error = 'Negative number of pirates. Change parameters'
        elif nbr_coins < (nbr_pirates-1)/2:
            self.is_error = True
            self.msg_error = 'Too much pirates. First captain cannot survive'
        else:
            self.nbr_coins = nbr_coins
            self.nbr_pirates = nbr_pirates
            self.all_pirates = []

    def coins_distribution(self):
        """
        The captain's distribution
        1 to odd pirates
        0 to even pirates
        """
        curt_pirate = Pirate(1, self.nbr_coins-math.floor((self.nbr_pirates-1)/2), 0)
        self.all_pirates.append(curt_pirate)

        for curt_idx_pirate in range(2, self.nbr_pirates+1):
            curt_reward = curt_idx_pirate % 2
            curt_pirate = Pirate(curt_idx_pirate, curt_reward, 1-curt_reward)
            self.all_pirates.append(curt_pirate)

    def captain_survival(self):
        """
        :return: Checking if the captain survives thx to his distribution
        """
        nbr_votes_for_cap = 1
        for curt_pirate in self.all_pirates:
            if curt_pirate.vote_captain():
                nbr_votes_for_cap += 1

        if nbr_votes_for_cap > (self.nbr_pirates-1)/2:
            return True
        else:
            self.msg_error = 'The allocation does not allow the captain to survive'
            return False

    def write_in_txt(self):
        """
        :return: Writes all the result in a .txt file
        """
        text_file = open(self.output_file, "w")

        if self.is_error:
            text_file.write("Error in the game: %s" % self.msg_error)
        else:
            text_file.write(self.msg_error + "\n")

            for curt_pirate in self.all_pirates:
                text_file.write("Pirate number: "
                                + str(curt_pirate.order)
                                + " has a reward of "
                                + str(curt_pirate.reward)
                                + "\n")

        text_file.close()
