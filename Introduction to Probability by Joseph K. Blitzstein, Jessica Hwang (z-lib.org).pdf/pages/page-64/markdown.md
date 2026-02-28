since there are 26 favorable possibilities for the *second* card, and for each of those, the first card can be any other card (recall from 1 that chronological order is not needed in the multiplication rule).

A neater way to see that $P(B)=1/2$ is by *symmetry*: from a vantage point before having done the experiment, the second card is equally likely to be any card in the deck.

We now have all the pieces needed to apply the definition of conditional probability:

$P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{25/204}{1/2}=\frac{25}{102},$
$P(B|A)=\frac{P(B\cap A)}{P(A)}=\frac{25/204}{1/4}=\frac{25}{51}.$

This is a simple example, but already there are several things worth noting.

1. It’s extremely important to be careful about which events to put on which side of the conditioning bar. In particular, $P(A|B)\neq P(B|A)$. The next section explores how $P(A|B)$ and $P(B|A)$ are related in general. Confusing these two quantities is called the *prosecutor’s fallacy* and is discussed in Section 2.8. If instead we had defined $B$ to be the event that the second card is a heart, then the two conditional probabilities would have been equal.

2. Both $P(A|B)$ and $P(B|A)$ make sense (intuitively and mathematically); the chronological order in which cards were chosen does not dictate which conditional probabilities we can look at. When we calculate conditional probabilities, we are considering what *information* observing one event provides about another event, not whether one event *causes* another. For further intuition, imagine that someone spreads out the cards and draws one card with their left hand and another card with their right hand, at the same time. Defining $A$ and $B$ based on the left hand’s card and the right hand’s card rather than the first card and second card would not change the structure of the problem in any important way.

3. We can also see that $P(B|A)=25/51$ by a direct interpretation of what conditional probability means: if the first card drawn is a heart, then the remaining cards consist of 25 red cards and 26 black cards (all of which are equally likely to be drawn next), so the conditional probability of getting a red card is $25/(25+26)=25/51$. It is harder to find $P(A|B)$ in this way: if we learn that the second card is red, we might think “that’s nice to know, but what we really want to know is whether it’s a heart!” The conditional probability results from later sections in this chapter give us methods for getting around this issue. ∎

To shed more light on what conditional probability means, here are two intuitive interpretations.