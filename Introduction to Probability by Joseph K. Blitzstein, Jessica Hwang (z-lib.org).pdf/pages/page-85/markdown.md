Two-step method: After the first test, the posterior odds of Fred having the disease are

$\frac{P(D|T_{1})}{P(D^{c}|T_{1})}=\frac{1}{99}\cdot\frac{0.95}{0.05}\approx 0.19,$

from the above. These posterior odds become the new prior odds, and then updating based on the second test gives

$\frac{P(D|T_{1}\cap T_{2})}{P(D^{c}|T_{1}\cap T_{2})}$ $=\frac{P(D|T_{1})}{P(D^{c}|T_{1})}\frac{P(T_{2}|D,T_{1})}{P(T_{2}|D^{c},T_{1})}$
$=\left(\frac{1}{99}\cdot\frac{0.95}{0.05}\right)\frac{0.95}{0.05}=\frac{361}{99}\approx 3.646,$

which is the same result as above.

Note that with a second positive test result, the probability that Fred has the disease jumps from 0.16 to 0.78, making us much more confident that Fred is actually afflicted with conditionitis. The moral of the story is that getting a second opinion is a good idea! $\square$

### 2.7 Conditioning as a problem-solving tool

Conditioning is a powerful tool for solving problems because it lets us engage in wishful thinking: when we encounter a problem that would be made easier if only we knew whether $E$ happened or not, we can condition on $E$ and then on $E^{c}$, consider these possibilities separately, then combine them using LOTP.

#### 2.7.1 Strategy: condition on what you wish you knew

###### Example 2.7.1 (Monty Hall).

On the game show Let’s Make a Deal, hosted by Monty Hall, a contestant chooses one of three closed doors, two of which have a goat behind them and one of which has a car. Monty, who knows where the car is, then opens one of the two remaining doors. The door he opens always has a goat behind it (he never reveals the car!). If he has a choice, then he picks a door at random with equal probabilities. Monty then offers the contestant the option of switching to the other unopened door. If the contestant’s goal is to get the car, should she switch doors?