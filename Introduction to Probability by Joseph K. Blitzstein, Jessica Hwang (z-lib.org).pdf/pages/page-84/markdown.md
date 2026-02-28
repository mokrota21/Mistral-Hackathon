Conditional probability

# 2.6 Coherency of Bayes’ rule

An important property of Bayes’ rule is that it is coherent: if we receive multiple pieces of information and wish to update our probabilities to incorporate all the information, it does not matter whether we update sequentially, taking each piece of evidence into account one at a time, or simultaneously, using all the evidence at once. Suppose, for example, that we’re conducting a weeklong experiment that yields data at the end of each day. We could use Bayes’ rule every day to update our probabilities based on the data from that day. Or we could go on vacation for the week, come back on Friday afternoon, and update using the entire week’s worth of data. Either method will give the same result.

Let’s look at a concrete application of this principle.

###### Example 2.6.1 (Testing for a rare disease, continued).

Fred, who tested positive for conditionitis in Example 2.3.9, decides to get tested a second time. The new test is independent of the original test (given his disease status) and has the same sensitivity and specificity. Unfortunately for Fred, he tests positive a second time. Find the probability that Fred has the disease, given the evidence, in two ways: in one step, conditioning on both test results simultaneously, and in two steps, first updating the probabilities based on the first test result, and then updating again based on the second test result.

Solution:

Let $D$ be the event that he has the disease, $T_{1}$ that the first test result is positive, and $T_{2}$ that the second test result is positive. In Example 2.3.9, we used Bayes’ rule and the law of total probability to find $P(D|T_{1})$. Another quick solution uses the odds form of Bayes’ rule:

$\frac{P(D|T_{1})}{P(D^{c}|T_{1})}=\frac{P(D)}{P(D^{c})}\frac{P(T_{1}|D)}{P(T_{1}|D^{c})}=\frac{1}{99}\cdot\frac{0.95}{0.05}\approx 0.19.$

Since $P(D|T_{1})/(1-P(D|T_{1}))=0.19$, we have $P(D|T_{1})=0.19/(1+0.19)\approx 0.16$, in agreement with our answer from before. The odds form of Bayes’ rule is faster in this case because we don’t need to compute the unconditional probability $P(T_{1})$ in the denominator of the ordinary Bayes’ rule. Now, again using the odds form of Bayes’ rule, let’s find out what happens if Fred tests positive a second time.

One-step method: Updating based on both test results at once, we have

$\frac{P(D|T_{1}\cap T_{2})}{P(D^{c}|T_{1}\cap T_{2})}$ $=\frac{P(D)}{P(D^{c})}\frac{P(T_{1}\cap T_{2}|D)}{P(T_{1}\cap T_{2}|D^{c})}$
$=\frac{1}{99}\cdot\frac{0.95^{2}}{0.05^{2}}=\frac{361}{99}\approx 3.646,$

which corresponds to a probability of $0.78$.