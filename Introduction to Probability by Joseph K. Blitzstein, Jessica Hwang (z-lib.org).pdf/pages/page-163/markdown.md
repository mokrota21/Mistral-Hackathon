Introduction to Probability

42.  $\odot$  Let  $X$  be a random day of the week, coded so that Monday is 1, Tuesday is 2, etc. (so  $X$  takes values  $1, 2, \ldots, 7$ , with equal probabilities). Let  $Y$  be the next day after  $X$  (again represented as an integer between 1 and 7). Do  $X$  and  $Y$  have the same distribution? What is  $P(X &lt; Y)$ ?
43. (a) Is it possible to have two r.v.s  $X$  and  $Y$  such that  $X$  and  $Y$  have the same distribution but  $P(X &lt; Y) \geq p$ , where:

-  $p = 0.9?$
-  $p = 0.99?$
-  $p = 0.9999999999999?$
-  $p = 1$ ?

For each, give an example showing it is possible, or prove it is impossible.

Hint: Do the previous question first.

(b) Consider the same question as in Part (a), but now assume that  $X$  and  $Y$  are independent. Do your answers change?
44. For  $x$  and  $y$  binary digits (0 or 1), let  $x \oplus y$  be 0 if  $x = y$  and 1 if  $x \neq y$  (this operation is called exclusive or (often abbreviated to XOR), or addition mod 2).

(a) Let  $X \sim \operatorname{Bern}(p)$  and  $Y \sim \operatorname{Bern}(1/2)$ , independently. What is the distribution of  $X \oplus Y$ ?
(b) With notation as in (a), is  $X \oplus Y$  independent of  $X$ ? Is  $X \oplus Y$  independent of  $Y$ ? Be sure to consider both the case  $p = 1/2$  and the case  $p \neq 1/2$ .
(c) Let  $X_{1},\ldots ,X_{n}$  be i.i.d.  $\operatorname {Bern}(1 / 2)$  . For each nonempty subset  $J$  of  $\{1,2,\dots ,n\}$  , let

$$
Y _ {J} = \bigoplus_ {j \in J} X _ {j},
$$

where the notation means to "add" in the  $\oplus$  sense all the elements of  $J$ ; the order in which this is done doesn't matter since  $x \oplus y = y \oplus x$  and  $(x \oplus y) \oplus z = x \oplus (y \oplus z)$ . Show that  $Y_J \sim \operatorname{Bern}(1/2)$  and that these  $2^n - 1$  r.v.s are pairwise independent, but not independent. For example, we can use this to simulate 1023 pairwise independent fair coin tosses using only 10 independent fair coin tosses.

Hint: Apply the previous parts with  $p = 1/2$ . Show that if  $J$  and  $K$  are two different nonempty subsets of  $\{1, 2, \ldots, n\}$ , then we can write  $Y_J = A \oplus B$ ,  $Y_K = A \oplus C$ , where  $A$  consists of the  $X_i$  with  $i \in J \cap K$ ,  $B$  consists of the  $X_i$  with  $i \in J \cap K^c$ , and  $C$  consists of the  $X_i$  with  $i \in J^c \cap K$ . Then  $A, B, C$  are independent since they are based on disjoint sets of  $X_i$ . Also, at most one of these sets of  $X_i$  can be empty. If  $J \cap K = \emptyset$ , then  $Y_J = B$ ,  $Y_K = C$ . Otherwise, compute  $P(Y_J = y, Y_K = z)$  by conditioning on whether  $A = 1$ .

## Mixed practice

45.  $\odot$  A new treatment for a disease is being tested, to see whether it is better than the standard treatment. The existing treatment is effective on  $50\%$  of patients. It is believed initially that there is a 2/3 chance that the new treatment is effective on  $60\%$  of patients, and a 1/3 chance that the new treatment is effective on  $50\%$  of patients. In a pilot study, the new treatment is given to 20 random patients, and is effective for 15 of them.

(a) Given this information, what is the probability that the new treatment is better than the standard treatment?
(b) A second study is done later, giving the new treatment to 20 new random patients. Given the results of the first study, what is the PMF for how many of the new patients the new treatment is effective on? (Letting  $p$  be the answer to (a), your answer can be left in terms of  $p$ .)