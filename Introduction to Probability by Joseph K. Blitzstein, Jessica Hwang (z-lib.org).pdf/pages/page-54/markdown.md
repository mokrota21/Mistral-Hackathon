24. A certain family has 6 children, consisting of 3 boys and 3 girls. Assuming that all birth orders are equally likely, what is the probability that the 3 eldest children are the 3 girls?
25. A city with 6 districts has 6 robberies in a particular week. Assume the robberies are located randomly, with all possibilities for which robbery occurred where equally likely. What is the probability that some district had more than 1 robbery?
26. A survey is being conducted in a city with 1 million residents. It would be far too expensive to survey all of the residents, so a random sample of size 1000 is chosen (in practice, there are many challenges with sampling, such as obtaining a complete list of everyone in the city, and dealing with people who refuse to participate). The survey is conducted by choosing people one at a time, *with* replacement and with equal probabilities.

(a) Explain how sampling with vs. without replacement here relates to the birthday problem.

(b) Find the probability that at least one person will get chosen more than once.
27. A *hash table* is a commonly used data structure in computer science, allowing for fast information retrieval. For example, suppose we want to store some people’s phone numbers. Assume that no two of the people have the same name. For each name $x$, a *hash function* $h$ is used, letting $h(x)$ be the location that will be used to store $x$’s phone number. After such a table has been computed, to look up $x$’s phone number one just recomputes $h(x)$ and then looks up what is stored in that location.

The hash function $h$ is deterministic, since we don’t want to get different results every time we compute $h(x)$. But $h$ is often chosen to be *pseudorandom*. For this problem, assume that true randomness is used. Let there be $k$ people, with each person’s phone number stored in a random location (with equal probabilities for each location, independently of where the other people’s numbers are stored), represented by an integer between 1 and $n$. Find the probability that at least one location has more than one phone number stored there.
28. A college has 10 time slots for its courses, and blithely assigns courses to completely random time slots, independently. The college offers exactly 3 statistics courses. What is the probability that 2 or more of the statistics courses are in the same time slot?
29. For each part, decide whether the blank should be filled in with $=$, $<$, or $>$, and give a clear explanation.

(a) (probability that the total after rolling 4 fair dice is 21) ___ (probability that the total after rolling 4 fair dice is 22)

(b) (probability that a random 2-letter word is a palindrome) ___ (probability that a random 3-letter word is a palindrome)
30. With definitions as in the previous problem, find the probability that a random $n$-letter word is a palindrome for $n=7$ and for $n=8$.
31. Elk dwell in a certain forest. There are $N$ elk, of which a simple random sample of size $n$ are captured and tagged (“simple random sample” means that all $\binom{N}{n}$ sets of $n$ elk are equally likely). The captured elk are returned to the population, and then a new sample is drawn, this time with size $m$. This is an important method that is widely used in ecology, known as *capture-recapture*. What is the probability that exactly $k$ of the $m$