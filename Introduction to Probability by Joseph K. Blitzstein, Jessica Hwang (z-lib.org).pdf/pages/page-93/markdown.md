Introduction to Probability

Let  $A$  be the event that the husband commits abuse against his wife, and let  $G$  be the event that the husband is guilty. The defense's argument is that  $P(G|A) = 1/10,000$ , so guilt is still extremely unlikely conditional on a previous history of abuse.

However, the defense attorney fails to condition on a crucial fact: in this case, we know that the wife was murdered. Therefore, the relevant probability is not  $P(G|A)$ , but  $P(G|A, M)$ , where  $M$  is the event that the wife was murdered.

Bayes' rule with extra conditioning gives

$$
\begin{array}{l} P (G | A, M) = \frac {P (A | G , M) P (G | M)}{P (A | G , M) P (G | M) + P (A | G ^ {c} , M) P (G ^ {c} | M)} \\ = \frac {0 . 5 \cdot 0 . 2}{0 . 5 \cdot 0 . 2 + 0 . 1 \cdot 0 . 8} \\ = \frac {5}{9}. \\ \end{array}
$$

So the posterior probability of guilt,  $P(G|A, M)$ , is over 5,000 times as large as the quantity  $P(G|A)$  that the defense attorney focused on. Conditioning on the evidence of abuse increases the probability of guilt from  $P(G|M) = 0.2$  to  $P(G|A, M) \approx 0.56$ , so the defendant's history of abuse gives very important information, contrary to the defense attorney's argument.

In the above calculation of  $P(G|A, M)$ , we did not use the defense attorney's  $P(G|A)$  number anywhere; it is irrelevant to our calculation because it does not account for the fact that the wife was murdered. We must condition on all the evidence.

We end this chapter with a paradox about conditional probability and aggregation of data.

Example 2.8.3 (Simpson's paradox). Two doctors, Dr. Hibbert and Dr. Nick, each perform two types of surgeries: heart surgery and Band-Aid removal. Each surgery can be either a success or a failure. The two doctors' respective records are given in the following tables, and shown graphically in Figure 2.6, where white dots represent successful surgeries and black dots represent failed surgeries.

|   | Heart | Band-Aid  |
| --- | --- | --- |
|  Success | 70 | 10  |
|  Failure | 20 | 0  |

Dr. Hibbert

|   | Heart | Band-Aid  |
| --- | --- | --- |
|  Success | 2 | 81  |
|  Failure | 8 | 9  |

Dr. Nick

Dr. Hibbert had a higher success rate than Dr. Nick in heart surgeries: 70 out of 90 versus 2 out of 10. Dr. Hibbert also had a higher success rate in Band-Aid removal: 10 out of 10 versus 81 out of 90. But if we aggregate across the two types of surgeries to compare overall surgery success rates, Dr. Hibbert was successful in 80 out of 100 surgeries while Dr. Nick was successful in 83 out of 100 surgeries: Dr. Nick's overall success rate is higher!