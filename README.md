# PiratesRiddle

How to solve the pirates treasure riddle?

## Parameters
- n ordered pirates
- 100 coins treasure

## Game 
1/ first (captain) pirate gives a distribution
2/ all pirates vote to accept the distribution or kill the captain
3/ game is over if the distribution is accepted. Otherwise, the captain is killed, the second pirate becomes the new captain (n-1 pirates now)
4/ so far so long

## Solution
The captain keeps for himself 100-floor((n-1)/2) and gives 1 coin to every odd pirate (the 3th, the 5th, etc.)
Each pirate with a coin will vote for the captain to survive because if the don’t, with the new captain having the same tactic, they will be even pirates and get no coin.

## Optimality ?
This tactic is the optimal one for the captain because he cannot give less.
This is simple, the vote is democratic so at least 50% of the pirates has to vote for the captain’s survival. If the captain gives less than floor((n-1)/2) coins, less than 50% of the pirates will have a reward. With no current reward they do not have interest to vote for the captain survival.

## Code
Giving a number of pirates and a number of coins. The code will allocate the coins to every pirate.

- main.py 
- constants.py : contains parameters
- pirate.py : contains the Pirate class (attributes order, reward, last_reward)
- game.py : contains the class Game that makes the distribution of coins
- output.txt : the results of the allocation


Run the main.py file after changing parameters in constants.py