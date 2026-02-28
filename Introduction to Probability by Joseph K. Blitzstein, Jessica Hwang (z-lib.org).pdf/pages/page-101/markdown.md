Introduction to Probability

# Conditioning on evidence

1.  A spam filter is designed by looking at commonly occurring phrases in spam. Suppose that 80% of email is spam. In 10% of the spam emails, the phrase “free money” is used, whereas this phrase is only used in 1% of non-spam emails. A new email has just arrived, which does mention “free money”. What is the probability that it is spam?
2.  A woman is pregnant with twin boys. Twins may be either identical or fraternal. Suppose that 1/3 of twins born are identical, that identical twins have a 50% chance of being both boys and a 50% chance of being both girls, and that for fraternal twins each twin independently has a 50% chance of being a boy and a 50% chance of being a girl. Given the above information, what is the probability that the woman’s twins are identical?
3. According to the CDC (Centers for Disease Control and Prevention), men who smoke are 23 times more likely to develop lung cancer than men who don’t smoke. Also according to the CDC, 21.6% of men in the U.S. smoke. What is the probability that a man in the U.S. is a smoker, given that he develops lung cancer?
4. Fred is answering a multiple-choice problem on an exam, and has to choose one of $n$ options (exactly one of which is correct). Let $K$ be the event that he knows the answer, and $R$ be the event that he gets the problem right (either through knowledge or through luck). Suppose that if he knows the right answer he will definitely get the problem right, but if he does not know then he will guess completely randomly. Let $P(K)=p$.

(a) Find $P(K|R)$ (in terms of $p$ and $n$).

(b) Show that $P(K|R)\geq p$, and explain why this makes sense intuitively. When (if ever) does $P(K|R)$ equal $p$?
5. Three cards are dealt from a standard, well-shuffled deck. The first two cards are flipped over, revealing the Ace of Spades as the first card and the 8 of Clubs as the second card. Given this information, find the probability that the third card is an ace in two ways: using the definition of conditional probability, and by symmetry.
6. A hat contains 100 coins, where 99 are fair but one is double-headed (always landing Heads). A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times. Given this information, what is the probability that the chosen coin is double-headed? (Of course, another approach here would be to look at both sides of the coin—but this is a metaphorical coin.)
7. A hat contains 100 coins, where at least 99 are fair, but there may be one that is double-headed (always landing Heads); if there is no such coin, then all 100 are fair. Let $D$ be the event that there is such a coin, and suppose that $P(D)=1/2$. A coin is chosen uniformly at random. The chosen coin is flipped 7 times, and it lands Heads all 7 times.

(a) Given this information, what is the probability that one of the coins is double-headed?

(b) Given this information, what is the probability that the chosen coin is double-headed?
8. The screens used for a certain type of cell phone are manufactured by 3 companies, A, B, and C. The proportions of screens supplied by A, B, and C are 0.5, 0.3, and 0.2, respectively, and their screens are defective with probabilities 0.01, 0.02, and 0.03, respectively. Given that the screen on such a phone is defective, what is the probability that Company A manufactured it?
9. (a) Show that if events $A_{1}$ and $A_{2}$ have the same prior probability $P(A_{1})=P(A_{2})$, $A_{1}$ implies $B$, and $A_{2}$ implies $B$, then $A_{1}$ and $A_{2}$ have the same posterior probability $P(A_{1}|B)=P(A_{2}|B)$ if it is observed that $B$ occurred.

(b) Explain why (a) makes sense intuitively, and give a concrete example.