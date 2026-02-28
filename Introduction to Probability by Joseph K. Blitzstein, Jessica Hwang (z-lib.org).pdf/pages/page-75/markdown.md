Introduction to Probability

Now let’s focus in on those individuals who test positive; that is, let’s condition on a positive test result. The 95 true positives (i.e., the individuals who test positive and have the disease) are far outnumbered by the 495 false positives (i.e., the individuals who test positive despite not having the disease). So most people who test positive for the disease don’t actually have the disease! ∎

###### Example 2.3.10 (Six-fingered man).

A crime has been committed in a certain country. The perpetrator is one (and only one) of the $n$ men who live in the country. Initially, these $n$ men are all deemed equally likely to be the perpetrator. An eyewitness then reports that the crime was committed by a man with six fingers on his right hand.

Let $p_{0}$ be the probability that an innocent man has six fingers on his right hand, and $p_{1}$ be the probability that the perpetrator has six fingers on his right hand, with $p_{0}&lt;p_{1}$. (We may have $p_{1}&lt;1$, since eyewitnesses are not 100% reliable.) Let $a=p_{0}/p_{1}$ and $b=(1-p_{1})/(1-p_{0})$.

Rugen lives in the country. He is found to have six fingers on his right hand.

(a) Given this information, what is the probability that Rugen is the perpetrator?

(b) Now suppose that all $n$ men who live in the country have their hands checked, and Rugen is the *only* one with six fingers on his right hand. Given this information, what is the probability that Rugen is the perpetrator?

Solution:

(a) Let $R$ be the event that Rugen is guilty and $M$ be the event that he has six fingers on his right hand. By Bayes’ rule and LOTP,

$P(R|M)=\frac{P(M|R)P(R)}{P(M|R)P(R)+P(M|R^{c})P(R^{c})}=\frac{p_{1}\cdot\frac{1}{n}}{p_{1}\cdot\frac{1}{n}+p_{0}\left(1-\frac{1}{n}\right)}=\frac{1}{1+a(n-1)}.$

(b) Let $N$ be the event that none of the men in the country other than Rugen have six fingers on their right hands. With notation as above,

$P(R|M,N)$ $=\frac{P(M,N|R)P(R)}{P(M,N|R)P(R)+P(M,N|R^{c})P(R^{c})}$
$=\frac{p_{1}(1-p_{0})^{n-1}\cdot\frac{1}{n}}{p_{1}(1-p_{0})^{n-1}\cdot\frac{1}{n}+p_{0}(1-p_{1})(1-p_{0})^{n-2}\left(1-\frac{1}{n}\right)}$
$=\frac{1}{1+ab(n-1)}.\qed$

##