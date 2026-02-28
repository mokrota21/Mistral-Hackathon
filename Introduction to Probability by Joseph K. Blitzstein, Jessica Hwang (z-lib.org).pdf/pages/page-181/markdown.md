Introduction to Probability

# 4.4 Indicator r.v.s and the fundamental bridge

This section is devoted to *indicator random variables*, which we already encountered in the previous chapter but will treat in much greater detail here. In particular, we will show that indicator r.v.s are an extremely useful tool for calculating expected values.

Recall from the previous chapter that the indicator r.v. $I_{A}$ (or $I(A)$) for an event $A$ is defined to be 1 if $A$ occurs and 0 otherwise. So $I_{A}$ is a Bernoulli random variable, where success is defined as “$A$ occurs” and failure is defined as “$A$ does not occur”. Some useful properties of indicator r.v.s are summarized below.

###### Theorem 4.4.1 (Indicator r.v. properties).

Let $A$ and $B$ be events. Then the following properties hold.

1. $(I_{A})^{k}=I_{A}$ for any positive integer $k$.
2. $I_{A^{c}}=1-I_{A}$.
3. $I_{A\cap B}=I_{A}I_{B}$.
4. $I_{A\cup B}=I_{A}+I_{B}-I_{A}I_{B}$.

###### Proof.

Property 1 holds since $0^{k}=0$ and $1^{k}=1$ for any positive integer $k$. Property 2 holds since $1-I_{A}$ is 1 if $A$ does not occur and 0 if $A$ occurs. Property 3 holds since $I_{A}I_{B}$ is 1 if both $I_{A}$ and $I_{B}$ are 1, and 0 otherwise. Property 4 holds since

$I_{A\cup B}=1-I_{A^{c}\cap B^{c}}=1-I_{A^{c}}I_{B^{c}}=1-(1-I_{A})(1-I_{B})=I_{A}+I_{B}-I_{A}I_{B}.$ ∎

Indicator r.v.s provide a link between probability and expectation; we call this fact the *fundamental bridge*.

###### Theorem 4.4.2 (Fundamental bridge between probability and expectation).

There is a one-to-one correspondence between events and indicator r.v.s, and the probability of an event $A$ is the expected value of its indicator r.v. $I_{A}$:

$P(A)=E(I_{A}).$

###### Proof.

For any event $A$, we have an indicator r.v. $I_{A}$. This is a one-to-one correspondence since $A$ uniquely determines $I_{A}$ and vice versa (to get from $I_{A}$ back to $A$, we can use the fact that $A=\{s\in S:I_{A}(s)=1\}$). Since $I_{A}\sim\text{Bern}(p)$ with $p=P(A)$, we have $E(I_{A})=P(A)$. ∎

The fundamental bridge connects events to their indicator r.v.s, and allows us to express *any* probability as an expectation. As an example, we give a short proof of inclusion-exclusion and a related inequality known as *Boole’s inequality* or *Bonferroni’s inequality* using indicator r.v.s.

##