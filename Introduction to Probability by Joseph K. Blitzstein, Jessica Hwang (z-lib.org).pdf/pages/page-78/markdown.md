Conditional probability

$P(H|A)=\sum_{i=1}^{n}\frac{1}{2^{i}}P(H|A_{i})$

$P(H|F)=P(H|F_{c},A_{c})$

Solution:

As before, let $A$ be the event that the chosen coin lands Heads three times, and define a new event $H$ for the chosen coin landing Heads on the fourth toss. We are interested in $P(H|A)$. It would be very helpful to know whether we have the fair coin. LOTP with extra conditioning gives us $P(H|A)$ as a weighted average of $P(H|F,A)$ and $P(H|F^{c},A)$, and within these two conditional probabilities we do know whether we have the fair coin:

$P(H|A)$ $=P(H|F,A)P(F|A)+P(H|F^{c},A)P(F^{c}|A)$
$\approx\frac{1}{2}\cdot 0.23+\frac{3}{4}\cdot(1-0.23)$
$\approx 0.69.$

The posterior probabilities $P(F|A)$ and $P(F^{c}|A)$ are from our answer to Example 2.3.7.

An equivalent way to solve this problem is to define a new probability function $\tilde{P}$ such that for any event $B$, $\tilde{P}(B)=P(B|A)$. This new function assigns probabilities that are updated with the knowledge that $A$ occurred. Then by the ordinary law of total probability,

$\tilde{P}(H)=\tilde{P}(H|F)\tilde{P}(F)+\tilde{P}(H|F^{c})\tilde{P}(F^{c}),$

which is exactly the same as our use of LOTP with extra conditioning. This once again illustrates the principle that conditional probabilities are probabilities. ∎

###### Example 2.4.5 (Unanimous agreement).

The article “Why too much evidence can be a bad thing” by Lisa Zyga *[30]* says:

&gt; Under ancient Jewish law, if a suspect on trial was unanimously found guilty by all judges, then the suspect was acquitted. This reasoning sounds counterintuitive, but the legislators of the time had noticed that unanimous agreement often indicates the presence of systemic error in the judicial process.

There are $n$ judges deciding a case. The suspect has prior probability $p$ of being guilty. Each judge votes whether to convict or acquit the suspect. With probability $s$, a systemic error occurs (e.g., the defense is incompetent). If a systemic error occurs, then the judges unanimously vote to convict (i.e., all $n$ judges vote to convict).

Whether a systemic error occurs is independent of whether the suspect is guilty. Given that a systemic error doesn’t occur and that the suspect is guilty, each judge has probability $c$ of voting to convict, independently. Given that a systemic error doesn’t occur and that the suspect is not guilty, each judge has probability $w$ of voting to convict, independently. Suppose that

$0&lt;p&lt;1,\,0&lt;s&lt;1,\mbox{ and }0&lt;w&lt;\frac{1}{2}&lt;c&lt;1.$

(a) For this part only, suppose that exactly $k$ out of $n$ judges vote to convict, where $k&lt;n$. Given this information, find the probability that the suspect is guilty.