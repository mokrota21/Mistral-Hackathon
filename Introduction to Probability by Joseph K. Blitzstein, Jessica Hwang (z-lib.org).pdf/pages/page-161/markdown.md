32. In Evan’s history class, 10 out of 100 key terms will be randomly selected to appear on the final exam; Evan must then choose 7 of those 10 to define. Since he knows the format of the exam in advance, Evan is trying to decide how many key terms he should study.

1. Suppose that Evan decides to study $s$ key terms, where $s$ is an integer between 0 and 100. Let $X$ be the number of key terms appearing on the exam that he has studied. What is the distribution of $X$? Give the name and parameters, in terms of $s$.
2. Using R or other software, calculate the probability that Evan knows at least 7 of the 10 key terms that appear on the exam, assuming that he studies $s=75$ key terms.
33. A book has $n$ typos. Two proofreaders, Prue and Frida, independently read the book. Prue catches each typo with probability $p_{1}$ and misses it with probability $q_{1}=1-p_{1}$, independently, and likewise for Frida, who has probabilities $p_{2}$ of catching and $q_{2}=1-p_{2}$ of missing each typo. Let $X_{1}$ be the number of typos caught by Prue, $X_{2}$ be the number caught by Frida, and $X$ be the number caught by at least one of the two proofreaders.

1. Find the distribution of $X$.
2. For this part only, assume that $p_{1}=p_{2}$. Find the conditional distribution of $X_{1}$ given that $X_{1}+X_{2}=t$.
34. There are $n$ students at a certain school, of whom $X\sim{\rm Bin}(n,p)$ are Statistics majors. A simple random sample of size $m$ is drawn (“simple random sample” means sampling without replacement, with all subsets of the given size equally likely).

1. Find the PMF of the number of Statistics majors in the sample, using the law of total probability (don’t forget to say what the support is). You can leave your answer as a sum (though with some algebra it can be simplified, by writing the binomial coefficients in terms of factorials and using the binomial theorem).
2. Give a story proof derivation of the distribution of the number of Statistics majors in the sample; simplify fully.

Hint: Does it matter whether the students declare their majors before or after the random sample is drawn?
35. Players A and B take turns in answering trivia questions, starting with player A answering the first question. Each time A answers a question, she has probability $p_{1}$ of getting it right. Each time B plays, he has probability $p_{2}$ of getting it right.

1. If A answers $m$ questions, what is the PMF of the number of questions she gets right?
2. If A answers $m$ times and B answers $n$ times, what is the PMF of the total number of questions they get right (you can leave your answer as a sum)? Describe exactly when/whether this is a Binomial distribution.
3. Suppose that the first player to answer correctly wins the game (with no predetermined maximum number of questions that can be asked). Find the probability that A wins the game.
36. There are $n$ voters in an upcoming election in a certain country, where $n$ is a large, even number. There are two candidates: Candidate A (from the Unite Party) and Candidate B (from the Untie Party). Let $X$ be the number of people who vote for Candidate A. Suppose that each voter chooses randomly whom to vote for, independently and with equal probabilities.

1. Find an exact expression for the probability of a tie in the election (so the candidates end up with the same number of votes).