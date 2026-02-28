Introduction to Probability

The contestant chooses a door. If this initial choice has the car, Monty *will* open another door, revealing a goat (choosing with equal probabilities among his two choices of door), and then offer the contestant the choice of whether to switch to the other unopened door.

If the contestant’s initial choice has a goat, then with probability $p$ Monty *will* open another door, revealing a goat, and then offer the contestant the choice of whether to switch to the other unopened door; but with probability $1-p$, Monty will *not* open a door, and the contestant must stick with their initial choice.

The contestant decides in advance to use the following strategy: initially choose door 1. Then, if Monty opens a door and offers the choice of whether to switch, do switch.

1. Find the unconditional probability that the contestant will get the car. Also, check what your answer reduces to in the extreme cases $p=0$ and $p=1$, and briefly explain why your answer makes sense in these two cases.

2. Monty now opens door 2, revealing a goat. So the contestant switches to door 3. Given this information, find the conditional probability that the contestant will get the car.
2. You are the contestant on the Monty Hall show. Monty is trying out a new version of his game, with rules as follows. You get to choose one of three doors. One door has a car behind it, another has a computer, and the other door has a goat (with all permutations equally likely). Monty, who knows which prize is behind each door, will open a door (but not the one you chose) and then let you choose whether to switch from your current choice to the other unopened door.

Assume that you prefer the car to the computer, the computer to the goat, and (by transitivity) the car to the goat.

1. Suppose for this part only that Monty always opens the door that reveals your less preferred prize out of the two alternatives, e.g., if he is faced with the choice between revealing the goat or the computer, he will reveal the goat. Monty opens a door, revealing a goat (this is again for this part only). Given this information, should you switch? If you do switch, what is your probability of success in getting the car?

2. Now suppose that Monty reveals your less preferred prize with probability $p$, and your more preferred prize with probability $q=1-p$. Monty opens a door, revealing a computer. Given this information, should you switch (your answer can depend on $p$)? If you do switch, what is your probability of success in getting the car (in terms of $p$)?
3. Monty Hall has introduced a new twist in his game, by generalizing the assumption that the initial probabilities for where the car is are $(\frac{1}{3},\frac{1}{3},\frac{1}{3})$. Specifically, there are three doors, behind one of which there is a car (which the contestant wants), and behind the other two of which there are goats (which the contestant doesn’t want). Initially, door $i$ has probability $p_{i}$ of having the car, where $p_{1},p_{2},p_{3}$ are known constants such that $0&lt;p_{1}\leq p_{2}\leq p_{3}&lt;1$ and $p_{1}+p_{2}+p_{3}=1$. The contestant chooses a door. Then Monty opens a door (other than the one the contestant chose) and offers the contestant the option of switching to the other unopened door.

1. Assume for this part that Monty knows in advance which door has the car. He always opens a door to reveal a goat, and if he has a choice of which door to open he chooses with equal probabilities. Suppose for this part that the contestant initially chooses door 3, and then Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch doors? (If whether to switch depends on the $p_{i}$’s, give a fully simplified criterion in terms of the $p_{i}$’s.)

2. Now assume instead that Monty does *not* know in advance where the car is. He randomly chooses which door to open (other than the one the contestant chose), with equal probabilities. (The game is spoiled if he reveals the car.) Suppose again that the