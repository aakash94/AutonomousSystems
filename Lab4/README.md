# project-6-rl
Trimmed down reinforcement project, and added Deep Q learning Pacman

LINK: https://inst.eecs.berkeley.edu/~cs188/sp21/project6/

Provide the formalisation of the above problem as an infinite-horizon discounted reward
MDP
M = ⟨S, A, (Pa)a∈A, r, s0, γ⟩,

Since the dice is 6 sided, N here is 6.

This means that you need to describe the set S of states for your problem, 

The state is represented by an array/list of length N+1. (N+1 is 7 for part A)
The ordering, while preserved in the list, is not essential to the representation of state.
Also, the length is N+1 (N+1 is 7 for part A) because of the pigeonhole principle, where the user will go bust at the N+1 th (N+1 is 7 for part A) number. 
 
Values 1-N represent the value of the dice. -1 represents no roll.
N+1(N+1 is 7 for part A) represents the <Stop>.

the initial state s0, 
[-1, -1, -1, -1, -1, -1, -1]

the set A of actions
Action 1: <Stop>
Action 2: Roll Dice



the transition probabilities Pa(s′|s) of going from state s to state s′ when taking action a (for each action a and pair of states s, s′), 
For Action 1: We add N to the state list, representing the end of the episode. 

For Action 2: With probability 1/N (N is 6 for part A) we add a number from the dice to the state list.


and the reward function r that encodes the reward r(a, s) obtained when taking action a in state s. 
Accumulated reward for Action 1: Product of  all numbers within the range (1,N) in the state list. 

Accumulated reward for Action 2: 0

To be faithful to the model seen in class, you also need to provide a discount factor γ
Γ = 0.9

