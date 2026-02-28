Texts in Statistical Science

# Introduction to Probability

Second Edition

![img-0.jpeg](img-0.jpeg)

Joseph K. Blitzstein
Jessica Hwang

CRC Press Taylor &amp; Francis Group A CHAPMAN &amp; HALL BOOK

# Introduction to Probability

## Second Edition

# CHAPMAN &amp; HALL/CRC

## Texts in Statistical Science Series

Joseph K. Blitzstein, *Harvard University, USA*

Julian J. Faraway, *University of Bath, UK*

Martin Tanner, *Northwestern University, USA*

Jim Zidek, *University of British Columbia, Canada*

Recently Published Titles

## Extending the Linear Model with R

Generalized Linear, Mixed Effects and Nonparametric Regression Models, Second Edition

J.J. Faraway

## Modeling and Analysis of Stochastic Systems, Third Edition

V.G. Kulkarni

## Pragmatics of Uncertainty

J.B. Kadane

## Stochastic Processes

From Applications to Theory

P.D. Moral and S. Penev

## Modern Data Science with R

B.S. Baumer, D.T. Kaplan, and N.J. Horton

## Generalized Additive Models

An Introduction with R, Second Edition

S. Wood

## Design of Experiments

An Introduction Based on Linear Models

Max Morris

## Introduction to Statistical Methods for Financial Models

T.A. Severini

## Statistical Regression and Classification

From Linear Models to Machine Learning

Norman Matloff

## Introduction to Functional Data Analysis

Piotr Kokoszka and Matthew Reimherr

## Stochastic Processes

An Introduction, Third Edition

P.W. Jones and P. Smith

## Theory of Stochastic Objects

Probability, Stochastic Processes and Inference

Athanasios Christou Micheas

## Linear Models and the Relevant Distributions and Matrix Algebra

David A. Harville

An Introduction to Generalized Linear Models, Fourth Edition
Annette J. Dobson and Adrian G. Barnett

Graphics for Statistics and Data Analysis with R
Kevin J. Keen

Statistics in Engineering, Second Edition
With Examples in MATLAB and R
Andrew Metcalfe, David A. Green, Tony Greenfield, Mahayaudin Mansor, Andrew Smith, and Jonathan Tuke

Introduction to Probability, Second Edition
Joseph K. Blitzstein and Jessica Hwang

For more information about this series, please visit: https://www.crcpress.com/go/textsseries

![img-1.jpeg](img-1.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

# Introduction to Probability
## Second Edition

Joseph K. Blitzstein
Harvard University
Cambridge, Massachusetts

Jessica Hwang
Stanford University
Stanford, California

CRC Press
Taylor &amp; Francis Group
Boca Raton London New York

CRC Press is an imprint of the
Taylor &amp; Francis Group, an informa business
A CHAPMAN &amp; HALL BOOK

CRC Press
Taylor &amp; Francis Group
6000 Broken Sound Parkway NW, Suite 300
Boca Raton, FL 33487-2742

© 2019 by Taylor &amp; Francis Group, LLC
CRC Press is an imprint of Taylor &amp; Francis Group, an Informa business

No claim to original U.S. Government works

Printed on acid-free paper
Version Date: 20190116

International Standard Book Number-13: 978-1-1383-6991-7 (Hardback)

This book contains information obtained from authentic and highly regarded sources. Reasonable efforts have been made to publish reliable data and information, but the author and publisher cannot assume responsibility for the validity of all materials or the consequences of their use. The authors and publishers have attempted to trace the copyright holders of all material reproduced in this publication and apologize to copyright holders if permission to publish in this form has not been obtained. If any copyright material has not been acknowledged please write and let us know so we may rectify in any future reprint.

Except as permitted under U.S. Copyright Law, no part of this book may be reprinted, reproduced, transmitted, or utilized in any form by any electronic, mechanical, or other means, now known or hereafter invented, including photocopying, microfilming, and recording, or in any information storage or retrieval system, without written permission from the publishers.

For permission to photocopy or use material electronically from this work, please access www.copyright.com (http://www.copyright.com/) or contact the Copyright Clearance Center, Inc. (CCC), 222 Rosewood Drive, Danvers, MA 01923, 978-750-8400. CCC is a not-for-profit organization that provides licenses and registration for a variety of users. For organizations that have been granted a photocopy license by the CCC, a separate system of payment has been arranged.

**Trademark Notice:** Product or corporate names may be trademarks or registered trademarks, and are used only for identification and explanation without intent to infringe.

Visit the Taylor &amp; Francis Web site at
http://www.taylorandfrancis.com

and the CRC Press Web site at
http://www.crcpress.com

To our mothers, Steffi and Min

![img-2.jpeg](img-2.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

Contents

Preface xiii

1 Probability and counting 1
1.1 Why study probability? 1
1.2 Sample spaces and Pebble World 3
1.3 Naive definition of probability 6
1.4 How to count 8
1.5 Story proofs 20
1.6 Non-naive definition of probability 21
1.7 Recap 26
1.8 R 29
1.9 Exercises 33

2 Conditional probability 45
2.1 The importance of thinking conditionally 45
2.2 Definition and intuition 46
2.3 Bayes' rule and the law of total probability 52
2.4 Conditional probabilities are probabilities 59
2.5 Independence of events 63
2.6 Coherency of Bayes' rule 67
2.7 Conditioning as a problem-solving tool 68
2.8 Pitfalls and paradoxes 74
2.9 Recap 79
2.10 R 80
2.11 Exercises 83

3 Random variables and their distributions 103
3.1 Random variables 103
3.2 Distributions and probability mass functions 106
3.3 Bernoulli and Binomial 112
3.4 Hypergeometric 115
3.5 Discrete Uniform 118
3.6 Cumulative distribution functions 120
3.7 Functions of random variables 123
3.8 Independence of r.v.s 129
3.9 Connections between Binomial and Hypergeometric 133
3.10 Recap 136

ix

X

Contents

3.11 R 138
3.12 Exercises 140

## 4 Expectation 149

4.1 Definition of expectation 149
4.2 Linearity of expectation 152
4.3 Geometric and Negative Binomial 157
4.4 Indicator r.v.s and the fundamental bridge 164
4.5 Law of the unconscious statistician (LOTUS) 170
4.6 Variance 171
4.7 Poisson 174
4.8 Connections between Poisson and Binomial 181
4.9 *Using probability and expectation to prove existence 184
4.10 Recap 189
4.11 R 192
4.12 Exercises 194

## 5 Continuous random variables 213

5.1 Probability density functions 213
5.2 Uniform 220
5.3 Universality of the Uniform 224
5.4 Normal 231
5.5 Exponential 238
5.6 Poisson processes 244
5.7 Symmetry of i.i.d. continuous r.v.s 248
5.8 Recap 250
5.9 R 253
5.10 Exercises 255

## 6 Moments 267

6.1 Summaries of a distribution 267
6.2 Interpreting moments 272
6.3 Sample moments 276
6.4 Moment generating functions 279
6.5 Generating moments with MGFs 283
6.6 Sums of independent r.v.s via MGFs 286
6.7 *Probability generating functions 287
6.8 Recap 292
6.9 R 293
6.10 Exercises 298

## 7 Joint distributions 303

7.1 Joint, marginal, and conditional 304
7.2 2D LOTUS 324
7.3 Covariance and correlation 326

Contents

7.4 Multinomial 332
7.5 Multivariate Normal 337
7.6 Recap 343
7.7 R 346
7.8 Exercises 348

8 Transformations 367

8.1 Change of variables 369
8.2 Convolutions 375
8.3 Beta 379
8.4 Gamma 387
8.5 Beta-Gamma connections 396
8.6 Order statistics 398
8.7 Recap 402
8.8 R 404
8.9 Exercises 407

9 Conditional expectation 415

9.1 Conditional expectation given an event 415
9.2 Conditional expectation given an r.v. 424
9.3 Properties of conditional expectation 426
9.4 *Geometric interpretation of conditional expectation 431
9.5 Conditional variance 432
9.6 Adam and Eve examples 436
9.7 Recap 439
9.8 R 441
9.9 Exercises 443

10 Inequalities and limit theorems 457

10.1 Inequalities 458
10.2 Law of large numbers 467
10.3 Central limit theorem 471
10.4 Chi-Square and Student-  $t$  477
10.5 Recap 480
10.6 R 483
10.7 Exercises 486

11 Markov chains 497

11.1 Markov property and transition matrix 497
11.2 Classification of states 502
11.3 Stationary distribution 506
11.4 Reversibility 513
11.5 Recap 520
11.6 R 521
11.7 Exercises 524

xii

Contents

## 12 Markov chain Monte Carlo 535

12.1 Metropolis-Hastings 536
12.2 Gibbs sampling 548
12.3 Recap 554
12.4 R 555
12.5 Exercises 557

## 13 Poisson processes 559

13.1 Poisson processes in one dimension 559
13.2 Conditioning, superposition, and thinning 561
13.3 Poisson processes in multiple dimensions 573
13.4 Recap 575
13.5 R 575
13.6 Exercises 577

## A Math 581

A.1 Sets 581
A.2 Functions 585
A.3 Matrices 590
A.4 Difference equations 592
A.5 Differential equations 593
A.6 Partial derivatives 594
A.7 Multiple integrals 594
A.8 Sums 596
A.9 Pattern recognition 599
A.10 Common sense and checking answers 599

## B R 601

B.1 Vectors 601
B.2 Matrices 602
B.3 Math 602
B.4 Sampling and simulation 603
B.5 Plotting 603
B.6 Programming 603
B.7 Summary statistics 604
B.8 Distributions 604

## C Table of distributions 605

## References 607

## Index 609

This book provides a modern introduction to probability and develops a foundation for understanding statistics, randomness, and uncertainty. A variety of applications and examples are explored, from basic coin-tossing and the study of coincidences to Google PageRank and Markov chain Monte Carlo. As probability is often considered to be a counterintuitive subject, many intuitive explanations, diagrams, and practice problems are given. Each chapter ends with a section showing how to explore the ideas of that chapter in R, a free software environment for statistical calculations and simulations.

Lecture videos from Stat 110 at Harvard, the course which gave rise to this book, are freely available at http://stat110.net. Additional supplementary materials such as R code, animations, and solutions to the exercises marked with $\circledS$, are also available at this site.

Calculus is a prerequisite for this book; there is no statistics prerequisite. The main mathematical challenge lies not in performing technical calculus derivations, but in translating between abstract concepts and concrete examples. Some major themes and features are listed below.

1. Stories. Throughout this book, definitions, theorems, and proofs are presented through stories: real-world interpretations that preserve mathematical precision and generality. We explore probability distributions using the generative stories that make them widely used in statistical modeling. When possible, we refrain from tedious derivations and instead aim to give interpretations and intuitions for why key results are true. Our experience is that this approach promotes long-term retention of the material by providing insight instead of demanding rote memorization.
2. Pictures. Since pictures are thousand-word stories, we supplement definitions with illustrations so that key concepts are associated with memorable diagrams. In many fields, the difference between a novice and an expert has been described as follows: the novice struggles to memorize a large number of seemingly disconnected facts and formulas, whereas the expert sees a unified structure in which a few principles and ideas connect these facts coherently. To help students see the structure of probability, we emphasize the connections between ideas (both verbally and visually), and at the end of most chapters we present recurring, ever-expanding maps of concepts and distributions.

3. Dual teaching of concepts and strategies. Our intent is that in reading this book, students will learn not only the concepts of probability, but also a set of problem-solving strategies that are widely applicable outside of probability. In the worked examples, we explain each step of the solution but also comment on how we knew to take the approach we did. Often we present multiple solutions to the same problem.

We explicitly identify and name important strategies such as symmetry and pattern recognition, and we proactively dispel common misunderstandings, which are marked with the $\Uparrow$ (biohazard) symbol.
4. Practice problems. The book contains about 600 exercises of varying difficulty. The exercises are intended to reinforce understanding of the material and strengthen problem-solving skills instead of requiring repetitive calculations. Some are strategic practice problems, grouped by theme to facilitate practice of a particular topic, while others are mixed practice, in which several earlier topics may need to be synthesized. About 250 exercises have detailed online solutions for practice and self-study.
5. Simulation, Monte Carlo, and R. Many probability problems are too difficult to solve exactly, and in any case it is important to be able to check one’s answer. We introduce techniques for exploring probability via simulation, and show that often a few lines of R code suffice to create a simulation for a seemingly complicated problem.
6. Focus on real-world relevance and statistical thinking. Examples and exercises in this book have a clear real-world motivation, with a particular focus on building a strong foundation for further study of statistical inference and modeling. We preview important statistical ideas such as sampling, simulation, Bayesian inference, and Markov chain Monte Carlo; other application areas include genetics, medicine, computer science, and information theory. Our choice of examples and exercises is intended to highlight the power, applicability, and beauty of probabilistic thinking.

The second edition benefits from hundreds of comments, questions, and reviews from students who took courses using the book, faculty who taught with the book, and readers using the book for self-study. We have added many new examples, exercises, and explanations based on our experience teaching with the book and the feedback we have received.

New supplementary materials have also been added at http://stat110.net, including animations and interactive visualizations that were created in connection with the edX online version of Stat 110. These are intended to help make probability feel more intuitive, visual, and tangible.

Acknowledgments

We thank our colleagues, the Stat 110 teaching assistants, and several thousand Stat 110 students for their comments and ideas related to the course and the book. In particular, we thank Alvin Siu, Angela Fan, Anji Tang, Anqi Zhao, Arman Sabbaghi, Carolyn Stein, David Jones, David Rosengarten, David Watson, Dennis Sun, Hyungsuk Tak, Johannes Ruf, Kari Lock, Keli Liu, Kelly Bodwin, Kevin Bartz, Lazhi Wang, Martin Lysy, Michele Zemplenyi, Miles Ott, Peng Ding, Rob Phillips, Sam Fisher, Sebastian Chiu, Sofia Hou, Sushmit Roy, Theresa Gebert, Valeria Espinosa, Viktoriia Liublinska, Viviana Garcia, William Chen, and Xander Marcus.

We also thank Ella Maru Studio for helping to create the cover image for the second edition. The image illustrates the interplay between two-dimensional and one-dimensional probability distributions.

We especially thank Bo Jiang, Raj Bhuptani, Shira Mitchell, Winston Lin, and the anonymous reviewers for their detailed comments, and Andrew Gelman, Carl Morris, Persi Diaconis, Stephen Blyth, Susan Holmes, and Xiao-Li Meng for countless insightful discussions about probability.

John Kimmel at Chapman & Hall/CRC Press provided wonderful editorial expertise throughout the writing of this book. We greatly appreciate his support.

Finally, we would like to express our deepest gratitude to our families for their love and encouragement.

Joe Blitzstein and Jessica Hwang
Cambridge, MA and Stanford, CA
January 2019

![img-3.jpeg](img-3.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

Probability and counting

#### 1.0.1 Luck. Coincidence. Randomness. Uncertainty. Risk. Doubt. Fortune. Chance.

You’ve probably heard these words countless times, but chances are that they were used in a vague, casual way. Unfortunately, despite its ubiquity in science and everyday life, probability can be deeply counterintuitive. If we rely on intuitions of doubtful validity, we run a serious risk of making inaccurate predictions or over-confident decisions. The goal of this book is to introduce probability as a logical framework for quantifying uncertainty and randomness in a principled way. We’ll also aim to strengthen intuition, both when our initial guesses coincide with logical reasoning and when we’re not so lucky.

### 1.1 Why study probability?

Mathematics is the logic of certainty; probability is the logic of uncertainty. Probability is extremely useful in a wide variety of fields, since it provides tools for understanding and explaining variation, separating signal from noise, and modeling complex phenomena. To give just a small sample from a continually growing list of applications:

1. Statistics: Probability is the foundation and language for statistics, enabling many powerful methods for using data to learn about the world.
2. Physics: Einstein famously said “God does not play dice with the universe”, but current understanding of quantum physics heavily involves probability at the most fundamental level of nature. Statistical mechanics is another major branch of physics that is built on probability.
3. Biology: Genetics is deeply intertwined with probability, both in the inheritance of genes and in modeling random mutations.
4. Computer science: Randomized algorithms make random choices while they are run, and in many important applications they are simpler and more efficient than any currently known deterministic alternatives. Probability also plays an essential role in studying the performance of algorithms, and in machine learning and artificial intelligence.

5. Meteorology: Weather forecasts are (or should be) computed and expressed in terms of probability.
6. Gambling: Many of the earliest investigations of probability were aimed at answering questions about gambling and games of chance.
7. Finance: At the risk of redundancy with the previous example, it should be pointed out that probability is central in quantitative finance. Modeling stock prices over time and determining “fair” prices for financial instruments are based heavily on probability.
8. Political science: In recent years, political science has become more and more quantitative and statistical, with applications such as analyzing surveys of public opinion, assessing gerrymandering, and predicting elections.
9. Medicine: The development of randomized clinical trials, in which patients are randomly assigned to receive treatment or placebo, has transformed medical research in recent years. As the biostatistician David Harrington remarked, “Some have conjectured that it could be the most significant advance in scientific medicine in the twentieth century…. In one of the delightful ironies of modern science, the randomized trial ‘adjusts’ for both observed and unobserved heterogeneity in a controlled experiment by introducing chance variation into the study design.” *[16]*
10. Life: Life is uncertain, and probability is the logic of uncertainty. While it isn’t practical to carry out a formal probability calculation for every decision made in life, thinking hard about probability can help us avert some common fallacies, shed light on coincidences, and make better predictions.

Probability provides procedures for principled problem-solving, but it can also produce pitfalls and paradoxes. For example, we’ll see in this chapter that even Gottfried Wilhelm von Leibniz and Sir Isaac Newton, the two people who independently discovered calculus in the 17th century, were not immune to basic errors in probability. Throughout this book, we will use the following strategies to help avoid potential pitfalls.

1. Simulation: A beautiful aspect of probability is that it is often possible to study problems via simulation. Rather than endlessly debating an answer with someone who disagrees with you, you can run a simulation and see empirically who is right. Each chapter in this book ends with a section that gives examples of how to do calculations and simulations in R, a free statistical computing environment.
2. Biohazards: Studying common mistakes is important for gaining a stronger understanding of what is and is not valid reasoning in probability. In this book, common mistakes are called biohazards and are denoted by ✟ (since making such mistakes can be hazardous to one’s health!).

Probability and counting

3. Sanity checks: After solving a problem one way, we will often try to solve the same problem in a different way or to examine whether our answer makes sense in simple and extreme cases.

# 1.2 Sample spaces and Pebble World

The mathematical framework for probability is built around sets. Imagine that an experiment is performed, resulting in one out of a set of possible outcomes. Before the experiment is performed, it is unknown which outcome will be the result; after, the result "crystallizes" into the actual outcome.

Definition 1.2.1 (Sample space and event). The sample space  $S$  of an experiment is the set of all possible outcomes of the experiment. An event  $A$  is a subset of the sample space  $S$ , and we say that  $A$  occurred if the actual outcome is in  $A$ .

![img-4.jpeg](img-4.jpeg)
FIGURE 1.1 A sample space as Pebble World, with two events  $A$  and  $B$  spotlighted.

The sample space of an experiment can be finite, countably infinite, or uncountably infinite (see Section A.1.5 of the math appendix for an explanation of countable and uncountable sets). When the sample space is finite, we can visualize it as Pebble World, as shown in Figure 1.1. Each pebble represents an outcome, and an event is a set of pebbles.

Performing the experiment amounts to randomly selecting one pebble. If all the pebbles are of the same mass, all the pebbles are equally likely to be chosen. This special case is the topic of the next two sections. In Section 1.6, we give a general definition of probability that allows the pebbles to differ in mass.

Set theory is very useful in probability, since it provides a rich language for express-

ing and working with events; Section A.1 of the math appendix provides a review of set theory. Set operations, especially unions, intersections, and complements, make it easy to build new events in terms of already-defined events. These concepts also let us express an event in more than one way; often, one expression for an event is much easier to work with than another expression for the same event.

For example, let $S$ be the sample space of an experiment and let $A,B\subseteq S$ be events. Then the union $A\cup B$ is the event that occurs if and only if *at least one* of $A,B$ occurs, the intersection $A\cap B$ is the event that occurs if and only if *both* $A$ and $B$ occur, and the complement $A^{c}$ is the event that occurs if and only if $A$ does *not* occur. We also have *De Morgan’s laws*:

$(A\cup B)^{c}=A^{c}\cap B^{c}\text{ and }(A\cap B)^{c}=A^{c}\cup B^{c},$

since saying that it is *not* the case that at least one of $A$ and $B$ occur is the same as saying that $A$ does not occur and $B$ does not occur, and saying that it is *not* the case that both occur is the same as saying that at least one does not occur. Analogous results hold for unions and intersections of more than two events.

In the example shown in Figure 1, $A$ is a set of 5 pebbles, $B$ is a set of 4 pebbles, $A\cup B$ consists of the 8 pebbles in $A$ or $B$ (including the pebble that is in both), $A\cap B$ consists of the pebble that is in both $A$ and $B$, and $A^{c}$ consists of the 4 pebbles that are not in $A$.

The notion of sample space is very general and abstract, so it is important to have some concrete examples in mind.

###### Example 1.2.2 (Coin flips).

A coin is flipped 10 times. Writing Heads as $H$ and Tails as $T$, a possible outcome (pebble) is $HHHTHHTTHT$, and the sample space is the set of all possible strings of length 10 of $H$’s and $T$’s. We can (and will) encode $H$ as 1 and $T$ as 0, so that an outcome is a sequence $(s_{1},\ldots,s_{10})$ with $s_{j}\in\{0,1\}$, and the sample space is the set of all such sequences. Now let’s look at some events:

1. Let $A_{1}$ be the event that the first flip is Heads. As a set,

$A_{1}=\{(1,s_{2},\ldots,s_{10}):s_{j}\in\{0,1\}\text{ for }2\leq j\leq 10\}.$

This is a subset of the sample space, so it is indeed an event; saying that $A_{1}$ occurs is the same thing as saying that the first flip is Heads. Similarly, let $A_{j}$ be the event that the $j$th flip is Heads for $j=2,3,\ldots,10$.

2. Let $B$ be the event that at least one flip was Heads. As a set,

$B=\bigcup_{j=1}^{10}A_{j}.$

3. Let $C$ be the event that all the flips were Heads. As a set,

$C=\bigcap_{j=1}^{10}A_{j}.$

Probability and counting

4. Let $D$ be the event that there were at least two consecutive Heads. As a set,

$D=\bigcup_{j=1}^{9}(A_{j}\cap A_{j+1}).\qed$

###### Example 1.2.3 (Pick a card, any card).

Pick a card from a standard deck of 52 cards. The sample space $S$ is the set of all 52 cards (so there are 52 pebbles, one for each card). Consider the following four events:

- $A$: card is an ace.
- $B$: card has a black suit.
- $D$: card is a diamond.
- $H$: card is a heart.

As a set, $H$ consists of 13 cards:

$\{\mbox{Ace of Hearts, Two of Hearts,}\dots\mbox{, King of Hearts}\}.$

We can create various other events in terms of the events $A,B,D$, and $H$. Unions, intersections, and complements are especially useful for this. For example:

- $A\cap H$ is the event that the card is the Ace of Hearts.
- $A\cap B$ is the event $\{\mbox{Ace of Spades, Ace of Clubs}\}$.
- $A\cup D\cup H$ is the event that the card is red or an ace.
- $(A\cup B)^{c}=A^{c}\cap B^{c}$ is the event that the card is a red non-ace.

Also, note that $(D\cup H)^{c}=D^{c}\cap H^{c}=B$, so $B$ can be expressed in terms of $D$ and $H$. On the other hand, the event that the card is a spade can’t be written in terms of $A,B,D,H$ since none of them are fine-grained enough to be able to distinguish between spades and clubs.

There are *many* other events that could be defined using this sample space. In fact, the counting methods introduced later in this chapter show that there are $2^{52}\approx 4.5\times 10^{15}$ events in this problem, even though there are only 52 pebbles.

What if the card drawn were a joker? That would indicate that we had the wrong sample space; we are assuming that the outcome of the experiment is guaranteed to be an element of $S$. ∎

As the preceding examples demonstrate, events can be described in English or in set notation. Sometimes the English description is easier to interpret while the set notation is easier to manipulate. Let $S$ be a sample space and $s_{\mathrm{actual}}$ be the actual outcome of the experiment (the pebble that ends up getting chosen when the experiment is performed). A mini-dictionary for converting between English and sets is given on the next page.

Introduction to Probability

|  English | Sets  |
| --- | --- |
|  Events and occurrences |   |
|  sample space | S  |
|  s is a possible outcome | s ∈ S  |
|  A is an event | A ⊆ S  |
|  A occurred | sactual ∈ A  |
|  something must happen | sactual ∈ S  |
|  New events from old events |   |
|  A or B (inclusive) | A ∪ B  |
|  A and B | A ∩ B  |
|  not A | Ac  |
|  A or B, but not both | (A ∩ Bc) ∪ (Ac ∩ B)  |
|  at least one of A1, ..., An | A1 ∪··· ∪ An  |
|  all of A1, ..., An | A1 ∩··· ∩ An  |
|  Relationships between events |   |
|  A implies B | A ⊆ B  |
|  A and B are mutually exclusive | A ∩ B = ∅  |
|  A1, ..., An are a partition of S | A1 ∪··· ∪ An = S, Ai ∩ Aj = ∅ for i ≠ j  |

# 1.3 Naive definition of probability

Historically, the earliest definition of the probability of an event was to count the number of ways the event could happen and divide by the total number of possible outcomes for the experiment. We call this the naive definition since it is restrictive and relies on strong assumptions; nevertheless, it is important to understand, and useful when not misused.

Definition 1.3.1 (Naive definition of probability). Let  $A$  be an event for an experiment with a finite sample space  $S$ . The naive probability of  $A$  is

$$
P _ {\mathrm {n a i v e}} (A) = \frac {| A |}{| S |} = \frac {\mathrm {n u m b e r o f o u t c o m e s f a v o r a b l e t o} A}{\mathrm {t o t a l n u m b e r o f o u t c o m e s i n} S}.
$$

(We use  $|A|$  to denote the size of  $A$ ; see Section A.1.5 of the math appendix.)

In terms of Pebble World, the naive definition just says that the probability of  $A$  is the fraction of pebbles that are in  $A$ . For example, in Figure 1.1 it says

$$
P _ {\mathrm {n a i v e}} (A) = \frac {5}{9}, P _ {\mathrm {n a i v e}} (B) = \frac {4}{9}, P _ {\mathrm {n a i v e}} (A \cup B) = \frac {8}{9}, P _ {\mathrm {n a i v e}} (A \cap B) = \frac {1}{9}.
$$

For the complements of the events just considered,

$P_{\rm naive}(A^{c})=\frac{4}{9},\ P_{\rm naive}(B^{c})=\frac{5}{9},\ P_{\rm naive}((A\cup B)^{c})=\frac{1}{9},\ P_{\rm naive}((A\cap B)^{c})=\frac{8}{9}.$

In general,

$P_{\rm naive}(A^{c})=\frac{|A^{c}|}{|S|}=\frac{|S|-|A|}{|S|}=1-\frac{|A|}{|S|}=1-P_{\rm naive}(A).$

In Section 1.6, we will see that this result about complements *always* holds for probability, even when we go beyond the naive definition. A good strategy when trying to find the probability of an event is to start by thinking about whether it will be easier to find the probability of the event or the probability of its complement. De Morgan’s laws are especially useful in this context, since it may be easier to work with an intersection than a union, or vice versa.

The naive definition is very restrictive in that it requires $S$ to be finite, with equal mass for each pebble. It has often been misapplied by people who assume equally likely outcomes without justification and make arguments to the effect of “either it will happen or it won’t, and we don’t know which, so it’s 50-50”. In addition to sometimes giving absurd probabilities, this type of reasoning isn’t even internally consistent. For example, it would say that the probability of life on Mars is 1/2 (“either there is or there isn’t life there”), but it would also say that the probability of *intelligent* life on Mars is 1/2, and it is clear intuitively—and by the properties of probability developed in Section 1.6—that the latter should have strictly lower probability than the former. But there are several important types of problems where the naive definition *is* applicable:

- when there is *symmetry* in the problem that makes outcomes equally likely. It is common to assume that a coin has a 50% chance of landing Heads when tossed, due to the physical symmetry of the coin. For a standard, well-shuffled deck of cards, it is reasonable to assume that all orders are equally likely. There aren’t certain overeager cards that especially like to be near the top of the deck; any particular location in the deck is equally likely to house any of the 52 cards.
- when the outcomes are equally likely *by design*. For example, consider conducting a survey of $n$ people in a population of $N$ people. A common goal is to obtain a *simple random sample*, which means that the $n$ people are chosen randomly with all subsets of size $n$ being equally likely. If successful, this ensures that the naive definition is applicable, but in practice this may be hard to accomplish because of various complications, such as not having a complete, accurate list of contact information for everyone in the population.

- when the naive definition serves as a useful null model. In this setting, we assume that the naive definition applies just to see what predictions it would yield, and then we can compare observed data with predicted values to assess whether the hypothesis of equally likely outcomes is tenable.

### 1.4 How to count

Calculating the naive probability of an event $A$ involves counting the number of pebbles in $A$ and the number of pebbles in the sample space $S$. Often the sets we need to count are extremely large. This section introduces some fundamental methods for counting; further methods can be found in books on combinatorics, the branch of mathematics that studies counting.

#### 1.4.1 Multiplication rule

In some problems, we can directly count the number of possibilities using a basic but versatile principle called the multiplication rule. We’ll see that the multiplication rule leads naturally to counting rules for sampling with replacement and sampling without replacement, two scenarios that often arise in probability and statistics.

###### Theorem 1.4.1 (Multiplication rule).

Consider a compound experiment consisting of two sub-experiments, Experiment A and Experiment B. Suppose that Experiment A has $a$ possible outcomes, and for each of those outcomes Experiment B has $b$ possible outcomes. Then the compound experiment has $ab$ possible outcomes.

To see why the multiplication rule is true, imagine a tree diagram as in Figure 1.2. Let the tree branch $a$ ways according to the possibilities for Experiment A, and for each of those branches create $b$ further branches for Experiment B. Overall, there are $\underbrace{b+b+\cdots+b}_{a}=ab$ possibilities.

It is often easier to think about the experiments as being in chronological order, but there is no requirement in the multiplication rule that Experiment A has to be performed before Experiment B.

###### Example 1.4.3 (Runners).

Suppose that 10 people are running a race. Assume that ties are not possible and that all 10 will complete the race, so there will be well-defined first place, second place, and third place winners. How many possibilities are there for the first, second, and third place winners?

Solution: There are 10 possibilities for who gets first place, then once that is fixed there are 9 possibilities for who gets second place, and once these are both fixed

Probability and counting

![img-5.jpeg](img-5.jpeg)
FIGURE 1.2

Tree diagram illustrating the multiplication rule. If Experiment A has 3 possible outcomes, for each of which Experiment B has 4 possible outcomes, then overall there are  $3 \cdot 4 = 12$  possible outcomes.

there are 8 possibilities for third place. So by the multiplication rule, there are  $10 \cdot 9 \cdot 8 = 720$  possibilities.

We did not have to consider the first place winner first. We could just as well have said that there are 10 possibilities for who got third place, then once that is fixed there are 9 possibilities for second place, and once those are both fixed there are 8 possibilities for first place. Or imagine that there are 3 platforms, which the first, second, and third place runners will stand on after the race. The platforms are gold, silver, and bronze, allocated to the first, second, and third place runners, respectively. Again there are  $10 \cdot 9 \cdot 8 = 720$  possibilities for how the platforms will be occupied after the race, and there is no reason that the platforms must be considered in the order (gold, silver, bronze).

Example 1.4.4 (Chessboard). How many squares are there in an  $8 \times 8$  chessboard, as in Figure 1.3? Even the name “ $8 \times 8$  chessboard” makes this easy: there are  $8 \cdot 8 = 64$  squares on the board. The grid structure makes this clear, but we can also think of this as an example of the multiplication rule: to specify a square, we can specify which row and which column it is in. There are 8 choices of row, for each of which there are 8 choices of column.

Furthermore, we can see without doing any calculations that half the squares are white and half are black. Imagine rotating the chessboard 90 degrees clockwise. Then all the positions that had a white square now contain a black square, and vice versa, so the number of white squares must equal the number of black squares. We

Introduction to Probability

![img-6.jpeg](img-6.jpeg)
FIGURE 1.3

![img-7.jpeg](img-7.jpeg)

An  $8 \times 8$  chessboard (left) and a crossword puzzle grid (right). The chessboard has  $8 \cdot 8 = 64$  squares, whereas counting the number of white squares in the crossword puzzle grid requires more work.

can also count the number of white squares using the multiplication rule: in each of the 8 rows there are 4 white squares, giving a total of  $8 \cdot 4 = 32$  white squares.

In contrast, it would require more effort to count the number of white squares in the crossword puzzle grid shown in Figure 1.3. The multiplication rule does not apply, since different rows sometimes have different numbers of white squares.  $\square$

Example 1.4.5 (Ice cream cones). Suppose you are buying an ice cream cone. You can choose whether to have a cake cone or a waffle cone, and whether to have chocolate, vanilla, or strawberry as your flavor. This decision process can be visualized with a tree diagram, as in Figure 1.4.

![img-8.jpeg](img-8.jpeg)
FIGURE 1.4

![img-9.jpeg](img-9.jpeg)

Tree diagram for choosing an ice cream cone. Regardless of whether the type of cone or the flavor is chosen first, there are  $2 \cdot 3 = 3 \cdot 2 = 6$  possibilities.

Probability and counting

By the multiplication rule, there are $2\cdot 3=6$ possibilities. This is a very simple example, but is worth thinking through in detail as a foundation for thinking about and visualizing more complicated examples. Soon we will encounter examples where drawing the tree in a legible size would take up more space than exists in the known universe, yet where conceptually we can still think in terms of the ice cream example. Some things to note:

1. It doesn’t matter whether you choose the type of cone first (“I’d like a waffle cone with chocolate ice cream”) or the flavor first (“I’d like chocolate ice cream on a waffle cone”). Either way, there are $2\cdot 3=3\cdot 2=6$ possibilities.

2. It doesn’t matter whether the same flavors are available on a cake cone as on a waffle cone. What matters is that there are exactly 3 flavor choices for each cone choice. If for some strange reason it were forbidden to have chocolate ice cream on a waffle cone, with no substitute flavor available (aside from vanilla and strawberry), there would be $3+2=5$ possibilities and the multiplication rule wouldn’t apply. In larger examples, such complications could make counting the number of possibilities vastly more difficult.

Now suppose you buy *two* ice cream cones on a certain day, one in the afternoon and the other in the evening. Write, for example, (cakeC, waffleV) to mean a cake cone with chocolate in the afternoon, followed by a waffle cone with vanilla in the evening. By the multiplication rule, there are $6^{2}=36$ possibilities in your delicious compound experiment.

But what if you’re only interested in what kinds of ice cream cones you had that day, not the order in which you had them, so you don’t want to distinguish, for example, between (cakeC, waffleV) and (waffleV, cakeC)? Are there now $36/2=18$ possibilities? No, since possibilities like (cakeC, cakeC) were already only listed once each. There are $6\cdot 5=30$ ordered possibilities $(x,y)$ with $x\neq y$, which turn into 15 possibilities if we treat $(x,y)$ as equivalent to $(y,x)$, plus 6 possibilities of the form $(x,x)$, giving a total of 21 possibilities. Note that if the 36 original ordered pairs $(x,y)$ are equally likely, then the 21 possibilities here are *not* equally likely. ∎

###### Example 1.4.6 (Subsets).

A set with $n$ elements has $2^{n}$ subsets, including the empty set $\emptyset$ and the set itself. This follows from the multiplication rule since for each element, we can choose whether to include it or exclude it. For example, the set $\{1,2,3\}$ has the 8 subsets $\emptyset,\{1\},\{2\},\{3\},\{1,2\},\{1,3\},\{2,3\},\{1,2,3\}$. This result explains why in Example 1.2.3 there are $2^{52}$ events that can be defined. ∎

We can use the multiplication rule to arrive at formulas for sampling with and without replacement. Many experiments in probability and statistics can be interpreted in one of these two contexts, so it is appealing that both formulas follow directly from the same basic counting principle.

###### Theorem 1.4.7 (Sampling with replacement).

Consider $n$ objects and making $k$ choices from them, one at a time *with replacement* (i.e., choosing a certain object does not preclude it from being chosen again). Then there are $n^{k}$ possible outcomes

(where order matters, in the sense that, e.g., choosing object 3 and then object 7 is counted as a different outcome than choosing object 7 and then object 3.)

For example, imagine a jar with $n$ balls, labeled from 1 to $n$. We sample balls one at a time with replacement, meaning that each time a ball is chosen, it is returned to the jar. Each sampled ball is a sub-experiment with $n$ possible outcomes, and there are $k$ sub-experiments. Thus, by the multiplication rule there are $n^{k}$ ways to obtain a sample of size $k$.

###### Theorem 1.4.8 (Sampling without replacement).

Consider $n$ objects and making $k$ choices from them, one at a time *without replacement* (i.e., choosing a certain object precludes it from being chosen again). Then there are $n(n-1)\cdots(n-k+1)$ possible outcomes for $1\leq k\leq n$, and $0$ possibilities for $k>n$ (where order matters). By convention, $n(n-1)\cdots(n-k+1)=n$ for $k=1$.

This result also follows directly from the multiplication rule: each sampled ball is again a sub-experiment, and the number of possible outcomes decreases by 1 each time. Note that for sampling $k$ out of $n$ objects without replacement, we need $k\leq n$, whereas in sampling with replacement the objects are inexhaustible.

###### Example 1.4.9 (Permutations and factorials).

A *permutation* of $1,2,\ldots,n$ is an arrangement of them in some order, e.g., $3,5,1,2,4$ is a permutation of $1,2,3,4,5$. By Theorem 1.4.8 with $k=n$, there are $n!$ permutations of $1,2,\ldots,n$. For example, there are $n!$ ways in which $n$ people can line up for ice cream. (Recall that $n!$ is $n(n-1)(n-2)\cdots 1$ for any positive integer $n$, and $0!=1$.) ∎

Theorems 1.4.7 and 1.4.8 are theorems about *counting*, but when the naive definition applies, we can use them to calculate *probabilities*. This brings us to our next example, a famous problem in probability called the *birthday problem*. The solution incorporates both sampling with replacement and sampling without replacement.

###### Example 1.4.10 (Birthday problem).

There are $k$ people in a room. Assume each person’s birthday is equally likely to be any of the 365 days of the year (we exclude February 29), and that people’s birthdays are independent (we will define *independence* formally later, but intuitively it means that knowing some people’s birthdays gives us no information about other people’s birthdays; this would not hold if, e.g., we knew that two of the people were twins). What is the probability that at least one pair of people in the group have the same birthday?

*Solution*:

There are $365^{k}$ ways to assign birthdays to the people in the room, since we can imagine the 365 days of the year being sampled $k$ times, with replacement. By assumption, all of these possibilities are equally likely, so the naive definition of probability applies.

Used directly, the naive definition says we just need to count the number of ways to assign birthdays to $k$ people such that there are two people who share a birthday.

Probability and counting

But this counting problem is hard, since it could be Emma and Steve who share a birthday, or Steve and Naomi, or all three of them, or the three of them could share a birthday while two others in the group share a different birthday, or various other possibilities.

Instead, let's count the complement: the number of ways to assign birthdays to  $k$  people such that no two people share a birthday. This amounts to sampling the 365 days of the year without replacement, so the number of possibilities is  $365 \cdot 364 \cdot 363 \cdots (365 - k + 1)$  for  $k \leq 365$ . Therefore the probability of no birthday matches in a group of  $k$  people is

$$
P (\mathrm {n o b i r t h d a y m a t c h}) = \frac {3 6 5 \cdot 3 6 4 \cdots (3 6 5 - k + 1)}{3 6 5 ^ {k}},
$$

and the probability of at least one birthday match is

$$
P (\mathrm {a t l e a s t 1 b i r t h d a y m a t c h}) = 1 - \frac {3 6 5 \cdot 3 6 4 \cdots (3 6 5 - k + 1)}{3 6 5 ^ {k}}.
$$

Figure 1.5 plots the probability of at least one birthday match as a function of  $k$ . The first value of  $k$  for which the probability of a match exceeds 0.5 is  $k = 23$ . Thus, in a group of 23 people, there is a better than  $50\%$  chance that there is at least one birthday match. At  $k = 57$ , the probability of a match already exceeds  $99\%$ .

![img-10.jpeg](img-10.jpeg)
FIGURE 1.5

Probability that in a room of  $k$  people, at least two were born on the same day. This probability first exceeds 0.5 when  $k = 23$ .

Of course, for  $k = 366$  we are guaranteed to have a match, but it's surprising that even with a much smaller number of people it's overwhelmingly likely that there is a birthday match. For a quick intuition into why it should not be so surprising, note that with 23 people there are  $\binom{23}{2} = 253$  pairs of people, any of which could be a birthday match.

Problems 26 and 27 show that the birthday problem is much more than a fun party game, and much more than a way to build intuition about coincidences; there are also important applications in statistics and computer science. Problem 62 explores the more general setting in which the probability is not necessarily $1/365$ for each day. It turns out that in the non-equal probability case, having at least one match becomes even *more* likely. ∎

#### 1.4.11 (Labeling objects).

Drawing a sample from a population is a very fundamental concept in statistics. It is important to think of the objects or people in the population as *named* or *labeled*. For example, if there are $n$ balls in a jar, we can imagine that they have labels from $1$ to $n$, even if the balls look the same to the human eye. In the birthday problem, we can give each person an ID (identification) number, rather than thinking of the people as indistinguishable particles or a faceless mob.

A related example is an instructive blunder made by Leibniz in a seemingly simple problem (see Gorroochurn *[14]* for discussion of this and a variety of other probability problems from a historical perspective).

###### Example 1.4.12 (Leibniz’s mistake).

If we roll two fair dice, which is more likely: a sum of $11$ or a sum of $12$?

*Solution*:

Label the dice A and B, and consider each die to be a sub-experiment. By the multiplication rule, there are $36$ possible outcomes for ordered pairs of the form (value of A, value of B), and they are equally likely by symmetry. Of these, $(5,6)$ and $(6,5)$ are favorable to a sum of $11$, while only $(6,6)$ is favorable to a sum of $12$. Therefore a sum of $11$ is twice as likely as a sum of $12$; the probability is $1/18$ for the former, and $1/36$ for the latter.

However, Leibniz wrongly argued that a sum of $11$ and a sum of $12$ are equally likely, claiming that each of these sums can be attained in only one way. Here Leibniz was making the mistake of treating the two dice as indistinguishable objects, viewing $(5,6)$ and $(6,5)$ as the same outcome.

What are the antidotes to Leibniz’s mistake? First, as explained in 1.4.11, we should *label* the objects in question instead of treating them as indistinguishable. If Leibniz had labeled his dice A and B, or green and orange, or left and right, he would not have made this mistake. Second, before we use counting for probability, we should ask ourselves whether the naive definition applies (see 1.4.23 for another example showing that caution is needed before applying the naive definition). ∎

#### 1.4.2 Adjusting for overcounting

In many counting problems, it is not easy to directly count each possibility once and only once. If, however, we are able to count each possibility exactly $c$ times

Probability and counting

for some $c$, then we can adjust by dividing by $c$. For example, if we have exactly double-counted each possibility, we can divide by 2 to get the correct count. We call this *adjusting for overcounting*.

###### Example 1.4.13 (Committees and teams).

Consider a group of four people.

(a) How many ways are there to choose a two-person committee?

(b) How many ways are there to break the people into two teams of two?

Solution:

(a) One way to count the possibilities is by listing them out: labeling the people as 1, 2, 3, 4, the possibilities are $\boxed{12}$, $\boxed{13}$, $\boxed{14}$, $\boxed{23}$, $\boxed{24}$, $\boxed{34}$.

Another approach is to use the multiplication rule with an adjustment for overcounting. By the multiplication rule, there are 4 ways to choose the first person on the committee and 3 ways to choose the second person on the committee, but this counts each possibility twice, since picking 1 and 2 to be on the committee is the same as picking 2 and 1 to be on the committee. Since we have overcounted by a factor of 2, the number of possibilities is $(4\cdot 3)/2=6$.

(b) Here are 3 ways to see that there are 3 ways to form the teams. Labeling the people as $1,2,3,4$, we can directly list out the possibilities: $\boxed{12}\boxed{34}$, $\boxed{13}\boxed{24}$, and $\boxed{14}\boxed{23}$. Listing out all possibilities would quickly become tedious or infeasible with more people though. Another approach is to note that it suffices to specify person 1’s teammate (and then the other team is determined). A third way is to use (a) to see that there are 6 ways to choose one team. This overcounts by a factor of 2, since picking 1 and 2 to be a team is equivalent to picking 3 and 4 to be a team. So again the answer is $6/2=3$. $\square$

A *binomial coefficient* counts the number of subsets of a certain size for a set, such as the number of ways to choose a committee of size $k$ from a set of $n$ people. Sets and subsets are by definition *unordered*, e.g., $\{3,1,4\}=\{4,1,3\}$, so we are counting the number of ways to choose $k$ objects out of $n$, without replacement and without distinguishing between the different orders in which they could be chosen.

###### Definition 1.4.14 (Binomial coefficient).

For any nonnegative integers $k$ and $n$, the *binomial coefficient* $\binom{n}{k}$, read as “$n$ choose $k$”, is the number of subsets of size $k$ for a set of size $n$.

For example, $\binom{4}{2}=6$, as shown in Example 1.4.13. The binomial coefficient $\binom{n}{k}$ is sometimes called a *combination*, but we do not use that terminology here since “combination” is such a useful general-purpose word. Algebraically, binomial coefficients can be computed as follows.

###### Theorem 1.4.15 (Binomial coefficient formula).

For $k\leq n$, we have

$\binom{n}{k}=\frac{n(n-1)\cdots(n-k+1)}{k!}=\frac{n!}{(n-k)!k!}\cdot$

For $k>n$, we have $\binom{n}{k}=0$.

###### Proof.

Let $A$ be a set with $|A|=n$. Any subset of $A$ has size at most $n$, so $\binom{n}{k}=0$ for $k>n$. Now let $k\leq n$. By Theorem 1.4.8, there are $n(n-1)\cdots(n-k+1)$ ways to make an *ordered* choice of $k$ elements without replacement. This overcounts each subset of interest by a factor of $k!$ (since we don’t care how these elements are ordered), so we can get the correct count by dividing by $k!$. ∎

$\nLeftrightarrow$ 1.4.16. The binomial coefficient $\binom{n}{k}$ is often defined in terms of factorials, but keep in mind that $\binom{n}{k}$ is $0$ if $k>n$, even though the factorial of a negative number is undefined. Also, the middle expression in Theorem 1.4.15 is often better for computation than the expression with factorials, since factorials grow *extremely* fast. For example,

$\binom{100}{2}=\frac{100\cdot 99}{2}=4950$

can even be done by hand, whereas computing $\binom{100}{2}=100!/(98!\cdot 2!)$ by first calculating $100!$ and $98!$ would be wasteful and possibly dangerous because of the extremely large numbers involved ($100!\approx 9.33\times 10^{157}$).

###### Example 1.4.17 (Club officers).

In a club with $n$ people, there are $n(n-1)(n-2)$ ways to choose a president, vice president, and treasurer, and there are

$\binom{n}{3}=\frac{n(n-1)(n-2)}{3!}$

ways to choose $3$ officers without predetermined titles. ∎

###### Example 1.4.18 (Permutations of a word).

How many ways are there to permute the letters in the word LALALAAA? To determine a permutation, we just need to choose where the $5$ A’s go (or, equivalently, just decide where the $3$ L’s go). So there are

$\binom{8}{5}=\binom{8}{3}=\frac{8\cdot 7\cdot 6}{3!}=56\text{ permutations}.$

How many ways are there to permute the letters in the word STATISTICS? Here are two approaches. We could choose where to put the S’s, then where to put the T’s (from the remaining positions), then where to put the I’s, then where to put the A (and then the C is determined). Alternatively, we can start with $10!$ and then adjust for overcounting, dividing by $3!3!2!$ to account for the fact that the S’s can be permuted among themselves in any way, and likewise for the T’s and I’s. This gives

$\binom{10}{3}\binom{7}{3}\binom{4}{2}\binom{2}{1}=\frac{10!}{3!3!2!}=50400\text{ possibilities}.\qed$

###### Example 1.4.19 (Binomial theorem).

The *binomial theorem* states that

$(x+y)^{n}=\sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k},$

for any nonnegative integer $n$. To prove the binomial theorem, expand out the product

$\underbrace{(x+y)(x+y)\ldots(x+y)}_{n\ \text{factors}}.$

Just as $(a+b)(c+d)=ac+ad+bc+bd$ is the sum of terms where we pick the $a$ or the $b$ from the first factor (but not both) and the $c$ or the $d$ from the second factor (but not both), the terms of $(x+y)^{n}$ are obtained by picking either the $x$ or the $y$ (but not both) from each factor. There are $\binom{n}{k}$ ways to choose exactly $k$ of the $x$’s, and each such choice yields the term $x^{k}y^{n-k}$. The binomial theorem follows. ∎

We can use binomial coefficients to calculate probabilities in many problems for which the naive definition applies.

###### Example 1.4.20 (Full house in poker).

A 5-card hand is dealt from a standard, well-shuffled 52-card deck. The hand is called a *full house* in poker if it consists of three cards of some rank and two cards of another rank, e.g., three 7’s and two 10’s (in any order). What is the probability of a full house?

*Solution*:

All of the $\binom{52}{5}$ possible hands are equally likely by symmetry, so the naive definition is applicable. To find the number of full house hands, use the multiplication rule (and imagine the tree). There are 13 choices for what rank we have three of; for concreteness, assume we have three 7’s and focus on that branch of the tree. There are $\binom{4}{3}$ ways to choose which 7’s we have. Then there are 12 choices for what rank we have two of, say 10’s for concreteness, and $\binom{4}{2}$ ways to choose two 10’s. Thus,

$P(\text{full house})=\frac{13\binom{4}{3}12\binom{4}{2}}{\binom{52}{5}}=\frac{3744}{2598960}\approx 0.00144.$

The decimal approximation is more useful when playing poker, but the answer in terms of binomial coefficients is exact and *self-annotating* (seeing $\binom{52}{5}$ is a much bigger hint about its origin than seeing 2598960). ∎

###### Example 1.4.21 (Newton-Pepys problem).

Isaac Newton was consulted about the following problem by Samuel Pepys, who wanted the information for gambling purposes. Which of the following events has the highest probability?

$A$: At least one 6 appears when 6 fair dice are rolled.

$B$: At least two 6’s appear when 12 fair dice are rolled.

$C$: At least three 6’s appear when 18 fair dice are rolled.

*Solution*:

The three experiments have $6^{6}$, $6^{12}$, and $6^{18}$ possible outcomes, respectively, and by symmetry the naive definition applies in all three experiments.

$A$: Instead of counting the number of ways to obtain at least one 6, it is easier to count the number of ways to get no 6’s. Getting no 6’s is equivalent to sampling the numbers 1 through 5 with replacement 6 times, so $5^{6}$ outcomes are favorable to $A^{c}$ (and $6^{6}-5^{6}$ are favorable to $A$). Thus

$P(A)=1-\frac{5^{6}}{6^{6}}\approx 0.67.$

$B$: Again we count the outcomes in $B^{c}$ first. There are $5^{12}$ ways to get no 6’s in 12 die rolls. There are $\binom{12}{1}5^{11}$ ways to get exactly one 6: we first choose which die lands 6, then sample the numbers 1 through 5 with replacement for the other 11 dice. Adding these, we get the number of ways to fail to obtain at least two 6’s. Then

$P(B)=1-\frac{5^{12}+\binom{12}{1}5^{11}}{6^{12}}\approx 0.62.$

$C$: We count the outcomes in $C^{c}$, i.e., the number of ways to get zero, one, or two 6’s in 18 die rolls. There are $5^{18}$ ways to get no 6’s, $\binom{18}{1}5^{17}$ ways to get exactly one 6, and $\binom{18}{2}5^{16}$ ways to get exactly two 6’s (choose which two dice will land 6, then decide how the other 16 dice will land).

$P(C)=1-\frac{5^{18}+\binom{18}{1}5^{17}+\binom{18}{2}5^{16}}{6^{18}}\approx 0.60.$

Therefore $A$ has the highest probability.

Newton arrived at the correct answer using similar calculations. Newton also provided Pepys with an intuitive argument for why $A$ was the most likely of the three; however, his intuition was invalid. As explained in Stigler *[24]*, using loaded dice could result in a different ordering of $A,B,C$, but Newton’s intuitive argument did not depend on the dice being fair. ∎

In this book, we care about counting not for its own sake, but because it sometimes helps us to find probabilities. Here is an example of a neat but treacherous counting problem; the solution is elegant, but it is rare that the result can be used with the naive definition of probability.

###### Example 1.4.22 (Bose-Einstein).

How many ways are there to choose $k$ times from a set of $n$ objects with replacement, if order doesn’t matter (we only care about how many times each object was chosen, not the order in which they were chosen)?

Solution:

When order does matter, the answer is $n^{k}$ by the multiplication rule, but this problem is much harder. We will solve it by solving an *isomorphic* problem (the same problem in a different guise).

Let us find the number of ways to put $k$ indistinguishable particles into $n$ distinguishable boxes. That is, swapping the particles in any way is not considered a separate

Probability and counting

possibility: all that matters are the counts for how many particles are in each box. This scenario is known as a Bose-Einstein problem, since the physicists Satyendra Nath Bose and Albert Einstein studied related problems about indistinguishable particles in the 1920s, using their ideas to successfully predict the existence of a strange state of matter known as a Bose-Einstein condensate.

Any configuration can be encoded as a sequence of  $|$ 's and  $\bullet$ 's in a natural way, as illustrated in Figure 1.6.

![img-11.jpeg](img-11.jpeg)

# FIGURE 1.6

Bose-Einstein encoding: putting  $k = 7$  indistinguishable particles into  $n = 4$  distinguishable boxes can be expressed as a sequence of  $|$ 's and  $\bullet$ 's, where  $|$  denotes a wall and  $\bullet$  denotes a particle.

To be valid, a sequence must start and end with a  $|$ , and have exactly  $n - 1$  's and exactly  $k$  's in between the starting and ending 's; conversely, any such sequence is a valid encoding for some configuration of particles in boxes. Imagine that we have written down the starting and ending 's, which represent the outer walls, and in between there are  $n + k - 1$  fill-in-the-blank slots in between the outer walls. We need only choose where to put the  $k$  's (since then where the  $n + k - 1$  interior 's go is completely determined). So the number of possibilities is  $\binom{n+k-1}{k}$ . This counting method is sometimes called the stars and bars argument, where here we have dots in place of stars.

To relate this result back to the original question, we can let each box correspond to one of the  $n$  objects and use the particles as "check marks" to tally how many times each object is selected. For example, if a certain box contains exactly 3 particles, that means the object corresponding to that box was chosen exactly 3 times. The particles being indistinguishable corresponds to the fact that we don't care about the order in which the objects are chosen. Thus, the answer to the original question is also  $\binom{n+k-1}{k}$ .

Another isomorphic problem is to count the number of solutions  $(x_{1},\ldots ,x_{n})$  to the equation  $x_{1} + x_{2} + \dots +x_{n} = k$ , where the  $x_{i}$  are nonnegative integers. This is equivalent since we can think of  $x_{i}$  as the number of particles in the  $i$ th box.

$\star 1.4.23$ . The Bose-Einstein result should not be used in the naive definition of probability except in very special circumstances. For example, consider a survey where a sample of size  $k$  is collected by choosing people from a population of size  $n$

one at a time, with replacement and with equal probabilities. Then the $n^{k}$ *ordered* samples are equally likely, making the naive definition applicable, but the $\binom{n+k-1}{k}$ unordered samples (where all that matters is how many times each person was sampled) are *not* equally likely.

As another example, with $n=365$ days in a year and $k$ people, how many possible *unordered* birthday lists are there? For example, for $k=3$, we want to count lists like (May 1, March 31, April 11), where all permutations are considered equivalent. We can’t do a simple adjustment for overcounting such as $n^{k}/3!$ since, e.g., there are 6 permutations of (May 1, March 31, April 11) but only 3 permutations of (March 31, March 31, April 11). By Bose-Einstein, the number of lists is $\binom{n+k-1}{k}$. But the ordered birthday lists are equally likely, not the unordered lists, so the Bose-Einstein value should not be used in calculating birthday probabilities. ∎

### 1.5 Story proofs

A *story proof* is a proof by interpretation. For counting problems, this often means counting the same thing in two different ways, rather than doing tedious algebra. A story proof often avoids messy calculations and goes further than an algebraic proof toward *explaining* why the result is true. The word “story” has several meanings, some more mathematical than others, but a story proof (in the sense in which we’re using the term) is a fully valid mathematical proof. Here are some examples of story proofs, which also serve as further examples of counting.

###### Example 1.5.1 (Choosing the complement).

For any nonnegative integers $n$ and $k$ with $k\leq n$, we have

$\binom{n}{k}=\binom{n}{n-k}.$

This is easy to check algebraically (by writing the binomial coefficients in terms of factorials), but a story proof makes the result easier to understand intuitively.

*Story proof*: Consider choosing a committee of size $k$ in a group of $n$ people. We know that there are $\binom{n}{k}$ possibilities. But another way to choose the committee is to specify which $n-k$ people are *not* on the committee; specifying who is on the committee determines who is *not* on the committee, and vice versa. So the two sides are equal, as they are two ways of counting the same thing. ∎

###### Example 1.5.2 (The team captain).

For any positive integers $n$ and $k$ with $k\leq n$,

$n\binom{n-1}{k-1}=k\binom{n}{k}.$

This is again easy to check algebraically (using the fact that $m!=m(m-1)!$ for any positive integer $m$), but a story proof is more insightful.

Probability and counting

Story proof: Consider a group of $n$ people, from which a team of $k$ will be chosen, one of whom will be the team captain. To specify a possibility, we could first choose the team captain and then choose the remaining $k-1$ team members; this gives the left-hand side. Equivalently, we could first choose the $k$ team members and then choose one of them to be captain; this gives the right-hand side. ∎

Example 1.5.3 (Vandermonde’s identity). A famous relationship between binomial coefficients, called Vandermonde’s identity, says that

$$
\binom{m + n}{k} = \sum_{j = 0}^{k} \binom{m}{j} \binom{n}{k - j}.
$$

This identity will come up several times in this book. Trying to prove it with a brute force expansion of all the binomial coefficients would be a nightmare. But a story proves the result elegantly and makes it clear why the identity holds.

Story proof: Consider a student organization consisting of $m$ juniors and $n$ seniors, from which a committee of size $k$ will be chosen. There are $\binom{m+n}{k}$ possibilities. If there are $j$ juniors in the committee, then there must be $k - j$ seniors in the committee. The right-hand side of the identity sums up the cases for $j$. ∎

Example 1.5.4 (Partnerships). Let’s use a story proof to show that

$$
\frac{(2n)!}{2^n \cdot n!} = (2n - 1)(2n - 3) \cdots 3 \cdot 1.
$$

Story proof: We will show that both sides count the number of ways to break $2n$ people into $n$ partnerships. Take $2n$ people, and give them ID numbers from 1 to $2n$. We can form partnerships by lining up the people in some order and then saying the first two are a pair, the next two are a pair, etc. This overcounts by a factor of $n! \cdot 2^n$ since the order of pairs doesn’t matter, nor does the order within each pair. Alternatively, count the number of possibilities by noting that there are $2n - 1$ choices for the partner of person 1, then $2n - 3$ choices for person 2 (or person 3, if person 2 was already paired to person 1), and so on. ∎

## 1.6 Non-naive definition of probability

We have now seen several methods for counting outcomes in a sample space, allowing us to calculate probabilities if the naive definition applies. But the naive definition can only take us so far, since it requires equally likely outcomes and can’t handle

²Vandermonde’s identity is named after the 18th century French mathematician Alexandre-Théophile Vandermonde, but it was discovered much earlier, and stated in 1303 by the Chinese mathematician Zhu Shijie.

an infinite sample space. To generalize the notion of probability, we’ll write down a short wish list of how we want probability to behave (in math, the items on the wish list are called *axioms*), and then define a probability function to be something that satisfies the properties we want!

Here is the general definition of probability that we’ll use for the rest of this book. It requires just two axioms, but from these axioms it is possible to prove a vast array of results about probability.

###### Definition 1.6.1 (General definition of probability).

A *probability space* consists of a sample space $S$ and a *probability function* $P$ which takes an event $A\subseteq S$ as input and returns $P(A)$, a real number between $0$ and $1$, as output. The function $P$ must satisfy the following axioms:

1. $P(\emptyset)=0$, $P(S)=1$.
2. If $A_{1},A_{2},\dots$ are disjoint events, then

$P\left(\bigcup_{j=1}^{\infty}A_{j}\right)=\sum_{j=1}^{\infty}P(A_{j}).$

(Saying that these events are *disjoint* means that they are *mutually exclusive*: $A_{i}\cap A_{j}=\emptyset$ for $i\neq j$.)

In Pebble World, the definition says that probability behaves like mass: the mass of an empty pile of pebbles is $0$, the total mass of all the pebbles is $1$, and if we have non-overlapping piles of pebbles, we can get their combined mass by adding the masses of the individual piles. Unlike in the naive case, we can now have pebbles of differing masses, and we can also have a countably infinite number of pebbles as long as their total mass is $1$.

We can even have uncountable sample spaces, such as having $S$ be an area in the plane. In this case, instead of pebbles, we can visualize mud spread out over a region, where the total mass of the mud is $1$.

Any function $P$ (mapping events to numbers in the interval $[0,1]$) that satisfies the two axioms is considered a valid probability function. However, the axioms don’t tell us how probability should be *interpreted*; different schools of thought exist.

The *frequentist* view of probability is that it represents a long-run frequency over a large number of repetitions of an experiment: if we say a coin has probability $1/2$ of Heads, that means the coin would land Heads $50\%$ of the time if we tossed it over and over and over.

The *Bayesian* view of probability is that it represents a degree of belief about the event in question, so we can assign probabilities to hypotheses like “candidate A will win the election” or “the defendant is guilty” even if it isn’t possible to repeat the same election or the same crime over and over again.

Probability and counting

The Bayesian and frequentist perspectives are complementary, and both will be helpful for developing intuition in later chapters. Regardless of how we choose to interpret probability, we can use the two axioms to derive other properties of probability, and these results will hold for any valid probability function.

Theorem 1.6.2 (Properties of probability). Probability has the following properties, for any events  $A$  and  $B$ .

1.  $P(A^c) = 1 - P(A)$ .
2. If  $A \subseteq B$ , then  $P(A) \leq P(B)$ .
3.  $P(A\cup B) = P(A) + P(B) - P(A\cap B)$

# Proof.

1. Since  $A$  and  $A^c$  are disjoint and their union is  $S$ , the second axiom gives

$$
P (S) = P (A \cup A ^ {c}) = P (A) + P (A ^ {c}),
$$

But  $P(S) = 1$  by the first axiom. So  $P(A) + P(A^c) = 1$ .

2. If  $A \subseteq B$ , then we can write  $B$  as the union of  $A$  and  $B \cap A^c$ , where  $B \cap A^c$  is the part of  $B$  not also in  $A$ . This is illustrated in the Venn diagram below.

![img-12.jpeg](img-12.jpeg)

Since  $A$  and  $B \cap A^c$  are disjoint, we can apply the second axiom:

$$
P (B) = P (A \cup (B \cap A ^ {c})) = P (A) + P (B \cap A ^ {c}).
$$

Probability is nonnegative, so  $P(B \cap A^c) \geq 0$ , proving that  $P(B) \geq P(A)$ .

3. The intuition for this result can be seen using a Venn diagram like the one below.

![img-13.jpeg](img-13.jpeg)

Introduction to Probability

The shaded region represents $A\cup B$, but the probability of this region is not the sum $P(A)+P(B)$, because that would count the football-shaped region $A\cap B$ twice. To correct for this, we subtract $P(A\cap B)$. This is a useful intuition, but not a proof.

For a proof using the axioms of probability, we can write $A\cup B$ as the union of the disjoint events $A$ and $B\cap A^{c}$. Then by the second axiom,

$P(A\cup B)=P(A\cup(B\cap A^{c}))=P(A)+P(B\cap A^{c}).$

So it suffices to show that $P(B\cap A^{c})=P(B)-P(A\cap B)$. Since $A\cap B$ and $B\cap A^{c}$ are disjoint and their union is $B$, another application of the second axiom gives us

$P(A\cap B)+P(B\cap A^{c})=P(B).$

So $P(B\cap A^{c})=P(B)-P(A\cap B)$, as desired.

The third property is a special case of inclusion-exclusion, a formula for finding the probability of a union of events when the events are not necessarily disjoint. We showed above that for two events $A$ and $B$,

$P(A\cup B)=P(A)+P(B)-P(A\cap B).$

For three events, inclusion-exclusion says

$P(A\cup B\cup C)$ $=P(A)+P(B)+P(C)$
$\quad-P(A\cap B)-P(A\cap C)-P(B\cap C)$
$\quad+P(A\cap B\cap C).$

For intuition, consider a triple Venn diagram like the one below.

![img-14.jpeg](img-14.jpeg)

To get the total area of the shaded region $A\cup B\cup C$, we start by adding the areas of the three circles, $P(A)+P(B)+P(C)$. The three football-shaped regions have each been counted twice, so we then subtract $P(A\cap B)+P(A\cap C)+P(B\cap C)$. Finally, the region in the center has been added three times and subtracted three times, so in order to count it exactly once, we must add it back again. This ensures that each region of the diagram has been counted once and exactly once.

Now we can write inclusion-exclusion for $n$ events.

###### Theorem 1.6.3 (Inclusion-exclusion).

For any events $A_{1},\ldots,A_{n}$,

\[ P\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum_{i}P(A_{i})-\sum_{i<j}P(A_{i}\cap A_{j})+\sum_{i<j<k}P(A_{i}\cap A_{j}\cap A_{k})-\ldots\\
+(-1)^{n+1}P(A_{1}\cap\cdots\cap A_{n}). \]

This formula can be proven by induction using just the axioms, but instead we’ll present a shorter proof in Chapter 4 after introducing some additional tools. The rationale behind the alternating addition and subtraction in the general formula is analogous to the special cases we’ve already considered.

The next example, de Montmort’s matching problem, is a famous application of inclusion-exclusion. Pierre Rémond de Montmort was a French mathematician who studied probability in the context of gambling and wrote a treatise *[19]* devoted to the analysis of various card games. He posed the following problem in 1708, based on a card game called Treize.

###### Example 1.6.4 (de Montmort’s matching problem).

Consider a well-shuffled deck of $n$ cards, labeled $1$ through $n$. You flip over the cards one by one, saying the numbers $1$ through $n$ as you do so. You win the game if, at some point, the number you say aloud is the same as the number on the card being flipped over (for example, if the $7$th card in the deck has the label $7$). What is the probability of winning?

*Solution*:

Let $A_{i}$ be the event that the $i$th card in the deck has the number $i$ written on it. We are interested in the probability of the union $A_{1}\cup\cdots\cup A_{n}$: as long as at least one of the cards has a number matching its position in the deck, you will win the game. (An ordering for which you lose is called a *derangement*, though hopefully no one has ever become deranged due to losing at this game.)

To find the probability of the union, we’ll use inclusion-exclusion. First,

$P(A_{i})=\frac{1}{n}$

for all $i$. One way to see this is with the naive definition of probability, using the full sample space: there are $n!$ possible orderings of the deck, all equally likely, and $(n-1)!$ of these are favorable to $A_{i}$ (fix the card numbered $i$ to be in the $i$th position in the deck, and then the remaining $n-1$ cards can be in any order). Another way to see this is by symmetry: the card numbered $i$ is equally likely to be in any of the $n$ positions in the deck, so it has probability $1/n$ of being in the $i$th spot. Second,

$P(A_{i}\cap A_{j})=\frac{(n-2)!}{n!}=\frac{1}{n(n-1)},$

since we require the cards numbered $i$ and $j$ to be in the $i$th and $j$th spots in the

ck and allow the remaining $n-2$ cards to be in any order, so $(n-2)!$ out of $n!$ possibilities are favorable to $A_{i}\cap A_{j}$. Similarly,

$P(A_{i}\cap A_{j}\cap A_{k})=\frac{1}{n(n-1)(n-2)},$

and the pattern continues for intersections of 4 events, etc.

In the inclusion-exclusion formula, there are $n$ terms involving one event, $\binom{n}{2}$ terms involving two events, $\binom{n}{3}$ terms involving three events, and so forth. By the symmetry of the problem, all $n$ terms of the form $P(A_{i})$ are equal, all $\binom{n}{2}$ terms of the form $P(A_{i}\cap A_{j})$ are equal, and the whole expression simplifies considerably:

$P\left(\bigcup_{i=1}^{n}A_{i}\right)$ $=\frac{n}{n}-\frac{\binom{n}{2}}{n(n-1)}+\frac{\binom{n}{3}}{n(n-1)(n-2)}-\cdots+(-1)^{n+1}\cdot\frac{1}{n!}$
$=1-\frac{1}{2!}+\frac{1}{3!}-\cdots+(-1)^{n+1}\cdot\frac{1}{n!}.$

Comparing this to the Taylor series for $1/e$ (see Section A.8 of the math appendix),

$e^{-1}=1-\frac{1}{1!}+\frac{1}{2!}-\frac{1}{3!}+\ldots,$

we see that for large $n$, the probability of winning the game is extremely close to $1-1/e$, or about $0.63$. Interestingly, as $n$ grows, the probability of winning approaches $1-1/e$ instead of going to $0$ or $1$. With a lot of cards in the deck, the number of possible locations for matching cards increases while the probability of any particular match decreases, and these two forces offset each other and balance to give a probability of about $1-1/e$. $\square$

Inclusion-exclusion is a very general formula for the probability of a union of events, but it helps us the most when there is symmetry among the events $A_{j}$; otherwise the sum can be extremely tedious. In general, when symmetry is lacking, we should try to use other tools before turning to inclusion-exclusion as a last resort.

### 1.7 Recap

Probability allows us to quantify uncertainty and randomness in a principled way. Probabilities arise when we perform an experiment: the set of all possible outcomes of the experiment is called the sample space, and a subset of the sample space is called an event. It is useful to be able to go back and forth between describing events in English and writing them down mathematically as sets (often using unions, intersections, and complements).

Pebble World can help us visualize sample spaces and events when the sample space is finite. In Pebble World, each outcome is a pebble, and an event is a set of pebbles. If all the pebbles have the same mass (i.e., are equally likely), we can apply the naive definition of probability, which lets us calculate probabilities by counting.

To this end, we discussed several tools for counting. When counting the number of possibilities, we often use the multiplication rule. For example, there are $n!$ permutations of the numbers $1,2,\ldots,n$ and there are $2^{n}$ subsets of a set with $n$ elements. If we can’t directly use the multiplication rule, we can sometimes count each possibility exactly $c$ times for some $c$, and then divide by $c$ to get the actual number of possibilities. For example, this strategy is useful for finding an expression for binomial coefficients in terms of factorials.

An important pitfall to avoid is misapplying the naive definition of probability, implicitly or explicitly assuming equally likely outcomes without justification. One technique to help avoid this is to give objects labels, for precision and so that we are not tempted to treat them as indistinguishable.

Moving beyond the naive definition, we define probability to be a function that takes an event and assigns to it a real number between $0$ and $1$. We require a valid probability function to satisfy two axioms:

1. $P(\emptyset)=0$, $P(S)=1$.

2. If $A_{1},A_{2},\ldots$ are disjoint events, then

$P\left(\bigcup_{j=1}^{\infty}A_{j}\right)=\sum_{j=1}^{\infty}P(A_{j}).$

Many useful properties can be derived from these axioms. For example,

$P(A^{c})=1-P(A)$

for any event $A$, and we have the inclusion-exclusion formula

\[ P\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum_{i}P(A_{i})-\sum_{i<j}P(A_{i}\cap A_{j})+\sum_{i<j<k}P(A_{i}\cap A_{j}\cap A_{k})-\ldots\\
+(-1)^{n+1}P(A_{1}\cap\cdots\cap A_{n}) \]

for any events $A_{1},\ldots,A_{n}$. For $n=2$, this is the much nicer-looking result

$P(A_{1}\cup A_{2})=P(A_{1})+P(A_{2})-P(A_{1}\cap A_{2}).$

Figure 7 illustrates how a probability function maps events to numbers between $0$ and $1$. We’ll add many new concepts to this diagram as we continue our journey through the field of probability.

Introduction to Probability

![img-15.jpeg](img-15.jpeg)
FIGURE 1.7 It is important to distinguish between events and probabilities. The former are sets, while the latter are numbers. Before the experiment is done, we generally don't know whether or not a particular event will occur (happen). So we assign it a probability of happening, using a probability function  $P$ . We can use set operations to define new events in terms of old events, and the properties of probabilities to relate the probabilities of the new events to those of the old events.

1.8 R

R is a very powerful, popular environment for statistical computing and graphics, freely available for Mac OS X, Windows, and UNIX systems. Knowing how to use R is an extremely useful skill. R and various supporting information can be obtained at https://www.r-project.org. RStudio is an excellent alternative interface for R, freely available at https://www.rstudio.com.

In the R section at the end of each chapter, we provide R code to let you try out some of the examples from the chapter, especially via simulation. These sections are not intended to be a full introduction to R; many R tutorials are available for free online, and many books on R are available. But the R sections show how to implement various simulations, computations, and visualizations that naturally accompany the material from each chapter. The R code at the end of each chapter is also available at http://stat110.net.

#### Vectors

R is built around vectors, and getting familiar with “vectorized thinking” is very important for using R effectively. To create a vector, we can use the c command (which stands for combine or concatenate). For example,

```
v <- c(3,1,4,1,5,9)
```

defines v to be the vector $(3,1,4,1,5,9)$. (The left arrow <- is typed as < followed by -. The symbol = can be used instead, but the arrow is more suggestive of the fact that the variable on the left is being set equal to the value on the right.) Similarly, n <- 110 sets $n$ equal to 110; R views $n$ as a vector of length 1.

```
sum(v)
```

adds up the entries of v, max(v) gives the largest value, min(v) gives the smallest value, and length(v) gives the length.

A shortcut for getting the vector $(1,2,\ldots,n)$ is to type 1:n; more generally, if $m$ and $n$ are integers then m:n gives the sequence of integers from $m$ to $n$ (in increasing order if $m\leq n$ and in decreasing order otherwise).

To access the $i$th entry of a vector v, use v[i]. We can also get subvectors easily:

```
v[c(1,3,5)]
```

gives the vector consisting of the 1st, 3rd, and 5th entries of v. It’s also possible to get a subvector by specifying what to exclude, using a minus sign:

```
v[-(2:4)]

gives the vector obtained by removing the 2nd through 4th entries of $\mathbf{v}$ (the parentheses are needed since -2:4 would be $(-2,-1,\ldots,4)$).

Many operations in R are interpreted *componentwise*. For example, in math the cube of a vector doesn’t have a standard definition, but in R typing v^3 simply cubes each entry individually. Similarly,

1/(1:100)^2

is a very compact way to get the vector $(1,\frac{1}{2^{2}},\frac{1}{3^{2}},\ldots,\frac{1}{100^{2}})$.

In math, $\mathbf{v}+\mathbf{w}$ is undefined if $\mathbf{v}$ and $\mathbf{w}$ are vectors of different lengths, but in R the shorter vector gets “recycled”! For example, v+3 adds 3 to each entry of $\mathbf{v}$.

##### Factorials and binomial coefficients

We can compute $n!$ using factorial(n) and $\binom{n}{k}$ using choose(n,k). As we have seen, factorials grow extremely quickly. What is the largest $n$ for which R returns a number for factorial(n)? Beyond that point, R will return Inf (infinity), with a warning message. But it may still be possible to use lfactorial(n) for larger values of $n$, which computes $\log(n!)$. Similarly, lchoose(n,k) computes $\log\binom{n}{k}$.

##### Sampling and simulation

The sample command is a useful way of drawing random samples in R. (Technically, they are *pseudo-random* since there is an underlying deterministic algorithm, but they “look like” random samples for almost all practical purposes.) For example,

n <- 10; k <- 5
sample(n,k)

generates an ordered random sample of 5 of the numbers from 1 to 10, without replacement, and with equal probabilities given to each number. To sample with replacement instead, just add in replace = TRUE:

n <- 10; k <- 5
sample(n,k,replace=TRUE)

To generate a random permutation of $1,2,\ldots,n$ we can use sample(n,n), which because of R’s default settings can be abbreviated to sample(n).

We can also use sample to draw from a non-numeric vector. For example, letters is built into R as the vector consisting of the 26 lowercase letters of the English alphabet, and sample(letters,7) will generate a random 7-letter “word” by sampling from the alphabet, without replacement.

The sample command also allows us to specify general probabilities for sampling each number. For example,

```
sample(4, 3, replace=TRUE, prob=c(0.1,0.2,0.3,0.4))
```

samples three numbers between 1 and 4, with replacement, and with probabilities given by $(0.1,0.2,0.3,0.4)$. If the sampling is without replacement, then at each stage the probability of any not-yet-chosen number is *proportional* to its original probability.

Generating *many* random samples allows us to perform a *simulation* for a probability problem. The replicate command, which is explained below, is a convenient way to do this.

#### 3.2.2 Matching problem simulation

Let’s show by simulation that the probability of a matching card in Example 1.6.4 is approximately $1-1/e$ when the deck is sufficiently large. Using R, we can perform the experiment a bunch of times and see how many times we encounter at least one matching card:

```
n <- 100
r <- replicate(10^4,sum(sample(n)==(1:n)))
sum(r>=1)/10^4
```

In the first line, we choose how many cards are in the deck (here, 100 cards). In the second line, let’s work from the inside out:

- sample(n)==(1:n) is a vector of length n, the $i$th element of which equals 1 if the $i$th card matches its position in the deck and 0 otherwise. That’s because for two numbers $a$ and $b$, the expression a==b is TRUE if $a=b$ and FALSE otherwise, and TRUE is encoded as 1 and FALSE is encoded as 0.
- sum adds up the elements of the vector, giving us the number of matching cards in this run of the experiment.
- replicate does this $10^{4}$ times. We store the results in r, a vector of length $10^{4}$ containing the numbers of matched cards from each run of the experiment.

In the last line, we add up the number of times where there was at least one matching card, and we divide by the number of simulations.

To explain what the code is doing within the code rather than in separate documentation, we can add *comments* using the # symbol to mark the start of a comment. Comments are ignored by R but can make the code much easier to understand for the reader (who could be you—even if you will be the only one using your code, it is often hard to remember what everything means and how the code is supposed to work when looking at it a month after writing it). Short comments can be on the

same line as the corresponding code; longer comments should be on separate lines. For example, a commented version of the above simulation is:

```
n <- 100 # number of cards
r <- replicate(10^4,sum(sample(n)==(1:n))) # shuffle; count matches
sum(r>=1)/10^4 # proportion with a match
```

What did you get when you ran the code? We got 0.63, which is quite close to $1-1/e$.

#### 3.2.2 Birthday problem calculation and simulation

The following code uses prod (which gives the product of a vector) to calculate the probability of at least one birthday match in a group of 23 people:

```
k <- 23
1-prod((365-k+1):365)/365^k
```

Better yet, R has built-in functions, pbirthday and qbirthday, for the birthday problem! pbirthday(k) returns the probability of at least one match if the room has k people. qbirthday(p) returns the number of people needed in order to have probability p of at least one match. For example, pbirthday(23) is 0.507 and qbirthday(0.5) is 23.

We can also find the probability of having at least one triple birthday match, i.e., three people with the same birthday; all we have to do is add coincident=3 to say we’re looking for triple matches. For example, pbirthday(23,coincident=3) returns 0.014, so 23 people give us only a 1.4% chance of a triple birthday match. qbirthday(0.5,coincident=3) returns 88, so we’d need 88 people to have at least a 50% chance of at least one triple birthday match.

To simulate the birthday problem, we can use

```
b <- sample(1:365,23,replace=TRUE)
tabulate(b)
```

to generate random birthdays for 23 people and then tabulate the counts of how many people were born on each day (the command table(b) creates a prettier table, but is slower). We can run $10^{4}$ repetitions as follows:

```
r <- replicate(10^4, max(tabulate(sample(1:365,23,replace=TRUE))))
sum(r>=2)/10^4
```

If the probabilities of various days are not all equal, the calculation becomes much more difficult, but the simulation can easily be extended since sample allows us to specify the probability of each day (by default sample assigns equal probabilities, so in the above the probability is 1/365 for each day).

Probability and counting

# 1.9 Exercises

Exercises marked with ⑧ have detailed solutions at http://stat110.net.

###### Counting

- How many ways are there to permute the letters in the word MISSISSIPPI?
- (a) How many 7-digit phone numbers are possible, assuming that the first digit can’t be a 0 or a 1?

(b) Re-solve (a), except now assume also that the phone number is not allowed to start with 911 (since this is reserved for emergency use, and it would not be desirable for the system to wait to see whether more digits were going to be dialed after someone has dialed 911).
- Fred is planning to go out to dinner each night of a certain week, Monday through Friday, with each dinner being at one of his ten favorite restaurants.

(a) How many possibilities are there for Fred’s schedule of dinners for that Monday through Friday, if Fred is not willing to eat at the same restaurant more than once?

(b) How many possibilities are there for Fred’s schedule of dinners for that Monday through Friday, if Fred is willing to eat at the same restaurant more than once, but is not willing to eat at the same place twice in a row (or more)?
- A *round-robin tournament* is being held with $n$ tennis players; this means that every player will play against every other player exactly once.

(a) How many possible outcomes are there for the tournament (the outcome lists out who won and who lost for each game)?

(b) How many games are played in total?
- A *knock-out tournament* is being held with $2^{n}$ tennis players. This means that for each round, the winners move on to the next round and the losers are eliminated, until only one person remains. For example, if initially there are $2^{4}=16$ players, then there are 8 games in the first round, then the 8 winners move on to round 2, then the 4 winners move on to round 3, then the 2 winners move on to round 4, the winner of which is declared the winner of the tournament. (There are various systems for determining who plays whom within a round, but these do not matter for this problem.)

(a) How many rounds are there?

(b) Count how many games in total are played, by adding up the numbers of games played in each round.

(c) Count how many games in total are played, this time by directly thinking about it without doing almost any calculation.

Hint: How many players need to be eliminated?
- There are 20 people at a chess club on a certain day. They each find opponents and start playing. How many possibilities are there for how they are matched up, assuming that in each game it *does* matter who has the white pieces (in a chess game, one player has the white pieces and the other player has the black pieces)?

7. Two chess players, A and B, are going to play 7 games. Each game has three possible outcomes: a win for A (which is a loss for B), a draw (tie), and a loss for A (which is a win for B). A win is worth 1 point, a draw is worth 0.5 points, and a loss is worth 0 points.

1. How many possible outcomes for the individual games are there, such that overall player A ends up with 3 wins, 2 draws, and 2 losses?
2. How many possible outcomes for the individual games are there, such that A ends up with 4 points and B ends up with 3 points?
3. Now assume that they are playing a best-of-7 match, where the match will end when either player has 4 points or when 7 games have been played, whichever is first. For example, if after 6 games the score is 4 to 2 in favor of A, then A wins the match and they don’t play a 7th game. How many possible outcomes for the individual games are there, such that the match lasts for 7 games and A wins by a score of 4 to 3?
8. 1. (a) How many ways are there to split a dozen people into 3 teams, where one team has 2 people, and the other two teams have 5 people each?
2. (b) How many ways are there to split a dozen people into 3 teams, where each team has 4 people?
9. 2. (a) How many paths are there from the point $(0,0)$ to the point $(110,111)$ in the plane such that each step either consists of going one unit up or one unit to the right?
3. (b) How many paths are there from $(0,0)$ to $(210,211)$, where each step consists of going one unit up or one unit to the right, and the path has to go through $(110,111)$?
10. To fulfill the requirements for a certain degree, a student can choose to take any 7 out of a list of 20 courses, with the constraint that at least 1 of the 7 courses must be a statistics course. Suppose that 5 of the 20 courses are statistics courses.

1. How many choices are there for which 7 courses to take?
2. Explain intuitively why the answer to (a) is not $\binom{5}{1}\cdot\binom{19}{6}$.
11. Let $A$ and $B$ be sets with $|A|=n,|B|=m$.

1. How many functions are there from $A$ to $B$ (i.e., functions with domain $A$, assigning an element of $B$ to each element of $A$)?
2. How many one-to-one functions are there from $A$ to $B$? (See Section A.2.1 of the math appendix for information about one-to-one functions.)
12. Four players, named A, B, C, and D, are playing a card game. A standard, well-shuffled deck of cards is dealt to the players (so each player receives a 13-card hand).

1. How many possibilities are there for the hand that player A will get? (Within a hand, the order in which cards were received doesn’t matter.)
2. How many possibilities are there overall for what hands everyone will get, assuming that it matters which player gets which hand, but not the order of cards within a hand?
3. Explain intuitively why the answer to Part (b) is not the fourth power of the answer to Part (a).
13. A certain casino uses 10 standard decks of cards mixed together into one big deck, which we will call a superdeck. Thus, the superdeck has $52\cdot 10=520$ cards, with 10 copies of each card. How many different 10-card hands can be dealt from the superdeck? The order of the cards does not matter, nor does it matter which of the original 10 decks the cards came from. Express your answer as a binomial coefficient.

Hint: Bose-Einstein.
14. You are ordering two pizzas. A pizza can be small, medium, large, or extra large, with any combination of 8 possible toppings (getting no toppings is allowed, as is getting all 8). How many possibilities are there for your two pizzas?

Probability and counting

# Story proofs

15. ⑤ Give a story proof that $\sum_{k=0}^{n} \binom{n}{k} = 2^n$.

16. ⑤ Show that for all positive integers $n$ and $k$ with $n \geq k$,

$$
\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k},
$$

doing this in two ways: (a) algebraically and (b) with a story, giving an interpretation for why both sides count the same thing.

Hint: for the story proof: Imagine an organization consisting of $n + 1$ people, with one of them pre-designated as the president of the organization.

17. Give a story proof that

$$
\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n},
$$

for all positive integers $n$.

18. Give a story proof that

$$
\sum_{k=1}^{n} k \binom{n}{k}^2 = n \binom{2n-1}{n-1},
$$

for all positive integers $n$.

Hint: Consider choosing a committee of size $n$ from two groups of size $n$ each, where only one of the two groups has people eligible to become the chair of the committee.

19. Give a story proof that

$$
\sum_{k=2}^{n} \binom{k}{2} \binom{n-k+2}{2} = \binom{n+3}{5},
$$

for all integers $n \geq 2$.

Hint: Consider the middle number in a subset of $\{1, 2, \ldots, n + 3\}$ of size 5.

20. ⑤ (a) Show using a story proof that

$$
\binom{k}{k} + \binom{k+1}{k} + \binom{k+2}{k} + \cdots + \binom{n}{k} = \binom{n+1}{k+1},
$$

where $n$ and $k$ are positive integers with $n \geq k$. This is called the hockey stick identity.

Hint: Imagine arranging a group of people by age, and then think about the oldest person in a chosen subgroup.

(b) Suppose that a large pack of Haribo gummi bears can have anywhere between 30 and 50 gummi bears. There are 5 delicious flavors: pineapple (clear), raspberry (red), orange (orange), strawberry (green, mysteriously), and lemon (yellow). There are 0 non-delicious flavors. How many possibilities are there for the composition of such a pack of gummi bears? You can leave your answer in terms of a couple binomial coefficients, but not a sum of lots of binomial coefficients.

21. Define $\binom{n}{k}$ as the number of ways to partition $\{1, 2, \ldots, n\}$ into $k$ nonempty subsets, or the number of ways to have $n$ students split up into $k$ groups such that each group has at least one student. For example, $\binom{4}{2} = 7$ because we have the following possibilities.

Introduction to Probability

$\bullet$ $\{1\}$, $\{2,3,4\}$
$\bullet$ $\{1,2\}$, $\{3,4\}$
$\bullet$ $\{2\}$, $\{1,3,4\}$
$\bullet$ $\{1,3\}$, $\{2,4\}$
$\bullet$ $\{3\}$, $\{1,2,4\}$
$\bullet$ $\{4\}$, $\{1,2,3\}$
$\bullet$ $\{1,4\}$, $\{2,3\}$

Prove the following identities:

(a)

$$
\left\{ \begin{array}{c} n + 1 \\ k \end{array} \right\} = \left\{ \begin{array}{c} n \\ k - 1 \end{array} \right\} + k \left\{ \begin{array}{c} n \\ k \end{array} \right\}.
$$

Hint: I'm either in a group by myself or I'm not.

(b)

$$
\sum_{j = k}^{n} \binom{n}{j} \left\{ \begin{array}{l} j \\ k \end{array} \right\} = \left\{ \begin{array}{l} n + 1 \\ k + 1 \end{array} \right\}.
$$

Hint: First decide how many people are not going to be in my group.

22. The Dutch mathematician R.J. Stroeker remarked:

Every beginning student of number theory surely must have marveled at the miraculous fact that for each natural number $n$ the sum of the first $n$ positive consecutive cubes is a perfect square. [26]

Furthermore, it is the square of the sum of the first $n$ positive integers! That is,

$$
1^{3} + 2^{3} + \cdots + n^{3} = (1 + 2 + \cdots + n)^{2}.
$$

Usually this identity is proven by induction, but that does not give much insight into why the result is true, nor does it help much if we wanted to compute the left-hand side but didn't already know this result. In this problem, you will give a story proof of the identity.

(a) Give a story proof of the identity

$$
1 + 2 + \cdots + n = \binom{n + 1}{2}.
$$

Hint: Consider a round-robin tournament (see Exercise 4).

(b) Give a story proof of the identity

$$
1^{3} + 2^{3} + \cdots + n^{3} = 6 \binom{n + 1}{4} + 6 \binom{n + 1}{3} + \binom{n + 1}{2}.
$$

It is then just basic algebra (not required for this problem) to check that the square of the right-hand side in (a) is the right-hand side in (b).

Hint: Imagine choosing a number between 1 and $n$ and then choosing 3 numbers between 0 and $n$ smaller than the original number, with replacement. Then consider cases based on how many distinct numbers were chosen.

## Naive definition of probability

23. Three people get into an empty elevator at the first floor of a building that has 10 floors. Each presses the button for their desired floor (unless one of the others has already pressed that button). Assume that they are equally likely to want to go to floors 2 through 10 (independently of each other). What is the probability that the buttons for 3 consecutive floors are pressed?

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

Introduction to Probability

elk in the new sample were previously tagged? (Assume that an elk that was captured before doesn’t become more or less likely to be captured again.)
32. Four cards are face down on a table. You are told that two are red and two are black, and you need to guess which two are red and which two are black. You do this by pointing to the two cards you’re guessing are red (and then implicitly you’re guessing that the other two are black). Assume that all configurations are equally likely, and that you do not have psychic powers. Find the probability that exactly $j$ of your guesses are correct, for $j=0,1,2,3,4$.
33. $\circledS$ A jar contains $r$ red balls and $g$ green balls, where $r$ and $g$ are fixed positive integers. A ball is drawn from the jar randomly (with all possibilities equally likely), and then a second ball is drawn randomly.

(a) Explain intuitively why the probability of the second ball being green is the same as the probability of the first ball being green.

(b) Define notation for the sample space of the problem, and use this to compute the probabilities from (a) and show that they are the same.

(c) Suppose that there are 16 balls in total, and that the probability that the two balls are the same color is the same as the probability that they are different colors. What are $r$ and $g$ (list all possibilities)?
34. $\circledS$ A random 5-card poker hand is dealt from a standard deck of cards. Find the probability of each of the following possibilities (in terms of binomial coefficients).

(a) A flush (all 5 cards being of the same suit; do not count a royal flush, which is a flush with an ace, king, queen, jack, and 10).

(b) Two pair (e.g., two 3’s, two 7’s, and an ace).
35. A random 13-card hand is dealt from a standard deck of cards. What is the probability that the hand contains at least 3 cards of every suit?
36. A group of 30 dice are thrown. What is the probability that 5 of each of the values $1,2,3,4,5,6$ appear?
37. A deck of cards is shuffled well. The cards are dealt one by one, until the first time an ace appears.

(a) Find the probability that no kings, queens, or jacks appear before the first ace.

(b) Find the probability that exactly one king, exactly one queen, and exactly one jack appear (in any order) before the first ace.
38. Tyrion, Cersei, and ten other people are sitting at a round table, with their seating arrangement having been randomly assigned. What is the probability that Tyrion and Cersei are sitting next to each other? Find this in two ways:

(a) using a sample space of size 12!, where an outcome is fully detailed about the seating;

(b) using a much smaller sample space, which focuses on Tyrion and Cersei.
39. An organization with $2n$ people consists of $n$ married couples. A committee of size $k$ is selected, with all possibilities equally likely. Find the probability that there are exactly $j$ married couples within the committee.
40. There are $n$ balls in a jar, labeled with the numbers $1,2,\ldots,n$. A total of $k$ balls are drawn, one by one *with replacement*, to obtain a sequence of numbers.

(a) What is the probability that the sequence obtained is strictly increasing?

(b) What is the probability that the sequence obtained is increasing (but not necessarily strictly increasing, i.e., there can be repetitions)?

4. Each of $n$ balls is independently placed into one of $n$ boxes, with all boxes equally likely. What is the probability that exactly one box is empty?
5. A *norepeatword* is a sequence of at least one (and possibly all) of the usual 26 letters a,b,c,…,z, with repetitions not allowed. For example, “course” is a norepeatword, but “statistics” is not. Order matters, e.g., “course” is not the same as “source”.

A norepeatword is chosen randomly, with all norepeatwords equally likely. Show that the probability that it uses all 26 letters is very close to $1/e$.

### Axioms of probability

1. Show that for any events $A$ and $B$,

$P(A)+P(B)-1\leq P(A\cap B)\leq P(A\cup B)\leq P(A)+P(B).$

For each of these three inequalities, give a simple criterion for when the inequality is actually an equality (e.g., give a simple condition such that $P(A\cap B)=P(A\cup B)$ if and only if the condition holds).
2. Let $A$ and $B$ be events. The *difference* $B-A$ is defined to be the set of all elements of $B$ that are not in $A$. Show that if $A\subseteq B$, then

$P(B-A)=P(B)-P(A),$

directly using the axioms of probability.
3. Let $A$ and $B$ be events. The *symmetric difference* $A\triangle B$ is defined to be the set of all elements that are in $A$ or $B$ but not both. In logic and engineering, this event is also called the *XOR* (*exclusive or*) of $A$ and $B$. Show that

$P(A\triangle B)=P(A)+P(B)-2P(A\cap B),$

directly using the axioms of probability.
4. Let $A_{1},A_{2},\ldots,A_{n}$ be events. Let $B_{k}$ be the event exactly $k$ of the $A_{i}$ occur, and $C_{k}$ be the event that at least $k$ of the $A_{i}$ occur, for $0\leq k\leq n$. Find a simple expression for $P(B_{k})$ in terms of $P(C_{k})$ and $P(C_{k+1})$.
5. Events $A$ and $B$ are *independent* if $P(A\cap B)=P(A)P(B)$ (independence is explored in detail in the next chapter).

(a) Give an example of independent events $A$ and $B$ in a finite sample space $S$ (with neither equal to $\emptyset$ or $S$), and illustrate it with a Pebble World diagram.

(b) Consider the experiment of picking a random point in the rectangle

$R=\{(x,y):0<x<1,0<y<1\},$

where the probability of the point being in any particular region contained within $R$ is the area of that region. Let $A_{1}$ and $B_{1}$ be rectangles contained within $R$, with areas not equal to $0$ or $1$. Let $A$ be the event that the random point is in $A_{1}$, and $B$ be the event that the random point is in $B_{1}$. Give a geometric description of when it is true that $A$ and $B$ are independent. Also, give an example where they are independent and another example where they are not independent.

(c) Show that if $A$ and $B$ are independent, then

$P(A\cup B)=P(A)+P(B)-P(A)P(B)=1-P(A^{c})P(B^{c}).$

Introduction to Probability

48.  $\odot$  Arby has a belief system assigning a number  $P_{\mathrm{Arby}}(A)$  between 0 and 1 to every event  $A$  (for some sample space). This represents Arby's degree of belief about how likely  $A$  is to occur. For any event  $A$ , Arby is willing to pay a price of  $1000 \cdot P_{\mathrm{Arby}}(A)$  dollars to buy a certificate such as the one shown below:

# Certificate

The owner of this certificate can redeem it for $1000 if A occurs. No value if A does not occur, except as required by federal, state, or local law. No expiration date.

Likewise, Arby is willing to sell such a certificate at the same price. Indeed, Arby is willing to buy or sell any number of certificates at this price, as Arby considers it the "fair" price.

Arby stubbornly refuses to accept the axioms of probability. In particular, suppose that there are two disjoint events  $A$  and  $B$  with

$$
P _ {\mathrm {A r b y}} (A \cup B) \neq P _ {\mathrm {A r b y}} (A) + P _ {\mathrm {A r b y}} (B).
$$

Show how to make Arby go bankrupt, by giving a list of transactions Arby is willing to make that will guarantee that Arby will lose money (you can assume it will be known whether  $A$  occurred and whether  $B$  occurred the day after any certificates are bought/sold).

# Inclusion-exclusion

49. A fair die is rolled  $n$  times. What is the probability that at least 1 of the 6 values never appears?
50.  $\odot$  A card player is dealt a 13-card hand from a well-shuffled, standard deck of cards. What is the probability that the hand is void in at least one suit ("void in a suit" means having no cards of that suit)?
51.  $\odot$  For a group of 7 people, find the probability that all 4 seasons (winter, spring, summer, fall) occur at least once each among their birthdays, assuming that all seasons are equally likely.
52. A certain class has 20 students, and meets on Mondays and Wednesdays in a classroom with exactly 20 seats. In a certain week, everyone in the class attends both days. On both days, the students choose their seats completely randomly (with one student per seat). Find the probability that no one sits in the same seat on both days of that week.
53. Fred needs to choose a password for a certain website. Assume that he will choose an 8-character password, and that the legal characters are the lowercase letters a, b, c, ..., z, the uppercase letters A, B, C, ..., Z, and the numbers 0, 1, ..., 9.

(a) How many possibilities are there if he is required to have at least one lowercase letter in his password?
(b) How many possibilities are there if he is required to have at least one lowercase letter and at least one uppercase letter in his password?
(c) How many possibilities are there if he is required to have at least one lowercase letter, at least one uppercase letter, and at least one number in his password?

54. ⑤ Alice attends a small college in which each class meets only once a week. She is deciding between 30 non-overlapping classes. There are 6 classes to choose from for each day of the week, Monday through Friday. Trusting in the benevolence of randomness, Alice decides to register for 7 randomly selected classes out of the 30, with all choices equally likely. What is the probability that she will have classes every day, Monday through Friday? (This problem can be done either directly using the naive definition of probability, or using inclusion-exclusion.)
55. A club consists of 10 seniors, 12 juniors, and 15 sophomores. An organizing committee of size 5 is chosen randomly (with all subsets of size 5 equally likely).

(a) Find the probability that there are exactly 3 sophomores in the committee.

(b) Find the probability that the committee has at least one representative from each of the senior, junior, and sophomore classes.

### Mixed practice

56. For each part, decide whether the blank should be filled in with =, <, or >, and give a clear explanation. In (a) and (b), order doesn’t matter.

(a) (number of ways to choose 5 people out of 10) ___ (number of ways to choose 6 people out of 10)

(b) (number of ways to break 10 people into 2 teams of 5) ___ (number of ways to break 10 people into a team of 6 and a team of 4)

(c) (probability that all 3 people in a group of 3 were born on January 1) ___ (probability that in a group of 3 people, 1 was born on each of January 1, 2, and 3)

Martin and Gale play an exciting game of “toss the coin”, where they toss a fair coin until the pattern $HH$ occurs (two consecutive Heads) or the pattern $TH$ occurs (Tails followed immediately by Heads). Martin wins the game if and only if $HH$ occurs before $TH$ occurs.

(d) (probability that Martin wins) ___ 1/2
57. Take a deep breath before attempting this problem. In the book *Innumeracy* *[20]*, John Allen Paulos writes:

> Now for better news of a kind of immortal persistence. First, take a deep breath. Assume Shakespeare’s account is accurate and Julius Caesar gasped [“Et tu, Brute!”] before breathing his last. What are the chances you just inhaled a molecule which Caesar exhaled in his dying breath?

Assume that one breath of air contains $10^{22}$ molecules, and that there are $10^{44}$ molecules in the atmosphere. (These are slightly simpler numbers than the estimates that Paulos gives; for the purposes of this problem, assume that these are exact. Of course, in reality there are many complications such as different types of molecules in the atmosphere, chemical reactions, variation in lung capacities, etc.)

Suppose that the molecules in the atmosphere now are the same as those in the atmosphere when Caesar was alive, and that in the 2000 years or so since Caesar, these molecules have been scattered completely randomly through the atmosphere. Also assume that Caesar’s last breath was sampled *without* replacement but that your breathing is sampled *with* replacement (without replacement makes more sense but with replacement is easier to work with, and is a good approximation since the number of molecules in the atmosphere is so much larger than the number of molecules in one breath).

Find the probability that at least one molecule in the breath you just took was shared with Caesar’s last breath, and give a simple approximation in terms of $e$.

Hint: As discussed in the math appendix, $(1+\frac{x}{n})^{n}\approx e^{x}$ for $n$ large.
58. A widget inspector inspects 12 widgets and finds that exactly 3 are defective. Unfortunately, the widgets then get all mixed up and the inspector has to find the 3 defective widgets again by testing widgets one by one.

1. Find the probability that the inspector will now have to test at least 9 widgets.
2. Find the probability that the inspector will now have to test at least 10 widgets.
59. There are 15 chocolate bars and 10 children. In how many ways can the chocolate bars be distributed to the children, in each of the following scenarios?

1. The chocolate bars are fungible (interchangeable).
2. The chocolate bars are fungible, and each child must receive at least one.

Hint: First give each child a chocolate bar, and then decide what to do with the rest.

1. The chocolate bars are not fungible (it matters which particular bar goes where).
2. The chocolate bars are not fungible, and each child must receive at least one.

Hint: The strategy suggested in (b) does not apply. Instead, consider *randomly* giving the chocolate bars to the children, and apply inclusion-exclusion.
60. Given $n\geq 2$ numbers $(a_{1},a_{2},\ldots,a_{n})$ with no repetitions, a *bootstrap sample* is a sequence $(x_{1},x_{2},\ldots,x_{n})$ formed from the $a_{j}$’s by sampling with replacement with equal probabilities. Bootstrap samples arise in a widely used statistical method known as the *bootstrap*. For example, if $n=2$ and $(a_{1},a_{2})=(3,1)$, then the possible bootstrap samples are $(3,3),(3,1),(1,3)$, and $(1,1)$.

1. How many possible bootstrap samples are there for $(a_{1},\ldots,a_{n})$?

1. How many possible bootstrap samples are there for $(a_{1},\ldots,a_{n})$, if order does not matter (in the sense that it only matters how many times each $a_{j}$ was chosen, not the order in which they were chosen)?

1. One random bootstrap sample is chosen (by sampling from $a_{1},\ldots,a_{n}$ with replacement, as described above). Show that not all unordered bootstrap samples (in the sense of (b)) are equally likely. Find an unordered bootstrap sample $\mathbf{b}_{1}$ that is as likely as possible, and an unordered bootstrap sample $\mathbf{b}_{2}$ that is as unlikely as possible. Let $p_{1}$ be the probability of getting $\mathbf{b}_{1}$ and $p_{2}$ be the probability of getting $\mathbf{b}_{2}$ (so $p_{i}$ is the probability of getting the *specific* unordered bootstrap sample $\mathbf{b}_{i}$). What is $p_{1}/p_{2}$? What is the ratio of the probability of getting an unordered bootstrap sample whose probability is $p_{1}$ to the probability of getting an unordered sample whose probability is $p_{2}$?
61. ⑧ There are 100 passengers lined up to board an airplane with 100 seats (with each seat assigned to one of the passengers). The first passenger in line crazily decides to sit in a randomly chosen seat (with all seats equally likely). Each subsequent passenger takes their assigned seat if available, and otherwise sits in a random available seat. What is the probability that the last passenger in line gets to sit in their assigned seat? (This is a common interview problem, and a beautiful example of the power of symmetry.)

Hint: Call the seat assigned to the $j$th passenger in line “seat $j$” (regardless of whether the airline calls it seat 23A or whatever). What are the possibilities for which seats are available to the last passenger in line, and what is the probability of each of these possibilities?

62. In the birthday problem, we assumed that all 365 days of the year are equally likely (and excluded February 29). In reality, some days are slightly more likely as birthdays than others. For example, scientists have long struggled to understand why more babies are born 9 months after a holiday. Let $\mathbf{p}=(p_{1},p_{2},\ldots,p_{365})$ be the vector of birthday probabilities, with $p_{j}$ the probability of being born on the $j$th day of the year (February 29 is still excluded, with no offense intended to Leap Dayers).

The $k$th *elementary symmetric polynomial* in the variables $x_{1},\ldots,x_{n}$ is defined by

$e_{k}(x_{1},\ldots,x_{n})=\sum_{1\leq j_{1}<j_{2}<\cdots<j_{k}\leq n}x_{j_{1}}\ldots x_{j_{k}}.$

This just says to add up all of the $\binom{n}{k}$ terms we can get by choosing and multiplying $k$ of the variables. For example, $e_{1}(x_{1},x_{2},x_{3})=x_{1}+x_{2}+x_{3}$, $e_{2}(x_{1},x_{2},x_{3})=x_{1}x_{2}+x_{1}x_{3}+x_{2}x_{3}$, and $e_{3}(x_{1},x_{2},x_{3})=x_{1}x_{2}x_{3}$.

Now let $k\geq 2$ be the number of people.

(a) Find a simple expression for the probability that there is at least one birthday match, in terms of $\mathbf{p}$ and an elementary symmetric polynomial.

(b) Explain intuitively why it makes sense that $P(\text{at least one birthday match})$ is minimized when $p_{j}=\frac{1}{365}$ for all $j$, by considering simple and extreme cases.

(c) The famous *arithmetic mean-geometric mean inequality* says that for $x,y\geq 0$,

$\frac{x+y}{2}\geq\sqrt{xy}.$

This inequality follows from adding $4xy$ to both sides of $x^{2}-2xy+y^{2}=(x-y)^{2}\geq 0$.

Define $\mathbf{r}=(r_{1},\ldots,r_{365})$ by $r_{1}=r_{2}=(p_{1}+p_{2})/2$, $r_{j}=p_{j}$ for $3\leq j\leq 365$. Using the arithmetic mean-geometric mean bound and the fact, which you should verify, that

$e_{k}(x_{1},\ldots,x_{n})=x_{1}x_{2}e_{k-2}(x_{3},\ldots,x_{n})+(x_{1}+x_{2})e_{k-1}(x_{3},\ldots,x_{n})+e_{k}(x_{3},\ldots,x_{n}),$

show that

$P(\text{at least one birthday match}|\mathbf{p})\geq P(\text{at least one birthday match}|\mathbf{r}),$

with strict inequality if $\mathbf{p}\neq\mathbf{r}$, where the “given $\mathbf{r}$” notation means that the birthday probabilities are given by $\mathbf{r}$. Using this, show that the value of $\mathbf{p}$ that minimizes the probability of at least one birthday match is given by $p_{j}=\frac{1}{365}$ for all $j$.

##

![img-16.jpeg](img-16.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

2 Conditional probability

We have introduced probability as a language for expressing our degrees of belief or uncertainties about events. Whenever we observe new evidence (i.e., obtain *data*), we acquire information that may affect our uncertainties. A new observation that is consistent with an existing belief could make us more sure of that belief, while a surprising observation could throw that belief into question. *Conditional probability* is the concept that addresses this fundamental question: how should we update our beliefs in light of the evidence we observe?

### 2.1 The importance of thinking conditionally

Conditional probability is essential for scientific, medical, and legal reasoning, since it shows how to incorporate evidence into our understanding of the world in a logical, coherent manner. In fact, a useful perspective is that *all probabilities are conditional*; whether or not it’s written explicitly, there is always background knowledge (or assumptions) built into every probability.

Suppose, for example, that one morning we are interested in the event $R$ that it will rain that day. Let $P(R)$ be our assessment of the probability of rain before looking outside. If we then look outside and see ominous clouds in the sky, then presumably our probability of rain should increase; we denote this new probability by $P(R|C)$ (read as “probability of $R$ given $C$”), where $C$ is the event of there being ominous clouds. When we go from $P(R)$ to $P(R|C)$, we say that we are “conditioning on $C$”. As the day progresses, we may obtain more and more information about the weather conditions, and we can continually update our probabilities. If we observe that events $B_{1},\ldots,B_{n}$ occurred, then we write our new conditional probability of rain given this evidence as $P(R|B_{1},\ldots,B_{n})$. If eventually we observe that it does start raining, our conditional probability becomes $1$.

Furthermore, we will see that conditioning is a very powerful problem-solving strategy, often making it possible to solve a complicated problem by decomposing it into manageable pieces with case-by-case reasoning. Just as in computer science a common strategy is to break a large problem up into bite-size pieces (or even byte-size pieces), in probability a common strategy is to reduce a complicated probability problem to a bunch of simpler conditional probability problems. In particular, we

will discuss a strategy known as *first-step analysis*, which often allows us to obtain recursive solutions to problems where the experiment has multiple stages.

Due to the central importance of conditioning, both as the means by which we update beliefs to reflect evidence and as a problem-solving strategy, we say that

*Conditioning is the soul of statistics.*

### 2.2 Definition and intuition

###### Definition 2.2.1 (Conditional probability).

If $A$ and $B$ are events with $P(B)>0$, then the *conditional probability* of $A$ given $B$, denoted by $P(A|B)$, is defined as

$P(A|B)=\frac{P(A\cap B)}{P(B)}.$

Here $A$ is the event whose uncertainty we want to update, and $B$ is the evidence we observe (or want to treat as given). We call $P(A)$ the *prior* probability of $A$ and $P(A|B)$ the *posterior* probability of $A$ (“prior” means before updating based on the evidence, and “posterior” means after updating based on the evidence).

It is important to interpret the event appearing after the vertical conditioning bar as the evidence that we have observed or that is being conditioned on: $P(A|B)$ is the probability of $A$ given the evidence $B$, *not* the probability of some entity called $A|B$. As discussed in 2.4.1, there is no such event as $A|B$.

For any event $A$, $P(A|A)=P(A\cap A)/P(A)=1$. Upon observing that $A$ has occurred, our updated probability for $A$ is $1$. If this weren’t the case, we would demand a new definition of conditional probability!

###### Example 2.2.2 (Two cards).

A standard deck of cards is shuffled well. Two cards are drawn randomly, one at a time without replacement. Let $A$ be the event that the first card is a heart, and $B$ be the event that the second card is red. Find $P(A|B)$ and $P(B|A)$.

*Solution*:

By the naive definition of probability and the multiplication rule,

$P(A\cap B)=\frac{13\cdot 25}{52\cdot 51}=\frac{25}{204},$

since a favorable outcome is determined by choosing any of the 13 hearts and then any of the remaining 25 red cards. Also, $P(A)=1/4$ since the 4 suits are equally likely, and

$P(B)=\frac{26\cdot 51}{52\cdot 51}=\frac{1}{2}$

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

Introduction to Probability

Intuition 2.2.3 (Pebble World). Consider a finite sample space, with the outcomes visualized as pebbles with total mass 1. Since  $A$  is an event, it is a set of pebbles, and likewise for  $B$ . Figure 2.1(a) shows an example.

![img-17.jpeg](img-17.jpeg)

![img-18.jpeg](img-18.jpeg)

![img-19.jpeg](img-19.jpeg)

# FIGURE 2.1

Pebble World intuition for  $P(A|B)$ . From left to right: (a) Events  $A$  and  $B$  are subsets of the sample space. (b) Because we know  $B$  occurred, get rid of the outcomes in  $B^c$ . (c) In the restricted sample space, renormalize so the total mass is still 1.

Now suppose that we learn that  $B$  occurred. In Figure 2.1(b), upon obtaining this information, we get rid of all the pebbles in  $B^c$  because they are incompatible with the knowledge that  $B$  has occurred. Then  $P(A \cap B)$  is the total mass of the pebbles remaining in  $A$ . Finally, in Figure 2.1(c), we renormalize, that is, divide all the masses by a constant so that the new total mass of the remaining pebbles is 1. This is achieved by dividing by  $P(B)$ , the total mass of the pebbles in  $B$ . The updated mass of the outcomes corresponding to event  $A$  is the conditional probability  $P(A|B) = P(A \cap B) / P(B)$ .

In this way, our probabilities have been updated in accordance with the observed evidence. Outcomes that contradict the evidence are discarded, and their mass is redistributed among the remaining outcomes, preserving the relative masses of the remaining outcomes. For example, if pebble 2 weighs twice as much as pebble 1 initially, and both are contained in  $B$ , then after conditioning on  $B$  it is still true that pebble 2 weighs twice as much as pebble 1. But if pebble 2 is not contained in  $B$ , then after conditioning on  $B$  its mass is updated to 0.

Intuition 2.2.4 (Frequentist interpretation). Recall that the frequentist interpretation of probability is based on relative frequency over a large number of repeated trials. Imagine repeating our experiment many times, generating a long list of observed outcomes. The conditional probability of  $A$  given  $B$  can then be thought of in a natural way: it is the fraction of times that  $A$  occurs, restricting attention to the trials where  $B$  occurs.

In Figure 2.2, our experiment has outcomes which can be written as a string of 0's and 1's;  $B$  is the event that the first digit is 1 and  $A$  is the event that the second digit is 1. Conditioning on  $B$ , we circle all the repetitions where  $B$  occurred, and then we look at the fraction of circled repetitions in which event  $A$  also occurred.

In symbols, let  $n_A, n_B, n_{AB}$  be the number of occurrences of  $A, B, A \cap B$  respectively in a large number  $n$  of repetitions of the experiment. The frequentist interpretation

Conditional probability

is that

$P(A)\approx\frac{n_{A}}{n},\,P(B)\approx\frac{n_{B}}{n},\,P(A\cap B)\approx\frac{n_{AB}}{n}.$

Then $P(A|B)$ is interpreted as $n_{AB}/n_{B}$, which equals $(n_{AB}/n)/(n_{B}/n)$. This interpretation again translates to $P(A|B)=P(A\cap B)/P(B)$. ∎

FIGURE 2.2
![img-20.jpeg](img-20.jpeg)
Frequentist intuition for $P(A|B)$. The repetitions where $B$ occurred are circled; among these, the repetitions where $A$ occurred are highlighted in bold. $P(A|B)$ is the long-run relative frequency of the repetitions where $A$ occurs, within the subset of repetitions where $B$ occurs.

For practice with applying the definition of conditional probability, let’s do some more examples. The next three examples all start with the same basic scenario of a family with two children, but subtleties arise depending on the exact assumptions and the exact information we condition on.

###### Example 2.2.5 (Two children).

Martin Gardner posed the following puzzle in the 1950s, in his column in Scientific American.

- *Mr. Jones has two children. The older child is a girl. What is the probability that both children are girls?*
- *Mr. Smith has two children. At least one of them is a boy. What is the probability that both children are boys?*

At first glance this problem seems like it should be a simple application of conditional probability, but for decades there have been controversies about whether or why the two parts of the problem should have different answers, and the extent to which the problem is ambiguous. Gardner gave the answers $1/2$ and $1/3$ to the two parts, respectively, which may seem paradoxical: why should it matter whether we learn the older child’s gender, as opposed to just learning one child’s gender?

It is important to clarify the assumptions of the problem. Several implicit assumptions are being made to obtain the answers that Gardner gave.

- It assumes that gender is binary, so that each child can be definitively categorized as a boy or a girl. In fact, many people don’t neatly fit into either of the categories “male” or “female”, and identify themselves as having a non-binary gender.
- It assumes that $P(\text{boy})=P(\text{girl})$, both for the elder child and for the younger child. In fact, in most countries slightly more boys are born than girls. For example, in the United States it is commonly estimated that 105 boys are born for every 100 girls who are born.
- It assumes that the genders of the two children are independent, i.e., knowing the elder child’s gender gives no information about the younger child’s gender, and vice versa. This would be unrealistic if, e.g., the children were identical twins.

Under these (admittedly problematic) simplifying assumptions, we can solve the problem as follows.

*Solution*:

With the assumptions listed above, the definition of conditional probability gives

$P(\text{both girls}|\text{elder is a girl})=\frac{P(\text{both girls, elder is a girl})}{P(\text{elder is a girl})}=\frac{1/4}{1/2}=1/2,$
$P(\text{both girls}|\text{at least one girl})=\frac{P(\text{both girls, at least one girl})}{P(\text{at least one girl})}=\frac{1/4}{3/4}=1/3.$

(We solved the second part of the problem in terms of girls rather than boys to make it a bit easier to compare the two parts of the problem.) It may seem counterintuitive that the two results are different, since there is no reason for us to care whether the elder child is a girl as opposed to the younger child. Indeed, by symmetry,

$P(\text{both girls}|\text{younger is a girl})=P(\text{both girls}|\text{elder is a girl})=1/2.$

However, there is no such symmetry between the conditional probabilities $P(\text{both girls}|\text{elder is a girl})$ and $P(\text{both girls}|\text{at least one girl})$. Saying that the elder child is a girl designates a *specific* child, and then the other child (the younger child) has a 50% chance of being a girl. “At least one” does *not* refer to a specific child. Conditioning on a specific child being a girl knocks away 2 of the 4 “pebbles” in the sample space $\{GG,GB,BG,BB\}$, where, for example, $GB$ means the elder child is a girl and the younger child is a boy. In contrast, conditioning on at least one child being a girl knocks away only $BB$. ∎

###### Example 2.2.6 (Random child is a girl).

A family has two children. You randomly run into one of the two, and learn that she is a girl. With assumptions as in the previous example, what is the conditional probability that both are girls? Also assume that you are equally likely to run into either child, and that which one you run into has nothing to do with gender.

Solution:

Intuitively, the answer should be $1/2$: imagine that the child we encountered is in front of us and the other is at home. Both being girls just says that the child who is at home is a girl, which seems to have nothing to do with the fact that the child in front of us is a girl. But let us check this more carefully, using the definition of conditional probability. This is also good practice with writing events in set notation.

Let $G_{1},G_{2}$, and $G_{3}$ be the events that the elder, younger, and random child is a girl, respectively. By assumption, $P(G_{1})=P(G_{2})=P(G_{3})=1/2$ . By the naive definition, or by independence as explained in Section 2.5, $P(G_{1}\cap G_{2})=1/4$. Thus,

$P(G_{1}\cap G_{2}|G_{3})=P(G_{1}\cap G_{2}\cap G_{3})/P(G_{3})=(1/4)/(1/2)=1/2,$

since $G_{1}\cap G_{2}\cap G_{3}=G_{1}\cap G_{2}$ (if both children are girls, it guarantees that the random child is a girl).

Keep in mind though that in order to arrive at $1/2$, an assumption was needed about how the random child was selected. In statistical language, we say that we collected a *random sample*; here the sample consists of one of the two children. One of the most important principles in statistics is that it is essential to think carefully about how the sample was collected, not just stare at the raw data without understanding where they came from. To take a simple extreme case, suppose that a repressive law forbids a boy from leaving the house if he has a sister. Then “the random child is a girl” is equivalent to “at least one of the children is a girl”, so the problem reduces to the first part of Example 2.2.5. ∎

###### Example 2.2.7 (A girl born in winter).

A family has two children. Find the probability that both children are girls, given that at least one of the two is a girl who was born in winter. In addition to the assumptions from Example 2.2.5, assume that the four seasons are equally likely and that gender is independent of season. (This means that knowing the gender gives no information about the probabilities of the seasons, and vice versa; see Section 2.5 for much more about independence.)

*Solution*:

By definition of conditional probability,

$P(\text{both girls}|\text{at least one winter girl})=\frac{P(\text{both girls, at least one winter girl})}{P(\text{at least one winter girl})}.$

Since the probability that a specific child is a winter-born girl is $1/8$, the denominator equals

$P(\text{at least one winter girl})=1-(7/8)^{2}.$

To compute the numerator, use the fact that “both girls, at least one winter girl” is the same event as “both girls, at least one winter child”; then use the assumption

that gender and season are independent:

$P(\text{both girls, at least one winter girl})$ $=P(\text{both girls, at least one winter child})$
$=(1/4)P(\text{at least one winter child})$
$=(1/4)(1-P(\text{both are non-winter}))$
$=(1/4)(1-(3/4)^{2}).$

Thus,

$P(\text{both girls}|\text{at least one winter girl})=\frac{(1/4)(1-(3/4)^{2})}{1-(7/8)^{2}}=\frac{7/64}{15/64}=7/15.$

At first this result seems absurd! In Example 2.2.5, the result was that the conditional probability of both children being girls, given that at least one is a girl, is 1/3; why should it be any different when we learn that at least one is a winter-born girl? The point is that information about the birth season brings “at least one is a girl” closer to “a specific one is a girl”. Conditioning on more and more specific information brings the probability closer and closer to 1/2.

For example, conditioning on “at least one is a girl who was born on a March 31 at 8:20 pm” comes very close to specifying a child, and learning information about a specific child does not give us information about the other child. The seemingly irrelevant information such as season of birth interpolates between the two parts of Example 2.2.5. Exercise 29 generalizes this example to an arbitrary characteristic that is independent of gender. $\square$

### 2.3 Bayes’ rule and the law of total probability

The definition of conditional probability is simple—just a ratio of two probabilities—but it has far-reaching consequences. The first consequence is obtained easily by moving the denominator in the definition to the other side of the equation.

###### Theorem 2.3.1 (Probability of the intersection of two events).

For any events $A$ and $B$ with positive probabilities,

$P(A\cap B)=P(B)P(A|B)=P(A)P(B|A).$

This follows from taking the definition of $P(A|B)$ and multiplying both sides by $P(B)$, and then taking the definition of $P(B|A)$ and multiplying both sides by $P(A)$. At first sight this theorem may not seem very useful: it *is* the definition of conditional probability, just written slightly differently, and anyway it seems circular to use $P(A|B)$ to help find $P(A\cap B)$ when $P(A|B)$ was defined in terms of $P(A\cap B)$. But we will see that the theorem is in fact very useful, since it often turns out to be

possible to find conditional probabilities without going back to the definition, and in such cases Theorem 2.3.1 can help us more easily find $P(A\cap B)$.

Applying Theorem 2.3.1 repeatedly, we can generalize to the intersection of $n$ events.

###### Theorem 2.3.2 (Probability of the intersection of $n$ events).

For any events $A_{1},\ldots,A_{n}$ with $P(A_{1},A_{2},\ldots,A_{n-1})>0$,

$P(A_{1},A_{2},\ldots,A_{n})=P(A_{1})P(A_{2}|A_{1})P(A_{3}|A_{1},A_{2})\cdots P(A_{n}|A_{1},\ldots,A_{n-1}),$

The commas denote intersections, e.g., $P(A_{3}|A_{1},A_{2})$ is $P(A_{3}|A_{1}\cap A_{2})$.

In fact, this is $n!$ theorems in one, since we can permute $A_{1},\ldots,A_{n}$ however we want without affecting the left-hand side. Often the right-hand side will be much easier to compute for some orderings than for others. For example,

$P(A_{1},A_{2},A_{3})=P(A_{1})P(A_{2}|A_{1})P(A_{3}|A_{1},A_{2})=P(A_{2})P(A_{3}|A_{2})P(A_{1}|A_{2},A_{3}),$

and there are 4 other expansions of this form too. It often takes practice and thought to be able to know which ordering to use.

We are now ready to introduce the two main theorems of this chapter—Bayes’ rule and the law of total probability—which will allow us to compute conditional probabilities in a wide range of problems. Bayes’ rule is an extremely famous, extremely useful result that relates $P(A|B)$ to $P(B|A)$.

###### Theorem 2.3.3 (Bayes’ rule).

$P(A|B)=\frac{P(B|A)P(A)}{P(B)}.$

This follows immediately from Theorem 2.3.1, which in turn followed immediately from the definition of conditional probability. Yet Bayes’ rule has important implications and applications in probability and statistics, since it is so often necessary to find conditional probabilities, and often $P(B|A)$ is much easier to find directly than $P(A|B)$ (or vice versa).

Another way to write Bayes’ rule is in terms of *odds* rather than probability.

###### Definition 2.3.4 (Odds).

The *odds* of an event $A$ are

$\text{odds}(A)=P(A)/P(A^{c}).$

For example, if $P(A)=2/3$, we say the odds in favor of $A$ are 2 to 1. (This is sometimes written as $2:1$, and is sometimes stated as 1 to 2 odds against $A$; care is needed since some sources do not explicitly state whether they are referring to odds in favor or odds against an event.) Of course we can also convert from odds back to probability:

$P(A)=\text{odds}(A)/(1+\text{odds}(A)).$

By taking the Bayes’ rule expression for $P(A|B)$ and dividing it by the Bayes’ rule expression for $P(A^{c}|B)$, we arrive at the odds form of Bayes’ rule.

###### Theorem 2.3.5 (Odds form of Bayes’ rule).

For any events $A$ and $B$ with positive probabilities, the odds of $A$ after conditioning on $B$ are

$\frac{P(A|B)}{P(A^{c}|B)}=\frac{P(B|A)}{P(B|A^{c})}\frac{P(A)}{P(A^{c})}.$

In words, this says that the *posterior odds* $P(A|B)/P(A^{c}|B)$ are equal to the *prior odds* $P(A)/P(A^{c})$ times the factor $P(B|A)/P(B|A^{c})$, which is known in statistics as the *likelihood ratio*. Sometimes it is convenient to work with this form of Bayes’ rule to get the posterior odds, and then if desired we can convert from odds back to probability.

The *law of total probability* (LOTP) relates conditional probability to unconditional probability. It is essential for fulfilling the promise that conditional probability can be used to decompose complicated probability problems into simpler pieces, and it is often used in tandem with Bayes’ rule.

###### Theorem 2.3.6 (Law of total probability).

Let $A_{1},\ldots,A_{n}$ be a partition of the sample space $S$ (i.e., the $A_{i}$ are disjoint events and their union is $S$), with $P(A_{i})>0$ for all $i$. Then

$P(B)=\sum_{i=1}^{n}P(B|A_{i})P(A_{i}).$

###### Proof.

Since the $A_{i}$ form a partition of $S$, we can decompose $B$ as

$B=(B\cap A_{1})\cup(B\cap A_{2})\cup\cdots\cup(B\cap A_{n}).$

This is illustrated in Figure 2.3, where we have chopped $B$ into the smaller pieces $B\cap A_{1}$ through $B\cap A_{n}$. By the second axiom of probability, because these pieces are disjoint, we can add their probabilities to get $P(B)$:

$P(B)=P(B\cap A_{1})+P(B\cap A_{2})+\cdots+P(B\cap A_{n}).$

Now we can apply Theorem 2.3.1 to each of the $P(B\cap A_{i})$:

$P(B)=P(B|A_{1})P(A_{1})+\cdots+P(B|A_{n})P(A_{n}).\qed$

The law of total probability tells us that to get the unconditional probability of $B$, we can divide the sample space into disjoint slices $A_{i}$, find the conditional probability of $B$ within each of the slices, then take a weighted sum of the conditional probabilities, where the weights are the probabilities $P(A_{i})$. The choice of how to divide up the sample space is crucial: a well-chosen partition will reduce a complicated problem into simpler pieces, whereas a poorly chosen partition will only exacerbate our problems, requiring us to calculate $n$ difficult probabilities instead of just one!

The next few examples show how we can use Bayes’ rule together with the law of total probability to update our beliefs based on observed evidence.

Conditional probability

![img-21.jpeg](img-21.jpeg)
FIGURE 2.3 The  $A_{i}$  partition the sample space;  $P(B)$  is equal to  $\sum_{i}P(B\cap A_{i})$

Example 2.3.7 (Random coin). You have one fair coin, and one biased coin which lands Heads with probability  $3/4$ . You pick one of the coins at random and flip it three times. It lands Heads all three times. Given this information, what is the probability that the coin you picked is the fair one?

# Solution:

Let  $A$  be the event that the chosen coin lands Heads three times and let  $F$  be the event that we picked the fair coin. We are interested in  $P(F|A)$ , but it is easier to find  $P(A|F)$  and  $P(A|F^c)$  since it helps to know which coin we have; this suggests using Bayes' rule and the law of total probability. Doing so, we have

$$
\begin{array}{l} P (F | A) = \frac {P (A | F) P (F)}{P (A)} \\ = \frac {P (A | F) P (F)}{P (A | F) P (F) + P (A | F ^ {c}) P (F ^ {c})} \\ = \frac {(1 / 2) ^ {3} \cdot 1 / 2}{(1 / 2) ^ {3} \cdot 1 / 2 + (3 / 4) ^ {3} \cdot 1 / 2} \\ \approx 0. 2 3. \\ \end{array}
$$

Before flipping the coin, we thought we were equally likely to have picked the fair coin as the biased coin:  $P(F) = P(F^c) = 1/2$ . Upon observing three Heads, however, it becomes more likely that we've chosen the biased coin than the fair coin, so  $P(F|A)$  is only about 0.23.

$\Leftrightarrow$  2.3.8 (Prior vs. posterior). It would not be correct in the calculation in the above example to say after the first step, “ $P(A) = 1$  because we know  $A$  happened.” It is true that  $P(A|A) = 1$ , but  $P(A)$  is the prior probability of  $A$  and  $P(F)$  is the prior probability of  $F$ —both are the probabilities before we observe any data in the

experiment. These must not be confused with posterior probabilities conditional on the evidence $A$.

###### Example 2.3.9 (Testing for a rare disease).

A patient named Fred is tested for a disease called conditionitis, a medical condition that afflicts 1% of the population. The test result is positive, i.e., the test claims that Fred has the disease. Let $D$ be the event that Fred has the disease and $T$ be the event that he tests positive.

Suppose that the test is “95% accurate”; there are different measures of the accuracy of a test, but in this problem it is assumed to mean that $P(T|D)=0.95$ and $P(T^{c}|D^{c})=0.95$. The quantity $P(T|D)$ is known as the sensitivity or true positive rate of the test, and $P(T^{c}|D^{c})$ is known as the specificity or true negative rate.

Find the conditional probability that Fred has conditionitis, given the evidence provided by the test result.

Solution:

Applying Bayes’ rule and the law of total probability, we have

$P(D|T)$ $=\frac{P(T|D)P(D)}{P(T)}$
$=\frac{P(T|D)P(D)}{P(T|D)P(D)+P(T|D^{c})P(D^{c})}$
$=\frac{0.95\cdot 0.01}{0.95\cdot 0.01+0.05\cdot 0.99}$
$\approx 0.16.$

So there is only a 16% chance that Fred has conditionitis, given that he tested positive, even though the test seems to be quite reliable!

Most people find it surprising to learn that the conditional probability of having the disease given a positive test result is only 16%, even though the test is 95% accurate (see Gigerenzer and Hoffrage *[13]*). The key to understanding this surprisingly low posterior probability of having the disease is to realize that there are two factors at play: the evidence from the test, and our prior information about the prevalence of the disease.

Although the test provides evidence in favor of disease, conditionitis is also a rare condition! The conditional probability $P(D|T)$ reflects a balance between these two factors, appropriately weighing the rarity of the disease against the rarity of a mistaken test result.

For further intuition, consider a population of 10000 people as illustrated in Figure 2.4, where 100 have conditionitis and 9900 don’t; this corresponds to a 1% disease rate. If we tested everybody in the population, we’d expect that out of the 100 diseased individuals, 95 would test positive and 5 would test negative. Out of the 9900 healthy individuals, we’d expect $(0.95)(9900)\approx 9405$ to test negative and 495 to test positive.

Conditional probability

![img-22.jpeg](img-22.jpeg)
FIGURE 2.4

Testing for a rare disease in a population of 10000 people, where the prevalence of the disease is  $1\%$  and the true positive and true negative rates are both equal to  $95\%$ . Bubbles are not to scale.

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

2.4 Conditional probabilities are probabilities

When we condition on an event $E$, we update our beliefs to be consistent with this knowledge, effectively putting ourselves in a universe where we know that $E$ occurred. Within our new universe, however, the laws of probability operate just as before. Conditional probability satisfies all the properties of probability! Therefore, any of the results we have derived about probability are still valid if we replace all unconditional probabilities with probabilities conditional on $E$. In particular:

- Conditional probabilities are between 0 and 1.
- $P(S|E)=1$, $P(\emptyset|E)=0$.
- If $A_{1},A_{2},\dots$ are disjoint, then $P(\cup_{j=1}^{\infty}A_{j}|E)=\sum_{j=1}^{\infty}P(A_{j}|E)$.
- $P(A^{c}|E)=1-P(A|E)$.
- Inclusion-exclusion: $P(A\cup B|E)=P(A|E)+P(B|E)-P(A\cap B|E)$.

###### 2.4.1.

When we write $P(A|E)$, it does *not* mean that $A|E$ is an event and we’re taking its probability; $A|E$ is not an event. Rather, $P(\cdot|E)$ is a probability function which assigns probabilities in accordance with the knowledge that $E$ has occurred, and $P(\cdot)$ is a different probability function which assigns probabilities without regard for whether $E$ has occurred or not. When we take an event $A$ and plug it into the $P(\cdot)$ function, we’ll get a number, $P(A)$; when we plug it into the $P(\cdot|E)$ function, we’ll get another number, $P(A|E)$, which incorporates the information (if any) provided by knowing that $E$ occurred.

To prove mathematically that conditional probabilities are probabilities, fix an event $E$ with $P(E)>0$, and for any event $A$, define $\tilde{P}(A)=P(A|E)$. This notation helps emphasize the fact that we are fixing $E$ and treating $P(\cdot|E)$ as our new probability function. We just need to check the two axioms of probability. First,

$\tilde{P}(\emptyset)=P(\emptyset|E)=\frac{P(\emptyset\cap E)}{P(E)}=0,\tilde{P}(S)=P(S|E)=\frac{P(S\cap E)}{P(E)}=1.$

Second, if $A_{1},A_{2},\dots$ are disjoint events, then

$\tilde{P}(A_{1}\cup A_{2}\cup\cdots)=\frac{P((A_{1}\cap E)\cup(A_{2}\cap E)\cup\cdots)}{P(E)}=\frac{\sum_{j=1}^{\infty}P(A_{j}\cap E)}{P(E)}=\sum_{j=1}^{\infty}\tilde{P}(A_{j}).$

So $\tilde{P}$ satisfies the axioms of probability.

Conversely, *all* probabilities can be thought of as conditional probabilities: whenever we make a probability statement, there is always some background information that we are conditioning on, even if we don’t state it explicitly. Consider the rain example from the beginning of this chapter. It would be natural to base the initial probability

Introduction to Probability

of rain today, $P(R)$, on the fraction of days in the past on which it rained. But which days in the past should we look at? If it’s November 1, should we only count past rainy days in autumn, thus conditioning on the season? What about conditioning on the exact month, or the exact day? We could ask the same about location: should we look at days when it rained in our exact location, or is it enough for it to have rained somewhere nearby?

In order to determine the seemingly unconditional probability $P(R)$, we actually have to make decisions about what background information to condition on! These choices require careful thought and different people may come up with different prior probabilities $P(R)$ (though everyone can agree on how to update based on new evidence).

Since all probabilities are conditional on background information, we can imagine that there is always a vertical conditioning bar, with background knowledge $K$ to the right of the vertical bar. Then the unconditional probability $P(A)$ is just shorthand for $P(A|K)$; the background knowledge is absorbed into the letter $P$ instead of being written explicitly.

To summarize our discussion in a nutshell:

Conditional probabilities are probabilities, and all probabilities are conditional.

We now state conditional forms of Bayes’ rule and the law of total probability. These are obtained by taking the ordinary forms of Bayes’ rule and LOTP and adding $E$ to the right of the vertical bar everywhere.

###### Theorem 2.4.2 (Bayes’ rule with extra conditioning).

Provided that $P(A\cap E)&gt;0$ and $P(B\cap E)&gt;0$, we have

$P(A|B,E)=\frac{P(B|A,E)P(A|E)}{P(B|E)}.$

###### Theorem 2.4.3 (LOTP with extra conditioning).

Let $A_{1},\ldots,A_{n}$ be a partition of $S$. Provided that $P(A_{i}\cap E)&gt;0$ for all $i$, we have

$P(B|E)=\sum_{i=1}^{n}P(B|A_{i},E)P(A_{i}|E).$

The extra conditioning forms of Bayes’ rule and LOTP can be proved similarly to how we verified that $\hat{P}$ satisfies the axioms of probability, but they also follow directly from the “metatheorem” that conditional probabilities are probabilities.

###### Example 2.4.4 (Random coin, continued).

Continuing with the scenario from Example 2.3.7, suppose that we have now seen our chosen coin land Heads three times. If we toss the coin a fourth time, what is the probability that it will land Heads once more?

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

(b) Now suppose that all $n$ judges vote to convict. Given this information, find the probability that the suspect is guilty.

(c) Is the answer to (b), viewed as a function of $n$, an increasing function? Give a short, intuitive explanation in words.

Solution:

(a) Since $k<n$, a systemic error didn’t occur. We will implicitly condition on this in this part. Let $G$ be the event that the suspect is guilty and $X$ be the number of judges who vote to convict. Using Bayes’ rule, LOTP, and the Binomial PMF,

$P(G|X=k)=\frac{P(X=k|G)P(G)}{P(X=k)}=\frac{pc^{k}(1-c)^{n-k}}{pc^{k}(1-c)^{n-k}+(1-p)w^{k}(1-w)^{n-k}}.$

(b) Let $U$ be the event $X=n$ and $B$ be the event that a systemic error occurs. Then

$P(G|U)=\frac{P(U|G)P(G)}{P(U)}=\frac{pP(U|G)}{pP(U|G)+(1-p)P(U|G^{c})}.$

By LOTP with extra conditioning,

$P(U|G)$ $=P(U|G,B)P(B|G)+P(U|G,B^{c})P(B^{c}|G)=s+(1-s)c^{n},$
$P(U|G^{c})$ $=P(U|G^{c},B)P(B|G^{c})+P(U|G^{c},B^{c})P(B^{c}|G^{c})=s+(1-s)w^{n}.$

Thus,

$P(G|U)=\frac{p(s+(1-s)c^{n})}{p(s+(1-s)c^{n})+(1-p)(s+(1-s)w^{n})}.$

(c) No, since a large value of $n$ yields a high chance of systemic error, and if a systemic error occurs then the judges’ votes are uninformative about whether the suspect is guilty. The answer to (b) reverts to the prior probability $p$ as $n\to\infty$. ∎

We often want to condition on more than one piece of information, and we now have several ways of doing that. For example, here are some approaches for finding $P(A|B,C)$:

1. We can think of $B,C$ as the single event $B\cap C$ and use the definition of conditional probability to get

$P(A|B,C)=\frac{P(A,B,C)}{P(B,C)}.$

This is a natural approach if it’s easiest to think about $B$ and $C$ in tandem. We can then try to evaluate the numerator and denominator. For example, we can use LOTP in both the numerator and the denominator, or we can write the numerator as $P(B,C|A)P(A)$ (which would give us a version of Bayes’ rule) and use LOTP to help with the denominator.

2. We can use Bayes’ rule with extra conditioning on $C$ to get

$P(A|B,C)=\frac{P(B|A,C)P(A|C)}{P(B|C)}.$

This is a natural approach if we want to think of everything in our problem as being conditioned on $C$.

3. We can use Bayes’ rule with extra conditioning on $B$ to get

$P(A|B,C)=\frac{P(C|A,B)P(A|B)}{P(C|B)}.$

This is the same as the previous approach, except with the roles of $B$ and $C$ swapped. We mention it separately just to emphasize that it’s a bad idea to plug into a formula without thinking about which event should play which role.

It is both challenging and powerful that there are a variety of ways to approach this kind of conditioning problem.

### 2.5 Independence of events

We have now seen several examples where conditioning on one event changes our beliefs about the probability of another event. The situation where events provide no information about each other is called independence.

###### Definition 2.5.1 (Independence of two events).

Events $A$ and $B$ are independent if

$P(A\cap B)=P(A)P(B).$

If $P(A)>0$ and $P(B)>0$, then this is equivalent to

$P(A|B)=P(A),$

and also equivalent to $P(B|A)=P(B)$.

In words, two events are independent if we can obtain the probability of their intersection by multiplying their individual probabilities. Alternatively, $A$ and $B$ are independent if learning that $B$ occurred gives us no information that would change our probabilities for $A$ occurring (and vice versa).

Note that independence is a symmetric relation: if $A$ is independent of $B$, then $B$ is independent of $A$.

$\text{\text{✺ 2.5.2.}$ Independence is completely different from disjointness. If $A$ and $B$ are disjoint, then $P(A\cap B)=0$, so disjoint events can be independent only if $P(A)=0$ or $P(B)=0$. Knowing that $A$ occurs tells us that $B$ definitely did not occur, so $A$ clearly conveys information about $B$, meaning the two events are not independent (except if $A$ or $B$ already has zero probability).

Intuitively, it makes sense that if $A$ provides no information about whether or not $B$ occurred, then it also provides no information about whether or not $B^{c}$ occurred. We now prove a handy result along those lines.

###### Proposition 2.5.3.

If $A$ and $B$ are independent, then $A$ and $B^{c}$ are independent, $A^{c}$ and $B$ are independent, and $A^{c}$ and $B^{c}$ are independent.

###### Proof.

Let $A$ and $B$ be independent. We will first show that $A$ and $B^{c}$ are independent. If $P(A)=0$, then $A$ is independent of *every* event, including $B^{c}$. So assume $P(A)\neq 0$. Then

$P(B^{c}|A)=1-P(B|A)=1-P(B)=P(B^{c}),$

so $A$ and $B^{c}$ are independent. Swapping the roles of $A$ and $B$, we have that $A^{c}$ and $B$ are independent. Using the fact that $A,B$ independent implies $A,B^{c}$ independent, with $A^{c}$ playing the role of $A$, we also have that $A^{c}$ and $B^{c}$ are independent. ∎

We also often need to talk about independence of three or more events.

###### Definition 2.5.4 (Independence of three events).

Events $A$, $B$, and $C$ are said to be *independent* if all of the following equations hold:

$P(A\cap B)$ $=P(A)P(B),$
$P(A\cap C)$ $=P(A)P(C),$
$P(B\cap C)$ $=P(B)P(C),$
$P(A\cap B\cap C)$ $=P(A)P(B)P(C).$

If the first three conditions hold, we say that $A$, $B$, and $C$ are *pairwise independent*. Pairwise independence does *not* imply independence: it is possible that just learning about $A$ or just learning about $B$ is of no use in predicting whether $C$ occurred, but learning that *both* $A$ and $B$ occurred could still be highly relevant for $C$. Here is a simple example of this distinction.

###### Example 2.5.5 (Pairwise independence doesn’t imply independence).

Consider two fair, independent coin tosses, and let $A$ be the event that the first is Heads, $B$ the event that the second is Heads, and $C$ the event that both tosses have the same result. Then $A$, $B$, and $C$ are pairwise independent but not independent, since $P(A\cap B\cap C)=1/4$ while $P(A)P(B)P(C)=1/8$. The point is that just knowing about $A$ or just knowing about $B$ tells us nothing about $C$, but knowing what happened with *both* $A$ and $B$ gives us information about $C$ (in fact, in this case it gives us perfect information about $C$). ∎

On the other hand, $P(A\cap B\cap C)=P(A)P(B)P(C)$ does not imply pairwise independence; this can be seen quickly by looking at the extreme case $P(A)=0$, when the equation becomes $0=0$, which tells us nothing about $B$ and $C$.

We can define independence of any number of events similarly. Intuitively, the idea is that knowing what happened with any particular subset of the events gives us no information about what happened with the events not in that subset.

###### Definition 2.5.6 (Independence of many events).

For $n$ events $A_{1},A_{2},\ldots,A_{n}$ to be *independent*, we require any pair to satisfy $P(A_{i}\cap A_{j})=P(A_{i})P(A_{j})$ (for $i\neq j$), any triplet to satisfy $P(A_{i}\cap A_{j}\cap A_{k})=P(A_{i})P(A_{j})P(A_{k})$ (for $i,j,k$ distinct), and similarly for all quadruplets, quintuplets, and so on. This can quickly become unwieldy, but later we will discuss other ways to think about independence. For infinitely many events, we say that they are independent if every finite subset of the events is independent.

Conditional independence is defined analogously to independence.

###### Definition 2.5.7 (Conditional independence).

Events $A$ and $B$ are said to be *conditionally independent* given $E$ if $P(A\cap B|E)=P(A|E)P(B|E)$.

It is easy to make terrible blunders stemming from confusing independence and conditional independence. Two events can be conditionally independent given $E$, but not independent given $E^{c}$. Two events can be conditionally independent given $E$, but not independent. Two events can be independent, but not conditionally independent given $E$.

In particular, $P(A,B)=P(A)P(B)$ does *not* imply $P(A,B|E)=P(A|E)P(B|E)$; we can’t just insert “given $E$” everywhere, as we did in going from LOTP to LOTP with extra conditioning. This is because LOTP *always* holds (it is a consequence of the axioms of probability), whereas $P(A,B)$ may or may not equal $P(A)P(B)$, depending on what $A$ and $B$ are.

The next few examples illustrate these distinctions. Great care is needed in working with conditional probabilities and conditional independence!

###### Example 2.5.9 (Conditional independence given $E$ vs. given $E^{c}$).

Suppose there are two types of classes: good classes and bad classes. In good classes, if you work hard, you are very likely to get an A. In bad classes, the professor randomly assigns grades to students regardless of their effort. Let $G$ be the event that a class is good, $W$ be the event that you work hard, and $A$ be the event that you receive an A. Then $W$ and $A$ are conditionally independent given $G^{c}$, but they are not conditionally independent given $G$. ∎

###### Example 2.5.10 (Conditional independence doesn’t imply independence).

Returning once more to the scenario from Example 2.3.7, suppose we have chosen either a fair coin or a biased coin with probability $3/4$ of Heads, but we do not know which one we have chosen. We flip the coin a number of times. Conditional on choosing the fair coin, the coin tosses are independent, with each toss having probability $1/2$ of Heads. Similarly, conditional on choosing the biased coin, the tosses are independent, each with probability $3/4$ of Heads.

However, the coin tosses are not unconditionally independent, because if we don’t know which coin we’ve chosen, then observing the sequence of tosses gives us information about whether we have the fair coin or the biased coin in our hand. This in turn helps us to predict the outcomes of future tosses from the same coin.

Introduction to Probability

To state this formally, let $F$ be the event that we’ve chosen the fair coin, and let $A_{1}$ and $A_{2}$ be the events that the first and second coin tosses land Heads. Conditional on $F$, $A_{1}$ and $A_{2}$ are independent, but $A_{1}$ and $A_{2}$ are not unconditionally independent because $A_{1}$ provides information about $A_{2}$. ∎

###### Example 2.5.11 (Independence doesn’t imply conditional independence).

My friends Alice and Bob are the only two people who ever call me on the phone. Each day, they decide independently whether to call me that day. Let $A$ be the event that Alice calls me next Friday and $B$ be the event that Bob calls me next Friday. Assume $A$ and $B$ are unconditionally independent with $P(A)&gt;0$ and $P(B)&gt;0$.

However, given that I receive exactly one call next Friday, $A$ and $B$ are no longer independent: the call is from Alice if and only if it is not from Bob. In other words, letting $C$ be the event that I receive exactly one call next Friday, $P(B|C)&gt;0$ while $P(B|A,C)=0$, so $A$ and $B$ are not conditionally independent given $C$. ∎

###### Example 2.5.12.

(Why is the baby crying?) A certain baby cries if and only if she is hungry, tired, or both. Let $C$ be the event that the baby is crying, $H$ be the event that she is hungry, and $T$ be the event that she is tired. Let $P(C)=c,P(H)=h$, and $P(T)=t$, where none of $c,h,t$ are equal to 0 or 1. Let $H$ and $T$ be independent.

(a) Find $c$, in terms of $h$ and $t$.

(b) Find $P(H|C),P(T|C)$, and $P(H,T|C)$.

(c) Are $H$ and $T$ conditionally independent given $C$? Explain in two ways: algebraically using the quantities from (b), and with an intuitive explanation in words.

Solution:

(a) Since $H$ and $T$ are independent, we have

$P(C)=P(H\cup T)=P(H)+P(T)-P(H\cap T)=h+t-ht$.

(b) By Bayes’ rule,

$P(H|C)$ $=\frac{P(C|H)P(H)}{P(C)}=\frac{h}{c},$

$P(T|C)$ $=\frac{P(C|T)P(T)}{P(C)}=\frac{t}{c},$

$P(H,T|C)$ $=\frac{P(C|H,T)P(H,T)}{P(C)}=\frac{ht}{c}.$

(c) No, $H$ and $T$ are not conditionally independent given $C$, since

$P(H,T|C)=\frac{ht}{c}&lt;\frac{ht}{c^{2}}=P(H|C)P(T|C).$

We can also see intuitively why they are not conditionally independent given $C$: if the baby is crying but not hungry, she must be tired.

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

Two-step method: After the first test, the posterior odds of Fred having the disease are

$\frac{P(D|T_{1})}{P(D^{c}|T_{1})}=\frac{1}{99}\cdot\frac{0.95}{0.05}\approx 0.19,$

from the above. These posterior odds become the new prior odds, and then updating based on the second test gives

$\frac{P(D|T_{1}\cap T_{2})}{P(D^{c}|T_{1}\cap T_{2})}$ $=\frac{P(D|T_{1})}{P(D^{c}|T_{1})}\frac{P(T_{2}|D,T_{1})}{P(T_{2}|D^{c},T_{1})}$
$=\left(\frac{1}{99}\cdot\frac{0.95}{0.05}\right)\frac{0.95}{0.05}=\frac{361}{99}\approx 3.646,$

which is the same result as above.

Note that with a second positive test result, the probability that Fred has the disease jumps from 0.16 to 0.78, making us much more confident that Fred is actually afflicted with conditionitis. The moral of the story is that getting a second opinion is a good idea! $\square$

### 2.7 Conditioning as a problem-solving tool

Conditioning is a powerful tool for solving problems because it lets us engage in wishful thinking: when we encounter a problem that would be made easier if only we knew whether $E$ happened or not, we can condition on $E$ and then on $E^{c}$, consider these possibilities separately, then combine them using LOTP.

#### 2.7.1 Strategy: condition on what you wish you knew

###### Example 2.7.1 (Monty Hall).

On the game show Let’s Make a Deal, hosted by Monty Hall, a contestant chooses one of three closed doors, two of which have a goat behind them and one of which has a car. Monty, who knows where the car is, then opens one of the two remaining doors. The door he opens always has a goat behind it (he never reveals the car!). If he has a choice, then he picks a door at random with equal probabilities. Monty then offers the contestant the option of switching to the other unopened door. If the contestant’s goal is to get the car, should she switch doors?

Conditional probability

![img-23.jpeg](img-23.jpeg)

![img-24.jpeg](img-24.jpeg)

![img-25.jpeg](img-25.jpeg)

# Solution:

Let's label the doors 1 through 3. Without loss of generality, we can assume the contestant picked door 1 (if she didn't pick door 1, we could simply relabel the doors, or rewrite this solution with the door numbers permuted). Monty opens a door, revealing a goat. As the contestant decides whether or not to switch to the remaining unopened door, what does she really wish she knew? Naturally, her decision would be a lot easier if she knew where the car was! This suggests that we should condition on the location of the car. Let  $C_i$  be the event that the car is behind door  $i$ , for  $i = 1,2,3$ . By the law of total probability,

$$
P (\mathrm {g e t c a r}) = P (\mathrm {g e t c a r} | C _ {1}) \cdot \frac {1}{3} + P (\mathrm {g e t c a r} | C _ {2}) \cdot \frac {1}{3} + P (\mathrm {g e t c a r} | C _ {3}) \cdot \frac {1}{3}.
$$

Suppose the contestant employs the switching strategy. If the car is behind door 1, then switching will fail, so  $P(\text{get car}|C_1) = 0$ . If the car is behind door 2 or 3, then because Monty always reveals a goat, the remaining unopened door must contain the car, so switching will succeed. Thus,

$$
P (\mathrm {g e t c a r}) = 0 \cdot \frac {1}{3} + 1 \cdot \frac {1}{3} + 1 \cdot \frac {1}{3} = \frac {2}{3},
$$

so the switching strategy succeeds  $2/3$  of the time. The contestant should switch to the other door.

Figure 2.5 is a tree diagram of the argument we have just outlined: using the switching strategy, the contestant will win as long as the car is behind doors 2 or 3, which has probability  $2/3$ . We can also give an intuitive frequentist argument in favor of switching. Imagine playing this game 1000 times. Typically, about 333 times your initial guess for the car's location will be correct, in which case switching will fail. The other 667 or so times, you will win by switching.

There's a subtlety though, which is that when the contestant chooses whether to switch, she also knows which door Monty opened. We showed that the unconditional probability of success is  $2/3$  (when following the switching strategy), but let's also show that the conditional probability of success for switching, given the information that Monty provides, is also  $2/3$ .

Let  $M_j$  be the event that Monty opens door  $j$ , for  $j = 2,3$ . Then

$$
P (\mathrm {g e t c a r}) = P (\mathrm {g e t c a r} | M _ {2}) P (M _ {2}) + P (\mathrm {g e t c a r} | M _ {3}) P (M _ {3}),
$$

Introduction to Probability

![img-26.jpeg](img-26.jpeg)
FIGURE 2.5 Tree diagram of Monty Hall problem. Switching gets the car  $2 / 3$  of the time.

where by symmetry  $P(M_2) = P(M_3) = 1/2$  and  $P(\text{get car}|M_2) = P(\text{get car}|M_3)$ . The symmetry here is that there is nothing in the statement of the problem that distinguishes between door 2 and door 3; in contrast, Problem 40 considers a scenario where Monty enjoys opening door 2 more than he enjoys opening door 3.

Let  $x = P(\text{get car}|M_2) = P(\text{get car}|M_3)$ . Plugging in what we know,

$$
\frac {2}{3} = P (\mathrm {g e t c a r}) = \frac {x}{2} + \frac {x}{2} = x,
$$

as claimed.

Bayes' rule also works nicely for finding the conditional probability of success using the switching strategy, given the evidence. Suppose that Monty opens door 2. Using the notation and results above,

$$
P (C _ {1} | M _ {2}) = \frac {P (M _ {2} | C _ {1}) P (C _ {1})}{P (M _ {2})} = \frac {(1 / 2) (1 / 3)}{1 / 2} = \frac {1}{3}.
$$

So given that Monty opens door 2, there is a  $1/3$  chance that the contestant's original choice of door has the car, which means that there is a  $2/3$  chance that the switching strategy will succeed.

Many people, upon seeing this problem for the first time, argue that there is no advantage to switching: "There are two doors remaining, and one of them has the car, so the chances are 50-50." After the last chapter, we recognize that this argument misapplies the naive definition of probability. Yet the naive definition, even when inappropriate, has a powerful hold on people's intuitions. When Marilyn vos Savant presented a correct solution to the Monty Hall problem in her column

Conditional probability

for Parade magazine in 1990, she received thousands upon thousands of letters from readers (even mathematicians) insisting that she was wrong.

To build correct intuition, let's consider an extreme case. Suppose that there are a million doors, 999,999 of which contain goats and 1 of which has a car. After the contestant's initial pick, Monty opens 999,998 doors with goats behind them and offers the choice to switch. In this extreme case, it becomes clear that the probabilities are not 50-50 for the two unopened doors; very few people would stubbornly stick with their original choice. The same is true for the three-door case.

Just as we had to make assumptions about how we came across the random girl in Example 2.2.6, here the  $2/3$  success rate of the switching strategy depends on the assumptions we make about how Monty decides which door to open. In the exercises, we consider several variants and generalizations of the Monty Hall problem, some of which change the desirability of the switching strategy.  $\square$

# 2.7.2 Strategy: condition on the first step

In problems with a recursive structure, it can often be useful to condition on the first step of the experiment. The next two examples apply this strategy, which we call first-step analysis.

Example 2.7.2 (Branching process). A single amoeba, Bobo, lives in a pond. After one minute Bobo will either die, split into two amoebas, or stay the same, with equal probability, and in subsequent minutes all living amoebas will behave the same way, independently. What is the probability that the amoeba population will eventually die out?

![img-27.jpeg](img-27.jpeg)

# Solution:

Let  $D$  be the event that the population eventually dies out; we want to find  $P(D)$ . We proceed by conditioning on the outcome at the first step: let  $B_i$  be the event that Bobo turns into  $i$  amoebas after the first minute, for  $i = 0,1,2$ . We know  $P(D|B_0) = 1$  and  $P(D|B_1) = P(D)$  (if Bobo stays the same, we're back to where we started). If Bobo splits into two, then we just have two independent versions

Introduction to Probability

of our original problem! We need both of the offspring to eventually die out, so  $P(D|B_2) = P(D)^2$ . Now we have exhausted all the possible cases and can combine them with the law of total probability:

$$
\begin{array}{l} P (D) = P (D | B _ {0}) \cdot \frac {1}{3} + P (D | B _ {1}) \cdot \frac {1}{3} + P (D | B _ {2}) \cdot \frac {1}{3} \\ = 1 \cdot \frac {1}{3} + P (D) \cdot \frac {1}{3} + P (D) ^ {2} \cdot \frac {1}{3}. \\ \end{array}
$$

Solving for  $P(D)$  gives  $P(D) = 1$ : the amoeba population will die out with probability 1.

The strategy of first-step analysis works here because the problem is self-similar in nature: when Bobo continues as a single amoeba or splits into two, we end up with another version or another two versions of our original problem. Conditioning on the first step allows us to express  $P(D)$  in terms of itself.

Example 2.7.3 (Gambler's ruin). Two gamblers, A and B, make a sequence of $1 bets. In each bet, gambler A has probability  $p$  of winning, and gambler B has probability  $q = 1 - p$  of winning. Gambler A starts with  $i$  dollars and gambler B starts with  $N - i$  dollars; the total wealth between the two remains constant since every time A loses a dollar, the dollar goes to B, and vice versa.

We can visualize this game as a random walk on the integers between 0 and  $N$ , where  $p$  is the probability of going to the right in a given step: imagine a person who starts at position  $i$  and, at each time step, moves one step to the right with probability  $p$  and one step to the left with probability  $q = 1 - p$ . The game ends when either A or B is ruined, i.e., when the random walk reaches 0 or  $N$ . What is the probability that A wins the game (walking away with all the money)?

![img-28.jpeg](img-28.jpeg)

# Solution:

We recognize that this game, like Bobo's reproductive process, has a recursive structure: after the first step, it's exactly the same game, except that A's wealth is now either  $i + 1$  or  $i - 1$ . Let  $p_i$  be the probability that A wins the game, given that A starts with  $i$  dollars. We will use first-step analysis to solve for the  $p_i$ . Let  $W$  be the event that A wins the game. By LOTP, conditioning on the outcome of the first

Conditional probability

round, we have

$$
\begin{array}{l}
p_{i} = P(W|\text{A starts at } i, \text{ wins round } 1) \cdot p + P(W|\text{A starts at } i, \text{ loses round } 1) \cdot q \\
= P(W|\text{A starts at } i + 1) \cdot p + P(W|\text{A starts at } i - 1) \cdot q \\
= p_{i+1} \cdot p + p_{i-1} \cdot q.
\end{array}
$$

This must be true for all $i$ from 1 to $N - 1$, and we also have the boundary conditions $p_0 = 0$ and $p_N = 1$. Now we can solve this equation, called a difference equation, to obtain the $p_i$. Section A.4 of the math appendix discusses how to solve difference equations, so we will omit some of the steps here.

The characteristic equation of the difference equation is $px^2 - x + q = 0$, which has roots 1 and $q/p$. If $p \neq 1/2$, these roots are distinct, and the general solution is

$$
p_{i} = a \cdot 1^{i} + b \cdot \left(\frac{q}{p}\right)^{i}.
$$

Using the boundary conditions $p_0 = 0$ and $p_N = 1$, we get

$$
a = -b = \frac{1}{1 - \left(\frac{q}{p}\right)^N},
$$

and we simply plug these back in to get the specific solution. If $p = 1/2$, the roots of the characteristic polynomial are not distinct, so the general solution is

$$
p_{i} = a \cdot 1^{i} + b \cdot i \cdot 1^{i}.
$$

The boundary conditions give $a = 0$ and $b = 1/N$.

In summary, the probability of A winning with a starting wealth of $i$ is

$$
p_{i} = \left\{
\begin{array}{ll}
\frac{1 - \left(\frac{q}{p}\right)^{i}}{1 - \left(\frac{q}{p}\right)^{N}} &amp; \text{if } p \neq 1/2, \\
\frac{i}{N} &amp; \text{if } p = 1/2.
\end{array}
\right.
$$

The $p = 1/2$ case is consistent with the $p \neq 1/2$ case, in the sense that

$$
\lim_{p \to \frac{1}{2}} \frac{1 - \left(\frac{q}{p}\right)^i}{1 - \left(\frac{q}{p}\right)^N} = \frac{i}{N}.
$$

To see this, let $x = q/p$ and let $x$ approach 1. By L'Hôpital's rule,

$$
\lim_{x \to 1} \frac{1 - x^{i}}{1 - x^{N}} = \lim_{x \to 1} \frac{i x^{i-1}}{N x^{N-1}} = \frac{i}{N}.
$$

The answer for the $p = 1/2$ case has a simple interpretation: A's probability of winning equals the proportion of the wealth that A starts out with. So if $p = 1/2$

and A starts out with much less money than B, then A’s chance of winning the game is low. Having $p<1/2$ may also make A’s chance of winning low, even if $p$ is only a little bit less than $1/2$ and the players start out with the same amount of money. For example, if $p=0.49$ and each player starts out with $100, then A has only about a 1.8% chance of winning the game.

We have focused on the probability of A winning the game, but what about B? Rather than starting from scratch, we can use *symmetry*: aside from notation, there is nothing in the description of the game to distinguish A from B. By symmetry, the probability of B winning from a starting wealth of $N-i$ is obtained by switching the roles of $q$ and $p$, and of $i$ and $N-i$. This gives

\[ P(\text{B wins}|\text{B starts at }N-i)=\left\{\begin{array}[]{ll}\frac{1-\left(\frac{p}{q}\right)^{N-i}}{1-\left(\frac{p}{q}\right)^{N}}&\text{if }p\neq 1/2,\\
\frac{N-i}{N}&\text{if }p=1/2.\end{array}\right. \]

It can then be verified that for all $i$ and all $p$, $P(\text{A wins})+P(\text{B wins})=1$, so the game is guaranteed to end: the probability is 0 that it will oscillate forever. ∎

### 2.8 Pitfalls and paradoxes

The next two examples are fallacies of conditional thinking that have arisen in the legal context. The prosecutor’s fallacy is the confusion of $P(A|B)$ with $P(B|A)$; the defense attorney’s fallacy is the failure to condition on *all* the evidence.

###### 2.8.1 (Prosecutor’s fallacy).

In 1998, Sally Clark was tried for murder after two of her sons died shortly after birth. During the trial, an expert witness for the prosecution testified that the probability of a newborn dying of sudden infant death syndrome (SIDS) was $1/8500$, so the probability of two deaths due to SIDS in one family was $(1/8500)^{2}$, or about one in 73 million. Therefore, he continued, the probability of Clark’s innocence was one in 73 million.

There are at least two major problems with this line of reasoning. First, the expert witness found the probability of the intersection of “first son dies of SIDS” and “second son dies of SIDS” by multiplying the individual event probabilities; as we know, this is only valid if deaths due to SIDS are *independent* within a family. This independence would not hold if genetic or other family-specific risk factors cause all newborns within certain families to be at increased risk of SIDS.

Second, the so-called expert has confused two different conditional probabilities: $P(\text{innocence}|\text{evidence})$ is different from $P(\text{evidence}|\text{innocence})$. The witness claims that the probability of observing two newborn deaths if the defendant were innocent is extremely low; that is, $P(\text{evidence}|\text{innocence})$ is small. What we are interested in,

Conditional probability

however, is $P(\mathrm{innocence}|\mathrm{evidence})$, the probability that the defendant is innocent given all the evidence. By Bayes’ rule,

$P(\mathrm{innocence}|\mathrm{evidence})=\frac{P(\mathrm{evidence}|\mathrm{innocence})P(\mathrm{innocence})}{P(\mathrm{evidence})},$

so to calculate the conditional probability of innocence given the evidence, we must take into account $P(\mathrm{innocence})$, the prior probability of innocence. This probability is extremely high: although double deaths due to SIDS are rare, so are double infanticides! Expanding the denominator as

$P(\mathrm{evidence}|\mathrm{innocence})P(\mathrm{innocence})+P(\mathrm{evidence}|\mathrm{guilt})P(\mathrm{guilt}),$

note that if $P(\mathrm{guilt})$ is small enough so that the second term is negligible compared to the first term, then the denominator of $P(\mathrm{innocence}|\mathrm{evidence})$ is approximately equal to the numerator, making $P(\mathrm{innocence}|\mathrm{evidence})$ close to 1.

The posterior probability of innocence given the evidence depends strongly on both $P(\mathrm{evidence}|\mathrm{innocence})$, which is very low, and $P(\mathrm{innocence})$, which is very high. The expert’s probability of $(1/8500)^{2}$, questionable in and of itself, is only part of the equation.

Sadly, Clark was convicted of murder and sent to prison, partly based on the expert’s wrongheaded testimony, and spent over three years in jail before her conviction was overturned. The outcry over the misuse of conditional probability in the Sally Clark case led to the review of hundreds of other cases where similar faulty logic was used by the prosecution.

$\nLeftrightarrow$ 2.8.2 (Defense attorney’s fallacy). A woman has been murdered, and her husband is put on trial for this crime. Evidence comes to light that the defendant had a history of abusing his wife. The defense attorney argues that the evidence of abuse should be excluded on grounds of irrelevance, since only 1 in 10,000 men with wives they abuse subsequently murder their wives. Should the judge grant the defense attorney’s motion to bar this evidence from trial?

Suppose that the defense attorney’s 1-in-10,000 figure is correct, and further assume the following for a relevant population of husbands and wives: 1 in 10 husbands abuse their wives, 1 in 5 murdered wives were murdered by their husbands, and 50% of husbands who murder their wives previously abused them. Also, assume that if the husband of a murdered wife is *not* guilty of the murder, then the probability that he abused his wife reverts to the unconditional probability of abuse.

How to define the “relevant population” and how to estimate such probabilities are difficult issues. For example, should we look at citywide, statewide, national, or international statistics? How should we account for unreported abuse and unsolved murders? What if murder rates are changing over time? For this problem, assume that a reasonable choice of the relevant population has been agreed on, and that the stated probabilities are known to be correct.

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

Conditional probability

![img-29.jpeg](img-29.jpeg)
Dr. Hibbert

![img-30.jpeg](img-30.jpeg)
Dr. Nick

# FIGURE 2.6

An example of Simpson's paradox. White dots represent successful surgeries and black dots represent failed surgeries. Dr. Hibbert is better in both types of surgery but has a lower overall success rate, because he is performing the harder type of surgery much more often than Dr. Nick is.

What's happening is that Dr. Hibbert, presumably due to his reputation as the superior doctor, is performing a greater number of heart surgeries, which are inherently riskier than Band-Aid removals. His overall success rate is lower not because of lesser skill on any particular type of surgery, but because a larger fraction of his surgeries are risky.

Let's use event notation to make this precise. For events  $A$ ,  $B$ , and  $C$ , we say that we have a Simpson's paradox if

$$
P (A | B, C) &lt;   P (A | B ^ {c}, C)
$$

$$
P (A | B, C ^ {c}) &lt;   P (A | B ^ {c}, C ^ {c}),
$$

but

$$
P (A | B) &gt; P (A | B ^ {c}).
$$

In this case, let  $A$  be the event of a successful surgery,  $B$  be the event that Dr. Nick is the surgeon, and  $C$  be the event that the surgery is a heart surgery. The conditions for Simpson's paradox are fulfilled because the probability of a successful surgery is lower under Dr. Nick than under Dr. Hibbert whether we condition on heart surgery or on Band-Aid removal, but the overall probability of success is higher for Dr. Nick.

The law of total probability tells us mathematically why this can happen:

$$
P (A | B) = P (A | C, B) P (C | B) + P (A | C ^ {c}, B) P (C ^ {c} | B)
$$

$$
P (A | B ^ {c}) = P (A | C, B ^ {c}) P (C | B ^ {c}) + P (A | C ^ {c}, B ^ {c}) P (C ^ {c} | B ^ {c}).
$$

The above equations express $P(A|B)$ as a weighted average of $P(A|C,B)$ and $P(A|C^{c},B)$, and $P(A|B^{c})$ as a weighted average of $P(A|C,B^{c})$ and $P(A|C^{c},B^{c})$. If the corresponding weights were the same in both of these weighted averages, then Simpson’s paradox could not occur. But the weights here are *different*:

$P(C|B)<P(C|B^{c})\mbox{ and }P(C^{c}|B)>P(C^{c}|B^{c}),$

since Dr. Nick is much less likely than Dr. Hibbert to be performing a heart surgery.

Although we have

$P(A|C,B)<P(A|C,B^{c})$

and

$P(A|C^{c},B)<P(A|C^{c},B^{c}),$

the fact that the weights are so different results in the inequality flipping when we do not condition on whether or not $C$ occurred:

$P(A|B)>P(A|B^{c}).$

Numerically, the two weighted averages are

$P(A|B)$ $=$ $0.83=(2/10)\cdot 0.1+(81/90)\cdot 0.9$
$P(A|B^{c})$ $=$ $0.80=(70/90)\cdot 0.9+(10/10)\cdot 0.1.$

The first equation (corresponding to Dr. Nick) puts much more weight on the second term (corresponding to the easier surgery) than does the second equation.

Aggregation across different types of surgeries presents a misleading picture of the doctors’ abilities because we lose the information about which doctor tends to perform which type of surgery. When we think *confounding variables* like surgery type could be at play, we should examine the disaggregated data to see what is really going on.

Simpson’s paradox arises in many real-world contexts. In the following examples, you should try to identify the events $A$, $B$, and $C$ that create the paradox.

- *Gender discrimination in college admissions*: In the 1970s, men were significantly more likely than women to be admitted for graduate study at the University of California, Berkeley, leading to charges of gender discrimination. Yet within most individual departments, women were admitted at a higher rate than men. It was found that women tended to apply to the departments with more competitive admissions, while men tended to apply to less competitive departments.
- *Baseball batting averages*: It is possible for player 1 to have a higher batting average than player 2 in the first half of a baseball season *and* a higher batting average than player 2 in the second half of the season, yet have a lower overall batting average for the entire season. It depends on how many at-bats the players have in each half of the season. (An *at-bat* is when it’s a player’s turn to try to hit the ball; the player’s *batting average* is the number of hits the player gets divided by the player’s number of at-bats.)

Conditional probability

- *Health effects of smoking*: Cochran *[4]* found that within any age group, cigarette smokers had higher mortality rates than cigar smokers, but because cigarette smokers were on average younger than cigar smokers, overall mortality rates were lower for cigarette smokers. ∎

### 2.9 Recap

The conditional probability of $A$ given $B$ is

$P(A|B)=\frac{P(A\cap B)}{P(B)}.$

Conditional probability has exactly the same properties as probability, but $P(\cdot|B)$ updates our uncertainty about events to reflect the observed evidence $B$. Events whose probabilities are unchanged after observing the evidence $B$ are said to be independent of $B$. Two events can also be conditionally independent given a third event $E$. Conditional independence does not imply unconditional independence, nor does unconditional independence imply conditional independence.

Two important results about conditional probability are Bayes’ rule, which relates $P(A|B)$ to $P(B|A)$, and the law of total probability, which allows us to get unconditional probabilities by partitioning the sample space and calculating conditional probabilities within each slice of the partition.

Bayes’ rule says that

$P(A|B)=\frac{P(B|A)P(A)}{P(B)},$

while LOTP says that

$P(B)=\sum_{i=1}^{n}P(B|A_{i})P(A_{i}),$

for any partition $A_{1},\ldots,A_{n}$ of the sample space. Bayes’ rule and LOTP are often used in tandem.

Conditioning is extremely helpful for problem-solving because it allows us to break a problem into smaller pieces, consider all possible cases separately, and then combine them. When using this strategy, we should try to condition on the information that, if known, would make the problem simpler, hence the saying *condition on what you wish you knew*. When a problem involves multiple stages, it can be helpful to *condition on the first step* to obtain a recursive relationship.

Common mistakes in thinking conditionally include:

- confusion of the prior probability $P(A)$ with the posterior probability $P(A|B)$;

Introduction to Probability

- the prosecutor’s fallacy, confusing $P(A|B)$ with $P(B|A)$;
- the defense attorney’s fallacy, failing to condition on all the evidence;
- unawareness of Simpson’s paradox and the importance of thinking carefully about whether to aggregate data.

Figure 2.7 illustrates how probabilities can be updated as new evidence comes in sequentially. Imagine that there is some event $A$ that we are interested in. On Monday morning, for example, our prior probability for $A$ is $P(A)$. If we observe on Monday afternoon that $B$ occurred, then we can use Bayes’ rule (or the definition of conditional probability) to compute the posterior probability $P(A|B)$.

We use this posterior probability for $A$ as the new prior on Tuesday morning, and then we continue to collect evidence. Suppose that on Tuesday we observe that $C$ occurred. Then we can compute the new posterior probability $P(A|B,C)$ in various ways (in this context, probably the most natural way is to use Bayes’ rule with extra conditioning on $B$). This in turn becomes the new prior if we are going to continue to collect evidence.

## 2.10 R

### Simulating the frequentist interpretation

Recall that the frequentist interpretation of conditional probability based on a large number $n$ of repetitions of an experiment is $P(A|B) \approx n_{AB} / n_B$, where $n_{AB}$ is the number of times that $A \cap B$ occurs and $n_B$ is the number of times that $B$ occurs. Let’s try this out by simulation, and verify the results of Example 2.2.5. So let’s simulate $n$ families, each with two children.

```
n &lt;- 10^5
child1 &lt;- sample(2,n,replace=TRUE)
child2 &lt;- sample(2,n,replace=TRUE)
```

Here `child1` is a vector of length $n$, where each element is a 1 or a 2. Letting 1 stand for “girl” and 2 stand for “boy”, this vector represents the gender of the elder child in each of the $n$ families. Similarly, `child2` represents the gender of the younger child in each family.

Alternatively, we could have used

```
sample(c("girl","boy"),n,replace=TRUE)
```

but it is more convenient working with numerical values.

Let $A$ be the event that both children are girls and $B$ the event that the elder is a girl.

Conditional probability

![img-31.jpeg](img-31.jpeg)
FIGURE 2.7 Conditional probability tells us how to update probabilities as new evidence comes in. Shown are the probabilities for an event  $A$  initially, after obtaining one piece of evidence  $B$ , and after obtaining a second piece of evidence  $C$ . The posterior for  $A$  after observing the first piece of evidence becomes the new prior before observing the second piece of evidence. After both  $B$  and  $C$  are observed, a new posterior for  $A$  can be found in various ways. This then becomes the new prior if more evidence will be collected.

Following the frequentist interpretation, we count the number of repetitions where $B$ occurred and name it n.b, and we also count the number of repetitions where $A\cap B$ occurred and name it n.ab. Finally, we divide n.ab by n.b to approximate $P(A|B)$.

n.b <- sum(child1==1) n.ab <- sum(child1==1 & child2==1) n.ab/n.b

The ampersand & is an elementwise AND, so n.ab is the number of families where both the first child and the second child are girls. When we ran this code, we got 0.50, which agrees with $P(\text{both girls}|\text{elder is a girl})=1/2$.

Now let $A$ be the event that both children are girls and $B$ the event that at least one of the children is a girl. Then $A\cap B$ is the same, but n.b needs to count the number of families where at least one child is a girl. This is accomplished with the elementwise OR operator | (this is *not* a conditioning bar; it is an inclusive OR, returning TRUE if at least one element is TRUE).

n.b <- sum(child1==1 | child2==1) n.ab <- sum(child1==1 & child2==1) n.ab/n.b

We got 0.33, which agrees with $P(\text{both girls}|\text{at least one girl})=1/3$.

#### Monty Hall simulation

Many long, bitter debates about the Monty Hall problem could have been averted by *trying it out* with a simulation. To study how well the never-switch strategy performs, let’s generate $10^{5}$ runs of the Monty Hall game. To simplify notation, assume the contestant always chooses door 1. Then we can generate a vector specifying which door has the car for each repetition:

n <- 10^5 cardoor <- sample(3,n,replace=TRUE)

At this point we could generate the vector specifying which doors Monty opens, but that’s unnecessary since the never-switch strategy succeeds if and only if door 1 has the car! So the fraction of times when the never-switch strategy succeeds is sum(cardoor==1)/n, which was 0.334 in our simulation. This is very close to the true value, 1/3.

What if we want to *play* the Monty Hall game interactively? We can do this by programming a *function*. Entering the following code in R defines a function called monty, which can then be invoked by entering the command monty() any time you feel like playing the game!

monty <- function() {
doors <- 1:3

# randomly pick where the car is
cardoor <- sample(doors,1)

# prompt player
print("Monty Hall says ‘Pick a door, any door!’")

# receive the player’s choice of door (should be 1,2, or 3)
chosen <- scan(what = integer(), nlines = 1, quiet = TRUE)

# pick Monty’s door (can’t be the player’s door or the car door)
if (chosen != cardoor) montydoor <- doors[-c(chosen, cardoor)]
else montydoor <- sample(doors[-chosen],1)

# find out whether the player wants to switch doors
print(paste("Monty opens door ", montydoor, "!", sep=""))
print("Would you like to switch (y/n)?")
reply <- scan(what = character(), nlines = 1, quiet = TRUE)

# interpret what player wrote as "yes" if it starts with "y"
if (substr(reply,1,1) == "y"){
chosen <- doors[-c(chosen,montydoor)]
}

# announce the result of the game!
if (chosen == cardoor) print("You won!")
else print("You lost!")
}
```

The print command prints its argument to the screen. We combine this with the paste command since if we used print("Monty opens door montydoor") then R would literally print “Monty opens door montydoor”. The scan command interactively requests input from the user; we use what = integer() when we want the user to enter an integer and what = character() when we want the user to enter text. Using substr(reply,1,1) extracts the first character of reply, in case the user replies with “yes” or “yep” or “yeah!” rather than with “y”.

### 2.11 Exercises

Exercises marked with 8 have detailed solutions at http://stat110.net.

####

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

10. Fred is working on a major project. In planning the project, two milestones are set up, with dates by which they should be accomplished. This serves as a way to track Fred’s progress. Let $A_{1}$ be the event that Fred completes the first milestone on time, $A_{2}$ be the event that he completes the second milestone on time, and $A_{3}$ be the event that he completes the project on time.

Suppose that $P(A_{j+1}|A_{j})=0.8$ but $P(A_{j+1}|A_{j}^{c})=0.3$ for $j=1,2$, since if Fred falls behind on his schedule it will be hard for him to get caught up. Also, assume that the second milestone supersedes the first, in the sense that once we know whether he is on time in completing the second milestone, it no longer matters what happened with the first milestone. We can express this by saying that $A_{1}$ and $A_{3}$ are conditionally independent given $A_{2}$ and they’re also conditionally independent given $A_{2}^{c}$.

1. Find the probability that Fred will finish the project on time, given that he completes the first milestone on time. Also find the probability that Fred will finish the project on time, given that he is late for the first milestone.
2. Suppose that $P(A_{1})=0.75$. Find the probability that Fred will finish the project on time.
11. An *exit poll* in an election is a survey taken of voters just after they have voted. One major use of exit polls has been so that news organizations can try to figure out as soon as possible who won the election, before the votes are officially counted. This has been notoriously inaccurate in various elections, sometimes because of *selection bias*: the sample of people who are invited to and agree to participate in the survey may not be similar enough to the overall population of voters.

Consider an election with two candidates, Candidate A and Candidate B. Every voter is invited to participate in an exit poll, where they are asked whom they voted for; some accept and some refuse. For a randomly selected voter, let $A$ be the event that they voted for A, and $W$ be the event that they are willing to participate in the exit poll. Suppose that $P(W|A)=0.7$ but $P(W|A^{c})=0.3$. In the exit poll, 60% of the respondents say they voted for A (assume that they are all honest), suggesting a comfortable victory for A. Find $P(A)$, the true proportion of people who voted for A.
12. Alice is trying to communicate with Bob, by sending a message (encoded in binary) across a channel.

1. Suppose for this part that she sends only one bit (a 0 or 1), with equal probabilities. If she sends a 0, there is a 5% chance of an error occurring, resulting in Bob receiving a 1; if she sends a 1, there is a 10% chance of an error occurring, resulting in Bob receiving a 0. Given that Bob receives a 1, what is the probability that Alice actually sent a 1?
2. To reduce the chance of miscommunication, Alice and Bob decide to use a *repetition code*. Again Alice wants to convey a 0 or a 1, but this time she repeats it two more times, so that she sends 000 to convey 0 and 111 to convey 1. Bob will decode the message by going with what the majority of the bits were. Assume that the error probabilities are as in (a), with error events for different bits independent of each other. Given that Bob receives 110, what is the probability that Alice intended to convey a 1?
13. Company A has just developed a diagnostic test for a certain disease. The disease afflicts 1% of the population. As defined in Example 2.3.9, the *sensitivity* of the test is the probability of someone testing positive, given that they have the disease, and the *specificity* of the test is the probability that of someone testing negative, given that they don’t have the disease. Assume that, as in Example 2.3.9, the sensitivity and specificity are both 0.95.

Company B, which is a rival of Company A, offers a competing test for the disease. Company B claims that their test is faster and less expensive to perform than Company A’s test, is less painful (Company A’s test requires an incision), and yet has a higher

Introduction to Probability

overall success rate, where overall success rate is defined as the probability that a random person gets diagnosed correctly.

(a) It turns out that Company B’s test can be described and performed very simply: no matter who the patient is, diagnose that they do not have the disease. Check whether Company B’s claim about overall success rates is true.

(b) Explain why Company A’s test may still be useful.

(c) Company A wants to develop a new test such that the overall success rate is higher than that of Company B’s test. If the sensitivity and specificity are equal, how high does the sensitivity have to be to achieve their goal? If (amazingly) they can get the sensitivity equal to 1, how high does the specificity have to be to achieve their goal? If (amazingly) they can get the specificity equal to 1, how high does the sensitivity have to be to achieve their goal?
14. Consider the following scenario, from Tversky and Kahneman *[27]*:

&gt; Let $A$ be the event that before the end of next year, Peter will have installed a burglar alarm system in his home. Let $B$ denote the event that Peter’s home will be burglarized before the end of next year.

(a) Intuitively, which do you think is bigger, $P(A|B)$ or $P(A|B^{c})$? Explain your intuition.

(b) Intuitively, which do you think is bigger, $P(B|A)$ or $P(B|A^{c})$? Explain your intuition.

(c) Show that for any events $A$ and $B$ (with probabilities not equal to 0 or 1), the inequality $P(A|B)&gt;P(A|B^{c})$ is equivalent to $P(B|A)&gt;P(B|A^{c})$.

(d) Tversky and Kahneman report that 131 out of 162 people whom they posed (a) and (b) to said that $P(A|B)&gt;P(A|B^{c})$ and $P(B|A)<p(b|a^{c})$. $a$="" $a$="" $a\cup="" $a$="" $b$="" $b$’="" $b$’’s="" $p(a|b)="" $p(a|b^{c})\geq="" $p(a|b^{c})\geq="" (c)="" (a)="" a="" a’="" and="" are="" be="" both="" by="" can="" case="" close="" condition="" containing="" contrapositive,="" contains="" centp.="" d$="" d$,="" d’).="" d’’s="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.="" d’’s.}$.="" d’’s.="" apply="" are="" as="" at="" average="" be="" being="" both="" by="" can="" case="" close="" condition="" contrapositive,="" contrapositive,="" contrapositive,="" consider="" contrapositive,="" data="" deep="" despite="" determine="" determine.="" determine.="" determine.="" each="" equal="" example="" explanation="" follows="" for="" from="" general="" give="" has="" have="" hoping="" if="" implies="" in="" information="" is="" it="" its="" lotp.="" log="" logic="" logic,="" makes="" many="" makes’="" makes’’s="" not="" not.="" of="" on="" opinion="" or="" our="" particular,="" piece="" possible="" probability,="" problem="" probability,="" probability,="" problem="" random="" refaced="" result="" right="" same="" say="" sense.="" show="" showing="" show’’s="" should="" show’’s.="" statement="" statements="" such="" that="" the="" then="" this="" to="" two="" uncertainly.="" uncertainty.="" uncertainty.="" we="" where="" which="" why="" will="" with="" would="">0$. Intuitively, this says that if someone dogmatically believes something with absolute certainty, then no amount of evidence will change their mind. The principle of avoiding assigning probabilities of 0 or 1 to any event (except for mathematical certainties) was named Cromwell’s rule by the statistician Dennis Lindley, due to Cromwell saying to the Church of Scotland, “Think it possible you may be mistaken.”

Hint: Write $P(B)=P(B\cap A)+P(B\cap A^{c})$, and then show that $P(B\cap A^{c})=0$.</p(b|a^{c})$.>

19. Explain the following Sherlock Holmes saying in terms of conditional probability, carefully distinguishing between prior and posterior probabilities: “It is an old maxim of mine that when you have excluded the impossible, whatever remains, however improbable, must be the truth.”
20. The Jack of Spades (with cider), Jack of Hearts (with tarts), Queen of Spades (with a wink), and Queen of Hearts (without tarts) are taken from a deck of cards. These four cards are shuffled, and then two are dealt. Note: Literary references to cider, tarts, and winks do not need to be considered when solving this problem.

1. Find the probability that both of these two cards are queens, given that the first card dealt is a queen.
2. Find the probability that both are queens, given that at least one is a queen.
3. Find the probability that both are queens, given that one is the Queen of Hearts.
21. A fair coin is flipped 3 times. The toss results are recorded on separate slips of paper (writing “H” if Heads and “T” if Tails), and the 3 slips of paper are thrown into a hat.

1. Find the probability that all 3 tosses landed Heads, given that at least 2 were Heads.
2. Two of the slips of paper are randomly drawn from the hat, and both show the letter H. Given this information, what is the probability that all 3 tosses landed Heads?
22. A bag contains one marble which is either green or blue, with equal probabilities. A green marble is put in the bag (so there are 2 marbles now), and then a random marble is taken out. The marble taken out is green. What is the probability that the remaining marble is also green?
23. Let $G$ be the event that a certain individual is guilty of a certain robbery. In gathering evidence, it is learned that an event $E_{1}$ occurred, and a little later it is also learned that another event $E_{2}$ also occurred. Is it possible that individually, these pieces of evidence increase the chance of guilt (so $P(G|E_{1})>P(G)$ and $P(G|E_{2})>P(G)$), but together they decrease the chance of guilt (so $P(G|E_{1},E_{2})<P(G)$)?
24. Is it possible to have events $A_{1},A_{2},B,C$ with $P(A_{1}|B)>P(A_{1}|C)$ and $P(A_{2}|B)>P(A_{2}|C)$, yet $P(A_{1}\cup A_{2}|B)<P(A_{1}\cup A_{2}|C)$? If so, find an example (with a “story” interpreting the events, as well as giving specific numbers); otherwise, show that it is impossible for this phenomenon to happen.
25. A crime is committed by one of two suspects, $A$ and $B$. Initially, there is equal evidence against both of them. In further investigation at the crime scene, it is found that the guilty party had a blood type found in 10% of the population. Suspect $A$ does match this blood type, whereas the blood type of Suspect $B$ is unknown.

1. Given this new information, what is the probability that $A$ is the guilty party?
2. Given this new information, what is the probability that $B$’s blood type matches that found at the crime scene?
26. To battle against spam, Bob installs two anti-spam programs. An email arrives, which is either legitimate (event $L$) or spam (event $L^{c}$), and which program $j$ marks as legitimate (event $M_{j}$) or marks as spam (event $M_{j}^{c}$) for $j\in\{1,2\}$. Assume that 10% of Bob’s email is legitimate and that the two programs are each “90% accurate” in the sense that $P(M_{j}|L)=P(M_{j}^{c}|L^{c})=9/10$. Also assume that given whether an email is spam, the two programs’ outputs are conditionally independent.

1. Find the probability that the email is legitimate, given that the 1st program marks it as legitimate (simplify).
2. Find the probability that the email is legitimate, given that both programs mark it as legitimate (simplify).

(c) Bob runs the 1st program and $M_{1}$ occurs. He updates his probabilities and then runs the 2nd program. Let $\tilde{P}(A)=P(A|M_{1})$ be the updated probability function after running the 1st program. Explain briefly in words whether or not $\tilde{P}(L|M_{2})=P(L|M_{1}\cap M_{2})$: is conditioning on $M_{1}\cap M_{2}$ in one step equivalent to first conditioning on $M_{1}$, then updating probabilities, and then conditioning on $M_{2}$?
27. Suppose that there are 5 blood types in the population, named type 1 through type 5, with probabilities $p_{1},p_{2},\ldots,p_{5}$. A crime was committed by two individuals. A suspect, who has blood type 1, has prior probability $p$ of being guilty. At the crime scene, blood evidence is collected, which shows that one of the criminals has type 1 and the other has type 2.

Find the posterior probability that the suspect is guilty, given the evidence. Does the evidence make it more likely or less likely that the suspect is guilty, or does this depend on the values of the parameters $p,p_{1},\ldots,p_{5}$? If it depends on these values, give a simple criterion for when the evidence makes it more likely that the suspect is guilty.
28. Fred has just tested positive for a certain disease.

(a) Given this information, find the posterior odds that he has the disease, in terms of the prior odds, the sensitivity of the test, and the specificity of the test.

(b) Not surprisingly, Fred is much more interested in $P(\text{have disease}|\text{test positive})$, known as the positive predictive value, than in the sensitivity $P(\text{test positive}|\text{have disease})$. A handy rule of thumb in biostatistics and epidemiology is as follows:

For a rare disease and a reasonably good test, specificity matters much more than sensitivity in determining the positive predictive value.

Explain intuitively why this rule of thumb works. For this part you can make up some specific numbers and interpret probabilities in a frequentist way as proportions in a large population, e.g., assume the disease afflicts 1% of a population of 10000 people and then consider various possibilities for the sensitivity and specificity.
29. A family has two children. Let $C$ be a characteristic that a child can have, and assume that each child has characteristic $C$ with probability $p$, independently of each other and of gender. For example, $C$ could be the characteristic “born in winter” as in Example 2.2.7. Under the assumptions of Example 2.2.5, show that the probability that both children are girls given that at least one is a girl with characteristic $C$ is $\frac{2-p}{4-p}$. Note that this is $1/3$ if $p=1$ (agreeing with the first part of Example 2.2.5) and approaches $1/2$ from below as $p\to 0$ (agreeing with Example 2.2.7).

### Independence and conditional independence

30. $\circledS$ A family has 3 children, creatively named $A,B$, and $C$.

(a) Discuss intuitively (but clearly) whether the event “$A$ is older than $B$” is independent of the event “$A$ is older than $C$”.

(b) Find the probability that $A$ is older than $B$, given that $A$ is older than $C$.
31. $\circledS$ Is it possible that an event is independent of itself? If so, when is this the case?
32. $\circledS$ Consider four nonstandard dice (the Efron dice), whose sides are labeled as follows (the 6 sides on each die are equally likely).

A: $4,4,4,4,0,0$

B: $3,3,3,3,3,3$

C: $6,6,2,2,2,2$

Conditional probability

D: $5,5,5,1,1,1$

These four dice are each rolled once. Let $A$ be the result for die A, $B$ be the result for die B, etc.

(a) Find $P(A&gt;B),P(B&gt;C),P(C&gt;D)$, and $P(D&gt;A)$.

(b) Is the event $A&gt;B$ independent of the event $B&gt;C$? Is the event $B&gt;C$ independent of the event $C&gt;D$? Explain.
33. Alice, Bob, and 100 other people live in a small town. Let $C$ be the set consisting of the 100 other people, let $A$ be the set of people in $C$ who are friends with Alice, and let $B$ be the set of people in $C$ who are friends with Bob. Suppose that for each person in $C$, Alice is friends with that person with probability $1/2$, and likewise for Bob, with all of these friendship statuses independent.

(a) Let $D\subseteq C$. Find $P(A=D)$.

(b) Find $P(A\subseteq B)$.

(c) Find $P(A\cup B=C)$.
34. Suppose that there are two types of drivers: good drivers and bad drivers. Let $G$ be the event that a certain man is a good driver, $A$ be the event that he gets into a car accident next year, and $B$ be the event that he gets into a car accident the following year. Let $P(G)=g$ and $P(A|G)=P(B|G)=p_{1},P(A|G^{c})=P(B|G^{c})=p_{2}$, with $p_{1}&lt;p_{2}$. Suppose that given the information of whether or not the man is a good driver, $A$ and $B$ are independent (for simplicity and to avoid being morbid, assume that the accidents being considered are minor and wouldn’t make the man unable to drive).

(a) Explain intuitively whether or not $A$ and $B$ are independent.

(b) Find $P(G|A^{c})$.

(c) Find $P(B|A^{c})$.
35. $\circledS$ You are going to play 2 games of chess with an opponent whom you have never played against before (for the sake of this problem). Your opponent is equally likely to be a beginner, intermediate, or a master. Depending on which, your chances of winning an individual game are 90%, 50%, or 30%, respectively.

(a) What is your probability of winning the first game?

(b) Congratulations: you won the first game! Given this information, what is the probability that you will also win the second game (assume that, given the skill level of your opponent, the outcomes of the games are independent)?

(c) Explain the distinction between assuming that the outcomes of the games are independent and assuming that they are conditionally independent given the opponent’s skill level. Which of these assumptions seems more reasonable, and why?
36. (a) Suppose that in the population of college applicants, being good at baseball is independent of having a good math score on a certain standardized test (with respect to some measure of “good”). A certain college has a simple admissions procedure: admit an applicant if and only if the applicant is good at baseball or has a good math score on the test.

Give an intuitive explanation of why it makes sense that among students that the college admits, having a good math score is *negatively associated* with being good at baseball, i.e., conditioning on having a good math score decreases the chance of being good at baseball.

(b) Show that if $A$ and $B$ are independent and $C=A\cup B$, then $A$ and $B$ are conditionally dependent given $C$ (as long as $P(A\cap B)>0$ and $P(A\cup B)<1$), with

$P(A|B,C)<P(A|C).$

This phenomenon is known as Berkson’s paradox, especially in the context of admissions to a school, hospital, etc.
37. Two different diseases cause a certain weird symptom; anyone who has either or both of these diseases will experience the symptom. Let $D_{1}$ be the event of having the first disease, $D_{2}$ be the event of having the second disease, and $W$ be the event of having the weird symptom. Suppose that $D_{1}$ and $D_{2}$ are independent with $P(D_{j})=p_{j}$, and that a person with neither of these diseases will have the weird symptom with probability $w_{0}$. Let $q_{j}=1-p_{j}$, and assume that $0<p_{j}<1$.

(a) Find $P(W)$.

(b) Find $P(D_{1}|W),P(D_{2}|W)$, and $P(D_{1},D_{2}|W)$.

(c) Determine algebraically whether or not $D_{1}$ and $D_{2}$ are conditionally independent given $W$.

(d) Suppose for this part only that $w_{0}=0$. Give a clear, convincing intuitive explanation in words of whether $D_{1}$ and $D_{2}$ are conditionally independent given $W$.
38. We want to design a spam filter for email. As described in Exercise 1, a major strategy is to find phrases that are much more likely to appear in a spam email than in a non-spam email. In that exercise, we only consider one such phrase: “free money”. More realistically, suppose that we have created a list of 100 words or phrases that are much more likely to be used in spam than in non-spam.

Let $W_{j}$ be the event that an email contains the $j$th word or phrase on the list. Let

$p=P(\text{spam}),p_{j}=P(W_{j}|\text{spam}),r_{j}=P(W_{j}|\text{not spam}),$

where “spam” is shorthand for the event that the email is spam.

Assume that $W_{1},\ldots,W_{100}$ are conditionally independent given that the email is spam, and conditionally independent given that it is not spam. A method for classifying emails (or other objects) based on this kind of assumption is called a naive Bayes classifier. (Here “naive” refers to the fact that the conditional independence is a strong assumption, not to Bayes being naive. The assumption may or may not be realistic, but naive Bayes classifiers sometimes work well in practice even if the assumption is not realistic.)

Under this assumption we know, for example, that

$P(W_{1},W_{2},W_{3}^{c},W_{4}^{c},\ldots,W_{100}^{c}|\text{spam})=p_{1}p_{2}(1-p_{3})(1-p_{4})\ldots(1-p_{100}).$

Without the naive Bayes assumption, there would be vastly more statistical and computational difficulties since we would need to consider $2^{100}\approx 1.3\times 10^{30}$ events of the form $A_{1}\cap A_{2}\cdots\cap A_{100}$ with each $A_{j}$ equal to either $W_{j}$ or $W_{j}^{c}$. A new email has just arrived, and it includes the 23rd, 64th, and 65th words or phrases on the list (but not the other 97). So we want to compute

$P(\text{spam}|W_{1}^{c},\ldots,W_{22}^{c},W_{23},W_{24}^{c},\ldots,W_{63}^{c},W_{64},W_{65},W_{66}^{c},\ldots,W_{100}^{c}).$

Note that we need to condition on all the evidence, not just the fact that $W_{23}\cap W_{64}\cap W_{65}$ occurred. Find the conditional probability that the new email is spam (in terms of $p$ and the $p_{j}$ and $r_{j}$

Conditional probability

39. (a) Consider the following 7-door version of the Monty Hall problem. There are 7 doors, behind one of which there is a car (which you want), and behind the rest of which there are goats (which you don’t want). Initially, all possibilities are equally likely for where the car is. You choose a door. Monty Hall then opens 3 goat doors, and offers you the option of switching to any of the remaining 3 doors.

Assume that Monty Hall knows which door has the car, will always open 3 goat doors and offer the option of switching, and that Monty chooses with equal probabilities from all his choices of which goat doors to open. Should you switch? What is your probability of success if you switch to one of the remaining 3 doors?

(b) Generalize the above to a Monty Hall problem where there are $n\geq 3$ doors, of which Monty opens $m$ goat doors, with $1\leq m\leq n-2$.
40. (c) Consider the Monty Hall problem, except that Monty enjoys opening door 2 more than he enjoys opening door 3, and if he has a choice between opening these two doors, he opens door 2 with probability $p$, where $\frac{1}{2}\leq p\leq 1$.

To recap: there are three doors, behind one of which there is a car (which you want), and behind the other two of which there are goats (which you don’t want). Initially, all possibilities are equally likely for where the car is. You choose a door, which for concreteness we assume is door 1. Monty Hall then opens a door to reveal a goat, and offers you the option of switching. Assume that Monty Hall knows which door has the car, will always open a goat door and offer the option of switching, and as above assume that if Monty Hall has a choice between opening door 2 and door 3, he chooses door 2 with probability $p$ (with $\frac{1}{2}\leq p\leq 1$).

(a) Find the unconditional probability that the strategy of always switching succeeds (unconditional in the sense that we do not condition on which of doors 2 or 3 Monty opens).

(b) Find the probability that the strategy of always switching succeeds, given that Monty opens door 2.

(c) Find the probability that the strategy of always switching succeeds, given that Monty opens door 3.
41. The ratings of Monty Hall’s show have dropped slightly, and a panicking executive producer complains to Monty that the part of the show where he opens a door lacks suspense: Monty always opens a door with a goat. Monty replies that the reason is so that the game is never spoiled by him revealing the car, but he agrees to update the game as follows.

Before each show, Monty secretly flips a coin with probability $p$ of Heads. If the coin lands Heads, Monty resolves to open a door with a goat (with equal probabilities if there is a choice). Otherwise, Monty resolves to open a random door, with equal probabilities. Of course, Monty will not open the door that the contestant initially chooses. The contestant knows $p$ but does not know the outcome of the coin flip. When the show starts, the contestant chooses a door. Monty (who knows where the car is) then opens a door. If the car is revealed, the game is over; if a goat is revealed, the contestant is offered the option of switching. Now suppose it turns out that the contestant chooses door 1 and then Monty opens door 2, revealing a goat. What is the contestant’s probability of success if they switch to door 3?
42. Consider the following variation of the Monty Hall problem, where in some situations Monty may *not* open a door and give the contestant the choice of whether to switch doors. Specifically, there are 3 doors, with 2 containing goats and 1 containing a car. The car is equally likely to be anywhere, and Monty knows where the car is. Let $0\leq p\leq 1$.

Introduction to Probability

The contestant chooses a door. If this initial choice has the car, Monty *will* open another door, revealing a goat (choosing with equal probabilities among his two choices of door), and then offer the contestant the choice of whether to switch to the other unopened door.

If the contestant’s initial choice has a goat, then with probability $p$ Monty *will* open another door, revealing a goat, and then offer the contestant the choice of whether to switch to the other unopened door; but with probability $1-p$, Monty will *not* open a door, and the contestant must stick with their initial choice.

The contestant decides in advance to use the following strategy: initially choose door 1. Then, if Monty opens a door and offers the choice of whether to switch, do switch.

1. Find the unconditional probability that the contestant will get the car. Also, check what your answer reduces to in the extreme cases $p=0$ and $p=1$, and briefly explain why your answer makes sense in these two cases.

2. Monty now opens door 2, revealing a goat. So the contestant switches to door 3. Given this information, find the conditional probability that the contestant will get the car.
2. You are the contestant on the Monty Hall show. Monty is trying out a new version of his game, with rules as follows. You get to choose one of three doors. One door has a car behind it, another has a computer, and the other door has a goat (with all permutations equally likely). Monty, who knows which prize is behind each door, will open a door (but not the one you chose) and then let you choose whether to switch from your current choice to the other unopened door.

Assume that you prefer the car to the computer, the computer to the goat, and (by transitivity) the car to the goat.

1. Suppose for this part only that Monty always opens the door that reveals your less preferred prize out of the two alternatives, e.g., if he is faced with the choice between revealing the goat or the computer, he will reveal the goat. Monty opens a door, revealing a goat (this is again for this part only). Given this information, should you switch? If you do switch, what is your probability of success in getting the car?

2. Now suppose that Monty reveals your less preferred prize with probability $p$, and your more preferred prize with probability $q=1-p$. Monty opens a door, revealing a computer. Given this information, should you switch (your answer can depend on $p$)? If you do switch, what is your probability of success in getting the car (in terms of $p$)?
3. Monty Hall has introduced a new twist in his game, by generalizing the assumption that the initial probabilities for where the car is are $(\frac{1}{3},\frac{1}{3},\frac{1}{3})$. Specifically, there are three doors, behind one of which there is a car (which the contestant wants), and behind the other two of which there are goats (which the contestant doesn’t want). Initially, door $i$ has probability $p_{i}$ of having the car, where $p_{1},p_{2},p_{3}$ are known constants such that $0&lt;p_{1}\leq p_{2}\leq p_{3}&lt;1$ and $p_{1}+p_{2}+p_{3}=1$. The contestant chooses a door. Then Monty opens a door (other than the one the contestant chose) and offers the contestant the option of switching to the other unopened door.

1. Assume for this part that Monty knows in advance which door has the car. He always opens a door to reveal a goat, and if he has a choice of which door to open he chooses with equal probabilities. Suppose for this part that the contestant initially chooses door 3, and then Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch doors? (If whether to switch depends on the $p_{i}$’s, give a fully simplified criterion in terms of the $p_{i}$’s.)

2. Now assume instead that Monty does *not* know in advance where the car is. He randomly chooses which door to open (other than the one the contestant chose), with equal probabilities. (The game is spoiled if he reveals the car.) Suppose again that the

Conditional probability

contestant initially chooses door 3, and then Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch doors? (If whether to switch depends on the $p_{i}$’s, give a fully simplified criterion in terms of the $p_{i}$’s.)

1. Repeat (a), except with the contestant initially choosing door 1 rather than door 3.
2. Repeat (b), except with the contestant initially choosing door 1 rather than door 3.
45. Monty Hall is trying out a new version of his game. In this version, instead of there always being 1 car and 2 goats, the prizes behind the doors are generated *independently*, with each door having probability $p$ of having a car and $q=1-p$ of having a goat. In detail: There are three doors, behind each of which there is one prize: either a car or a goat. For each door, there is probability $p$ that there is a car behind it and $q=1-p$ that there is a goat, independent of the other doors.

The contestant chooses a door. Monty, who knows the contents of each door, then opens one of the two remaining doors. In choosing which door to open, Monty will always reveal a goat if possible. If both of the remaining doors have the same kind of prize, Monty chooses randomly (with equal probabilities). After opening a door, Monty offers the contestant the option of switching to the other unopened door.

The contestant decides in advance to use the following strategy: first choose door 1. Then, after Monty opens a door, switch to the other unopened door.

1. Find the unconditional probability that the contestant will get a car.
2. Monty now opens door 2, revealing a goat. Given this information, find the conditional probability that the contestant will get a car.
46. Monty Hall is trying out a new version of his game, with rules as follows. The contestant gets to choose one of *four* doors. One door has a car behind it, another has an apple, another has a book, and another has a goat. All 24 permutations for which door has which prize are equally likely. In order from least preferred to most preferred, the contestant’s preferences are: goat, apple, book, car.

Monty, who knows which prize is behind each door, will open a door (other than the contestant’s initial choice) and then let the contestant choose whether to switch to another unopened door. Monty will reveal the least preferred prize (among the 3 doors other than the contestant’s initial choice) with probability $p$, the intermediately preferred prize with probability $1-p$, and the most preferred prize never.

The contestant decides in advance to use the following strategy: Initially choose door 1. After Monty opens a door, switch to one of the other two unopened doors, randomly choosing between them (with probability 1/2 each).

1. Find the unconditional probability that the contestant will get the car.

Hint: Condition on where the car is.

1. Find the unconditional probability that Monty will reveal the apple.

Hint: Condition on what is behind door 1.

1. Monty now opens a door, revealing the apple. Given this information, find the conditional probability that the contestant will get the car.
47. You are the contestant on Monty Hall’s game show. Hoping to double the excitement of the game, Monty will offer you *two* opportunities to switch to another door. Specifically, the new rules are as follows. There are *four* doors. Behind one door there is a car (which you want); behind the other three doors there are goats (which you don’t want). Initially, all possibilities are equally likely for where the car is. Monty knows where the car is, and when he has a choice of which door to open, he chooses with equal probabilities.

You choose a door, which for concreteness we assume is door 1. Monty opens a door

Introduction to Probability

(other than door 1), revealing a goat, and then offers you the option to switch to another door. Monty then opens *another* door (other than your currently selected door), revealing another goat. So now there are two open doors (with goats) and two unopened doors. Again Monty offers you the option to switch.

You decide in advance to use one of the following four strategies: stay-stay, stay-switch, switch-stay, switch-switch, where, for example, “stay-switch” means that the first time Monty offers you the choice of switching, you stay with your current selection, but then the second time Monty offers you the choice, you do switch doors. In each part below the goal is to find or compare *unconditional* probabilities, i.e., from a vantage point of before the game has started.

1. Find the probability of winning the car if you follow the stay-stay strategy.
2. Find the probability of winning the car if you follow the stay-switch strategy.
3. Find the probability of winning the car if you follow the switch-stay strategy.
4. Find the probability of winning the car if you follow the switch-switch strategy.
5. Which of these four strategies is the best?

### First-step analysis and gambler’s ruin

1. $\circledS$ A fair die is rolled repeatedly, and a running total is kept (which is, at each time, the total of all the rolls up until that time). Let $p_{n}$ be the probability that the running total is ever *exactly* $n$ (assume the die will always be rolled enough times so that the running total will eventually exceed $n$, but it may or may not ever equal $n$).

1. Write down a recursive equation for $p_{n}$ (relating $p_{n}$ to earlier terms $p_{k}$ in a simple way). Your equation should be true for all positive integers $n$, so give a definition of $p_{0}$ and $p_{k}$ for $k&lt;0$ so that the recursive equation is true for small values of $n$.
2. Find $p_{7}$.
3. Give an intuitive explanation for the fact that $p_{n}\to 1/3.5=2/7$ as $n\to\infty$.
2. A sequence of $n\geq 1$ independent trials is performed, where each trial ends in “success” or “failure” (but not both). Let $p_{i}$ be the probability of success in the $i$th trial, $q_{i}=1-p_{i}$, and $b_{i}=q_{i}-1/2$, for $i=1,2,\ldots,n$. Let $A_{n}$ be the event that the number of successful trials is even.

1. Show that for $n=2$, $P(A_{2})=1/2+2b_{1}b_{2}$.
2. Show by induction that

$P(A_{n})=1/2+2^{n-1}b_{1}b_{2}\ldots b_{n}.$

(This result is very useful in cryptography. Also, note that it implies that if $n$ coins are flipped, then the probability of an even number of Heads is $1/2$ if and only if at least one of the coins is fair.) Hint: Group some trials into a supertrial.

1. Check directly that the result of (b) is true in the following simple cases: $p_{i}=1/2$ for some $i$; $p_{i}=0$ for all $i$; $p_{i}=1$ for all $i$.
3. Calvin and Hobbes play a match consisting of a series of games, where Calvin has probability $p$ of winning each game (independently). They play with a “win by two” rule: the first player to win two games more than his opponent wins the match. Find the probability that Calvin wins the match (in terms of $p$), in two different ways:

1. by conditioning, using the law of total probability.
2. by interpreting the problem as a gambler’s ruin problem.

Conditional probability

51.  A gambler repeatedly plays a game where in each round, he wins a dollar with probability $1/3$ and loses a dollar with probability $2/3$. His strategy is “quit when he is ahead by $2”. Suppose that he starts with a million dollars. Show that the probability that he’ll ever be ahead by $2 is less than $1/4$.

52. As in the gambler’s ruin problem, two gamblers, A and B, make a series of bets, until one of the gamblers goes bankrupt. Let A start out with $i$ dollars and B start out with $N - i$ dollars, and let $p$ be the probability of A winning a bet, with $0 &lt; p &lt; \frac{1}{2}$. Each bet is for $\frac{1}{k}$ dollars, with $k$ a positive integer, e.g., $k = 1$ is the original gambler’s ruin problem and $k = 20$ means they’re betting nickels. Find the probability that A wins the game, and determine what happens to this as $k \to \infty$.

53. There are 100 equally spaced points around a circle. At 99 of the points, there are sheep, and at 1 point, there is a wolf. At each time step, the wolf randomly moves either clockwise or counterclockwise by 1 point. If there is a sheep at that point, he eats it. The sheep don’t move. What is the probability that the sheep who is initially opposite the wolf is the last one remaining?

54. An immortal drunk man wanders around randomly on the integers. He starts at the origin, and at each step he moves 1 unit to the right or 1 unit to the left, with probabilities $p$ and $q = 1 - p$ respectively, independently of all his previous steps. Let $S_{n}$ be his position after $n$ steps.

(a) Let $p_k$ be the probability that the drunk ever reaches the value $k$, for all $k \geq 0$. Write down a difference equation for $p_k$ (you do not need to solve it for this part).

(b) Find $p_k$, fully simplified; be sure to consider all 3 cases: $p &lt; 1/2, p = 1/2$, and $p &gt; 1/2$. Feel free to assume that if $A_1, A_2, \ldots$ are events with $A_j \subseteq A_{j+1}$ for all $j$, then $P(A_n) \to P(\cup_{j=1}^{\infty} A_j)$ as $n \to \infty$ (because it is true; this is known as continuity of probability).

## Simpson’s paradox

55.  (a) Is it possible to have events $A, B, C$ such that $P(A|C) &lt; P(B|C)$ and $P(A|C^c) &lt; P(B|C^c)$, yet $P(A) &gt; P(B)$? That is, $A$ is less likely than $B$ given that $C$ is true, and also less likely than $B$ given that $C$ is false, yet $A$ is more likely than $B$ if we’re given no information about $C$. Show this is impossible (with a short proof) or find a counterexample (with a story interpreting $A, B, C$).

(b) If the scenario in (a) is possible, is it a special case of Simpson’s paradox, equivalent to Simpson’s paradox, or neither? If it is impossible, explain intuitively why it is impossible even though Simpson’s paradox is possible.

56.  $\odot$ Consider the following conversation from an episode of *The Simpsons*:

Lisa: Dad, I think he’s an ivory dealer! His boots are ivory, his hat is ivory, and I’m pretty sure that check is ivory.

Homer: Lisa, a guy who has lots of ivory is less likely to hurt Stampy than a guy whose ivory supplies are low.

Here Homer and Lisa are debating the question of whether or not the man (named Blackheart) is likely to hurt Stampy the Elephant if they sell Stampy to him. They clearly disagree about how to use their observations about Blackheart to learn about the probability (conditional on the evidence) that Blackheart will hurt Stampy.

(a) Define clear notation for the various events of interest here.

(b) Express Lisa’s and Homer’s arguments (Lisa’s is partly implicit) as conditional probability statements in terms of your notation from (a).

(c) Assume it is true that someone who has a lot of a commodity will have less desire to acquire more of the commodity. Explain what is wrong with Homer’s reasoning that the evidence about Blackheart makes it less likely that he will harm Stampy.
57. (a) There are two crimson jars (labeled $C_{1}$ and $C_{2}$) and two mauve jars (labeled $M_{1}$ and $M_{2}$). Each jar contains a mixture of green gummi bears and red gummi bears. Show by example that it is possible that $C_{1}$ has a much higher percentage of green gummi bears than $M_{1}$, and $C_{2}$ has a much higher percentage of green gummi bears than $M_{2}$, yet if the contents of $C_{1}$ and $C_{2}$ are merged into a new jar and likewise for $M_{1}$ and $M_{2}$, then the combination of $C_{1}$ and $C_{2}$ has a lower percentage of green gummi bears than the combination of $M_{1}$ and $M_{2}$.

(b) Explain how (a) relates to Simpson’s paradox, both intuitively and by explicitly defining events $A,B,C$ as in the statement of Simpson’s paradox.
58. As explained in this chapter, Simpson’s paradox says that it is possible to have events $A,B,C$ such that $P(A|B,C)<P(A|B^{c},C)$ and $P(A|B,C^{c})<P(A|B^{c},C^{c})$, yet $P(A|B)>P(A|B^{c})$.

(a) Can Simpson’s paradox occur if $A$ and $B$ are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible.

(b) Can Simpson’s paradox occur if $A$ and $C$ are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible.

(c) Can Simpson’s paradox occur if $B$ and $C$ are independent? If so, give a concrete example (with both numbers and an interpretation); if not, prove that it is impossible.
59. The book Red State, Blue State, Rich State, Poor State by Andrew Gelman *[12]* discusses the following election phenomenon: within any U.S. state, a wealthy voter is more likely to vote for a Republican than a poor voter, yet the wealthier states tend to favor Democratic candidates!

(a) Assume for simplicity that there are only 2 states (called Red and Blue), each of which has 100 people, and that each person is either rich or poor, and either a Democrat or a Republican. Make up numbers consistent with the above, showing how this phenomenon is possible, by giving a $2\times 2$ table for each state (listing how many people in each state are rich Democrats, etc.). So within each state, a rich voter is more likely to vote for a Republican than a poor voter, but the percentage of Democrats is higher in the state with the higher percentage of rich people than in the state with the lower percentage of rich people.

(b) In the setup of (a) (not necessarily with the numbers you made up there), let $D$ be the event that a randomly chosen person is a Democrat (with all 200 people equally likely), and $B$ be the event that the person lives in the Blue State. Suppose that 10 people move from the Blue State to the Red State. Write $P_{\rm old}$ and $P_{\rm new}$ for probabilities before and after they move. Assume that people do not change parties, so we have $P_{\rm new}(D)=P_{\rm old}(D)$. Is it possible that both $P_{\rm new}(D|B)>P_{\rm old}(D|B)$ and $P_{\rm new}(D|B^{c})>P_{\rm old}(D|B^{c})$ are true? If so, explain how it is possible and why it does not contradict the law of total probability $P(D)=P(D|B)P(B)+P(D|B^{c})P(B^{c})$; if not, show that it is impossible.

### Mixed practice

60. A patient is being given a blood test for the disease conditionitis. Let $p$ be the prior probability that the patient has conditionitis. The blood sample is sent to one of two labs for analysis, lab A or lab B. The choice of which lab to use is made randomly, independent of the patient’s disease status, with probability 1/2 for each lab.

Conditional probability

For lab A, the probability of someone testing *positive* given that they *do* have the disease is $a_{1}$, and the probability of someone testing *negative* given that they do *not* have the disease is $a_{2}$. The corresponding probabilities for lab B are $b_{1}$ and $b_{2}$.

1. Find the probability that the patient has the disease, given that they tested positive.

2. Find the probability that the patient’s blood sample was analyzed by lab A, given that the patient tested positive.
6. Fred decides to take a series of $n$ tests, to diagnose whether he has a certain disease (any individual test is not perfectly reliable, so he hopes to reduce his uncertainty by taking multiple tests). Let $D$ be the event that he has the disease, $p=P(D)$ be the prior probability that he has the disease, and $q=1-p$. Let $T_{j}$ be the event that he tests positive on the $j$th test.

1. Assume for this part that the test results are conditionally independent given Fred’s disease status. Let $a=P(T_{j}|D)$ and $b=P(T_{j}|D^{c})$, where $a$ and $b$ don’t depend on $j$. Find the posterior probability that Fred has the disease, given that he tests positive on all $n$ of the $n$ tests.

2. Suppose that Fred tests positive on all $n$ tests. However, some people have a certain gene that makes them *always* test positive. Let $G$ be the event that Fred has the gene. Assume that $P(G)=1/2$ and that $D$ and $G$ are independent. If Fred does *not* have the gene, then the test results are conditionally independent given his disease status. Let $a_{0}=P(T_{j}|D,G^{c})$ and $b_{0}=P(T_{j}|D^{c},G^{c})$, where $a_{0}$ and $b_{0}$ don’t depend on $j$. Find the posterior probability that Fred has the disease, given that he tests positive on all $n$ of the tests.
6. A certain hereditary disease can be passed from a mother to her children. Given that the mother has the disease, her children independently will have it with probability $1/2$. Given that she doesn’t have the disease, her children won’t have it either. A certain mother, who has probability $1/3$ of having the disease, has two children.

1. Find the probability that neither child has the disease.

2. Is whether the elder child has the disease independent of whether the younger child has the disease? Explain.

3. The elder child is found not to have the disease. A week later, the younger child is also found not to have the disease. Given this information, find the probability that the mother has the disease.
6. Three fair coins are tossed at the same time. Explain what is wrong with the following argument: “there is a 50% chance that the three coins all landed the same way, since obviously it is possible to find two coins that match, and then the other coin has a 50% chance of matching those two”.
6. An urn contains red, green, and blue balls. Let $r,g,b$ be the proportions of red, green, blue balls, respectively ($r+g+b=1$).

1. Balls are drawn randomly *with replacement*. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn.

Hint: Explain how this relates to finding the probability that a draw is green, given that it is either green or blue.

2. Balls are drawn randomly *without replacement*. Find the probability that the first time a green ball is drawn is before the first time a blue ball is drawn. Is the answer the same or different than the answer in (a)?

Hint: Imagine the balls all lined up, in the order in which they will be drawn. Note that where the red balls are standing in this line is irrelevant.

(c) Generalize the result from (a) to the following setting. Independent trials are performed, and the outcome of each trial is classified as being exactly one of type 1, type 2, …, or type $n$, with probabilities $p_{1},p_{2},\ldots,p_{n}$, respectively. Find the probability that the first trial to result in type $i$ comes before the first trial to result in type $j$, for $i\neq j$.
65. Marilyn vos Savant was asked the following question for her column in *Parade*:

> You’re at a party with 199 other guests when robbers break in and announce that they are going to rob one of you. They put 199 blank pieces of paper in a hat, plus one marked “you lose.” Each guest must draw, and the person who draws “you lose” will get robbed. The robbers offer you the option of drawing first, last, or at any time in between. When would you take your turn?

The draws are made *without replacement*, and for (a) are uniformly random.

1. Determine whether it is optimal to draw first, last, or somewhere in between (or whether it does not matter), to maximize the probability of not being robbed. Give a clear, concise, and compelling explanation.
2. More generally, suppose that there is one “you lose” piece of paper, with “weight” $v$, and there are $n$ blank pieces of paper, each with “weight” $w$. At each stage, draws are made with probability proportional to weight, i.e., the probability of drawing a particular piece of paper is its weight divided by the sum of the weights of all the remaining pieces of paper. Determine whether it is better to draw first or second (or whether it does not matter); here $v>0,w>0$, and $n\geq 1$ are known constants.
66. A fair die is rolled repeatedly, until the running total is at least 100 (at which point the rolling stops). Find the most likely value of the final running total (i.e., the value of the running total at the first time when it is at least 100).

Hint: Consider the possibilities for what the running total is just before the last roll.
67. Homer has a box of donuts, which currently contains exactly $c$ chocolate, $g$ glazed, and $j$ jelly donuts. Homer eats donuts one after another, each time choosing uniformly at random from the remaining donuts.

1. Find the probability that the last donut remaining in the box is a chocolate donut.
2. Find the probability of the following event: glazed is the first type of donut that Homer runs out of, and then jelly is the second type of donut that he runs out of.

Hint: Consider the last donut remaining, and the last donut that is either glazed or jelly.
68. Let $D$ be the event that a person develops a certain disease, and $C$ be the event that the person was exposed to a certain substance (e.g., $D$ may correspond to lung cancer and $C$ may correspond to smoking cigarettes). We are interested in whether exposure to the substance is related to developing the disease (and if so, how they are related).

The *odds ratio* is a very widely used measure in epidemiology of the association between disease and exposure, defined as

$\mathrm{OR}=\frac{\mathrm{odds}(D|C)}{\mathrm{odds}(D|C^{c})},$

where conditional odds are defined analogously to unconditional odds: $\mathrm{odds}(A|B)=\frac{P(A|B)}{P(A^{c}|B)}$. The *relative risk* of the disease for someone exposed to the substance, another widely used measure, is

$\mathrm{RR}=\frac{P(D|C)}{P(D|C^{c})}.$

The relative risk is especially easy to interpret, e.g., $\mathrm{RR}=2$ says that someone exposed to the substance is twice as likely to develop the disease as someone who isn’t exposed (though this does not necessarily mean that the substance *causes* the increased chance of getting the disease, nor is there necessarily a causal interpretation for the odds ratio).

Conditional probability

(a) Show that if the disease is rare, both for exposed people and for unexposed people, then the relative risk is approximately equal to the odds ratio.

(b) Let $p_{ij}$ for $i = 0,1$ and $j = 0,1$ be the probabilities in the following $2 \times 2$ table.

|   | D | D^{c}  |
| --- | --- | --- |
|  C | p_{11} | p_{10}  |
|  C^{c} | p_{01} | p_{00}  |

For example, $p_{10} = P(C, D^c)$. Show that the odds ratio can be expressed as a cross-product ratio, in the sense that

$$
\mathrm{OR} = \frac{p_{11} p_{00}}{p_{10} p_{01}}.
$$

(c) Show that the odds ratio has the neat symmetry property that the roles of $C$ and $D$ can be swapped without changing the value:

$$
\mathrm{OR} = \frac{\mathrm{odds}(C|D)}{\mathrm{odds}(C|D^c)}.
$$

This property is one of the main reasons why the odds ratio is so widely used, since it turns out that it allows the odds ratio to be estimated in a wide variety of problems where relative risk would be hard to estimate well.

69. A researcher wants to estimate the percentage of people in some population who have used illegal drugs, by conducting a survey. Concerned that a lot of people would lie when asked a sensitive question like “Have you ever used illegal drugs?”, the researcher uses a method known as randomized response. A hat is filled with slips of paper, each of which says either “I have used illegal drugs” or “I have not used illegal drugs”. Let $p$ be the proportion of slips of paper that say “I have used illegal drugs” ($p$ is chosen by the researcher in advance).

Each participant chooses a random slip of paper from the hat and answers (truthfully) “yes” or “no” to whether the statement on that slip is true. The slip is then returned to the hat. The researcher does not know which type of slip the participant had. Let $y$ be the probability that a participant will say “yes”, and $d$ be the probability that a participant has used illegal drugs.

(a) Find $y$, in terms of $d$ and $p$.

(b) What would be the worst possible choice of $p$ that the researcher could make in designing the survey? Explain.

(c) Now consider the following alternative system. Suppose that proportion $p$ of the slips of paper say “I have used illegal drugs”, but that now the remaining $1 - p$ say “I was born in winter” rather than “I have not used illegal drugs”. Assume that $1/4$ of people are born in winter, and that a person’s season of birth is independent of whether they have used illegal drugs. Find $d$, in terms of $y$ and $p$.

70. At the beginning of the play Rosencrantz and Guildenstern Are Dead by Tom Stoppard [25], Guildenstern is spinning coins and Rosencrantz is betting on the outcome for each. The coins have been landing Heads over and over again, prompting the following remark:

Guildenstern: A weaker man might be moved to re-examine his faith, if in nothing else at least in the law of probability.

The coin spins have resulted in Heads 92 times in a row.

(a) Fred and his friend are watching the play. Upon seeing the events described above, they have the following conversation:

Fred: That outcome would be incredibly unlikely with fair coins. They must be using trick coins (maybe with double-headed coins), or the experiment must have been rigged somehow (maybe with magnets).

Fred’s friend: It’s true that the string HH…H of length 92 is very unlikely; the chance is $1/2^{92}\approx 2\times 10^{-28}$ with fair coins. But any other specific string of H’s and T’s with length 92 has exactly the same probability! The reason the outcome seems extremely unlikely is that the number of possible outcomes grows exponentially as the number of spins grows, so any outcome would seem extremely unlikely. You could just as well have made the same argument even without looking at the results of their experiment, which means you really don’t have evidence against the coins being fair.

Discuss these comments, to help Fred and his friend resolve their debate.

(b) Suppose there are only two possibilities: either the coins are all fair (and spun fairly), or double-headed coins are being used (in which case the probability of Heads is 1). Let $p$ be the prior probability that the coins are fair. Find the posterior probability that the coins are fair, given that they landed Heads in 92 out of 92 trials.

(c) Continuing from (b), for which values of $p$ is the posterior probability that the coins are fair greater than 0.5? For which values of $p$ is it less than 0.05?
71. There are $n$ types of toys, which you are collecting one by one. Each time you buy a toy, it is randomly determined which type it has, with equal probabilities. Let $p_{ij}$ be the probability that just after you have bought your $i$th toy, you have exactly $j$ toy types in your collection, for $i\geq 1$ and $0\leq j\leq n$. (This problem is in the setting of the coupon collector problem, a famous problem which we study in Example 4.3.12.)

(a) Find a recursive equation expressing $p_{ij}$ in terms of $p_{i-1,j}$ and $p_{i-1,j-1}$, for $i\geq 2$ and $1\leq j\leq n$.

(b) Describe how the recursion from (a) can be used to calculate $p_{ij}$.
72. A/B testing is a form of randomized experiment that is used by many companies to learn about how customers will react to different treatments. For example, a company may want to see how users will respond to a new feature on their website (compared with how users respond to the current version of the website) or compare two different advertisements.

As the name suggests, two different treatments, Treatment A and Treatment B, are being studied. Users arrive one by one, and upon arrival are randomly assigned to one of the two treatments. The trial for each user is classified as “success” (e.g., the user made a purchase) or “failure”. The probability that the $n$th user receives Treatment A is allowed to depend on the outcomes for the previous users. This set-up is known as a two-armed bandit.

Many algorithms for how to randomize the treatment assignments have been studied. Here is an especially simple (but fickle) algorithm, called a stay-with-a-winner procedure:

1. Randomly assign the first user to Treatment A or Treatment B, with equal probabilities.
2. If the trial for the $n$th user is a success, stay with the same treatment for the $(n+1)$st user; otherwise, switch to the other treatment for the $(n+1)$st user.

Let $a$ be the probability of success for Treatment A, and $b$ be the probability of success for Treatment B. Assume that $a\neq b$, but that $a$ and $b$ are unknown (which is why the test is needed). Let $p_{n}$ be the probability of success on the $n$th trial and $a_{n}$ be the probability that Treatment A is assigned on the $n$th trial (using the above algorithm).

(a) Show that

$p_{n}$ $=(a-b)a_{n}+b,$
$a_{n+1}$ $=(a+b-1)a_{n}+1-b.$

(b) Use the results from (a) to show that $p_{n+1}$ satisfies the following recursive equation:

$p_{n+1}=(a+b-1)p_{n}+a+b-2ab.$

(c) Use the result from (b) to find the long-run probability of success for this algorithm, $\lim_{n\to\infty}p_{n}$, assuming that this limit exists.
73. In humans (and many other organisms), genes come in pairs. A certain gene comes in two types (alleles): type $a$ and type $A$. The genotype of a person for that gene is the types of the two genes in the pair: $AA,Aa$, or $aa$ ($aA$ is equivalent to $Aa$). Assume that the Hardy-Weinberg law applies here, which means that the frequencies of $AA,Aa,aa$ in the population are $p^{2},2p(1-p),(1-p)^{2}$ respectively, for some $p$ with $0<p<1$.

When a woman and a man have a child, the child’s gene pair has one gene contributed by each parent. Suppose that the mother is equally likely to contribute either of the two genes in her gene pair, and likewise for the father, independently. Also suppose that the genotypes of the parents are independent of each other (with probabilities given by the Hardy-Weinberg law).

(a) Find the probabilities of each possible genotype $(AA,Aa,aa)$ for a child of two random parents. Explain what this says about stability of the Hardy-Weinberg law from one generation to the next.

Hint: Condition on the genotypes of the parents.

(b) A person of type $AA$ or $aa$ is called homozygous (for the gene under consideration), and a person of type $Aa$ is called heterozygous (for that gene). Find the probability that a child is homozygous, given that both parents are homozygous. Also, find the probability that a child is heterozygous, given that both parents are heterozygous.

(c) Suppose that having genotype $aa$ results in a distinctive physical characteristic, so it is easy to tell by looking at someone whether or not they have that genotype. A mother and father, neither of whom are of type $aa$, have a child. The child is also not of type $aa$. Given this information, find the probability that the child is heterozygous.

Hint: Use the definition of conditional probability. Then expand both the numerator and the denominator using LOTP, conditioning on the genotypes of the parents.
74. A standard deck of cards will be shuffled and then the cards will be turned over one at a time until the first ace is revealed. Let $B$ be the event that the next card in the deck will also be an ace.

(a) Intuitively, how do you think $P(B)$ compares in size with $1/13$ (the overall proportion of aces in a deck of cards)? Explain your intuition. (Give an intuitive discussion rather than a mathematical calculation; the goal here is to describe your intuition explicitly.)

(b) Let $C_{j}$ be the event that the first ace is at position $j$ in the deck. Find $P(B|C_{j})$ in terms of $j$, fully simplified.

(c) Using the law of total probability, find an expression for $P(B)$ as a sum. (The sum can be left unsimplified, but it should be something that could easily be computed in software such as R that can calculate sums.)

(d) Find a fully simplified expression for $P(B)$ using a symmetry argument.

Hint: If you were deciding whether to bet on the next card after the first ace being an ace or to bet on the last card in the deck being an ace, would you have a preference?

![img-32.jpeg](img-32.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

Random variables and their distributions

In this chapter, we introduce *random variables*, an incredibly useful concept that simplifies notation and expands our ability to quantify uncertainty and summarize the results of experiments. Random variables are essential throughout the rest of this book, and throughout statistics, so it is crucial to think through what they mean, both intuitively and mathematically.

### 3.1 Random variables

To see why our current notation can quickly become unwieldy, consider again the gambler’s ruin problem from Chapter 2. In this problem, we may be very interested in how much wealth each gambler has at any particular time. So we could make up notation like letting $A_{jk}$ be the event that gambler A has exactly $j$ dollars after $k$ rounds, and similarly defining an event $B_{jk}$ for gambler B, for all $j$ and $k$.

This is already too complicated. Furthermore, we may also be interested in other quantities, such as the difference in their wealths (gambler A’s minus gambler B’s) after $k$ rounds, or the duration of the game (the number of rounds until one player is bankrupt). Expressing the event “the duration of the game is $r$ rounds” in terms of the $A_{jk}$ and $B_{jk}$ would involve a long, awkward string of unions and intersections. And then what if we want to express gambler A’s wealth as the equivalent amount in euros rather than dollars? We can multiply a *number* in dollars by a currency exchange rate, but we can’t multiply an *event* by an exchange rate.

Instead of having convoluted notation that obscures how the quantities of interest are related, wouldn’t it be nice if we could say something like the following?

> Let $X_{k}$ be the wealth of gambler A after $k$ rounds. Then $Y_{k}=N-X_{k}$ is the wealth of gambler B after $k$ rounds (where $N$ is the fixed total wealth); $X_{k}-Y_{k}=2X_{k}-N$ is the difference in wealths after $k$ rounds; $c_{k}X_{k}$ is the wealth of gambler A in euros after $k$ rounds, where $c_{k}$ is the euros per dollar exchange rate after $k$ rounds; and the duration is $R=\min\{n:X_{n}=0\text{ or }Y_{n}=0\}$.

The notion of a random variable will allow us to do exactly this! It needs to be introduced carefully though, to make it both conceptually and technically correct. Sometimes a definition of “random variable” is given that is a barely paraphrased

Introduction to Probability

version of "a random variable is a variable that takes on random values", but such a feeble attempt at a definition fails to say where the randomness come from. Nor does it help us to derive properties of random variables: we're familiar with working with algebraic equations like  $x^{2} + y^{2} = 1$ , but what are the valid mathematical operations if  $x$  and  $y$  are random variables? To make the notion of random variable precise, we define it as a function mapping the sample space to the real line. (See the math appendix for review of some concepts about functions.)

![img-33.jpeg](img-33.jpeg)

# FIGURE 3.1

A random variable maps the sample space into the real line. The r.v.  $X$  depicted here is defined on a sample space with 6 elements, and has possible values 0, 1, and 4. The randomness comes from choosing a random pebble according to the probability function  $P$  for the sample space.

Definition 3.1.1 (Random variable). Given an experiment with sample space  $S$ , a random variable (r.v.) is a function from the sample space  $S$  to the real numbers  $\mathbb{R}$ . It is common, but not required, to denote random variables by capital letters.

Thus, a random variable  $X$  assigns a numerical value  $X(s)$  to each possible outcome  $s$  of the experiment. The randomness comes from the fact that we have a random experiment (with probabilities described by the probability function  $P$ ); the mapping itself is deterministic, as illustrated in Figure 3.1. The same r.v. is shown in a simpler way in the left panel of Figure 3.2, in which we inscribe the values inside the pebbles.

This definition is abstract but fundamental; one of the most important skills to develop when studying probability and statistics is the ability to go back and forth between abstract ideas and concrete examples. Relatedly, it is important to work on recognizing the essential pattern or structure of a problem and how it connects

to problems you have studied previously. We will often discuss stories that involve tossing coins or drawing balls from urns because they are simple, convenient scenarios to work with, but many other problems are *isomorphic*: they have the same essential structure, but in a different guise.

To start, let’s consider a coin-tossing example. The structure of the problem is that we have a sequence of trials where there are two possible outcomes for each trial. Here we think of the possible outcomes as $H$ (Heads) and $T$ (Tails), but we could just as well think of them as “success” and “failure” or as 1 and 0, for example.

###### Example 3.1.2 (Coin tosses).

Consider an experiment where we toss a fair coin twice. The sample space consists of four possible outcomes: $S=\{HH,HT,TH,TT\}$. Here are some random variables on this space (for practice, you can think up some of your own). Each r.v. is a numerical summary of some aspect of the experiment.

- Let $X$ be the number of Heads. This is a random variable with possible values 0, 1, and 2. Viewed as a function, $X$ assigns the value 2 to the outcome $HH$, 1 to the outcomes $HT$ and $TH$, and 0 to the outcome $TT$. That is,

$X(HH)=2,X(HT)=X(TH)=1,X(TT)=0.$
- Let $Y$ be the number of Tails. In terms of $X$, we have $Y=2-X$. In other words, $Y$ and $2-X$ are the same r.v.: $Y(s)=2-X(s)$ for all $s$.
- Let $I$ be 1 if the first toss lands Heads and 0 otherwise. Then $I$ assigns the value 1 to the outcomes $HH$ and $HT$ and 0 to the outcomes $TH$ and $TT$. This r.v. is an example of what is called an *indicator random variable* since it indicates whether the first toss lands Heads, using 1 to mean “yes” and 0 to mean “no”.

We can also encode the sample space as $\{(1,1),(1,0),(0,1),(0,0)\}$, where 1 is the code for Heads and 0 is the code for Tails. Then we can give explicit formulas for $X,Y,I$:

$X(s_{1},s_{2})=s_{1}+s_{2},\ Y(s_{1},s_{2})=2-s_{1}-s_{2},\ I(s_{1},s_{2})=s_{1},$

where for simplicity we write $X(s_{1},s_{2})$ to mean $X((s_{1},s_{2}))$, etc.

For most r.v.s we will consider, it is tedious or infeasible to write down an explicit formula in this way. Fortunately, it is usually unnecessary to do so, since (as we saw in this example) there are other ways to define an r.v., and (as we will see throughout the rest of this book) there are many ways to study the properties of an r.v. other than by doing computations with an explicit formula for what it maps each outcome $s$ to. ∎

As in the previous chapters, for a sample space with a finite number of outcomes we can visualize the outcomes as pebbles, with the mass of a pebble corresponding to its probability, such that the total mass of the pebbles is 1. A random variable simply labels each pebble with a number. Figure 3.2 shows two random variables

Introduction to Probability

defined on the same sample space: the pebbles or outcomes are the same, but the real numbers assigned to the outcomes are different.

![img-34.jpeg](img-34.jpeg)
FIGURE 3.2

![img-35.jpeg](img-35.jpeg)

Two random variables defined on the same sample space.

As we've mentioned earlier, the source of the randomness in a random variable is the experiment itself, in which a sample outcome  $s \in S$  is chosen according to a probability function  $P$ . Before we perform the experiment, the outcome  $s$  has not yet been realized, so we don't know the value of  $X$ , though we could calculate the probability that  $X$  will take on a given value or range of values. After we perform the experiment and the outcome  $s$  has been realized, the random variable crystallizes into the numerical value  $X(s)$ .

Random variables provide numerical summaries of the experiment in question. This is very handy because the sample space of an experiment is often incredibly complicated or high-dimensional, and the outcomes  $s \in S$  may be non-numeric. For example, the experiment may be to collect a random sample of people in a certain city and ask them various questions, which may have numeric (e.g., age or height) or non-numeric (e.g., political party or favorite movie) answers. The fact that r.v.s take on numerical values is a very convenient simplification compared to having to work with the full complexity of  $S$  at all times.

# 3.2 Distributions and probability mass functions

There are two main types of random variables used in practice: discrete r.v.s and continuous r.v.s. In this chapter and the next, our focus is on discrete r.v.s. Continuous r.v.s are introduced in Chapter 5.

Definition 3.2.1 (Discrete random variable). A random variable  $X$  is said to be discrete if there is a finite list of values  $a_1, a_2, \ldots, a_n$  or an infinite list of values  $a_1, a_2, \ldots$  such that  $P(X = a_j \text{ for some } j) = 1$ . If  $X$  is a discrete r.v., then the

finite or countably infinite set of values $x$ such that $P(X=x)>0$ is called the *support* of $X$.

Most commonly in applications, the support of a discrete r.v. is a set of integers. In contrast, a *continuous* r.v. can take on any real value in an interval (possibly even the entire real line); such r.v.s are defined more precisely in 5. It is also possible to have an r.v. that is a hybrid of discrete and continuous, such as by flipping a coin and then generating a discrete r.v. if the coin lands Heads and generating a continuous r.v. if the coin lands Tails. But the starting point for understanding such r.v.s is to understand discrete and continuous r.v.s.

Given a random variable, we would like to be able to describe its behavior using the language of probability. For example, we might want to answer questions about the probability that the r.v. will fall into a given range: if $L$ is the lifetime earnings of a randomly chosen U.S. college graduate, what is the probability that $L$ exceeds a million dollars? If $M$ is the number of major earthquakes in California in the next five years, what is the probability that $M$ equals 0?

The *distribution* of a random variable provides the answers to these questions; it specifies the probabilities of all events associated with the r.v., such as the probability of it equaling 3 and the probability of it being at least 110. We will see that there are several equivalent ways to express the distribution of an r.v. For a discrete r.v., the most natural way to do so is with a *probability mass function*, which we now define.

###### Definition 3.2.2 (Probability mass function).

The *probability mass function* (PMF) of a discrete r.v. $X$ is the function $p_{X}$ given by $p_{X}(x)=P(X=x)$. Note that this is positive if $x$ is in the support of $X$, and 0 otherwise.

###### 3.2.3.

In writing $P(X=x)$, we are using $X=x$ to denote an *event*, consisting of all outcomes $s$ to which $X$ assigns the number $x$. This event is also written as $\{X=x\}$; formally, $\{X=x\}$ is defined as $\{s\in S:X(s)=x\}$, but writing $\{X=x\}$ is shorter and more intuitive. Going back to Example 3.1.2, if $X$ is the number of Heads in two fair coin tosses, then $\{X=1\}$ consists of the sample outcomes $HT$ and $TH$, which are the two outcomes to which $X$ assigns the number 1. Since $\{HT,TH\}$ is a subset of the sample space, it is an event. So it makes sense to talk about $P(X=1)$, or more generally, $P(X=x)$. If $\{X=x\}$ were anything other than an event, it would make no sense to calculate its probability! It does not make sense to write “$P(X)$”; we can only take the probability of an event, not of an r.v.

Let’s look at a few examples of PMFs.

###### Example 3.2.4 (Coin tosses continued).

In this example we’ll find the PMFs of all the random variables in Example 3.1.2, the example with two fair coin tosses. Here are the r.v.s we defined, along with their PMFs:

- $X$, the number of Heads. Since $X$ equals 0 if $TT$ occurs, 1 if $HT$ or $TH$ occurs,

Introduction to Probability

and 2 if  $HH$  occurs, the PMF of  $X$  is the function  $p_X$  given by

$$
p _ {X} (0) = P (X = 0) = 1 / 4,
$$

$$
p _ {X} (1) = P (X = 1) = 1 / 2,
$$

$$
p _ {X} (2) = P (X = 2) = 1 / 4,
$$

and  $p_X(x) = 0$  for all other values of  $x$ .

-  $Y = 2 - X$ , the number of Tails. Reasoning as above or using the fact that

$$
P (Y = y) = P (2 - X = y) = P (X = 2 - y) = p _ {X} (2 - y),
$$

the PMF of  $Y$  is

$$
p _ {Y} (0) = P (Y = 0) = 1 / 4,
$$

$$
p _ {Y} (1) = P (Y = 1) = 1 / 2,
$$

$$
p _ {Y} (2) = P (Y = 2) = 1 / 4,
$$

and  $p_{Y}(y) = 0$  for all other values of  $y$ .

Note that  $X$  and  $Y$  have the same PMF (that is,  $p_X$  and  $p_Y$  are the same function) even though  $X$  and  $Y$  are not the same r.v. (that is,  $X$  and  $Y$  are two different functions from  $\{HH, HT, TH, TT\}$  to the real line).

-  $I$ , the indicator of the first toss landing Heads. Since  $I$  equals 0 if  $TH$  or  $TT$  occurs and 1 if  $HH$  or  $HT$  occurs, the PMF of  $I$  is

$$
p _ {I} (0) = P (I = 0) = 1 / 2,
$$

$$
p _ {I} (1) = P (I = 1) = 1 / 2,
$$

and  $p_I(i) = 0$  for all other values of  $i$ .

![img-36.jpeg](img-36.jpeg)

![img-37.jpeg](img-37.jpeg)

![img-38.jpeg](img-38.jpeg)

# FIGURE 3.3

Left to right: PMFs of  $X$ ,  $Y$ , and  $I$ , with  $X$  the number of Heads in two fair coin tosses,  $Y$  the number of Tails, and  $I$  the indicator of Heads on the first toss.

The PMFs of  $X$ ,  $Y$ , and  $I$  are plotted in Figure 3.3. Vertical bars are drawn to make it easier to compare the heights of different points.

Random variables and their distributions

Example 3.2.5 (Sum of die rolls). We roll two fair 6-sided dice. Let  $T = X + Y$  be the total of the two rolls, where  $X$  and  $Y$  are the individual rolls. The sample space of this experiment has 36 equally likely outcomes:

$$
S = \{(1, 1), (1, 2), \dots , (6, 5), (6, 6) \}.
$$

For example, 7 of the 36 outcomes  $s$  are shown in the table below, along with the corresponding values of  $X, Y$ , and  $T$ . After the experiment is performed, we observe values for  $X$  and  $Y$ , and then the observed value of  $T$  is the sum of those values.

|  s | X | Y | X + Y  |
| --- | --- | --- | --- |
|  (1,2) | 1 | 2 | 3  |
|  (1,6) | 1 | 6 | 7  |
|  (2,5) | 2 | 5 | 7  |
|  (3,1) | 3 | 1 | 4  |
|  (4,3) | 4 | 3 | 7  |
|  (5,4) | 5 | 4 | 9  |
|  (6,6) | 6 | 6 | 12  |

Since the dice are fair, the PMF of  $X$  is

$$
P (X = j) = 1 / 6,
$$

for  $j = 1,2,\ldots ,6$  (and  $P(X = j) = 0$  otherwise); we say that  $X$  has a Discrete Uniform distribution on  $1,2,\ldots ,6$ . Similarly,  $Y$  is also Discrete Uniform on  $1,2,\ldots ,6$ .

Note that  $Y$  has the same distribution as  $X$  but is not the same random variable as  $X$ . In fact, we have

$$
P (X = Y) = 6 / 3 6 = 1 / 6.
$$

Two more r.v.s in this experiment with the same distribution as  $X$  are  $7 - X$  and  $7 - Y$ . To see this, we can use the fact that for a standard die,  $7 - X$  is the value on the bottom if  $X$  is the value on the top. If the top value is equally likely to be any of the numbers  $1, 2, \ldots, 6$ , then so is the bottom value. Note that even though  $7 - X$  has the same distribution as  $X$ , it is never equal to  $X$  in a run of the experiment!

Let's now find the PMF of  $T$ . By the naive definition of probability,

$$
P (T = 2) = P (T = 1 2) = 1 / 3 6,
$$

$$
P (T = 3) = P (T = 1 1) = 2 / 3 6,
$$

$$
P (T = 4) = P (T = 1 0) = 3 / 3 6,
$$

$$
P (T = 5) = P (T = 9) = 4 / 3 6,
$$

$$
P (T = 6) = P (T = 8) = 5 / 3 6,
$$

$$
P (T = 7) = 6 / 3 6.
$$

For all other values of  $t$ ,  $P(T = t) = 0$ . We can see directly that the support of  $T$

Introduction to Probability

is  $\{2,3,\ldots ,12\}$  just by looking at the possible totals for two dice, but as a check, note that

$$
P (T = 2) + P (T = 3) + \dots + P (T = 1 2) = 1,
$$

which shows that all possibilities have been accounted for. The symmetry property of  $T$  that appears above,  $P(T = t) = P(T = 14 - t)$ , makes sense since each outcome  $\{X = x, Y = y\}$  which makes  $T = t$  has a corresponding outcome  $\{X = 7 - x, Y = 7 - y\}$  of the same probability which makes  $T = 14 - t$ .

![img-39.jpeg](img-39.jpeg)
FIGURE 3.4 PMF of the sum of two die rolls.

The PMF of  $T$  is plotted in Figure 3.4; it has a triangular shape, and the symmetry noted above is very visible.

Example 3.2.6 (Children in a U.S. household). Suppose we choose a household in the United States at random. Let  $X$  be the number of children in the chosen household. Since  $X$  can only take on integer values, it is a discrete r.v. The probability that  $X$  takes on the value  $x$  is proportional to the number of households in the United States with  $x$  children.

Using data from the 2010 General Social Survey [23], we can approximate the proportion of households with 0 children, 1 child, 2 children, etc., and hence approximate the PMF of  $X$ , which is plotted in Figure 3.5.

We will now state the properties of a valid PMF.

Theorem 3.2.7 (Valid PMFs). Let  $X$  be a discrete r.v. with support  $x_{1}, x_{2}, \ldots$  (assume these values are distinct and, for notational simplicity, that the support is countably infinite; the analogous results hold if the support is finite). The PMF  $p_{X}$  of  $X$  must satisfy the following two criteria:

- Nonnegative:  $p_X(x) &gt; 0$  if  $x = x_j$  for some  $j$ , and  $p_X(x) = 0$  otherwise;
- Sums to 1:  $\sum_{j=1}^{\infty} p_X(x_j) = 1$ .

Random variables and their distributions

![img-40.jpeg](img-40.jpeg)
FIGURE 3.5 PMF of the number of children in a randomly selected U.S. household.

Proof. The first criterion is true since probability is nonnegative. The second is true since  $X$  must take on some value, and the events  $\{X = x_{j}\}$  are disjoint, so

$$
\sum_ {j = 1} ^ {\infty} P (X = x _ {j}) = P \left(\bigcup_ {j = 1} ^ {\infty} \{X = x _ {j} \}\right) = P (X = x _ {1} \text {o r} X = x _ {2} \text {o r} \dots) = 1.
$$

Conversely, if distinct values  $x_{1}, x_{2}, \ldots$  are specified and we have a function satisfying the two criteria above, then this function is the PMF of some r.v.; we will show how to construct such an r.v. in Chapter 5.

We claimed earlier that the PMF is one way of expressing the distribution of a discrete r.v. This is because once we know the PMF of  $X$ , we can calculate the probability that  $X$  will fall into a given subset of the real numbers by summing over the appropriate values of  $x$ , as the next example shows.

Example 3.2.8. Returning to Example 3.2.5, let  $T$  be the sum of two fair die rolls. We have already calculated the PMF of  $T$ . Now suppose we're interested in the probability that  $T$  is in the interval [1, 4]. There are only three values in the interval [1, 4] that  $T$  can take on, namely, 2, 3, and 4. We know the probability of each of these values from the PMF of  $T$ , so

$$
P (1 \leq T \leq 4) = P (T = 2) + P (T = 3) + P (T = 4) = 6 / 3 6.
$$

In general, given a discrete r.v.  $X$  and a set  $B$  of real numbers, if we know the PMF of  $X$  we can find  $P(X \in B)$ , the probability that  $X$  is in  $B$ , by summing up the heights of the vertical bars at points in  $B$  in the plot of the PMF of  $X$ . Knowing the PMF of a discrete r.v. determines its distribution.

3.3 Bernoulli and Binomial

Some distributions are so ubiquitous in probability and statistics that they have their own names. We will introduce these *named distributions* throughout the book, starting with a very simple but useful case: an r.v. that can take on only two possible values, 0 and 1.

###### Definition 3.3.1 (Bernoulli distribution).

An r.v. $X$ is said to have the *Bernoulli distribution* with parameter $p$ if $P(X=1)=p$ and $P(X=0)=1-p$, where $0<p<1$. We write this as $X\sim\text{Bern}(p)$. The symbol $\sim$ is read “is distributed as”.

*Any* r.v. whose possible values are 0 and 1 has a $\text{Bern}(p)$ distribution, with $p$ the probability of the r.v. equaling 1. This number $p$ in $\text{Bern}(p)$ is called the *parameter* of the distribution; it determines which specific Bernoulli distribution we have. Thus there is not just one Bernoulli distribution, but rather a *family* of Bernoulli distributions, indexed by $p$. For example, if $X\sim\text{Bern}(1/3)$, it would be correct but incomplete to say “$X$ is Bernoulli”; to fully specify the distribution of $X$, we should both say its name (Bernoulli) and its parameter value (1/3), which is the point of the notation $X\sim\text{Bern}(1/3)$.

*Any* event has a Bernoulli r.v. that is naturally associated with it, equal to 1 if the event happens and 0 otherwise. This is called the *indicator random variable* of the event; we will see that such r.v.s are extremely useful.

###### Definition 3.3.2 (Indicator random variable).

The *indicator random variable* of an event $A$ is the r.v. which equals 1 if $A$ occurs and 0 otherwise. We will denote the indicator r.v. of $A$ by $I_{A}$ or $I(A)$. Note that $I_{A}\sim\text{Bern}(p)$ with $p=P(A)$.

We often imagine Bernoulli r.v.s using coin tosses, but this is just convenient language for discussing the following general story.

###### Story 3.3.3 (Bernoulli trial).

An experiment that can result in either a “success” or a “failure” (but not both) is called a *Bernoulli trial*. A Bernoulli random variable can be thought of as the *indicator of success* in a Bernoulli trial: it equals 1 if success occurs and 0 if failure occurs in the trial. ∎

Because of this story, the parameter $p$ is often called the *success probability* of the $\text{Bern}(p)$ distribution. Once we start thinking about Bernoulli trials, it’s hard not to start thinking about what happens when we have more than one trial.

###### Story 3.3.4 (Binomial distribution).

Suppose that $n$ *independent* Bernoulli trials are performed, each with the same success probability $p$. Let $X$ be the number of successes. The distribution of $X$ is called the *Binomial distribution* with parameters $n$ and $p$. We write $X\sim\text{Bin}(n,p)$ to mean that $X$ has the Binomial distribution with parameters $n$ and $p$, where $n$ is a positive integer and $0<p<1$. ∎

Notice that we define the Binomial distribution not by its PMF, but by a *story

about the type of experiment that could give rise to a random variable with a Binomial distribution. The most famous distributions in statistics all have stories which explain why they are so often used as models for data, or as the building blocks for more complicated distributions.

Thinking about the named distributions first and foremost in terms of their stories has many benefits. It facilitates pattern recognition, allowing us to see when two problems are essentially identical in structure; it often leads to cleaner solutions that avoid PMF calculations altogether; and it helps us understand how the named distributions are connected to one another. Here it is clear that $\mathrm{Bern}(p)$ is the same distribution as $\mathrm{Bin}(1,p)$: the Bernoulli is a special case of the Binomial.

Using the story definition of the Binomial, let’s find its PMF.

###### Theorem 3.3.5 (Binomial PMF).

If $X\sim\mathrm{Bin}(n,p)$, then the PMF of $X$ is

$P(X=k)={n\choose k}p^{k}(1-p)^{n-k}$

for $k=0,1,\ldots,n$ (and $P(X=k)=0$ otherwise).

$\nLeftrightarrow$ 3.3.6. To save writing, it is often left implicit that a PMF is zero wherever it is not specified to be nonzero, but in any case it is important to understand what the support of a random variable is, and good practice to check that PMFs are valid. If two discrete r.v.s have the same PMF, then they also must have the same support. So we sometimes refer to the support of a discrete distribution; this is the support of any r.v. with that distribution.

###### Proof.

An experiment consisting of $n$ independent Bernoulli trials produces a sequence of successes and failures. The probability of any specific sequence of $k$ successes and $n-k$ failures is $p^{k}(1-p)^{n-k}$. There are ${n\choose k}$ such sequences, since we just need to select where the successes are. Therefore, letting $X$ be the number of successes,

$P(X=k)={n\choose k}p^{k}(1-p)^{n-k}$

for $k=0,1,\ldots,n$, and $P(X=k)=0$ otherwise. This is a valid PMF because it is nonnegative and it sums to $1$ by the binomial theorem. ∎

Figure 3.6 shows plots of the Binomial PMF for various values of $n$ and $p$. Note that the PMF of the $\mathrm{Bin}(10,1/2)$ distribution is symmetric about $5$, but when the success probability is not $1/2$, the PMF is skewed. For a fixed number of trials $n$, $X$ tends to be larger when the success probability is high and lower when the success probability is low, as we would expect from the story of the Binomial distribution. Also recall that in any PMF plot, the sum of the heights of the vertical bars must be $1$.

We’ve used Story 3.3.4 to find the $\mathrm{Bin}(n,p)$ PMF. The story also gives us a straightforward proof of the fact that if $X$ is Binomial, then $n-X$ is also Binomial.

Introduction to Probability

![img-41.jpeg](img-41.jpeg)

![img-42.jpeg](img-42.jpeg)

![img-43.jpeg](img-43.jpeg)
FIGURE 3.6 Some Binomial PMFs. In the lower left, we plot the  $\mathrm{Bin}(100,0.03)$  PMF between 0 and 10 only, as the probability of more than 10 successes is close to 0.

![img-44.jpeg](img-44.jpeg)

###### Theorem 3.3.7.

Let $X\sim\mathrm{Bin}(n,p)$, and $q=1-p$ (we often use $q$ to denote the failure probability of a Bernoulli trial). Then $n-X\sim\mathrm{Bin}(n,q)$.

###### Proof.

Using the story of the Binomial, interpret $X$ as the number of successes in $n$ independent Bernoulli trials. Then $n-X$ is the number of failures in those trials. Interchanging the roles of success and failure, we have $n-X\sim\mathrm{Bin}(n,q)$. Alternatively, we can check that $n-X$ has the $\mathrm{Bin}(n,q)$ PMF. Let $Y=n-X$. The PMF of $Y$ is

$P(Y=k)=P(X=n-k)={n\choose n-k}p^{n-k}q^{k}={n\choose k}q^{k}p^{n-k},$

for $k=0,1,\ldots,n$. ∎

###### Corollary 3.3.8.

Let $X\sim\mathrm{Bin}(n,p)$ with $p=1/2$ and $n$ even. Then the distribution of $X$ is symmetric about $n/2$, in the sense that $P(X=n/2+j)=P(X=n/2-j)$ for all nonnegative integers $j$.

###### Proof.

By Theorem 3.3.7, $n-X$ is also $\mathrm{Bin}(n,1/2)$, so

$P(X=k)=P(n-X=k)=P(X=n-k)$

for all nonnegative integers $k$. Letting $k=n/2+j$, the desired result follows. This explains why the $\mathrm{Bin}(10,1/2)$ PMF is symmetric about $5$ in Figure 3.6. ∎

###### Example 3.3.9 (Coin tosses continued).

Going back to Example 3.1.2, we now know that $X\sim\mathrm{Bin}(2,1/2)$, $Y\sim\mathrm{Bin}(2,1/2)$, and $I\sim\mathrm{Bern}(1/2)$. Consistent with Theorem 3.3.7, $X$ and $Y=2-X$ have the same distribution, and consistent with Corollary 3.3.8, the distribution of $X$ (and of $Y$) is symmetric about $1$. ∎

### 3.4 Hypergeometric

If we have an urn filled with $w$ white and $b$ black balls, then drawing $n$ balls out of the urn *with replacement* yields a $\mathrm{Bin}(n,w/(w+b))$ distribution for the number of white balls obtained in $n$ trials, since the draws are independent Bernoulli trials, each with probability $w/(w+b)$ of success. If we instead sample *without replacement*, as illustrated in Figure 3.7, then the number of white balls follows a *Hypergeometric distribution*.

###### Story 3.4.1 (Hypergeometric distribution).

Consider an urn with $w$ white balls and $b$ black balls. We draw $n$ balls out of the urn at random without replacement, such that all ${w+b\choose n}$ samples are equally likely. Let $X$ be the number of white balls in the sample. Then $X$ is said to have the *Hypergeometric distribution* with parameters $w$, $b$, and $n$; we denote this by $X\sim\mathrm{HGeom}(w,b,n)$. ∎

Introduction to Probability

![img-45.jpeg](img-45.jpeg)
FIGURE 3.7

Hypergeometric story. An urn contains  $w = 6$  white balls and  $b = 4$  black balls. We sample  $n = 5$  without replacement. The number  $X$  of white balls in the sample is Hypergeometric; here we observe  $X = 3$ .

As with the Binomial distribution, we can obtain the PMF of the Hypergeometric distribution from the story.

Theorem 3.4.2 (Hypergeometric PMF). If  $X \sim \mathrm{HGeom}(w, b, n)$ , then the PMF of  $X$  is

$$
P (X = k) = \frac {\binom {w} {k} \binom {b} {n - k}}{\binom {w + b} {n}},
$$

for integers  $k$  satisfying  $0 \leq k \leq w$  and  $0 \leq n - k \leq b$ , and  $P(X = k) = 0$  otherwise.

Proof. To get  $P(X = k)$ , we first count the number of possible ways to draw exactly  $k$  white balls and  $n - k$  black balls from the urn (without distinguishing between different orderings for getting the same set of balls). If  $k &gt; w$  or  $n - k &gt; b$ , then the draw is impossible. Otherwise, there are  $\binom{w}{k} \binom{b}{n-k}$  ways to draw  $k$  white and  $n - k$  black balls by the multiplication rule, and there are  $\binom{w+b}{n}$  total ways to draw  $n$  balls. Since all samples are equally likely, the naive definition of probability gives

$$
P (X = k) = \frac {\binom {w} {k} \binom {b} {n - k}}{\binom {w + b} {n}}
$$

for integers  $k$  satisfying  $0 \leq k \leq w$  and  $0 \leq n - k \leq b$ . This PMF is valid because the numerator, summed over all  $k$ , equals  $\binom{w + b}{n}$  by Vandermonde's identity (Example 1.5.3), so the PMF sums to 1.

The Hypergeometric distribution comes up in many scenarios which, on the surface, have little in common with white and black balls in an urn. The essential structure of the Hypergeometric story is that items in a population are classified using two sets of tags: in the urn story, each ball is either white or black (this is the first set of tags), and each ball is either sampled or not sampled (this is the second set of tags). Furthermore, at least one of these sets of tags is assigned completely at random (in the urn story, the balls are sampled randomly, with all sets of the correct size equally likely). Then  $X \sim \mathrm{HGeom}(w, b, n)$  represents the number of twice-tagged items: in the urn story, balls that are both white and sampled.

Random variables and their distributions

The next two examples show seemingly dissimilar scenarios that are nonetheless isomorphic to the urn story.

Example 3.4.3 (Elk capture-recapture). A forest has  $N$  elk. Today,  $m$  of the elk are captured, tagged, and released into the wild. At a later date,  $n$  elk are recaptured at random. Assume that the recaptured elk are equally likely to be any set of  $n$  of the elk, e.g., an elk that has been captured does not learn how to avoid being captured again.

By the story of the Hypergeometric, the number of tagged elk in the recaptured sample is  $\mathrm{HGeom}(m,N - m,n)$ . The  $m$  tagged elk in this story correspond to the white balls and the  $N - m$  untagged elk correspond to the black balls. Instead of sampling  $n$  balls from the urn, we recapture  $n$  elk from the forest.

Example 3.4.4 (Aces in a poker hand). In a five-card hand drawn at random from a well-shuffled standard deck, the number of aces in the hand has the HGeom(4, 48, 5) distribution, which can be seen by thinking of the aces as white balls and the non-aces as black balls. Using the Hypergeometric PMF, the probability that the hand has exactly three aces is

$$
\frac {\binom {4} {3} \binom {4 8} {2}}{\binom {5 2} {5}} \approx 0. 0 0 1 7.
$$

The following table summarizes how the above examples can be thought of in terms of two sets of tags. In each example, the r.v. of interest is the number of items falling into both the second and the fourth columns: white and sampled, tagged and recaptured, ace and in one's hand.

|  Story | First set of tags |   | Second set of tags  |   |
| --- | --- | --- | --- | --- |
|  urn | white | black | sampled | not sampled  |
|  elk | tagged | untagged | recaptured | not recaptured  |
|  cards | ace | not ace | in hand | not in hand  |

The next theorem describes a symmetry between two Hypergeometric distributions with different parameters; the proof follows from swapping the two sets of tags in the Hypergeometric story.

Theorem 3.4.5. The  $\mathrm{HGeom}(w,b,n)$  and  $\mathrm{HGeom}(n,w + b - n,w)$  distributions are identical. That is, if  $X\sim \mathrm{HGeom}(w,b,n)$  and  $Y\sim \mathrm{HGeom}(n,w + b - n,w)$ , then  $X$  and  $Y$  have the same distribution.

Proof. Using the story of the Hypergeometric, imagine an urn with  $w$  white balls,  $b$  black balls, and a sample of size  $n$  made without replacement. Let  $X \sim \mathrm{HGeom}(w, b, n)$  be the number of white balls in the sample, thinking of white/black as the first set of tags and sampled/not sampled as the second set of tags. Let  $Y \sim \mathrm{HGeom}(n, w + b - n, w)$  be the number of sampled balls among the white balls, thinking of sampled/not sampled as the first set of tags and white/black as

the second set of tags. Both $X$ and $Y$ count the number of white sampled balls, so they have the same distribution.

Alternatively, we can check algebraically that $X$ and $Y$ have the same PMF:

$P(X=k)=\frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}=\frac{w!b!n!(w+b-n)!}{k!(w+b)!(w-k)!(n-k)!(b-n+k)!},$
$P(Y=k)=\frac{\binom{n}{k}\binom{w+b-n}{w-k}}{\binom{w+b}{w}}=\frac{w!b!n!(w+b-n)!}{k!(w+b)!(w-k)!(n-k)!(b-n+k)!}.$

We prefer the story proof because it is less tedious and more memorable. $\blacksquare$

#### 3.4.6 (Binomial vs. Hypergeometric).

The Binomial and Hypergeometric distributions are often confused. Both are discrete distributions taking on integer values between $0$ and $n$ for some $n$, and both can be interpreted as the number of successes in $n$ Bernoulli trials (for the Hypergeometric, each tagged elk in the recaptured sample can be considered a success and each untagged elk a failure). However, a crucial part of the Binomial story is that the Bernoulli trials involved are independent. The Bernoulli trials in the Hypergeometric story are dependent, since the sampling is done without replacement: knowing that one elk in our sample is tagged decreases the probability that the second elk will also be tagged.

### 3.5 Discrete Uniform

A very simple story, closely connected to the naive definition of probability, describes picking a random number from some finite set of possibilities.

###### Story 3.5.1 (Discrete Uniform distribution).

Let $C$ be a finite, nonempty set of numbers. Choose one of these numbers uniformly at random (i.e., all values in $C$ are equally likely). Call the chosen number $X$. Then $X$ is said to have the Discrete Uniform distribution with parameter $C$; we denote this by $X\sim\text{DUnif}(C)$. $\square$

The PMF of $X\sim\text{DUnif}(C)$ is

$P(X=x)=\frac{1}{|C|}$

for $x\in C$ (and $0$ otherwise), since a PMF must sum to $1$. As with questions based on the naive definition of probability, questions based on a Discrete Uniform distribution reduce to counting problems. Specifically, for $X\sim\text{DUnif}(C)$ and any $A\subseteq C$, we have

$P(X\in A)=\frac{|A|}{|C|}.$

###### Example 3.5.2 (Random slips of paper).

There are 100 slips of paper in a hat, each of which has one of the numbers $1,2,\ldots,100$ written on it, with no number appearing more than once. Five of the slips are drawn, one at a time.

First consider random sampling with replacement (with equal probabilities).

(a) What is the distribution of how many of the drawn slips have a value of at least 80 written on them?

(b) What is the distribution of the value of the $j$th draw (for $1\leq j\leq 5)$?

(c) What is the probability that the number 100 is drawn at least once?

Now consider random sampling without replacement (with all sets of five slips equally likely to be chosen).

(d) What is the distribution of how many of the drawn slips have a value of at least 80 written on them?

(e) What is the distribution of the value of the $j$th draw (for $1\leq j\leq 5)$?

(f) What is the probability that the number 100 is drawn in the sample?

Solution:

(a) By the story of the Binomial, the distribution is $\mathrm{Bin}(5,0.21)$.

(b) Let $X_{j}$ be the value of the $j$th draw. By symmetry, $X_{j}\sim\mathrm{DUnif}(1,2,\ldots,100)$. There aren’t certain slips that love being chosen on the $j$th draw and others that avoid being chosen then; all are equally likely.

(c) Taking complements,

$P(X_{j}=100\ \mathrm{for\ at\ least\ one\ }j)=1-P(X_{1}\neq 100,\ldots,X_{5}\neq 100).$

By the naive definition of probability, this is

$1-(99/100)^{5}\approx 0.049.$

This solution just uses new notation for concepts from Chapter 1. It is useful to have this new notation since it is compact and flexible. In the above calculation, it is important to see why

$P(X_{1}\neq 100,\ldots,X_{5}\neq 100)=P(X_{1}\neq 100)\ldots P(X_{5}\neq 100).$

This follows from the naive definition in this case, but a more general way to think about such statements is through independence of r.v.s, a concept discussed in detail in Section 3.8.

(d) By the story of the Hypergeometric, the distribution is $\mathrm{HGeom}(21,79,5)$.

(e) Let $Y_{j}$ be the value of the $j$th draw. By symmetry, $Y_{j}\sim\mathrm{DUnif}(1,2,\ldots,100)$.

Learning any $Y_{i}$ gives information about the other values (so $Y_{1},\ldots,Y_{5}$ are *not* independent, as defined in Section 3.8), but symmetry still holds since, unconditionally, the $j$th slip drawn is equally likely to be any of the slips. This is the *unconditional* distribution of $Y_{j}$: we are working from a vantage point before drawing any of the slips.

For further insight into why each of $Y_{1},\ldots,Y_{5}$ is Discrete Uniform and how to think about $Y_{j}$ unconditionally, imagine that instead of one person drawing five slips, one at a time, there are five people who draw one slip each, all reaching into the hat *simultaneously*, with all possibilities equally likely for who gets which slip. This formulation does not change the problem in any important way, and it helps avoid getting distracted by irrelevant chronological details. Label the five people $1,2,\ldots,5$ in some way, e.g., from youngest to oldest, and let $Z_{j}$ be the value drawn by person $j$. By symmetry, $Z_{j}\sim\text{DUnif}(1,2,\ldots,100)$ for each $j$; the $Z_{j}$’s are dependent but, looked at individually, each person is drawing a uniformly random slip.

(f) The events $Y_{1}=100,\ldots,Y_{5}=100$ are disjoint since we are now sampling without replacement, so

$P(Y_{j}=100\text{ for some }j)=P(Y_{1}=100)+\cdots+P(Y_{5}=100)=0.05.$

*Sanity check*: This answer makes sense intuitively since we can just as well think of first choosing five random slips out of 100 blank slips and then randomly writing the numbers from 1 to 100 on the slips, which gives a 5/100 chance that the number 100 is on one of the five chosen slips.

It would be bizarre if the answer to (c) were greater than or equal to the answer to (f), since sampling without replacement makes it easier to find the number 100. (For the same reason, when searching for a lost possession it makes more sense to sample locations without replacement than with replacement.) But it makes sense that the answer to (c) is only slightly less than the answer to (f), since it is unlikely in (c) that the same slip will be sampled more than once (though by the birthday problem it’s less unlikely than many people would guess).

More generally, if $k$ slips are drawn without replacement, where $0\leq k\leq 100$, then the same reasoning gives that the probability of drawing the number 100 is $k/100$. Note that this makes sense in the extreme case $k=100$, since in that case we draw *all* of the slips. ∎

### 3.6 Cumulative distribution functions

Another function that describes the distribution of an r.v. is the *cumulative distribution function* (CDF). Unlike the PMF, which only discrete r.v.s possess, the CDF is defined for *all* r.v.s.

Random variables and their distributions

Definition 3.6.1. The cumulative distribution function (CDF) of an r.v.  $X$  is the function  $F_{X}$  given by  $F_{X}(x) = P(X \leq x)$ . When there is no risk of ambiguity, we sometimes drop the subscript and just write  $F$  (or some other letter) for a CDF.

The next example demonstrates that for discrete r.v.s, we can freely convert between CDF and PMF.

Example 3.6.2. Let  $X \sim \operatorname{Bin}(4,1/2)$ . Figure 3.8 shows the PMF and CDF of  $X$ .

![img-46.jpeg](img-46.jpeg)
FIGURE 3.8

![img-47.jpeg](img-47.jpeg)

$\operatorname{Bin}(4,1/2)$  PMF and CDF. The height of the vertical bar  $P(X = 2)$  in the PMF is also the height of the jump in the CDF at 2.

- From PMF to CDF: To find  $P(X \leq 1.5)$ , which is the CDF evaluated at 1.5, we sum the PMF over all values of the support that are less than or equal to 1.5:

$$
P (X \leq 1. 5) = P (X = 0) + P (X = 1) = \left(\frac {1}{2}\right) ^ {4} + 4 \left(\frac {1}{2}\right) ^ {4} = \frac {5}{1 6}.
$$

Similarly, the value of the CDF at an arbitrary point  $x$  is the sum of the heights of the vertical bars of the PMF at values less than or equal to  $x$ .

- From CDF to PMF: The CDF of a discrete r.v. consists of jumps and flat regions. The height of a jump in the CDF at  $x$  is equal to the value of the PMF at  $x$ . For example, in Figure 3.8, the height of the jump in the CDF at 2 is the same as the height of the corresponding vertical bar in the PMF; this is indicated in the figure with curly braces. The flat regions of the CDF correspond to values outside the support of  $X$ , so the PMF is equal to 0 in those regions.

Valid CDFs satisfy the following criteria.

Theorem 3.6.3 (Valid CDFs). Any CDF  $F$  has the following properties.

- Increasing: If  $x_{1} \leq x_{2}$ , then  $F(x_{1}) \leq F(x_{2})$ .

- Right-continuous: As in Figure 3.8, the CDF is continuous except possibly for having some jumps. Wherever there is a jump, the CDF is continuous from the right. That is, for any $a$, we have

$F(a)=\lim_{x\to a^{+}}F(x).$
- Convergence to $0$ and $1$ in the limits:

$\lim_{x\to-\infty}F(x)=0\text{ and }\lim_{x\to\infty}F(x)=1.$

###### Proof.

The above criteria are true for *all* CDFs, but for simplicity we will only prove it for the case where $F$ is the CDF of a discrete r.v. $X$ whose possible values are $0,1,2,\dots$. As an example of how to visualize the criteria, consider Figure 3.8: the CDF shown there is increasing (with some flat regions), continuous from the right (it is continuous except at jumps, and each jump has an open dot at the bottom and a closed dot at the top), and it converges to $0$ as $x\to-\infty$ and to $1$ as $x\to\infty$ (in this example, it reaches $0$ and $1$; in some examples, one or both of these values may be approached but never reached).

The first criterion is true since the event $\{X\leq x_{1}\}$ is a subset of the event $\{X\leq x_{2}\}$, so $P(X\leq x_{1})\leq P(X\leq x_{2})$.

For the second criterion, note that

$P(X\leq x)=P(X\leq\lfloor x\rfloor),$

where $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$. For example, $P(X\leq 4.9)=P(X\leq 4)$ since $X$ is integer-valued. So $F(a+b)=F(a)$ for any $b>0$ that is small enough so that $a+b<\lfloor a\rfloor+1$, e.g., for $a=4.9$, this holds for $0<b<0.1$. This implies $F(a)=\lim_{x\to a^{+}}F(x)$ (in fact, it’s much stronger since it says $F(x)$ *equals* $F(a)$ when $x$ is close enough to $a$ and on the right).

For the third criterion, we have $F(x)=0$ for $x<0$, and

$\lim_{x\to\infty}F(x)=\lim_{x\to\infty}P(X\leq\lfloor x\rfloor)=\lim_{x\to\infty}\sum_{n=0}^{\lfloor x\rfloor}P(X=n)=\sum_{n=0}^{\infty}P(X=n)=1.$

The converse is true too: we will show in Chapter 5 that given any function $F$ meeting these criteria, we can construct a random variable whose CDF is $F$.

To recap, we have now seen three equivalent ways of expressing the distribution of a random variable. Two of these are the PMF and the CDF: we know these two functions contain the same information, since we can always figure out the CDF from the PMF and vice versa. Generally the PMF is easier to work with for discrete r.v.s, since evaluating the CDF requires a summation.

A third way to describe a distribution is with a story that explains (in a precise way) how the distribution can arise. We used the stories of the Binomial and Hypergeometric distributions to derive the corresponding PMFs. Thus the story and the PMF also contain the same information, though we can often achieve more intuitive proofs with the story than with PMF calculations.

### 3.7 Functions of random variables

In this section we will discuss what it means to take a function of a random variable, and we will build understanding for why *a function of a random variable is a random variable*. That is, if $X$ is a random variable, then $X^{2}$, $e^{X}$, and $\sin(X)$ are also random variables, as is $g(X)$ for any function $g:\mathbb{R}\to\mathbb{R}$.

For example, imagine that two basketball teams (A and B) are playing a seven-game match, and let $X$ be the number of wins for team A (so $X\sim\text{Bin}(7,1/2)$ if the teams are evenly matched and the games are independent). Let $g(x)=7-x$, and let $h(x)=1$ if $x\geq 4$ and $h(x)=0$ if $x<4$. Then $g(X)=7-X$ is the number of wins for team B, and $h(X)$ is the indicator of team A winning the majority of the games. Since $X$ is an r.v., both $g(X)$ and $h(X)$ are also r.v.s.

To see how to define functions of an r.v. formally, let’s rewind a bit. At the beginning of this chapter, we considered a random variable $X$ defined on a sample space with 6 elements. Figure 3.1 used arrows to illustrate how $X$ maps each pebble in the sample space to a real number, and the left half of Figure 3.2 showed how we can equivalently imagine $X$ writing a real number inside each pebble.

Now we can, if we want, apply the same function $g$ to all the numbers inside the pebbles. Instead of the numbers $X(s_{1})$ through $X(s_{6})$, we now have the numbers $g(X(s_{1}))$ through $g(X(s_{6}))$, which gives a new mapping from sample outcomes to real numbers—we’ve created a new random variable, $g(X)$.

###### Definition 3.7.1 (Function of an r.v.).

For an experiment with sample space $S$, an r.v. $X$, and a function $g:\mathbb{R}\to\mathbb{R}$, $g(X)$ is the r.v. that maps $s$ to $g(X(s))$ for all $s\in S$.

Taking $g(x)=\sqrt{x}$ for concreteness, Figure 3.9 shows that $g(X)$ is the *composition* of the functions $X$ and $g$, saying “first apply $X$, then apply $g$”. Figure 3.10 represents $g(X)$ more succinctly by directly labeling the sample outcomes. Both figures show us that $g(X)$ is an r.v.; if $X$ crystallizes to 4, then $g(X)$ crystallizes to 2.

Given a discrete r.v. $X$ with a known PMF, how can we find the PMF of $Y=g(X)$? In the case where $g$ is a one-to-one function, the answer is straightforward: the support of $Y$ is the set of all $g(x)$ with $x$ in the support of $X$, and

$P(Y=g(x))=P(g(X)=g(x))=P(X=x).$

Introduction to Probability

![img-48.jpeg](img-48.jpeg)
FIGURE 3.9

The r.v.  $X$  is defined on a sample space with 6 elements, and has possible values 0, 1, and 4. The function  $g$  is the square root function. Composing  $X$  and  $g$  gives the random variable  $g(X) = \sqrt{X}$ , which has possible values 0, 1, and 2.

![img-49.jpeg](img-49.jpeg)
FIGURE 3.10

Since  $g(X) = \sqrt{X}$  labels each pebble with a number, it is an r.v.

Random variables and their distributions

The case where  $Y = g(X)$  with  $g$  one-to-one is illustrated in the following tables; the idea is that if the distinct possible values of  $X$  are  $x_{1}, x_{2}, \ldots$  with probabilities  $p_{1}, p_{2}, \ldots$  (respectively), then the distinct possible values of  $Y$  are  $g(x_{1}), g(x_{2}), \ldots$ , with the same list  $p_{1}, p_{2}, \ldots$  of probabilities.

|  x | P(X=x)  |
| --- | --- |
|  x1 | p1  |
|  x2 | p2  |
|  x3 | p3  |
|  : | :  |

PMF of  $X$ , in table form

|  y | P(Y=y)  |
| --- | --- |
|  g(x1) | p1  |
|  g(x2) | p2  |
|  g(x3) | p3  |
|  : | :  |

PMF of  $Y$ , in table form

This suggests a strategy for finding the PMF of an r.v. with an unfamiliar distribution: try to express the r.v. as a one-to-one function of an r.v. with a known distribution. The next example illustrates this method.

Example 3.7.2 (Random walk). A particle moves  $n$  steps on a number line. The particle starts at 0, and at each step it moves 1 unit to the right or to the left, with equal probabilities. Assume all steps are independent. Let  $Y$  be the particle's position after  $n$  steps. Find the PMF of  $Y$ .

# Solution:

Consider each step to be a Bernoulli trial, where right is considered a success and left is considered a failure. Then the number of steps the particle takes to the right is a  $\operatorname{Bin}(n, 1/2)$  random variable, which we can name  $X$ . If  $X = j$ , then the particle has taken  $j$  steps to the right and  $n - j$  steps to the left, giving a final position of  $j - (n - j) = 2j - n$ . So we can express  $Y$  as a one-to-one function of  $X$ , namely,  $Y = 2X - n$ . Since  $X$  takes values in  $\{0, 1, 2, \ldots, n\}$ ,  $Y$  takes values in  $\{-n, 2 - n, 4 - n, \ldots, n\}$ .

The PMF of  $Y$  can then be found from the PMF of  $X$ :

$$
P (Y = k) = P (2 X - n = k) = P (X = (n + k) / 2) = \left( \begin{array}{c} n \\ \frac {n + k}{2} \end{array} \right) \left(\frac {1}{2}\right) ^ {n},
$$

if  $k$  is an integer between  $-n$  and  $n$  (inclusive) such that  $n + k$  is an even number.

If  $g$  is not one-to-one, then for a given  $y$ , there may be multiple values of  $x$  such that  $g(x) = y$ . To compute  $P(g(X) = y)$ , we need to sum up the probabilities of  $X$  taking on any of these candidate values of  $x$ .

Theorem 3.7.3 (PMF of  $g(X)$ ). Let  $X$  be a discrete r.v. and  $g: \mathbb{R} \to \mathbb{R}$ . Then the support of  $g(X)$  is the set of all  $y$  such that  $g(x) = y$  for at least one  $x$  in the support of  $X$ , and the PMF of  $g(X)$  is

$$
P (g (X) = y) = \sum_ {x: g (x) = y} P (X = x),
$$

Introduction to Probability

for all $y$ in the support of $g(X)$.

Example 3.7.4. Continuing as in the previous example, let $D$ be the particle's distance from the origin after $n$ steps. Assume that $n$ is even. Find the PMF of $D$.

Solution:

We can write $D = |Y|$; this is a function of $Y$, but it isn't one-to-one. The event $D = 0$ is the same as the event $Y = 0$. For $k = 2,4,\ldots ,n$, the event $D = k$ is the same as the event $\{Y = k\} \cup \{Y = -k\}$. So the PMF of $D$ is

$$
P (D = 0) = \left( \begin{array}{c} n \\ \frac {n}{2} \end{array} \right) \left(\frac {1}{2}\right) ^ {n},
$$

$$
P (D = k) = P (Y = k) + P (Y = - k) = 2 \binom {n} {\frac {n + k}{2}} \left(\frac {1}{2}\right) ^ {n},
$$

for $k = 2,4,\ldots ,n$. In the final step we used symmetry (imagine a new random walk that moves left each time our random walk moves right, and vice versa) to see that $P(Y = k) = P(Y = -k)$.

The same reasoning we have used to handle functions of one random variable can be extended to deal with functions of multiple random variables. We have already seen an example of this with the addition function (which maps two numbers $x, y$ to their sum $x + y$): in Example 3.2.5, we saw how to view $T = X + Y$ as an r.v. in its own right, where $X$ and $Y$ are obtained by rolling dice.

Definition 3.7.5 (Function of two r.v.s). Given an experiment with sample space $S$, if $X$ and $Y$ are r.v.s that map $s \in S$ to $X(s)$ and $Y(s)$ respectively, then $g(X,Y)$ is the r.v. that maps $s$ to $g(X(s),Y(s))$.

Note that we are assuming that $X$ and $Y$ are defined on the same sample space $S$. Usually we assume that $S$ is chosen to be rich enough to encompass whatever r.v.s we wish to work with. For example, if $X$ is based on a coin flip and $Y$ is based on a die roll, and we initially were using the sample space $S_{1} = \{H,T\}$ for $X$ and the sample space $S_{2} = \{1,2,3,4,5,6\}$ for $Y$, we can easily redefine $X$ and $Y$ so that both are defined on the richer space $S = S_{1} \times S_{2} = \{(s_{1},s_{2}): s_{1} \in S_{1}, s_{2} \in S_{2}\}$.

One way to understand the mapping from $S$ to $\mathbb{R}$ represented by the r.v. $g(X,Y)$ is with a table displaying the values of $X, Y$, and $g(X,Y)$ under various possible outcomes. Interpreting $X + Y$ as an r.v. is intuitive: if we observe $X = x$ and $Y = y$, then $X + Y$ crystallizes to $x + y$. For a less familiar example like $\max(X,Y)$, students often are unsure how to interpret it as an r.v. But the idea is the same: if we observe $X = x$ and $Y = y$, then $\max(X,Y)$ crystallizes to $\max(x,y)$.

Example 3.7.6 (Maximum of two die rolls). We roll two fair 6-sided dice. Let $X$ be the number on the first die and $Y$ the number on the second die. The following table gives the values of $X, Y$, and $\max(X, Y)$ under 7 of the 36 outcomes in the sample space, analogously to the table in Example 3.2.5.

Random variables and their distributions

|  s | X | Y | max(X,Y)  |
| --- | --- | --- | --- |
|  (1,2) | 1 | 2 | 2  |
|  (1,6) | 1 | 6 | 6  |
|  (2,5) | 2 | 5 | 5  |
|  (3,1) | 3 | 1 | 3  |
|  (4,3) | 4 | 3 | 4  |
|  (5,4) | 5 | 4 | 5  |
|  (6,6) | 6 | 6 | 6  |

So  $\max(X, Y)$  assigns a numerical value to each sample outcome. The PMF is

$P(\max (X,Y) = 1) = 1 / 36,$

$P(\max (X,Y) = 2) = 3 / 36,$

$P(\max (X,Y) = 3) = 5 / 36,$

$P(\max (X,Y) = 4) = 7 / 36,$

$P(\max (X,Y) = 5) = 9 / 36,$

$P(\max (X,Y) = 6) = 11 / 36.$

These probabilities can be obtained by tabulating the values of  $\max(x, y)$  in a  $6 \times 6$  grid and counting how many times each value appears in the grid, or with calculations such as

$P(\max (X,Y) = 5) = P(X = 5,Y\leq 4) + P(X\leq 4,Y = 5) + P(X = 5,Y = 5)$

$= 2P(X = 5,Y\leq 4) + 1 / 36$

$= 2(4 / 36) + 1 / 36 = 9 / 36.$

$\star$  3.7.7 (Category errors and sympathetic magic). Many common mistakes in probability can be traced to confusing two of the following fundamental objects with each other: distributions, random variables, events, and numbers. Such mistakes are examples of category errors. In general, a category error is a mistake that doesn't just happen to be wrong, but in fact is necessarily wrong since it is based on the wrong category of object. For example, answering the question "How many people live in Boston?" with "-42" or "π" or "pink elephants" would be a category error—we may not know the population size of a city, but we do know that it is a nonnegative integer at any point in time. To help avoid being categorically wrong, always think about what category an answer should have.

An especially common category error is to confuse a random variable with its distribution. We call this error sympathetic magic; this term comes from anthropology, where it is used for the belief that one can influence an object by manipulating a representation of that object. The following saying sheds light on the distinction between a random variable and its distribution:

The word is not the thing; the map is not the territory. - Alfred Korzybski

Introduction to Probability

We can think of the distribution of a random variable as a map or blueprint describing the r.v. Just as different houses can share the same blueprint, different r.v.s can have the same distribution, even if the experiments they summarize, and the sample spaces they map from, are not the same.

Here are two examples of sympathetic magic:

- Given an r.v.  $X$ , trying to get the PMF of  $2X$  by multiplying the PMF of  $X$  by 2. It does not make sense to multiply a PMF by 2, since the probabilities would no longer sum to 1. As we saw above, if  $X$  takes on values  $x_{j}$  with probabilities  $p_{j}$ , then  $2X$  takes on values  $2x_{j}$  with probabilities  $p_{j}$ . Therefore the PMF of  $2X$  is a horizontal stretch of the PMF of  $X$ ; it is not a vertical stretch, as would result from multiplying the PMF by 2. Figure 3.11 shows the PMF of a discrete r.v.  $X$  with support  $\{0,1,2,3,4\}$ , along with the PMF of  $2X$ , which has support  $\{0,2,4,6,8\}$ . Note that  $X$  can take on odd values, but  $2X$  is necessarily even.

![img-50.jpeg](img-50.jpeg)

![img-51.jpeg](img-51.jpeg)
FIGURE 3.11 PMF of  $X$  (above) and PMF of  $2X$  (below).

Random variables and their distributions

- Claiming that because $X$ and $Y$ have the same distribution, $X$ must always equal $Y$, i.e., $P(X=Y)=1$. Just because two r.v.s have the same distribution does not mean they are always equal, or *ever* equal. We saw this in Example 3.2.5. As another example, consider flipping a fair coin once. Let $X$ be the indicator of Heads and $Y=1-X$ be the indicator of Tails. Both $X$ and $Y$ have the $\operatorname{Bern}(1/2)$ distribution, but the event $X=Y$ is impossible. The PMFs of $X$ and $Y$ are the same function, but $X$ and $Y$ are different mappings from the sample space to the real numbers.

If $Z$ is the indicator of Heads in a second flip (independent of the first flip), then $Z$ is also $\operatorname{Bern}(1/2)$, but $Z$ is not the same r.v. as $X$. Here

$P(Z=X)=P(HH\text{ or }TT)=1/2.$

### 3.8 Independence of r.v.s

Just as we had the notion of independence of events, we can define independence of random variables. Intuitively, if two r.v.s $X$ and $Y$ are independent, then knowing the value of $X$ gives no information about the value of $Y$, and vice versa. The definition formalizes this idea.

###### Definition 3.8.1 (Independence of two r.v.s).

Random variables $X$ and $Y$ are said to be *independent* if

$P(X\leq x,Y\leq y)=P(X\leq x)P(Y\leq y),$

for all $x,y\in\mathbb{R}$.

In the discrete case, this is equivalent to the condition

$P(X=x,Y=y)=P(X=x)P(Y=y),$

for all $x,y$ with $x$ in the support of $X$ and $y$ in the support of $Y$.

The definition for more than two r.v.s is analogous.

###### Definition 3.8.2 (Independence of many r.v.s).

Random variables $X_{1},\ldots,X_{n}$ are *independent* if

$P(X_{1}\leq x_{1},\ldots,X_{n}\leq x_{n})=P(X_{1}\leq x_{1})\ldots P(X_{n}\leq x_{n}),$

for all $x_{1},\ldots,x_{n}\in\mathbb{R}$. For infinitely many r.v.s, we say that they are independent if every finite subset of the r.v.s is independent.

Comparing this to the criteria for independence of $n$ events, it may seem strange that the independence of $X_{1},\ldots,X_{n}$ requires just one equality, whereas for events we

Introduction to Probability

needed to verify pairwise independence for all  $\binom{n}{2}$  pairs, three-way independence for all  $\binom{n}{3}$  triplets, and so on. However, upon closer examination of the definition, we see that independence of r.v.s requires the equality to hold for all possible  $x_{1},\ldots ,x_{n}$  — infinitely many conditions! If we can find even a single list of values  $x_{1},\ldots ,x_{n}$  for which the above equality fails to hold, then  $X_{1},\ldots ,X_{n}$  are not independent.

$\star 3.8.3$ . If  $X_{1}, \ldots, X_{n}$  are independent, then they are pairwise independent, i.e.,  $X_{i}$  is independent of  $X_{j}$  for  $i \neq j$ . The idea behind proving that  $X_{i}$  and  $X_{j}$  are independent is to let all the  $x_{k}$  other than  $x_{i}, x_{j}$  go to  $\infty$  in the definition of independence, since we already know  $X_{k} &lt; \infty$  is true (though it takes some work to give a complete justification for the limit). But pairwise independence does not imply independence in general, as we saw in Chapter 2 for events.

Example 3.8.4. In a roll of two fair dice, if  $X$  is the number on the first die and  $Y$  is the number on the second die, then  $X + Y$  is not independent of  $X - Y$  since

$$
0 = P (X + Y = 1 2, X - Y = 1) \neq P (X + Y = 1 2) P (X - Y = 1) = \frac {1}{3 6} \cdot \frac {5}{3 6}.
$$

Knowing the total is 12 tells us the difference must be 0, so the r.v.s provide information about each other.

If  $X$  and  $Y$  are independent then it is also true, e.g., that  $X^2$  is independent of  $Y^4$ , since if  $X^2$  provided information about  $Y^4$ , then  $X$  would give information about  $Y$  (using  $X^2$  and  $Y^4$  as intermediaries:  $X$  determines  $X^2$ , which would give information about  $Y^4$ , which in turn would give information about  $Y$ ). More generally, we have the following result (for which we omit a formal proof).

Theorem 3.8.5 (Functions of independent r.v.s). If  $X$  and  $Y$  are independent r.v.s, then any function of  $X$  is independent of any function of  $Y$ .

Definition 3.8.6 (i.i.d.). We will often work with random variables that are independent and have the same distribution. We call such r.v.s independent and identically distributed, or i.i.d. for short.

$\star 3.8.7$  (i. vs. i.d.). "Independent" and "identically distributed" are two often-confused but completely different concepts. Random variables are independent if they provide no information about each other; they are identically distributed if they have the same PMF (or equivalently, the same CDF). Whether two r.v.s are independent has nothing to do with whether they have the same distribution. We can have r.v.s that are:

- independent and identically distributed. Let  $X$  be the result of a die roll, and let  $Y$  be the result of a second, independent die roll. Then  $X$  and  $Y$  are i.i.d.
- independent and not identically distributed. Let  $X$  be the result of a die roll, and let  $Y$  be the closing price of the Dow Jones (a stock market index) a month from now. Then  $X$  and  $Y$  provide no information about each other (one would fervently hope), and  $X$  and  $Y$  do not have the same distribution.

Random variables and their distributions

- dependent and identically distributed. Let $X$ be the number of Heads in $n$ independent fair coin tosses, and let $Y$ be the number of Tails in those same $n$ tosses. Then $X$ and $Y$ are both distributed $\operatorname{Bin}(n, 1/2)$, but they are highly dependent: if we know $X$, then we know $Y$ perfectly.
- dependent and not identically distributed. Let $X$ be the indicator of whether the majority party retains control of the House of Representatives in the U.S. after the next election, and let $Y$ be the average favorability rating of the majority party in polls taken within a month of the election. Then $X$ and $Y$ are dependent, and $X$ and $Y$ do not have the same distribution.

By taking a sum of i.i.d. Bernoulli r.v.s, we can write down the story of the Binomial distribution in an algebraic form.

Theorem 3.8.8. If $X \sim \operatorname{Bin}(n, p)$, viewed as the number of successes in $n$ independent Bernoulli trials with success probability $p$, then we can write $X = X_{1} + \dots + X_{n}$ where the $X_{i}$ are i.i.d. $\operatorname{Bern}(p)$.

Proof. Let $X_{i} = 1$ if the $i$th trial was a success, and 0 if the $i$th trial was a failure. It's as though we have a person assigned to each trial, and we ask each person to raise their hand if their trial was a success. If we count the number of raised hands (which is the same as adding up the $X_{i}$), we get the total number of successes.

An important fact about the Binomial distribution is that the sum of independent Binomial r.v.s with the same success probability is also Binomial.

Theorem 3.8.9. If $X \sim \operatorname{Bin}(n, p)$, $Y \sim \operatorname{Bin}(m, p)$, and $X$ is independent of $Y$, then $X + Y \sim \operatorname{Bin}(n + m, p)$.

Proof. We present three proofs, since each illustrates a useful technique.

1. LOTP: We can directly find the PMF of $X + Y$ by conditioning on $X$ (or $Y$, whichever we prefer) and using the law of total probability:

$$
\begin{array}{l}
P (X + Y = k) = \sum_ {j = 0} ^ {k} P (X + Y = k | X = j) P (X = j) \\
= \sum_ {j = 0} ^ {k} P (Y = k - j) P (X = j) \\
= \sum_ {j = 0} ^ {k} \binom {m} {k - j} p ^ {k - j} q ^ {m - k + j} \binom {n} {j} p ^ {j} q ^ {n - j} \\
= p ^ {k} q ^ {n + m - k} \sum_ {j = 0} ^ {k} \binom {m} {k - j} \binom {n} {j} \\
= \binom {n + m} {k} p ^ {k} q ^ {n + m - k}.
\end{array}
$$

Introduction to Probability

In the second line, we used the independence of $X$ and $Y$ to justify dropping the conditioning in

$P(X+Y=k|X=j)=P(Y=k-j|X=j)=P(Y=k-j),$

and in the last line, we used the fact that

$\sum_{j=0}^{k}{m\choose k-j}{n\choose j}={n+m\choose k}$

by Vandermonde’s identity. The resulting expression is the Bin$(n+m,p)$ PMF, so $X+Y\sim$ Bin$(n+m,p)$.

2. Representation: A much simpler proof is to represent both $X$ and $Y$ as the sum of i.i.d. Bern$(p)$ r.v.s: $X=X_{1}+\cdots+X_{n}$ and $Y=Y_{1}+\cdots+Y_{m}$, where the $X_{i}$ and $Y_{j}$ are all i.i.d. Bern$(p)$. Then $X+Y$ is the sum of $n+m$ i.i.d. Bern$(p)$ r.v.s, so its distribution, by the previous theorem, is Bin$(n+m,p)$.

3. Story: By the Binomial story, $X$ is the number of successes in $n$ independent trials and $Y$ is the number of successes in $m$ additional independent trials, all with the same success probability, so $X+Y$ is the total number of successes in the $n+m$ trials, which is the story of the Bin$(n+m,p)$ distribution.

Of course, if we have a definition for independence of r.v.s, we should have an analogous definition for conditional independence of r.v.s.

###### Definition 3.8.10 (Conditional independence of r.v.s).

Random variables $X$ and $Y$ are *conditionally independent* given an r.v. $Z$ if for all $x,y\in\mathbb{R}$ and all $z$ in the support of $Z$,

$P(X\leq x,Y\leq y|Z=z)=P(X\leq x|Z=z)P(Y\leq y|Z=z).$

For discrete r.v.s, an equivalent definition is to require

$P(X=x,Y=y|Z=z)=P(X=x|Z=z)P(Y=y|Z=z).$

As we might expect from the name, this is the definition of independence, except that we condition on $Z=z$ everywhere, and require the equality to hold for all $z$ in the support of $Z$.

###### Definition 3.8.11 (Conditional PMF).

For any discrete r.v.s $X$ and $Z$, the function $P(X=x|Z=z)$, when considered as a function of $x$ for fixed $z$, is called the *conditional PMF of $X$ given $Z=z$*.

Independence of r.v.s does not imply conditional independence, nor vice versa. First let us show why independence does not imply conditional independence.

Random variables and their distributions

###### Example 3.8.12 (Matching pennies).

Consider the simple game called *matching pennies*. Each of two players, A and B, has a fair penny. They flip their pennies independently. If the pennies match, A wins; otherwise, B wins. Let $X$ be 1 if A’s penny lands Heads and $-1$ otherwise, and define $Y$ similarly for B (the r.v.s $X$ and $Y$ are called *random signs*).

Let $Z=XY$, which is 1 if A wins and $-1$ if B wins. Then $X$ and $Y$ are unconditionally independent, but given $Z=1$, we know that $X=Y$ (the pennies match). So $X$ and $Y$ are conditionally dependent given $Z$. ∎

###### Example 3.8.13 (Two friends).

Consider again the “I have only two friends who ever call me” scenario from Example 2.5.11, except now with r.v. notation. Let $X$ be the indicator of Alice calling me next Friday, $Y$ be the indicator of Bob calling me next Friday, and $Z$ be the indicator of exactly one of them calling me next Friday. Then $X$ and $Y$ are independent (by assumption). But given $Z=1$, we have that $X$ and $Y$ are completely dependent: given that $Z=1$, we have $Y=1-X$. ∎

Next let’s see why conditional independence does not imply independence.

###### Example 3.8.14 (Mystery opponent).

Suppose that you are going to play two games of tennis against one of two identical twins. Against one of the twins, you are evenly matched, and against the other you have a $3/4$ chance of winning. Suppose that you can’t tell which twin you are playing against until after the two games. Let $Z$ be the indicator of playing against the twin with whom you’re evenly matched, and let $X$ and $Y$ be the indicators of victory in the first and second games, respectively.

Conditional on $Z=1$, $X$ and $Y$ are i.i.d. Bern(1/2), and conditional on $Z=0$, $X$ and $Y$ are i.i.d. Bern(3/4). So $X$ and $Y$ are conditionally independent given $Z$. Unconditionally, $X$ and $Y$ are dependent because observing $X=1$ makes it more likely that we are playing the twin who is worse. That is,

$P(Y=1|X=1)&gt;P(Y=1).$

Past games give us information which helps us infer who our opponent is, which in turn helps us predict future games! Note that this example is isomorphic to the “random coin” scenario from Example 2.3.7. ∎

### 3.9 Connections between Binomial and Hypergeometric

The Binomial and Hypergeometric distributions are connected in two important ways. As we will see in this section, we can get from the Binomial to the Hypergeometric by *conditioning*, and we can get from the Hypergeometric to the Binomial by *taking a limit*. We’ll start with a motivating example.

###### Example 3.9.1 (Fisher exact test).

A scientist wishes to study whether women or

Introduction to Probability

men are more likely to have a certain disease, or whether they are equally likely. A random sample of  $n$  women and  $m$  men is gathered, and each person is tested for the disease (assume for this problem that the test is completely accurate). The numbers of women and men in the sample who have the disease are  $X$  and  $Y$  respectively, with  $X \sim \operatorname{Bin}(n, p_1)$  and  $Y \sim \operatorname{Bin}(m, p_2)$ , independently. Here  $p_1$  and  $p_2$  are unknown, and we are interested in testing whether  $p_1 = p_2$  (this is known as a null hypothesis in statistics).

Consider a  $2 \times 2$  table with rows corresponding to disease status and columns corresponding to gender. Each entry is the count of how many people have that disease status and gender, so  $n + m$  is the sum of all 4 entries. Suppose that it is observed that  $X + Y = r$ .

The Fisher exact test is based on conditioning on both the row and column sums, so  $n, m, r$  are all treated as fixed, and then seeing if the observed value of  $X$  is "extreme" compared to this conditional distribution. Assuming the null hypothesis, find the conditional PMF of  $X$  given  $X + Y = r$ .

Solution:

First we'll build the  $2 \times 2$  table, treating  $n$ ,  $m$ , and  $r$  as fixed.

|   | Women | Men | Total  |
| --- | --- | --- | --- |
|  Disease | x | r-x | r  |
|  No disease | n-x | m-r+x | n+m-r  |
|  Total | n | m | n+m  |

Next, let's compute the conditional PMF  $P(X = x|X + Y = r)$ . By Bayes' rule,

$$
\begin{array}{l} P (X = x | X + Y = r) = \frac {P (X + Y = r | X = x) P (X = x)}{P (X + Y = r)} \\ = \frac {P (Y = r - x) P (X = x)}{P (X + Y = r)}. \\ \end{array}
$$

The step  $P(X + Y = r|X = x) = P(Y = r - x)$  is justified by the independence of  $X$  and  $Y$ . Assuming the null hypothesis and letting  $p = p_1 = p_2$ , we have  $X \sim \operatorname{Bin}(n, p)$  and  $Y \sim \operatorname{Bin}(m, p)$ , independently, so  $X + Y \sim \operatorname{Bin}(n + m, p)$ . Thus,

$$
\begin{array}{l} P (X = x | X + Y = r) = \frac {\binom {m} {r - x} p ^ {r - x} (1 - p) ^ {m - r + x} \binom {n} {x} p ^ {x} (1 - p) ^ {n - x}}{\binom {n + m} {r} p ^ {r} (1 - p) ^ {n + m - r}} \\ = \frac {\binom {n} {x} \binom {m} {r - x}}{\binom {n + m} {r}}. \\ \end{array}
$$

So the conditional distribution of  $X$  is Hypergeometric with parameters  $n, m, r$ .

To understand why the Hypergeometric appeared, seemingly out of nowhere, let's connect this problem to the elk story for the Hypergeometric. In the elk story, we are

Random variables and their distributions

interested in the distribution of the number of tagged elk in the recaptured sample. By analogy, think of women as tagged elk and men as untagged elk. Instead of recapturing  $r$  elk at random from the forest, we infect  $X + Y = r$  people with the disease; under the null hypothesis, the set of diseased people is equally likely to be any set of  $r$  people. Thus, conditional on  $X + Y = r$ ,  $X$  represents the number of women among the  $r$  diseased individuals. This is exactly analogous to the number of tagged elk in the recaptured sample, which is distributed  $\mathrm{HGeom}(n,m,r)$ .

An interesting fact, which turns out to be useful in statistics, is that the conditional distribution of  $X$  does not depend on  $p$ : unconditionally,  $X \sim \operatorname{Bin}(n,p)$ , but  $p$  disappears from the parameters of the conditional distribution! This makes sense upon reflection, since once we know  $X + Y = r$ , we can work directly with the fact that we have a population with  $r$  diseased and  $n + m - r$  healthy people, without worrying about the value of  $p$  that originally generated the population.

This motivating example serves as a proof of the following theorem.

Theorem 3.9.2. If  $X \sim \operatorname{Bin}(n,p)$ ,  $Y \sim \operatorname{Bin}(m,p)$ , and  $X$  is independent of  $Y$ , then the conditional distribution of  $X$  given  $X + Y = r$  is  $\mathrm{HGeom}(n,m,r)$ .

In the other direction, the Binomial is a limiting case of the Hypergeometric.

Theorem 3.9.3. If  $X \sim \mathrm{HGeom}(w, b, n)$  and  $N = w + b \to \infty$  such that  $p = w / (w + b)$  remains fixed, then the PMF of  $X$  converges to the  $\operatorname{Bin}(n, p)$  PMF.

Proof. We take the stated limit of the  $\mathrm{HGeom}(w,b,n)$  PMF:

$$
\begin{array}{l} P (X = k) = \frac {\binom {w} {k} \binom {b} {n - k}}{\binom {w + b} {n}} \\ = \binom {n} {k} \frac {\binom {w + b - n} {w - k}}{\binom {w + b} {w}} \quad \text {by Theorem 3.4.5} \\ = \binom {n} {k} \frac {w !}{(w - k) !} \frac {b !}{(b - n + k) !} \frac {(w + b - n) !}{(w + b) !} \\ = \binom {n} {k} \frac {w (w - 1) \dots (w - k + 1) b (b - 1) \dots (b - n + k + 1)}{(w + b) (w + b - 1) \dots (w + b - n + 1)} \\ = \binom {n} {k} \frac {p \left(p - \frac {1}{N}\right) \dots \left(p - \frac {k - 1}{N}\right) q \left(q - \frac {1}{N}\right) \dots \left(q - \frac {n - k - 1}{N}\right)}{\left(1 - \frac {1}{N}\right) \left(1 - \frac {2}{N}\right) \dots \left(1 - \frac {n - 1}{N}\right)}. \\ \end{array}
$$

As  $N\to \infty$  , the denominator goes to 1, and the numerator goes to  $p^k q^{n - k}$  . Thus

$$
P (X = k) \to \left( \begin{array}{c} n \\ k \end{array} \right) p ^ {k} q ^ {n - k},
$$

which is the  $\operatorname{Bin}(n,p)$  PMF.

The stories of the Binomial and Hypergeometric provide intuition for this result: given an urn with  $w$  white balls and  $b$  black balls, the Binomial distribution arises

from sampling $n$ balls from the urn with replacement, while the Hypergeometric arises from sampling without replacement. As the number of balls in the urn grows very large relative to the number of balls that are drawn, sampling with replacement and sampling without replacement become essentially equivalent. In practical terms, this theorem tells us that if $N=w+b$ is large relative to $n$, we can approximate the HGeom$(w,b,n)$ PMF by the Bin$(n,w/(w+b))$ PMF.

The birthday problem implies that it is surprisingly likely that some ball will be sampled more than once if sampling with replacement; for example, if 1,200 out of 1,000,000 balls are drawn randomly with replacement, then there is about a 51% chance that some ball will be drawn more than once! But this becomes less and less likely as $N$ grows, and even if it is likely that there will be a few coincidences, the approximation can still be reasonable if it is very likely that the vast majority of balls in the sample are sampled only once each.

### 3.10 Recap

A random variable (r.v.) is a function assigning a real number to every possible outcome of an experiment. The distribution of an r.v. $X$ is a full specification of the probabilities for the events associated with $X$, such as $\{X=3\}$ and $\{1\leq X\leq 5\}$. The distribution of a discrete r.v. can be defined using a PMF, a CDF, or a story. The PMF of $X$ is the function $P(X=x)$ for $x\in\mathbb{R}$. The CDF of $X$ is the function $P(X\leq x)$ for $x\in\mathbb{R}$. A story for $X$ describes an experiment that could give rise to a random variable with the same distribution as $X$.

For a PMF to be valid, it must be nonnegative and sum to 1. For a CDF to be valid, it must be increasing, right-continuous, converge to 0 as $x\to-\infty$, and converge to 1 as $x\to\infty$.

It is important to distinguish between a random variable and its distribution: the distribution is a blueprint for building the r.v., but different r.v.s can have the same distribution, just as different houses can be built from the same blueprint.

Four named discrete distributions are the Bernoulli, Binomial, Hypergeometric, and Discrete Uniform. Each of these is actually a *family* of distributions, indexed by parameters; to fully specify one of these distributions, we need to give both the name and the parameter values.

- A Bern($p$) r.v. is the indicator of success in a Bernoulli trial with probability of success $p$.
- A Bin($n,p$) r.v. is the number of successes in $n$ independent Bernoulli trials, all with the same probability $p$ of success.

Random variables and their distributions

- A HGeom  $(w, b, n)$  r.v. is the number of white balls obtained in a sample of size  $n$  drawn without replacement from an urn of  $w$  white and  $b$  black balls.
- A DUnif  $(C)$  r.v. is obtained by randomly choosing an element of the finite set  $C$ , with equal probabilities for each element.

A function of a random variable is still a random variable. If we know the PMF of  $X$ , we can find  $P(g(X) = k)$ , the PMF of  $g(X)$ , by translating the event  $\{g(X) = k\}$  into an equivalent event involving  $X$ , then using the PMF of  $X$ .

Two random variables are independent if knowing the value of one r.v. gives no information about the value of the other. This is unrelated to whether the two r.v.s are identically distributed. In Chapter 7, we will learn how to deal with dependent random variables by considering them jointly rather than separately.

We have now seen four fundamental types of objects in probability: distributions, random variables, events, and numbers. Figure 3.12 shows connections between these four fundamental objects. A CDF can be used as a blueprint for generating an r.v., and then there are various events describing the behavior of the r.v., such as the events  $X \leq x$  for all  $x$ . Knowing the probabilities of these events determines the CDF, taking us full circle. For a discrete r.v. we can also use the PMF as a blueprint, and go from distribution to r.v. to events and back again.

![img-52.jpeg](img-52.jpeg)

# FIGURE 3.12

Four fundamental objects in probability: distributions (blueprints), random variables, events, and numbers. From a CDF  $F$  we can generate an r.v.  $X$ . From  $X$ , we can generate many other r.v.s by taking functions of  $X$ . There are various events describing the behavior of  $X$ . Most notably, for any constant  $x$  the events  $X \leq x$  and  $X = x$  are of interest. Knowing the probabilities of these events for all  $x$  gives us the CDF and (in the discrete case) the PMF, taking us full circle.

3.11 R

#### Distributions in R

All of the named distributions that we’ll encounter in this book have been implemented in R. In this section we’ll explain how to work with the Binomial and Hypergeometric distributions in R. We will also explain in general how to generate r.v.s from any discrete distribution with a finite support. Typing help(distributions) gives a handy list of built-in distributions; many others are available through R packages that can be loaded.

In general, for many named discrete distributions, three functions starting with d, p, and r will give the PMF, CDF, and random generation, respectively. Note that the function starting with p is not the PMF, but rather is the CDF.

#### Binomial distribution

The Binomial distribution is associated with the following three R functions: dbinom, pbinom, and rbinom. For the Bernoulli distribution we can just use the Binomial functions with $n=1$.

- dbinom is the Binomial PMF. It takes three inputs: the first is the value of $x$ at which to evaluate the PMF, and the second and third are the parameters $n$ and $p$. For example, dbinom(3,5,0.2) returns the probability $P(X=3)$ where $X\sim\text{Bin}(5,0.2)$. In other words,

$\text{dbinom}(3,5,0.2)=\binom{5}{3}(0.2)^{3}(0.8)^{2}=0.0512.$
- pbinom is the Binomial CDF. It takes three inputs: the first is the value of $x$ at which to evaluate the CDF, and the second and third are the parameters. pbinom(3,5,0.2) is the probability $P(X\leq 3)$ where $X\sim\text{Bin}(5,0.2)$. So

$\text{pbinom}(3,5,0.2)=\sum_{k=0}^{3}\binom{5}{k}(0.2)^{k}(0.8)^{5-k}=0.9933.$
- rbinom is a function for generating Binomial random variables. For rbinom, the first input is *how many* r.v.s we want to generate, and the second and third inputs are still the parameters. Thus the command rbinom(7,5,0.2) produces realizations of seven i.i.d. $\text{Bin}(5,0.2)$ r.v.s. When we ran this command, we got

```
2 1 0 0 1 0 0
```

but you’ll probably get something different when you try it!

We can also evaluate PMFs and CDFs at an entire vector of values. For example, recall that 0:n is a quick way to list the integers from 0 to $n$. The command dbinom(0:5,5,0.2) returns 6 numbers, $P(X=0),P(X=1),\ldots,P(X=5)$, where $X\sim\text{Bin}(5,0.2)$.

#### Hypergeometric distribution

The Hypergeometric distribution also has three functions: dhyper, phyper, and rhyper. As one might expect, dhyper is the Hypergeometric PMF, phyper is the Hypergeometric CDF, and rhyper generates Hypergeometric r.v.s. Since the Hypergeometric distribution has three parameters, each of these functions takes four inputs. For dhyper and phyper, the first input is the value at which we wish to evaluate the PMF or CDF, and the remaining inputs are the parameters of the distribution.

Thus dhyper(k,w,b,n) returns $P(X=k)$ where $X\sim\text{HGeom}(w,b,n)$, and phyper(k,w,b,n) returns $P(X\leq k)$. For rhyper, the first input is the number of r.v.s we want to generate, and the remaining inputs are the parameters; rhyper(100,w,b,n) generates 100 i.i.d. HGeom$(w,b,n)$ r.v.s.

#### Discrete distributions with finite support

We can generate r.v.s from any discrete distribution with finite support using the sample command. When we first introduced the sample command, we said that it can be used in the form sample(n,k) or sample(n,k,replace=TRUE) to sample $k$ times from the integers 1 through $n$, either without or with replacement. For example, to generate 5 independent DUnif$(1,2,\ldots,100)$ r.v.s, we can use the command sample(100,5,replace=TRUE).

It turns out that sample is far more versatile. If we want to sample from the values $x_{1},\ldots,x_{n}$ with probabilities $p_{1},\ldots,p_{n}$, we simply create a vector x containing all the $x_{i}$ and a vector p containing all the $p_{i}$, then feed them into sample. Suppose we want realizations of i.i.d. r.v.s $X_{1},\ldots,X_{100}$ whose PMF is

$P(X_{j}=0)=0.25,$
$P(X_{j}=1)=0.5,$
$P(X_{j}=5)=0.1,$
$P(X_{j}=10)=0.15,$

and $P(X_{j}=x)=0$ for all other values of $x$. First, we use the c function to create vectors with the support of the distribution and the corresponding probabilities.

```
x <- c(0,1,5,10)
p <- c(0.25,0.5,0.1,0.15)

Next, we use sample. Here’s how to get 100 draws from the PMF above:

```
sample(x,100,prob=p,replace=TRUE)
```

The inputs are the vector x to sample from, the sample size (100 in this case), the probabilities p to use when sampling from x (if this is omitted, the probabilities are assumed equal), and whether to sample with replacement.

### 3.12 Exercises

Exercises marked with ⑧ have detailed solutions at http://stat110.net.

PMFs and CDFs

1. People are arriving at a party one at a time. While waiting for more people to arrive they entertain themselves by comparing their birthdays. Let $X$ be the number of people needed to obtain a birthday match, i.e., before person $X$ arrives no two people have the same birthday, but when person $X$ arrives there is a match. Find the PMF of $X$.
2. (a) Independent Bernoulli trials are performed, with probability 1/2 of success, until there has been at least one success. Find the PMF of the number of trials performed.

(b) Independent Bernoulli trials are performed, with probability 1/2 of success, until there has been at least one success and at least one failure. Find the PMF of the number of trials performed.
3. Let $X$ be an r.v. with CDF $F$, and $Y=\mu+\sigma X$, where $\mu$ and $\sigma$ are real numbers with $\sigma>0$. (Then $Y$ is called a *location-scale transformation* of $X$; we will encounter this concept many times in Chapter 5 and beyond.) Find the CDF of $Y$, in terms of $F$.
4. Let $n$ be a positive integer and

$F(x)=\frac{\lfloor x\rfloor}{n}$

for $0\leq x\leq n$, $F(x)=0$ for $x<0$, and $F(x)=1$ for $x>n$, where $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$. Show that $F$ is a CDF, and find the PMF that it corresponds to.
5. (a) Show that $p(n)=\left(\frac{1}{2}\right)^{n+1}$ for $n=0,1,2,\dots$ is a valid PMF for a discrete r.v.

(b) Find the CDF of a random variable with the PMF from (a).
6. ⑧ *Benford’s law* states that in a very large variety of real-life data sets, the first digit approximately follows a particular distribution with about a 30% chance of a 1, an 18% chance of a 2, and in general

$P(D=j)=\log_{10}\left(\frac{j+1}{j}\right),\text{ for }j\in\{1,2,3,\dots,9\},$

where $D$ is the first digit of a randomly chosen element. Check that this is a valid PMF (using properties of logs, not with a calculator).
7. Bob is playing a video game that has 7 levels. He starts at level 1, and has probability $p_{1}$ of reaching level 2. In general, given that he reaches level $j$, he has probability $p_{j}$ of reaching level $j+1$, for $1\leq j\leq 6$. Let $X$ be the highest level that he reaches. Find the PMF of $X$ (in terms of $p_{1},\dots,p_{6}$).

###

8. There are 100 prizes, with one worth $1, one worth $2, $\dots$, and one worth $100. There are 100 boxes, each of which contains one of the prizes. You get 5 prizes by picking random boxes one at a time, *without replacement*. Find the PMF of how much your most valuable prize is worth (as a simple expression in terms of binomial coefficients).
9. Let $F_{1}$ and $F_{2}$ be CDFs, $0<p<1$, and $F(x)=pF_{1}(x)+(1-p)F_{2}(x)$ for all $x$.

(a) Show directly that $F$ has the properties of a valid CDF (see Theorem 3.6.3). The distribution defined by $F$ is called a *mixture* of the distributions defined by $F_{1}$ and $F_{2}$.

(b) Consider creating an r.v. in the following way. Flip a coin with probability $p$ of Heads. If the coin lands Heads, generate an r.v. according to $F_{1}$; if the coin lands Tails, generate an r.v. according to $F_{2}$. Show that the r.v. obtained in this way has CDF $F$.
10. (a) Is there a discrete distribution with support $1,2,3,\dots$, such that the value of the PMF at $n$ is proportional to $1/n$?

Hint: See the math appendix for a review of some facts about series.

(b) Is there a discrete distribution with support $1,2,3,\dots$, such that the value of the PMF at $n$ is proportional to $1/n^{2}$?
11. 1 Let $X$ be an r.v. whose possible values are $0,1,2,\dots$, with CDF $F$. In some countries, rather than using a CDF, the convention is to use the function $G$ defined by $G(x)=P(X<x)$ to specify a distribution. Find a way to convert from $F$ to $G$, i.e., if $F$ is a known function, show how to obtain $G(x)$ for all real $x$.
12. (a) Give an example of r.v.s $X$ and $Y$ such that $F_{X}(x)\leq F_{Y}(x)$ for all $x$, where the inequality is strict for some $x$. Here $F_{X}$ is the CDF of $X$ and $F_{Y}$ is the CDF of $Y$. For the example you gave, sketch the CDFs of both $X$ and $Y$ on the same axes. Then sketch their PMFs on a second set of axes.

(b) In Part (a), you found an example of two different CDFs where the first is less than or equal to the second everywhere. Is it possible to find two different PMFs where the first is less than or equal to the second everywhere? In other words, find discrete r.v.s $X$ and $Y$ such that $P(X=x)\leq P(Y=x)$ for all $x$, where the inequality is strict for some $x$, or show that it is impossible to find such r.v.s.
13. Let $X,Y,Z$ be discrete r.v.s such that $X$ and $Y$ have the same conditional distribution given $Z$, i.e., for all $a$ and $z$ we have

$P(X=a|Z=z)=P(Y=a|Z=z).$

Show that $X$ and $Y$ have the same distribution (unconditionally, not just when given $Z$).
14. Let $X$ be the number of purchases that Fred will make on the online site for a certain company (in some specified time period). Suppose that the PMF of $X$ is $P(X=k)=e^{-\lambda}\lambda^{k}/k!$ for $k=0,1,2,\dots$. This distribution is called the *Poisson distribution* with parameter $\lambda$, and it will be studied extensively in later chapters.

(a) Find $P(X\geq 1)$ and $P(X\geq 2)$ without summing infinite series.

(b) Suppose that the company only knows about people who have made at least one purchase on their site (a user sets up an account to make a purchase, but someone who has never made a purchase there doesn’t appear in the customer database). If the company computes the number of purchases for everyone in their database, then these data are draws from the *conditional* distribution of the number of purchases, given that at least one purchase is made. Find the conditional PMF of $X$ given $X\geq 1$. (This conditional distribution is called a *truncated Poisson distribution*.)

Introduction to Probability

# Named distributions

15. Find the CDF of an r.v. $X\sim\mathrm{DUnif}(1,2,\ldots,n).$

16. Let $X\sim\mathrm{DUnif}(C)$, and $B$ be a nonempty subset of $C$. Find the conditional distribution of $X$, given that $X$ is in $B$.

17. An airline overbooks a flight, selling more tickets for the flight than there are seats on the plane (figuring that it’s likely that some people won’t show up). The plane has 100 seats, and 110 people have booked the flight. Each person will show up for the flight with probability 0.9, independently. Find the probability that there will be enough seats for everyone who shows up for the flight.

18. $\circledS$ (a) In the World Series of baseball, two teams (call them A and B) play a sequence of games against each other, and the first team to win four games wins the series. Let $p$ be the probability that A wins an individual game, and assume that the games are independent. What is the probability that team A wins the series?

(b) Give a clear intuitive explanation of whether the answer to (a) depends on whether the teams always play 7 games (and whoever wins the majority wins the series), or the teams stop playing more games as soon as one team has won 4 games (as is actually the case in practice: once the match is decided, the two teams do not keep playing more games).

19. In a chess tournament, $n$ games are being played, independently. Each game ends in a win for one player with probability 0.4 and ends in a draw (tie) with probability 0.6. Find the PMFs of the number of games ending in a draw, and of the number of players whose games end in draws.

20. Suppose that a lottery ticket has probability $p$ of being a winning ticket, independently of other tickets. A gambler buys 3 tickets, hoping this will triple the chance of having at least one winning ticket.

(a) What is the distribution of how many of the 3 tickets are winning tickets?

(b) Show that the probability that at least 1 of the 3 tickets is winning is $3p - 3p^{2} + p^{3}$, in two different ways: by using inclusion-exclusion, and by taking the complement of the desired event and then using the PMF of a certain named distribution.

(c) Show that the gambler’s chances of having at least one winning ticket do not quite triple (compared with buying only one ticket), but that they do approximately triple if $p$ is small.

21. $\circledS$ Let $X \sim \operatorname{Bin}(n, p)$ and $Y \sim \operatorname{Bin}(m, p)$, independent of $X$. Show that $X - Y$ is not Binomial.

22. There are two coins, one with probability $p_1$ of Heads and the other with probability $p_2$ of Heads. One of the coins is randomly chosen (with equal probabilities for the two coins). It is then flipped $n \geq 2$ times. Let $X$ be the number of times it lands Heads.

(a) Find the PMF of $X$.

(b) What is the distribution of $X$ if $p_1 = p_2$?

(c) Give an intuitive explanation of why $X$ is not Binomial for $p_1 \neq p_2$ (its distribution is called a mixture of two Binomials). You can assume that $n$ is large for your explanation, so that the frequentist interpretation of probability can be applied.

23. There are $n$ people eligible to vote in a certain election. Voting requires registration. Decisions are made independently. Each of the $n$ people will register with probability $p_1$. Given that a person registers, they will vote with probability $p_2$. Given that a person votes, they will vote for Kodos (who is one of the candidates) with probability $p_3$. What is the distribution of the number of votes for Kodos (give the PMF, fully simplified, or the name of the distribution, including its parameters)?

24. Let $X$ be the number of Heads in 10 fair coin tosses.

1. Find the conditional PMF of $X$, given that the first two tosses both land Heads.
2. Find the conditional PMF of $X$, given that at least two tosses land Heads.
25. Alice flips a fair coin $n$ times and Bob flips another fair coin $n+1$ times, resulting in independent $X\sim{\rm Bin}(n,\frac{1}{2})$ and $Y\sim{\rm Bin}(n+1,\frac{1}{2})$.

1. Show that $P(X<Y)=P(n-X<n+1-Y)$.
2. Compute $P(X<Y)$.

Hint: Use (a) and the fact that $X$ and $Y$ are integer-valued.
26. If $X\sim{\rm HGeom}(w,b,n)$, what is the distribution of $n-X$? Give a short proof.
27. Recall de Montmort’s matching problem from Chapter 1: in a deck of $n$ cards labeled 1 through $n$, a match occurs when the number on the card matches the card’s position in the deck. Let $X$ be the number of matching cards. Is $X$ Binomial? Is $X$ Hypergeometric?
28. There are $n$ eggs, each of which hatches a chick with probability $p$ (independently). Each of these chicks survives with probability $r$, independently. What is the distribution of the number of chicks that hatch? What is the distribution of the number of chicks that survive? (Give the PMFs; also give the names of the distributions and their parameters, if applicable.)
29. A sequence of $n$ independent experiments is performed. Each experiment is a success with probability $p$ and a failure with probability $q=1-p$. Show that conditional on the number of successes, all valid possibilities for the list of outcomes of the experiment are equally likely.
30. A certain company has $n+m$ employees, consisting of $n$ women and $m$ men. The company is deciding which employees to promote.

1. Suppose for this part that the company decides to promote $t$ employees, where $1\leq t\leq n+m$, by choosing $t$ random employees (with equal probabilities for each set of $t$ employees). What is the distribution of the number of women who get promoted?
2. Now suppose that instead of having a predetermined number of promotions to give, the company decides independently for each employee, promoting the employee with probability $p$. Find the distributions of the number of women who are promoted, the number of women who are not promoted, and the number of employees who are promoted.
3. In the set-up from (b), find the conditional distribution of the number of women who are promoted, given that exactly $t$ employees are promoted.
31. Once upon a time, a famous statistician offered tea to a lady. The lady claimed that she could tell whether milk had been added to the cup before or after the tea. The statistician decided to run some experiments to test her claim.

1. The lady is given 6 cups of tea, where it is known in advance that 3 will be milk-first and 3 will be tea-first, in a completely random order. The lady gets to taste each and then guess which 3 were milk-first. Assume for this part that she has no ability whatsoever to distinguish milk-first from tea-first cups of tea. Find the probability that at least 2 of her 3 guesses are correct.
2. Now the lady is given one cup of tea, with probability $1/2$ of it being milk-first. She needs to say whether she thinks it was milk-first. Let $p_{1}$ be the lady’s probability of being correct given that it was milk-first, and $p_{2}$ be her probability of being correct given that it was tea-first. She claims that the cup was milk-first. Find the posterior odds that the cup is milk-first, given this information.

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

(b) Use Stirling’s approximation, which approximates the factorial function as

$n!\approx\sqrt{2\pi n}\left(\frac{n}{e}\right)^{n},$

to find a simple approximation to the probability of a tie. Your answer should be of the form $1/\sqrt{cn}$, with $c$ a constant (which you should specify).
- A message is sent over a noisy channel. The message is a sequence $x_{1},x_{2},\ldots,x_{n}$ of $n$ bits ($x_{i}\in\{0,1\}$). Since the channel is noisy, there is a chance that any bit might be corrupted, resulting in an error (a $0$ becomes a $1$ or vice versa). Assume that the error events are independent. Let $p$ be the probability that an individual bit has an error ($0<p<1/2$). Let $y_{1},y_{2},\ldots,y_{n}$ be the received message (so $y_{i}=x_{i}$ if there is no error in that bit, but $y_{i}=1-x_{i}$ if there is an error there).

To help detect errors, the $n$th bit is reserved for a parity check: $x_{n}$ is defined to be $0$ if $x_{1}+x_{2}+\cdots+x_{n-1}$ is even, and $1$ if $x_{1}+x_{2}+\cdots+x_{n-1}$ is odd. When the message is received, the recipient checks whether $y_{n}$ has the same parity as $y_{1}+y_{2}+\cdots+y_{n-1}$. If the parity is wrong, the recipient knows that at least one error occurred; otherwise, the recipient assumes that there were no errors.

(a) For $n=5,p=0.1$, what is the probability that the received message has errors which go undetected?

(b) For general $n$ and $p$, write down an expression (as a sum) for the probability that the received message has errors which go undetected.

(c) Give a simplified expression, not involving a sum of a large number of terms, for the probability that the received message has errors which go undetected.

Hint for (c): Letting

$a=\sum_{k\text{ even, }k\geq 0}\binom{n}{k}p^{k}(1-p)^{n-k}\text{ and }b=\sum_{k\text{ odd, }k\geq 1}\binom{n}{k}p^{k}(1-p)^{n-k},$

the binomial theorem makes it possible to find simple expressions for $a+b$ and $a-b$, which then makes it possible to obtain $a$ and $b$.

## Independence of r.v.s

- (a) Give an example of dependent r.v.s $X$ and $Y$ such that $P(X<Y)=1$.
- (b) Give an example of independent r.v.s $X$ and $Y$ such that $P(X<Y)=1$.
- Give an example of two discrete random variables $X$ and $Y$ on the same sample space such that $X$ and $Y$ have the same distribution, with support $\{1,2,\ldots,10\}$, but the event $X=Y$ *never* occurs. If $X$ and $Y$ are independent, is it still possible to construct such an example?
- Suppose $X$ and $Y$ are discrete r.v.s such that $P(X=Y)=1$. This means that $X$ and $Y$ always take on the same value.

(a) Do $X$ and $Y$ have the same PMF?

(b) Is it possible for $X$ and $Y$ to be independent?
- If $X,Y,Z$ are r.v.s such that $X$ and $Y$ are independent and $Y$ and $Z$ are independent, does it follow that $X$ and $Z$ are independent?

Hint: Think about simple and extreme examples.

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

46. Independent Bernoulli trials are performed, with success probability 1/2 for each trial. An important question that often comes up in such settings is how many trials to perform. Many controversies have arisen in statistics over the issue of how to analyze data coming from an experiment where the number of trials can depend on the data collected so far.

For example, if we can follow the rule “keep performing trials until there are more than twice as many failures as successes, and then stop”, then naively looking at the ratio of failures to successes (if and when the process stops) will give more than 2:1 rather than the true theoretical 1:1 ratio; this could be a very misleading result! However, it might *never* happen that there are more than twice as many failures as successes; in this problem, you will find the probability of that happening.

(a) Two gamblers, A and B, make a series of bets, where each has probability 1/2 of winning a bet, but A gets $2 for each win and loses $1 for each loss (a very favorable game for A!). Assume that the gamblers are allowed to borrow money, so they can and do gamble forever. Let $p_{k}$ be the probability that A, starting with $$k, will ever reach $0, for each $k\geq 0$. Explain how this story relates to the original problem, and how the original problem can be solved if we can find $p_{k}$.

(b) Find $p_{k}$.

Hint: As in the gambler’s ruin, set up and solve a difference equation for $p_{k}$. We have $p_{k}\to 0$ as $k\to\infty$ (you don’t need to prove this, but it should make sense since the game is so favorable to A, which will result in A’s fortune going to $\infty$; a formal proof, not required here, could be done using the *law of large numbers*, an important theorem from Chapter 10). The solution can be written neatly in terms of the golden ratio.

(c) Find the probability of ever having more than twice as many failures as successes with independent Bern(1/2) trials, as originally desired.
47. A copy machine is used to make $n$ pages of copies per day. The machine has two trays in which paper gets loaded, and each page used is taken randomly and independently from one of the trays. At the beginning of the day, the trays are refilled so that they each have $m$ pages.

(a) Let pbinom($x,n,p$) be the CDF of the Bin($n,p$) distribution, evaluated at $x$. In terms of pbinom, find a simple expression for the probability that both trays have enough paper on any particular day, when this probability is strictly between 0 and 1 (also specify the values of $m$ for which the probability is 0 and the values for which it is 1).

Hint: Be careful about whether inequalities are strict, since the Binomial is discrete.

(b) Using a computer, find the smallest value of $m$ for which there is at least a 95% chance that both trays have enough paper on a particular day, for $n=10,n=100,n=1000$, and $n=10000$.

Hint: If you use R, you may find the following commands useful:
g <- function(m,n) *[your answer from (a)]* defines a function $g$ such that $g(m,n)$ is your answer from (a), g(1:100,100) gives the vector $(g(1,100),\ldots,g(100,100))$, which(v>0.95) gives the indices of the components of vector v that exceed 0.95, and min(w) gives the minimum of a vector w.

![img-53.jpeg](img-53.jpeg)

# Taylor &amp; Francis

Taylor &amp; Francis Group

http://taylorandfrancis.com

4.1 Definition of expectation

In the previous chapter, we introduced the *distribution* of a random variable, which gives us full information about the probability that the r.v. will fall into any particular set. For example, we can say how likely it is that the r.v. will exceed 1000, that it will equal 5, or that it will be in the interval $[0,7]$. It can be unwieldy to manage so many probabilities though, so often we want just one number summarizing the “average” value of the r.v.

There are several senses in which the word “average” is used, but by far the most commonly used is the *mean* of an r.v., also known as its *expected value*. In addition, much of statistics is about understanding *variability* in the world, so it is often important to know how “spread out” the distribution is; we will formalize this with the concepts of *variance* and *standard deviation*. As we’ll see, variance and standard deviation are defined in terms of expected values, so the uses of expected values go far beyond just computing averages.

Given a list of numbers $x_{1},x_{2},\ldots,x_{n}$, the familiar way to average them is to add them up and divide by $n$. This is called the *arithmetic mean*, and is defined by

$\bar{x}=\frac{1}{n}\sum_{j=1}^{n}x_{j}.$

More generally, we can define a *weighted mean* of $x_{1},\ldots,x_{n}$ as

$\text{weighted-mean}(x)=\sum_{j=1}^{n}x_{j}p_{j},$

where the weights $p_{1},\ldots,p_{n}$ are pre-specified nonnegative numbers that add up to 1 (so the unweighted mean $\bar{x}$ is obtained when $p_{j}=1/n$ for all $j$).

The definition of expectation for a discrete r.v. is inspired by the weighted mean of a list of numbers, with weights given by probabilities.

###### Definition 4.1.1 (Expectation of a discrete r.v.).

The *expected value* (also called the *expectation* or *mean*) of a discrete r.v. $X$ whose distinct possible values are

$x_{1},x_{2},\dots$ is defined by

$E(X)=\sum_{j=1}^{\infty}x_{j}P(X=x_{j}).$

If the support is finite, then this is replaced by a finite sum. We can also write

$E(X)=\sum_{x}\underbrace{x}_{\text{value}}\underbrace{P(X=x)}_{\text{PMF at }x},$

where the sum is over the support of $X$ (in any case, $xP(X=x)$ is $0$ for any $x$ not in the support). The expectation is undefined if $\sum_{j=1}^{\infty}|x_{j}|P(X=x_{j})$ diverges, since then the series for $E(X)$ diverges or its value depends on the order in which the $x_{j}$ are listed.

In words, the expected value of $X$ is a weighted average of the possible values that $X$ can take on, weighted by their probabilities. Let’s check that the definition makes sense in a few simple examples:

1. Let $X$ be the result of rolling a fair $6$-sided die, so $X$ takes on the values $1,2,3,4,5,6$, with equal probabilities. Intuitively, we should be able to get the average by adding up these values and dividing by $6$. Using the definition, the expected value is

$E(X)=\frac{1}{6}(1+2+\dots+6)=3.5,$

as we expected. Note that $X$ *never* equals its mean in this example. This is similar to the fact that the average number of children per household in some country could be $1.8$, but that doesn’t mean that a typical household has $1.8$ children!
2. Let $X\sim\text{Bern}(p)$ and $q=1-p$. Then

$E(X)=1p+0q=p,$

which makes sense intuitively since it is between the two possible values of $X$, compromising between $0$ and $1$ based on how likely each is. This is illustrated in Figure 4.1 for a case with $p<1/2$: two pebbles are being balanced on a seesaw. For the seesaw to balance, the fulcrum (shown as a triangle) must be at $p$, which in physics terms is the *center of mass*.

The frequentist interpretation would be to consider a large number of independent Bernoulli trials, each with probability $p$ of success. Writing $1$ for “success” and $0$ for “failure”, in the long run we would expect to have data consisting of a list of numbers where the proportion of $1$’s is very close to $p$. The average of a list of $0$’s and $1$’s *is* the proportion of $1$’s.
3. Let $X$ have $3$ distinct possible values, $a_{1},a_{2},a_{3}$, with probabilities $p_{1},p_{2},p_{3}$, respectively. Imagine running a simulation where $n$ independent draws

Expectation

![img-54.jpeg](img-54.jpeg)

# FIGURE 4.1

Center of mass of two pebbles, depicting that  $E(X) = p$  for  $X \sim \operatorname{Bern}(p)$ . Here  $q$  and  $p$  denote the masses of the two pebbles.

from the distribution of  $X$  are generated. For  $n$  large, we would expect to have about  $p_1n a_1$ 's,  $p_2n a_2$ 's, and  $p_3n a_3$ 's. (We will look at a more mathematical version of this example when we study the law of large numbers in Chapter 10.) If the simulation results are close to these expected results, then the arithmetic mean of the simulation results is approximately

$$
\frac {p _ {1} n \cdot a _ {1} + p _ {2} n \cdot a _ {2} + p _ {3} n \cdot a _ {3}}{n} = p _ {1} a _ {1} + p _ {2} a _ {2} + p _ {3} a _ {3} = E (X).
$$

Note that  $E(X)$  depends only on the distribution of  $X$ . This follows directly from the definition, but is worth recording since it is fundamental.

Proposition 4.1.2. If  $X$  and  $Y$  are discrete r.v.s with the same distribution, then  $E(X) = E(Y)$  (if either side exists).

Proof. In the definition of  $E(X)$ , we only need to know the PMF of  $X$ .

The converse of the above proposition is false since the expected value is just a one-number summary, not nearly enough to specify the entire distribution; it's a measure of where the "center" is but does not determine, for example, how spread out the distribution is or how likely the r.v. is to be positive. Figure 4.2 shows an example of two different PMFs with the same expected value (balancing point).

$\star 4.1.3$  (Replacing an r.v. by its expectation). For any discrete r.v.  $X$ , the expected value  $E(X)$  is a number (if it exists). A common mistake is to replace an r.v. by its expectation without justification, which is wrong both mathematically ( $X$  is a function,  $E(X)$  is a constant) and statistically (it ignores the variability of  $X$ ), except in the degenerate case where  $X$  is a constant.

Notation 4.1.4. We often abbreviate  $E(X)$  to  $EX$ . Similarly, we often abbreviate  $E(X^2)$  to  $EX^2$ , and  $E(X^n)$  to  $EX^n$ .

$\star 4.1.5$ . Paying attention to the order of operations is crucial when working with expectation. As stated above,  $EX^2$  is the expectation of the random variable  $X^2$ , not the square of the number  $EX$ . Unless the parentheses explicitly indicate otherwise,

Introduction to Probability

![img-55.jpeg](img-55.jpeg)
FIGURE 4.2

![img-56.jpeg](img-56.jpeg)

The expected value does not determine the distribution: different PMFs can have the same balancing point.

for the expectation of an r.v. raised to a power, first we take the power and then we take the expectation. For example,  $E(X - 1)^4$  is  $E\left((X - 1)^4\right)$ , not  $(E(X - 1))^4$ .

# 4.2 Linearity of expectation

The most important property of expectation is linearity: the expected value of a sum of r.v.s is the sum of the individual expected values.

Theorem 4.2.1 (Linearity of expectation). For any r.v.s  $X, Y$  and any constant  $c$ ,

$$
E (X + Y) = E (X) + E (Y),
$$

$$
E (c X) = c E (X).
$$

The second equation says that we can take out constant factors from an expectation; this is both intuitively reasonable and easily verified from the definition. The first equation,  $E(X + Y) = E(X) + E(Y)$ , also seems reasonable when  $X$  and  $Y$  are independent. What may be surprising is that it holds even if  $X$  and  $Y$  are dependent! To build intuition for this, consider the extreme case where  $X$  always equals  $Y$ . Then  $X + Y = 2X$ , and both sides of  $E(X + Y) = E(X) + E(Y)$  are equal to  $2E(X)$ , so linearity still holds even in the most extreme case of dependence.

Linearity is true for all r.v.s, not just discrete r.v.s, but in this chapter we will prove it only for discrete r.v.s. Before proving linearity, it is worthwhile to recall some basic facts about averages. If we have a list of numbers, say  $(1,1,1,1,1,3,3,5)$ , we can calculate their mean by adding all the values and dividing by the length of the list, so that each element of the list gets a weight of  $\frac{1}{8}$ :

$$
\frac {1}{8} (1 + 1 + 1 + 1 + 1 + 3 + 3 + 5) = 2.
$$

Expectation

But another way to calculate the mean is to group together all the 1's, all the 3's, and all the 5's, and then take a weighted average, giving appropriate weights to 1's, 3's, and 5's:

$$
\frac {5}{8} \cdot 1 + \frac {2}{8} \cdot 3 + \frac {1}{8} \cdot 5 = 2.
$$

This insight—that averages can be calculated in two ways, ungrouped or grouped—is all that is needed to prove linearity! Recall that  $X$  is a function which assigns a real number to every outcome  $s$  in the sample space. The r.v.  $X$  may assign the same value to multiple sample outcomes. When this happens, our definition of expectation groups all these outcomes together into a super-pebble whose weight,  $P(X = x)$ , is the total weight of the constituent pebbles. This grouping process is illustrated in Figure 4.3 for a hypothetical r.v. taking values in  $\{0,1,2\}$ . So our definition of expectation corresponds to the grouped way of taking averages.

![img-57.jpeg](img-57.jpeg)

![img-58.jpeg](img-58.jpeg)

# FIGURE 4.3

Left:  $X$  assigns a number to each pebble in the sample space. Right: Grouping the pebbles by the value that  $X$  assigns to them, the 9 pebbles become 3 super-pebbles. The weight of a super-pebble is the sum of the weights of the constituent pebbles.

The advantage of this definition is that it allows us to work with the distribution of  $X$  directly, without returning to the sample space. The disadvantage comes when we have to prove theorems like this one, for if we have another r.v.  $Y$  on the same sample space, the super-pebbles created by  $Y$  are different from those created from  $X$ , with different weights  $P(Y = y)$ ; this makes it difficult to combine  $\sum_{x} xP(X = x)$  and  $\sum_{y} yP(Y = y)$ .

Fortunately, we know there's another equally valid way to calculate an average: we can take a weighted average of the values of individual pebbles. In other words, if  $X(s)$  is the value that  $X$  assigns to pebble  $s$ , we can take the weighted average

$$
E (X) = \sum_ {s} X (s) P (\{s \}),
$$

where  $P(\{s\})$  is the weight of pebble  $s$ . This corresponds to the ungrouped way of taking averages. The advantage of this definition is that it breaks down the sample space into the smallest possible units, so we are now using the same weights  $P(\{s\})$  for every random variable defined on this sample space. If  $Y$  is another random

variable, then

$E(Y)=\sum_{s}Y(s)P(\{s\}).$

We *can* combine $\sum_{s}X(s)P(\{s\})$ and $\sum_{s}Y(s)P(\{s\})$, which gives

$E(X)+E(Y)=\sum_{s}X(s)P(\{s\})+\sum_{s}Y(s)P(\{s\})=\sum_{s}(X+Y)(s)P(\{s\})=E(X+Y).$

Another intuition for linearity of expectation is via the concept of *simulation*. If we simulate many, many times from the distribution of $X$, the histogram of the simulated values will look very much like the true PMF of $X$. In particular, the *arithmetic mean* of the simulated values will be very close to the true value of $E(X)$ (the precise nature of this convergence is described by the law of large numbers, an important theorem that we will discuss in detail in Chapter 10).

Let $X$ and $Y$ be r.v.s summarizing a certain experiment. Suppose we perform the experiment $n$ times, where $n$ is a very large number, and we write down the values realized by $X$ and $Y$ each time. For each repetition of the experiment, we obtain an $X$ value, a $Y$ value, and (by adding them) an $X+Y$ value. In Figure 4.4, each row represents a repetition of the experiment. The left column contains the draws of $X$, the middle column contains the draws of $Y$, and the right column contains the draws of $X+Y$.

There are two ways to calculate the sum of all the numbers in the last column. The straightforward way is just to add all the numbers in that column. But an equally valid way is to add all the numbers in the first column, add all the numbers in the second column, and then add the two column sums.

Dividing by $n$ everywhere, what we’ve argued is that the following procedures are equivalent:

- Taking the arithmetic mean of all the numbers in the last column. By the law of large numbers, this is very close to $E(X+Y)$.
- Taking the arithmetic mean of the first column and the arithmetic mean of the second column, then adding the two column means. By the law of large numbers, this is very close to $E(X)+E(Y)$.

Linearity of expectation thus emerges as a simple fact about arithmetic (we’re just adding numbers in two different orders)! Notice that nowhere in our argument did we rely on whether $X$ and $Y$ were independent. In fact, in Figure 4.4, $X$ and $Y$ appear to be dependent: $Y$ tends to be large when $X$ is large, and $Y$ tends to be small when $X$ is small (in the language of Chapter 7, we say that $X$ and $Y$ are *positively correlated*). But this dependence is irrelevant: shuffling the draws of $Y$ could completely alter the pattern of dependence between $X$ and $Y$, but would have no effect on the column sums.

Expectation

|  X | Y | X+Y  |
| --- | --- | --- |
|  3 | 4 | 7  |
|  2 | 2 | 4  |
|  6 | 8 | 14  |
|  10 | 23 | 33  |
|  1 | -3 | -2  |
|  1 | 0 | 1  |
|  5 | 9 | 14  |
|  4 | 1 | 5  |
|  : | : | :  |

$$
\frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} + \frac {1}{n} \sum_ {i = 1} ^ {n} y _ {i} = \frac {1}{n} \sum_ {i = 1} ^ {n} (x _ {i} + y _ {i})
$$

$$
E (X) + E (Y) = E (X + Y)
$$

# FIGURE 4.4

Intuitive view of linearity of expectation. Each row represents a repetition of the experiment; the three columns are the realized values of  $X$ ,  $Y$ , and  $X + Y$ , respectively. Adding all the numbers in the last column is equivalent to summing the first column and the second column separately, then adding the two column sums. So the mean of the last column is the sum of the first and second column means; this is linearity of expectation.

Linearity is an extremely handy tool for calculating expected values, often allowing us to bypass the definition of expected value altogether. Let’s use linearity to find the expectations of the Binomial and Hypergeometric distributions.

###### Example 4.2.2 (Binomial expectation).

For $X\sim\text{Bin}(n,p)$, let’s find $E(X)$ in two ways. By definition of expectation,

$E(X)=\sum_{k=0}^{n}kP(X=k)=\sum_{k=0}^{n}k\binom{n}{k}p^{k}q^{n-k}.$

From Example 1.5.2, we know $k\binom{n}{k}=n\binom{n-1}{k-1}$, so

$\sum_{k=0}^{n}k\binom{n}{k}p^{k}q^{n-k}$ $=n\sum_{k=0}^{n}\binom{n-1}{k-1}p^{k}q^{n-k}$
$=np\sum_{k=1}^{n}\binom{n-1}{k-1}p^{k-1}q^{n-k}$
$=np\sum_{j=0}^{n-1}\binom{n-1}{j}p^{j}q^{n-1-j}$
$=np.$

The sum in the penultimate line equals $1$ because it is the sum of the $\text{Bin}(n-1,p)$ PMF (or by the binomial theorem). Therefore, $E(X)=np$.

This proof required us to remember combinatorial identities and manipulate binomial coefficients. Using linearity of expectation, we obtain a *much* shorter path to the same result. Let’s write $X$ as the sum of $n$ independent $\text{Bern}(p)$ r.v.s:

$X=I_{1}+\cdots+I_{n},$

where each $I_{j}$ has expectation $E(I_{j})=1p+0q=p$. By linearity,

$E(X)=E(I_{1})+\cdots+E(I_{n})=np.\qed$

###### Example 4.2.3 (Hypergeometric expectation).

Let $X\sim\text{HGeom}(w,b,n)$, interpreted as the number of white balls in a sample of size $n$ drawn without replacement from an urn with $w$ white and $b$ black balls. As in the Binomial case, we can write $X$ as a sum of Bernoulli random variables,

$X=I_{1}+\cdots+I_{n},$

where $I_{j}$ equals $1$ if the $j$th ball in the sample is white and $0$ otherwise. By symmetry, $I_{j}\sim\text{Bern}(p)$ with $p=w/(w+b)$, since unconditionally the $j$th ball drawn is equally likely to be any of the balls.

Unlike in the Binomial case, the $I_{j}$ are not independent, since the sampling is without replacement: given that a ball in the sample is white, there is a lower

chance that another ball in the sample is white. However, linearity still holds for dependent random variables! Thus,

$E(X)=nw/(w+b).\qed$

As another example of the power of linearity, we can give a quick proof of the intuitive idea that “bigger r.v.s have bigger expectations”.

###### Proposition 4.2.4 (Monotonicity of expectation).

Let $X$ and $Y$ be r.v.s such that $X\geq Y$ with probability 1. Then $E(X)\geq E(Y)$, with equality holding if and only if $X=Y$ with probability 1.

###### Proof.

This result holds for all r.v.s, but we will prove it only for discrete r.v.s since this chapter focuses on discrete r.v.s. The r.v. $Z=X-Y$ is nonnegative (with probability 1), so $E(Z)\geq 0$ since $E(Z)$ is defined as a sum of nonnegative terms. By linearity,

$E(X)-E(Y)=E(X-Y)\geq 0,$

as desired. If $E(X)=E(Y)$, then by linearity we also have $E(Z)=0$, which implies that $P(X=Y)=P(Z=0)=1$ since if even one term in the sum defining $E(Z)$ is positive, then the whole sum is positive. ∎

### 4.3 Geometric and Negative Binomial

We now introduce two more famous discrete distributions, the Geometric and Negative Binomial, and calculate their expected values.

###### Story 4.3.1 (Geometric distribution).

Consider a sequence of independent Bernoulli trials, each with the same success probability $p\in(0,1)$, with trials performed until a success occurs. Let $X$ be the number of *failures* before the first successful trial. Then $X$ has the *Geometric distribution* with parameter $p$; we denote this by $X\sim\operatorname{Geom}(p)$. ∎

For example, if we flip a fair coin until it lands Heads for the first time, then the number of Tails before the first occurrence of Heads is distributed as $\operatorname{Geom}(1/2)$.

To get the Geometric PMF from the story, imagine the Bernoulli trials as a string of 0’s (failures) ending in a single 1 (success). Each 0 has probability $q=1-p$ and the final 1 has probability $p$, so a string of $k$ failures followed by one success has probability $q^{k}p$.

###### Theorem 4.3.2 (Geometric PMF).

If $X\sim\operatorname{Geom}(p)$, then the PMF of $X$ is

$P(X=k)=q^{k}p$

for $k=0,1,2,\dots$, where $q=1-p$.

######

This is a valid PMF because, summing a geometric series (see the math appendix for a review of geometric series), we have

$\sum_{k=0}^{\infty}q^{k}p=p\sum_{k=0}^{\infty}q^{k}=p\cdot\frac{1}{1-q}=1.$

Just as the binomial theorem shows that the Binomial PMF is valid, a geometric series shows that the Geometric PMF is valid! A geometric series can also be used to obtain the Geometric CDF.

###### Theorem 4.3.3 (Geometric CDF).

If $X\sim\mathrm{Geom}(p)$, then the CDF of $X$ is

\[ F(x)=\begin{cases}1-q^{\lfloor x\rfloor+1},\text{ if }x\geq 0;\\
0,\text{ if }x<0,\end{cases} \]

where $q=1-p$ and $\lfloor x\rfloor$ is the greatest integer less than or equal to $x$.

###### Proof.

Let $F$ be the CDF of $X$. We will find $F(x)$ first for the case $x<0$, then for the case that $x$ is a nonnegative integer, and lastly for the case that $x$ is a nonnegative real number. For $x<0$, $F(x)=0$ since $X$ can’t be negative. For $n$ a nonnegative integer,

$F(n)=\sum_{k=0}^{n}P(X=k)=p\sum_{k=0}^{n}q^{k}=p\cdot\frac{1-q^{n+1}}{1-q}=1-q^{n+1}.$

We can also get the same result from the fact that the event $X\geq n+1$ means that the first $n+1$ trials were failures:

$F(n)=1-P(X>n)=1-P(X\geq n+1)=1-q^{n+1}.$

For real $x\geq 0$,

$F(x)=P(X\leq x)=P(X\leq\lfloor x\rfloor),$

since $X$ always takes on integer values. For example,

$P(X\leq 3.7)=P(X\leq 3)+P(3<X\leq 3.7)=P(X\leq 3).$

Therefore, $F$ is as claimed. ∎

Figure 4.3 displays the $\mathrm{Geom}(0.5)$ PMF and CDF from $0$ to $6$. All Geometric PMFs have a similar shape; the greater the success probability $p$, the more quickly the PMF decays to $0$.

$\text{\text{✳ 4.3.4 (Conventions for the Geometric).}$ There are differing conventions for the definition of the Geometric distribution; some sources define the Geometric as the total number of *trials*, including the success. In this book, the Geometric distribution excludes the success, and the *First Success* distribution includes the success.

Expectation

![img-59.jpeg](img-59.jpeg)
FIGURE 4.5

![img-60.jpeg](img-60.jpeg)

Geom(0.5) PMF and CDF.

Definition 4.3.5 (First Success distribution). In a sequence of independent Bernoulli trials with success probability  $p$ , let  $Y$  be the number of trials until the first successful trial, including the success. Then  $Y$  has the First Success distribution with parameter  $p$ ; we denote this by  $Y \sim \mathrm{FS}(p)$ .

It is easy to convert back and forth between the two but important to be careful about which convention is being used. If  $Y \sim \mathrm{FS}(p)$  then  $Y - 1 \sim \mathrm{Geom}(p)$ , and we can convert between the PMFs of  $Y$  and  $Y - 1$  by writing

$$
P (Y = k) = P (Y - 1 = k - 1).
$$

Conversely, if  $X \sim \operatorname{Geom}(p)$ , then  $X + 1 \sim \operatorname{FS}(p)$ .

Example 4.3.6 (Geometric expectation). Let  $X \sim \operatorname{Geom}(p)$ . By definition,

$$
E (X) = \sum_ {k = 0} ^ {\infty} k q ^ {k} p,
$$

where  $q = 1 - p$ . This sum looks unpleasant; it's not a geometric series because of the extra  $k$  multiplying each term. But we notice that each term looks similar to  $kq^{k-1}$ , the derivative of  $q^k$  (with respect to  $q$ ), so let's start there:

$$
\sum_ {k = 0} ^ {\infty} q ^ {k} = \frac {1}{1 - q}.
$$

This geometric series converges since  $0 &lt; q &lt; 1$ . Differentiating both sides with respect to  $q$ , we get

$$
\sum_ {k = 0} ^ {\infty} k q ^ {k - 1} = \frac {1}{(1 - q) ^ {2}}.
$$

Finally, if we multiply both sides by $pq$, we recover the original sum we wanted to find:

$E(X)=\sum_{k=0}^{\infty}kq^{k}p=pq\sum_{k=0}^{\infty}kq^{k-1}=pq\frac{1}{(1-q)^{2}}=\frac{q}{p}.$

In Example 9.1.8, we will give a story proof of the same result, based on first-step analysis: condition on the result of the first trial in the story interpretation of $X$. If the first trial is a success, we know $X=0$ and if it’s a failure, we have one wasted trial and then are back where we started. ∎

###### Example 4.3.7 (First Success expectation).

Since we can write $Y\sim\text{FS}(p)$ as $Y=X+1$ where $X\sim\text{Geom}(p)$, we have

$E(Y)=E(X+1)=\frac{q}{p}+1=\frac{1}{p}.\qed$

The Negative Binomial distribution generalizes the Geometric distribution: instead of waiting for just one success, we can wait for any predetermined number $r$ of successes.

###### Story 4.3.8 (Negative Binomial distribution).

In a sequence of independent Bernoulli trials with success probability $p$, if $X$ is the number of *failures* before the $r$th success, then $X$ is said to have the *Negative Binomial distribution* with parameters $r$ and $p$, denoted $X\sim\text{NBin}(r,p)$. ∎

Both the Binomial and the Negative Binomial distributions are based on independent Bernoulli trials; they differ in the *stopping rule* and in what they are counting. The Binomial counts the number of successes in a fixed number of *trials*; the Negative Binomial counts the number of failures until a fixed number of *successes*.

In light of these similarities, it comes as no surprise that the derivation of the Negative Binomial PMF bears a resemblance to the corresponding derivation for the Binomial.

###### Theorem 4.3.9 (Negative Binomial PMF).

If $X\sim\text{NBin}(r,p)$, then the PMF of $X$ is

$P(X=n)=\binom{n+r-1}{r-1}p^{r}q^{n}$

for $n=0,1,2\ldots$, where $q=1-p$.

###### Proof.

Imagine a string of 0’s and 1’s, with 1’s representing successes. The probability of any *specific* string of $n$ 0’s and $r$ 1’s is $p^{r}q^{n}$. How many such strings are there? Because we stop as soon as we hit the $r$th success, the string must terminate in a 1. Among the other $n+r-1$ positions, we choose $r-1$ places for the remaining 1’s to go. So the overall probability of exactly $n$ failures before the $r$th success is

$P(X=n)=\binom{n+r-1}{r-1}p^{r}q^{n},\quad n=0,1,2,\ldots.$

Just as a Binomial r.v. can be represented as a sum of i.i.d. Bernoullis, a Negative Binomial r.v. can be represented as a sum of i.i.d. Geometrics.

###### Theorem 4.3.10.

Let $X\sim\text{NBin}(r,p)$, viewed as the number of failures before the $r$th success in a sequence of independent Bernoulli trials with success probability $p$. Then we can write $X=X_{1}+\cdots+X_{r}$ where the $X_{i}$ are i.i.d. $\text{Geom}(p)$.

###### Proof.

Let $X_{1}$ be the number of failures until the first success, $X_{2}$ be the number of failures between the first success and the second success, and in general, $X_{i}$ be the number of failures between the $(i-1)$st success and the $i$th success.

Then $X_{1}\sim\text{Geom}(p)$ by the story of the Geometric distribution. After the first success, the number of additional failures until the next success is still Geometric! So $X_{2}\sim\text{Geom}(p)$, and similarly for all the $X_{i}$. Furthermore, the $X_{i}$ are independent because the trials are all independent of each other. Adding the $X_{i}$, we get the total number of failures before the $r$th success, which is $X$. ∎

Using linearity, the expectation of the Negative Binomial now follows without any additional calculations.

###### Example 4.3.11 (Negative Binomial expectation).

Let $X\sim\text{NBin}(r,p)$. By the previous theorem, we can write $X=X_{1}+\cdots+X_{r}$, where the $X_{i}$ are i.i.d. $\text{Geom}(p)$. By linearity,

$E(X)=E(X_{1})+\cdots+E(X_{r})=r\cdot\frac{q}{p}.\qed$

The next example is a famous problem in probability and an instructive application of the Geometric and First Success distributions. It is usually stated as a problem about collecting coupons, hence its name, but we’ll use toys instead of coupons.

###### Example 4.3.12 (Coupon collector).

Suppose there are $n$ types of toys, which you are collecting one by one, with the goal of getting a complete set. When collecting toys, the toy types are random (as is sometimes the case, for example, with toys included in cereal boxes or included with kids’ meals from a fast food restaurant). Assume that each time you collect a toy, it is equally likely to be any of the $n$ types. What is the expected number of toys needed until you have a complete set?

*Solution*:

Let $N$ be the number of toys needed; we want to find $E(N)$. Our strategy will be to break up $N$ into a sum of simpler r.v.s so that we can apply linearity. So write

$N=N_{1}+N_{2}+\cdots+N_{n},$

where $N_{1}$ is the number of toys until the first toy type you haven’t seen before (which is always $1$, as the first toy is always a new type), $N_{2}$ is the additional number of toys until the second toy type you haven’t seen before, and so forth. Figure 6 illustrates these definitions with $n=3$ toy types.

Introduction to Probability

![img-61.jpeg](img-61.jpeg)

# FIGURE 4.6

Coupon collector,  $n = 3$ . Here  $N_{1}$  is the time (number of toys collected) until the first new toy type,  $N_{2}$  is the additional time until the second new type, and  $N_{3}$  is the additional time until the third new type. The total number of toys for a complete set is  $N_{1} + N_{2} + N_{3}$ .

By the story of the FS distribution,  $N_{2} \sim \mathrm{FS}((n - 1) / n)$ : after collecting the first toy type, there's a  $1 / n$  chance of getting the same toy you already had (failure) and an  $(n - 1) / n$  chance you'll get something new (success). Similarly,  $N_{3}$ , the additional number of toys until the third new toy type, is distributed  $\mathrm{FS}((n - 2) / n)$ . In general,

$$
N _ {j} \sim \mathrm {F S} ((n - j + 1) / n).
$$

By linearity,

$$
\begin{array}{l} E (N) = E \left(N _ {1}\right) + E \left(N _ {2}\right) + E \left(N _ {3}\right) + \dots + E \left(N _ {n}\right) \\ = 1 + \frac {n}{n - 1} + \frac {n}{n - 2} + \dots + n \\ = n \sum_ {j = 1} ^ {n} \frac {1}{j}. \\ \end{array}
$$

For large  $n$ , this is very close to  $n(\log n + 0.577)$ .

Before we leave this example, let's take a moment to connect it to our proof of Theorem 4.3.10, the representation of the Negative Binomial as a sum of i.i.d. Geometrics. In both problems, we are waiting for a specified number of successes, and we approach the problem by considering the intervals between successes. There are two major differences:

- In Theorem 4.3.10, we exclude the successes themselves, so the number of failures between two successes is Geometric. In the coupon collector problem, we include the successes because we want to count the total number of toys, so we have First Success r.v.s instead.
- In Theorem 4.3.10, the probability of success in each trial never changes, so the total number of failures is a sum of i.i.d. Geometrics. In the coupon collector problem, the probability of success decreases after each success, since it becomes harder and harder to find a new toy type you haven't seen before; so the  $N_{j}$  are not identically distributed, though they are independent.

4.3.13 (Expectation of a nonlinear function of an r.v.). Expectation is linear,

but in general we do *not* have $E(g(X))=g(E(X))$ for arbitrary functions $g$. We must be careful not to move the $E$ around when $g$ is not linear. The next example shows a situation in which $E(g(X))$ is *very* different from $g(E(X))$.

###### Example 4.3.14 (St. Petersburg paradox).

Suppose a wealthy stranger offers to play the following game with you. You will flip a fair coin until it lands Heads for the first time, and you will receive $2 if the game lasts for 1 round, $4 if the game lasts for 2 rounds, $8 if the game lasts for 3 rounds, and in general, $2^{n} if the game lasts for $n$ rounds. What is the fair value of this game (the expected payoff)? How much would you be willing to pay to play this game once?

*Solution*:

Let $X$ be your winnings from playing the game. By definition, $X=2^{N}$ where $N$ is the number of rounds that the game lasts. Then $X$ is 2 with probability 1/2, 4 with probability 1/4, 8 with probability 1/8, and so on, so

$E(X)=\frac{1}{2}\cdot 2+\frac{1}{4}\cdot 4+\frac{1}{8}\cdot 8+\cdots=\infty.$

The expected winnings are infinite! On the other hand, the number of rounds $N$ that the game lasts is the number of tosses until the first Heads, so $N\sim\text{FS}(1/2)$ and $E(N)=2$. Thus $E(2^{N})=\infty$ while $2^{E(N)}=4$. Infinity certainly does not equal 4, illustrating the danger of confusing $E(g(X))$ with $g(E(X))$ when $g$ is not linear.

This problem is often considered a paradox because although the game’s expected payoff is infinite, most people would not be willing to pay very much to play the game (even if they could afford to lose the money). One explanation is to note that *the amount of money in the real world is finite*. Suppose that if the game lasts longer than 40 rounds, the wealthy stranger flees the country and you get nothing. Since $2^{40}\approx 1.1\times 10^{12}$, this still gives you the potential to earn over a trillion dollars, and anyway it’s incredibly unlikely that the game will last longer than 40 rounds. But in this setting, your expected value is

$E(X)=\sum_{n=1}^{40}\frac{1}{2^{n}}\cdot 2^{n}+\sum_{n=41}^{\infty}\frac{1}{2^{n}}\cdot 0=40.$

Is this drastic reduction because the wealthy stranger may flee the country? Let’s suppose instead that the wealthy stranger caps your winnings at $2^{40}$, so if the game lasts more than 40 rounds you will get this amount rather than walking away empty-handed. Now your expected value is

$E(X)=\sum_{n=1}^{40}\frac{1}{2^{n}}\cdot 2^{n}+\sum_{n=41}^{\infty}\frac{1}{2^{n}}\cdot 2^{40}=40+1=41,$

an increase of only $1 from the previous scenario. The $\infty$ in the St. Petersburg paradox is driven by an infinite “tail” of extremely rare events where you get extremely large payoffs. Cutting off this tail at some point, which makes sense in the real world, dramatically reduces the expected value of the game. ∎

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

###### Example 4.4.3 (Boole, Bonferroni, and inclusion-exclusion).

Let $A_{1},A_{2},\ldots,A_{n}$ be events. Note that

$I(A_{1}\cup\cdots\cup A_{n})\leq I(A_{1})+\cdots+I(A_{n}),$

since if the left-hand side is 0 this is immediate, and if the left-hand side is 1 then at least one term on the right-hand side must be 1. Taking the expectation of both sides and using linearity and the fundamental bridge, we have

$P(A_{1}\cup\cdots\cup A_{n})\leq P(A_{1})+\cdots+P(A_{n}),$

which is called *Boole’s inequality* or *Bonferroni’s inequality*. To prove inclusion-exclusion for $n=2$, we can take the expectation of both sides in Property 4 of Theorem 4.4.1. For general $n$, we can use properties of indicator r.v.s as follows:

$1-I(A_{1}\cup\cdots\cup A_{n})$ $=I(A_{1}^{c}\cap\cdots\cap A_{n}^{c})$
$=(1-I(A_{1}))\cdots(1-I(A_{n}))$
$=1-\sum_{i}I(A_{i})+\sum_{i<j}I(A_{i})I(A_{j})-\cdots+(-1)^{n}I(A_{1})\cdots I(A_{n}).$

Taking the expectation of both sides, by the fundamental bridge we have proven the inclusion-exclusion theorem. ∎

Conversely, the fundamental bridge is also extremely useful in many expected value problems. We can often express a complicated discrete r.v. whose distribution we don’t know as a sum of indicator r.v.s, which are extremely simple. The fundamental bridge lets us find the expectation of the indicators; then, using linearity, we obtain the expectation of our original r.v. This strategy is extremely useful and versatile—in fact, we already used it when deriving the expectations of the Binomial and Hypergeometric distributions earlier in this chapter!

Recognizing problems that are amenable to this strategy and then defining the indicator r.v.s takes practice, so it is important to study a lot of examples and solve a lot of problems. In applying the strategy to a random variable that counts the number of [noun]s, we should have an indicator for each potential [noun]. This [noun] could be a person, place, or thing; we will see examples of all three types.

We’ll start by revisiting two problems from Chapter 1, de Montmort’s matching problem and the birthday problem.

###### Example 4.4.4 (Matching continued).

We have a well-shuffled deck of $n$ cards, labeled 1 through $n$. A card is a *match* if the card’s position in the deck matches the card’s label. Let $X$ be the number of matches; find $E(X)$.

*Solution*:

First let’s check whether $X$ could have any of the named distributions we have studied. The Binomial and Hypergeometric are the only two candidates since the value of $X$ must be an integer between 0 and $n$. But neither of these distributions

has the right support because $X$ can’t take on the value $n-1$: if $n-1$ cards are matches, then the $n$th card must be a match as well. So $X$ does not follow a named distribution we have studied, but we can readily find its mean using indicator r.v.s: let’s write $X=I_{1}+I_{2}+\cdots+I_{n}$, where

\[ I_{j}=\left\{\begin{array}[]{ll}1&\mbox{if the $j$th card in the deck is a match,}\\
0&\mbox{otherwise.}\end{array}\right. \]

In other words, $I_{j}$ is the indicator for $A_{j}$, the event that the $j$th card in the deck is a match. We can imagine that each $I_{j}$ “raises its hand” to be counted if its card is a match; adding up the raised hands, we get the total number of matches, $X$.

By the fundamental bridge,

$E(I_{j})=P(A_{j})=\frac{1}{n}$

for all $j$. So by linearity,

$E(X)=E(I_{1})+\cdots+E(I_{n})=n\cdot\frac{1}{n}=1.$

The expected number of matched cards is $1$, regardless of $n$. Even though the $I_{j}$ are dependent in a complicated way that makes the distribution of $X$ neither Binomial nor Hypergeometric, linearity still holds. ∎

###### Example 4.4.5 (Distinct birthdays, birthday matches).

In a group of $n$ people, under the usual assumptions about birthdays, what is the expected number of distinct birthdays among the $n$ people, i.e., the expected number of days on which at least one of the people was born? What is the expected number of birthday matches, i.e., pairs of people with the same birthday?

*Solution*:

Let $X$ be the number of distinct birthdays, and write $X=I_{1}+\cdots+I_{365}$, where

\[ I_{j}=\left\{\begin{array}[]{ll}1&\mbox{if the $j$th day is represented,}\\
0&\mbox{otherwise.}\end{array}\right. \]

We create an indicator for each *day* of the year because $X$ counts the number of *days* of the year that are represented. By the fundamental bridge,

$E(I_{j})=P(j\mbox{th day is represented})=1-P(\mbox{no one born on day $j$)}=1-\left(\frac{364}{365}\right)^{n}$

for all $j$. Then by linearity,

$E(X)=365\left(1-\left(\frac{364}{365}\right)^{n}\right).$

Now let $Y$ be the number of birthday matches. Label the people as $1,2,\ldots,n$, and order the $\binom{n}{2}$ pairs of people in some definite way. Then we can write

$Y=J_{1}+\cdots+J_{\binom{n}{2}},$

$J_{i}$ is the indicator of the $i$th pair of people having the same birthday. We create an indicator for each *pair of people* since $Y$ counts the number of *pairs of people* with the same birthday. The probability of any two people having the same birthday is $1/365$, so again by the fundamental bridge and linearity,

$E(Y)=\frac{\binom{n}{2}}{365}.\qed$

In addition to the fundamental bridge and linearity, the last two examples used a basic form of symmetry to simplify the calculations greatly: within each sum of indicator r.v.s, each indicator had the same expected value. For example, in the matching problem the probability of the $j$th card being a match does not depend on $j$, so we can just take $n$ times the expected value of the first indicator r.v.

Other forms of symmetry can also be extremely helpful when available. The next two examples showcase a form of symmetry that stems from having equally likely permutations. Note how symmetry, linearity, and the fundamental bridge are used in tandem to make seemingly very hard problems manageable.

###### Example 4.4.6 (Putnam problem).

A permutation $a_{1},a_{2},\ldots,a_{n}$ of $1,2,\ldots,n$ has a *local maximum* at $j$ if $a_{j}>a_{j-1}$ and $a_{j}>a_{j+1}$ (for $2\leq j\leq n-1$; for $j=1$, a local maximum at $j$ means $a_{1}>a_{2}$ while for $j=n$, it means $a_{n}>a_{n-1}$). For example, $4,2,5,3,6,1$ has $3$ local maxima, at positions $1$, $3$, and $5$. The Putnam exam (a famous, hard math competition, on which the median score is often a $0$) from 2006 posed the following question: for $n\geq 2$, what is the average number of local maxima of a random permutation of $1,2,\ldots,n$, with all $n!$ permutations equally likely?

*Solution*:

This problem can be solved quickly using indicator r.v.s, symmetry, and the fundamental bridge. Let $I_{1},\ldots,I_{n}$ be indicator r.v.s, where $I_{j}$ is $1$ if there is a local maximum at position $j$, and $0$ otherwise. We are interested in the expected value of $\sum_{j=1}^{n}I_{j}$. For $1<j<n$, $EI_{j}=1/3$ since having a local maximum at $j$ is equivalent to $a_{j}$ being the largest of $a_{j-1},a_{j},a_{j+1}$, which has probability $1/3$ since all orders are equally likely. For $j=1$ or $j=n$, we have $EI_{j}=1/2$ since then there is only one neighbor. Thus, by linearity,

$E\left(\sum_{j=1}^{n}I_{j}\right)=2\cdot\frac{1}{2}+(n-2)\cdot\frac{1}{3}=\frac{n+1}{3}.\qed$

The next example introduces the *Negative Hypergeometric* distribution, which completes the following table. The table shows the distributions for four sampling schemes: the sampling can be done with or without replacement, and the stopping rule can require a fixed number of draws or a fixed number of successes.

Introduction to Probability

|   | With replacement | Without replacement  |
| --- | --- | --- |
|  Fixed number of trials | Binomial | Hypergeometric  |
|  Fixed number of successes | Negative Binomial | Negative Hypergeometric  |

Example 4.4.7 (Negative Hypergeometric). An urn contains  $w$  white balls and  $b$  black balls, which are randomly drawn one by one without replacement, until  $r$  white balls have been obtained. The number of black balls drawn before drawing the  $r$ th white ball has a Negative Hypergeometric distribution with parameters  $w, b, r$ . We denote this distribution by  $\mathrm{NHGeom}(w, b, r)$ . Of course, we assume that  $r \leq w$ . For example, if we shuffle a deck of cards and deal them one at a time, the number of cards dealt before uncovering the first ace is  $\mathrm{NHGeom}(4, 48, 1)$ .

As another example, suppose a college offers  $g$  good courses and  $b$  bad courses (for some definition of "good" and "bad"), and a student wants to find 4 good courses to take. Not having any idea which of the courses are good, the student randomly tries out courses one at a time, stopping when they have obtained 4 good courses. Then the number of bad courses the student tries out is  $\mathrm{NHGeom}(g, b, 4)$ .

We can obtain the PMF of  $X \sim \mathrm{NHGeom}(w, b, r)$  by noting that, in the urn context,  $X = k$  means that the  $(r + k)$ th ball chosen is white and exactly  $r - 1$  of the first  $r + k - 1$  balls chosen are white. This gives

$$
P (X = k) = \frac {\binom {w} {r - 1} \binom {b} {k}}{\binom {w + b} {r + k - 1}} \cdot \frac {w - r + 1}{w + b - r - k + 1}
$$

for  $k = 0,1,\ldots ,b$  (and 0 otherwise).

Alternatively, we can imagine that we continue drawing balls until the urn has been emptied out; this is valid since whether or not we continue to draw balls after obtaining the  $r$ th white ball has no effect on  $X$ . Think of the  $w + b$  balls as lined up in a random order, the order in which they will be drawn.

Then  $X = k$  means that among the first  $r + k - 1$  balls there are exactly  $r - 1$  white balls, then there is a white ball, and then among the last  $w + b - r - k$  balls there are exactly  $w - r$  white balls. All  $\binom{w+b}{w}$  possibilities for the locations of the white balls in the line are equally likely. So by the naive definition of probability, we have the following slightly simpler expression for the PMF:

$$
P (X = k) = \frac {\binom {r + k - 1} {r - 1} \binom {w + b - r - k} {w - r}}{\binom {w + b} {w}},
$$

for  $k = 0,1,\ldots ,b$  (and 0 otherwise).

Finding the expected value of a Negative Hypergeometric r.v. directly from the definition of expectation results in complicated sums. But the answer is very simple: for  $X \sim \mathrm{NHGeom}(w, b, r)$ , we have  $E(X) = rb / (w + 1)$ .

Let's prove this using indicator r.v.s. As explained above, we can assume that we

continue drawing balls until the urn is empty. First consider the case $r=1$. Label the black balls as $1,2,\ldots,b$, and let $I_{j}$ be the indicator of black ball $j$ being drawn before any white balls have been drawn. Then $P(I_{j}=1)=1/(w+1)$ since, listing out the order in which black ball $j$ and the white balls are drawn (ignoring the other balls), all orders are equally likely by symmetry, and $I_{j}=1$ is equivalent to black ball $j$ being first in this list. So by linearity,

$E\left(\sum_{j=1}^{b}I_{j}\right)=\sum_{j=1}^{b}E(I_{j})=b/(w+1).$

Sanity check: This answer makes sense since it is increasing in $b$, decreasing in $w$, and correct in the extreme cases $b=0$ (when no black balls will be drawn) and $w=0$ (when all the black balls will be exhausted before drawing a nonexistent white ball). Moreover, note that $b/(w+1)$ looks similar to, but is strictly smaller than, $b/w$, which is the expected value of a $\text{Geom}(w/(w+b))$ r.v. It makes sense that sampling without replacement should give a smaller expected waiting time than sampling with replacement. Similarly, if you are searching for something you lost, it makes more sense to choose locations to check without replacement, rather than wasting time looking over and over again in locations you already ruled out.

For general $r$, write $X=X_{1}+X_{2}+\cdots+X_{r}$, where $X_{1}$ is the number of black balls before the first white ball, $X_{2}$ is the number of black balls after the first white ball but before the second white ball, etc. By essentially the same argument we used to handle the $r=1$ case, we have $E(X_{j})=b/(w+1)$ for each $j$. So by linearity,

$E(X)=rb/(w+1).\qed$

Closely related to indicator r.v.s is an alternative expression for the expectation of a nonnegative integer-valued r.v. $X$. Rather than summing up values of $X$ times values of the PMF of $X$, we can sum up probabilities of the form $P(X>n)$ (known as tail probabilities), over nonnegative integers $n$.

###### Theorem 4.4.8 (Expectation via survival function).

Let $X$ be a nonnegative integer-valued r.v. Let $F$ be the CDF of $X$, and $G(x)=1-F(x)=P(X>x)$. The function $G$ is called the survival function of $X$. Then

$E(X)=\sum_{n=0}^{\infty}G(n).$

That is, we can obtain the expectation of $X$ by summing up the survival function (or, stated otherwise, summing up tail probabilities of the distribution).

###### Proof.

For simplicity, we will prove the result only for the case that $X$ is bounded, i.e., there is a nonnegative integer $b$ such that $X$ is always at most $b$. We can represent $X$ as a sum of indicator r.v.s: $X=I_{1}+I_{2}+\cdots+I_{b}$, where $I_{n}=I(X\geq n)$. For

example, if $X=7$ occurs, then $I_{1}$ through $I_{7}$ equal 1 while the other indicators equal 0.

By linearity and the fundamental bridge, and the fact that $\{X\geq k\}$ is the same event as $\{X>k-1\}$,

$E(X)=\sum_{k=1}^{b}E(I_{k})=\sum_{k=1}^{b}P(X\geq k)=\sum_{n=0}^{b-1}P(X>n)=\sum_{n=0}^{\infty}G(n).$

As a quick example, we use the above result to give another derivation of the mean of a Geometric r.v.

###### Example 4.4.9 (Geometric expectation redux).

Let $X\sim\text{Geom}(p)$, and $q=1-p$. Using the Geometric story, $\{X>n\}$ is the event that the first $n+1$ trials are all failures. So by Theorem 4.4.8,

$E(X)=\sum_{n=0}^{\infty}P(X>n)=\sum_{n=0}^{\infty}q^{n+1}=\frac{q}{1-q}=\frac{q}{p},$

confirming what we already knew about the mean of a Geometric. $\square$

### 4.5 Law of the unconscious statistician (LOTUS)

As we saw in the St. Petersburg paradox, $E(g(X))$ does *not* equal $g(E(X))$ in general if $g$ is not linear. So how do we correctly calculate $E(g(X))$? Since $g(X)$ is an r.v., one way is to first find the distribution of $g(X)$ and then use the definition of expectation. Perhaps surprisingly, it turns out that it is possible to find $E(g(X))$ directly using the distribution of $X$, without first having to find the distribution of $g(X)$. This is done using the *law of the unconscious statistician* (LOTUS).

###### Theorem 4.5.1 (LOTUS).

If $X$ is a discrete r.v. and $g$ is a function from $\mathbb{R}$ to $\mathbb{R}$, then

$E(g(X))=\sum_{x}g(x)P(X=x),$

where the sum is taken over all possible values of $X$.

This means that we can get the expected value of $g(X)$ knowing only $P(X=x)$, the PMF of $X$; we don’t need to know the PMF of $g(X)$. The name comes from the fact that in going from $E(X)$ to $E(g(X))$ it is tempting just to change $x$ to $g(x)$ in the definition, which can be done very easily and mechanically, perhaps in a state of unconsciousness. On second thought, it may sound too good to be true that finding the distribution of $g(X)$ is not needed for this calculation, but LOTUS says it *is* true.

Before proving LOTUS in general, let’s see why it is true in some special cases. Let $X$ have support $0,1,2,\dots$ with probabilities $p_{0},p_{1},p_{2},\dots$, so the PMF is $P(X=n)=p_{n}$. Then $X^{3}$ has support $0^{3},1^{3},2^{3},\dots$ with probabilities $p_{0},p_{1},p_{2},\dots$, so

$E(X)$ $=\sum_{n=0}^{\infty}np_{n},$
$E(X^{3})$ $=\sum_{n=0}^{\infty}n^{3}p_{n}.$

As claimed by LOTUS, to edit the expression for $E(X)$ into an expression for $E(X^{3})$, we can just change the $n$ in front of the $p_{n}$ to an $n^{3}$. This was an easy example since the function $g(x)=x^{3}$ is one-to-one. But LOTUS holds much more generally. The key insight needed for the proof of LOTUS for general $g$ is the same as the one we used for the proof of linearity: the expectation of $g(X)$ can be written in ungrouped form as

$E(g(X))=\sum_{s}g(X(s))P(\{s\}),$

where the sum is over all the pebbles in the sample space, but we can also group the pebbles into super-pebbles according to the value that $X$ assigns to them. Within the super-pebble $X=x$, $g(X)$ always takes on the value $g(x)$. Therefore,

$E(g(X))$ $=\sum_{s}g(X(s))P(\{s\})$
$=\sum_{x}\sum_{s:X(s)=x}g(X(s))P(\{s\})$
$=\sum_{x}g(x)\sum_{s:X(s)=x}P(\{s\})$
$=\sum_{x}g(x)P(X=x).$

In the last step, we used the fact that $\sum_{s:X(s)=x}P(\{s\})$ is the weight of the super-pebble $X=x$.

### 4.6 Variance

One important application of LOTUS is for finding the variance of a random variable. Like expected value, variance is a single-number summary of the distribution of a random variable. While the expected value tells us the center of mass of a distribution, the variance tells us how spread out the distribution is.

###### Definition 4.6.1 (Variance and standard deviation).

The variance of an r.v. $X$ is

$\mathrm{Var}(X)=E(X-EX)^{2}.$

The square root of the variance is called the *standard deviation* (SD):

$\mathrm{SD}(X)=\sqrt{\mathrm{Var}(X)}.$

Recall that when we write $E(X-EX)^{2}$, we mean the expectation of the random variable $(X-EX)^{2}$, *not* $(E(X-EX))^{2}$ (which is 0 by linearity).

The variance of $X$ measures how far $X$ is from its mean on average, but instead of simply taking the average difference between $X$ and its mean $EX$, we take the average *squared* difference. To see why, note that the average deviation from the mean, $E(X-EX)$, always equals 0 by linearity; positive and negative deviations cancel each other out. By squaring the deviations, we ensure that both positive and negative deviations contribute to the overall variability. However, because variance is an average squared distance, it has the wrong units: if $X$ is in dollars, $\mathrm{Var}(X)$ is in squared dollars. To get back to our original units, we take the square root; this gives us the standard deviation.

One might wonder why variance isn’t defined as $E|X-EX|$, which would achieve the goal of counting both positive and negative deviations while maintaining the same units as $X$. This measure of variability isn’t nearly as popular as $E(X-EX)^{2}$, for a variety of reasons. Most notably, the absolute value function isn’t differentiable at 0, whereas the squaring function is differentiable everywhere and is central in various fundamental mathematical results such as the Pythagorean theorem.

An equivalent expression for variance is $\mathrm{Var}(X)=E(X^{2})-(EX)^{2}$. This formula is often easier to work with when doing actual calculations. Since this is the variance formula we will use over and over again, we state it as its own theorem.

###### Theorem 4.6.2.

For any r.v. $X$,

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}.$

###### Proof.

Let $\mu=EX$. Expanding $(X-\mu)^{2}$ and using linearity, the variance of $X$ is

$E(X-\mu)^{2}=E(X^{2}-2\mu X+\mu^{2})=E(X^{2})-2\mu EX+\mu^{2}=E(X^{2})-\mu^{2}.\qed$

Variance has the following properties. The first two are easily verified from the definition, the third will be addressed in a later chapter, and the last one is proven just after stating it.

- $\mathrm{Var}(X+c)=\mathrm{Var}(X)$ for any constant $c$. Intuitively, if we shift a distribution to the left or right, that should affect the center of mass of the distribution but not its spread.
- $\mathrm{Var}(cX)=c^{2}\mathrm{Var}(X)$ for any constant $c$.
- If $X$ and $Y$ are independent, then $\mathrm{Var}(X+Y)=\mathrm{Var}(X)+\mathrm{Var}(Y)$. We prove this and discuss it more in Chapter 7. This is not true in general if $X$ and $Y$ are dependent. For example, in the extreme case where $X$ always equals $Y$, we have

$\mathrm{Var}(X+Y)=\mathrm{Var}(2X)=4\mathrm{Var}(X)>2\mathrm{Var}(X)=\mathrm{Var}(X)+\mathrm{Var}(Y)$

if $\operatorname{Var}(X)>0$ (which will be true unless $X$ is a constant, as the next property shows).
- $\operatorname{Var}(X)\geq 0$, with equality if and only if $P(X=a)=1$ for some constant $a$. In other words, the only random variables that have zero variance are constants (which can be thought of as degenerate r.v.s); all other r.v.s have positive variance.

To prove the last property, note that $\operatorname{Var}(X)$ is the expectation of the *nonnegative* r.v. $(X-EX)^{2}$, so $\operatorname{Var}(X)\geq 0$. If $P(X=a)=1$ for some constant $a$, then $E(X)=a$ and $E(X^{2})=a^{2}$, so $\operatorname{Var}(X)=0$. Conversely, suppose that $\operatorname{Var}(X)=0$. Then $E(X-EX)^{2}=0$, which shows that $(X-EX)^{2}=0$ has probability $1$, which in turn shows that $X$ equals its mean with probability $1$.

#### 4.6.3 (Variance is not linear).

Unlike expectation, variance is *not* linear. The constant comes out *squared* in $\operatorname{Var}(cX)=c^{2}\operatorname{Var}(X)$, and the variance of the sum of r.v.s may not be the sum of their variances if they are dependent.

###### Example 4.6.4 (Geometric and Negative Binomial variance).

In this example we’ll use LOTUS to compute the variance of the Geometric distribution.

Let $X\sim\operatorname{Geom}(p)$. We already know $E(X)=q/p$. By LOTUS,

$E(X^{2})=\sum_{k=0}^{\infty}k^{2}P(X=k)=\sum_{k=0}^{\infty}k^{2}pq^{k}=\sum_{k=1}^{\infty}k^{2}pq^{k}.$

We’ll find this using a tactic similar to how we found the expectation, starting from the geometric series

$\sum_{k=0}^{\infty}q^{k}=\frac{1}{1-q}$

and taking derivatives. After differentiating once with respect to $q$, we have

$\sum_{k=1}^{\infty}kq^{k-1}=\frac{1}{(1-q)^{2}}.$

We start the sum from $k=1$ since the $k=0$ term is $0$ anyway. If we differentiate again, we’ll get $k(k-1)$ instead of $k^{2}$ as we want, so let’s replenish our supply of $q$’s by multiplying both sides by $q$. This gives

$\sum_{k=1}^{\infty}kq^{k}=\frac{q}{(1-q)^{2}}.$

Now we are ready to take another derivative:

$\sum_{k=1}^{\infty}k^{2}q^{k-1}=\frac{1+q}{(1-q)^{3}},$

so

$E(X^{2})=\sum_{k=1}^{\infty}k^{2}pq^{k}=pq\frac{1+q}{(1-q)^{3}}=\frac{q(1+q)}{p^{2}}.$

Finally,

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}=\frac{q(1+q)}{p^{2}}-\left(\frac{q}{p}\right)^{2}=\frac{q}{p^{2}}.$

This is also the variance of the First Success distribution, since shifting by a constant does not affect the variance.

Since an $\mathrm{NBin}(r,p)$ r.v. can be represented as a sum of $r$ i.i.d. $\mathrm{Geom}(p)$ r.v.s by Theorem 4.3.10, and since variance is additive for independent random variables, it follows that the variance of the $\mathrm{NBin}(r,p)$ distribution is $r\cdot\frac{q}{p^{2}}$. ∎

LOTUS is an all-purpose tool for computing $E(g(X))$ for any $g$, but as it usually leads to complicated sums, it should be used as a last resort. For variance calculations, our trusty indicator r.v.s can sometimes be used in place of LOTUS, as in the next example.

###### Example 4.6.5 (Binomial variance).

Let’s find the variance of $X\sim\mathrm{Bin}(n,p)$ using indicator r.v.s to avoid tedious sums. Represent $X=I_{1}+I_{2}+\cdots+I_{n}$, where $I_{j}$ is the indicator of the $j$th trial being a success. Each $I_{j}$ has variance

$\mathrm{Var}(I_{j})=E(I_{j}^{2})-(E(I_{j}))^{2}=p-p^{2}=p(1-p).$

(Recall that $I_{j}^{2}=I_{j}$, so $E(I_{j}^{2})=E(I_{j})=p$.)

Since the $I_{j}$ are independent, we can add their variances to get the variance of their sum:

$\mathrm{Var}(X)=\mathrm{Var}(I_{1})+\cdots+\mathrm{Var}(I_{n})=np(1-p).$

Alternatively, we can find $E(X^{2})$ by first finding $E\binom{X}{2}$. The latter sounds more complicated, but actually it is simpler since $\binom{X}{2}$ is the number of *pairs* of successful trials. Creating an indicator r.v. for each pair of trials, we have

$E\binom{X}{2}=\binom{n}{2}p^{2}.$

Thus,

$n(n-1)p^{2}=E(X(X-1))=E(X^{2})-E(X)=E(X^{2})-np,$

which again gives

$\mathrm{Var}(X)=E(X^{2})-(EX)^{2}=(n(n-1)p^{2}+np)-(np)^{2}=np(1-p).$

Exercise 48 uses this strategy to find the variance of the Hypergeometric. ∎

### 4.7 Poisson

The last discrete distribution that we’ll introduce in this chapter is the Poisson, which is an extremely popular distribution for modeling discrete data. We’ll introduce its PMF, mean, and variance, and then discuss its story in more detail.

###### Definition 4.7.1 (Poisson distribution).

An r.v. $X$ has the Poisson distribution with parameter $\lambda$, where $\lambda>0$, if the PMF of $X$ is

$P(X=k)=\frac{e^{-\lambda}\lambda^{k}}{k!},\quad k=0,1,2,\ldots.$

We write this as $X\sim\text{Pois}(\lambda)$.

This is a valid PMF because of the Taylor series $\sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}$.

###### Example 4.7.2 (Poisson expectation and variance).

Let $X\sim\text{Pois}(\lambda)$. We will show that the mean and variance are both equal to $\lambda$. For the mean, we have

$E(X)$ $=e^{-\lambda}\sum_{k=0}^{\infty}k\frac{\lambda^{k}}{k!}$
$=e^{-\lambda}\sum_{k=1}^{\infty}k\frac{\lambda^{k}}{k!}$
$=\lambda e^{-\lambda}\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k-1)!}$
$=\lambda e^{-\lambda}e^{\lambda}=\lambda.$

First we dropped the $k=0$ term because it was $0$. Then we took a $\lambda$ out of the sum so that what was left inside was just the Taylor series for $e^{\lambda}$.

To get the variance, we first find $E(X^{2})$. By LOTUS,

$E(X^{2})=\sum_{k=0}^{\infty}k^{2}P(X=k)=e^{-\lambda}\sum_{k=0}^{\infty}k^{2}\frac{\lambda^{k}}{k!}.$

From here, the derivation is very similar to that of the variance of the Geometric. Differentiate the familiar series

$\sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}$

with respect to $\lambda$ and replenish:

$\sum_{k=1}^{\infty}k\frac{\lambda^{k-1}}{k!}=e^{\lambda},$
$\sum_{k=1}^{\infty}k\frac{\lambda^{k}}{k!}=\lambda e^{\lambda}.$

Rinse and repeat:

$\sum_{k=1}^{\infty}k^{2}\frac{\lambda^{k-1}}{k!}=e^{\lambda}+\lambda e^{\lambda}=e^{\lambda}(1+\lambda),$
$\sum_{k=1}^{\infty}k^{2}\frac{\lambda^{k}}{k!}=e^{\lambda}\lambda(1+\lambda).$

Introduction to Probability

Finally,

$$
E (X ^ {2}) = e ^ {- \lambda} \sum_ {k = 0} ^ {\infty} k ^ {2} \frac {\lambda^ {k}}{k !} = e ^ {- \lambda} e ^ {\lambda} \lambda (1 + \lambda) = \lambda (1 + \lambda),
$$

so

$$
\operatorname {V a r} (X) = E \left(X ^ {2}\right) - (E X) ^ {2} = \lambda (1 + \lambda) - \lambda^ {2} = \lambda .
$$

Thus, the mean and variance of a  $\mathrm{Pois}(\lambda)$  r.v. are both equal to  $\lambda$ .

Figure 4.7 shows the PMF and CDF of the Pois(2) and Pois(5) distributions from  $k = 0$  to  $k = 10$ . It appears that the mean of the Pois(2) is around 2 and the mean of the Pois(5) is around 5, consistent with our findings above. The PMF of the Pois(2) is highly skewed, but as  $\lambda$  grows larger, the skewness is reduced and the PMF becomes more bell-shaped.

![img-62.jpeg](img-62.jpeg)

![img-63.jpeg](img-63.jpeg)

![img-64.jpeg](img-64.jpeg)
FIGURE 4.7 Top: Pois(2) PMF and CDF. Bottom: Pois(5) PMF and CDF.

![img-65.jpeg](img-65.jpeg)

The Poisson distribution is often used in situations where we are counting the

number of successes in a particular region or interval of time, and there are a large number of trials, each with a small probability of success. For example, the following random variables could follow a distribution that is approximately Poisson.
- The number of emails you receive in an hour. There are a lot of people who could potentially email you in that hour, but it is unlikely that any specific person will actually email you in that hour. Alternatively, imagine subdividing the hour into milliseconds. There are $3.6\times 10^{6}$ seconds in an hour, but in any specific millisecond it is unlikely that you will get an email.
- The number of chips in a chocolate chip cookie. Imagine subdividing the cookie into small cubes; the probability of getting a chocolate chip in a single cube is small, but the number of cubes is large.
- The number of earthquakes in a year in some region of the world. At any given time and location, the probability of an earthquake is small, but there are a large number of possible times and locations for earthquakes to occur over the course of the year.

The parameter $\lambda$ is interpreted as the *rate* of occurrence of these rare events; in the examples above, $\lambda$ could be 20 (emails per hour), 10 (chips per cookie), and 2 (earthquakes per year). The *Poisson paradigm* says that in applications similar to the ones above, we can approximate the distribution of the number of events that occur by a Poisson distribution.

###### Approximation 4.7.3 (Poisson paradigm).

Let $A_{1},\ldots,A_{n}$ be events with $p_{j}=P(A_{j})$, where $n$ is large, the $p_{j}$ are small, and the $A_{j}$ are independent or weakly dependent. Let

$X=\sum_{j=1}^{n}I(A_{j})$

count how many of the $A_{j}$ occur. Then $X$ is approximately distributed as $\mathrm{Pois}(\lambda)$, with $\lambda=\sum_{j=1}^{n}p_{j}$.

Proving that the above approximation is good is difficult, and would require first giving precise definitions of weak dependence (there are various ways to measure dependence of r.v.s) and of good approximations (there are various ways to measure how good an approximation is). A remarkable theorem is that if the $A_{j}$ are independent, $N\sim\mathrm{Pois}(\lambda)$, and $B$ is any set of nonnegative integers, then

$|P(X\in B)-P(N\in B)|\leq\min\left(1,\frac{1}{\lambda}\right)\sum_{j=1}^{n}p_{j}^{2}.$

This gives an upper bound on how much error is incurred from using a Poisson approximation. It also makes more precise how small the $p_{j}$ should be: we want $\sum_{j=1}^{n}p_{j}^{2}$ to be very small, or at least very small compared to $\lambda$. The result can be shown using an advanced technique known as the *Stein-Chen method*.

The Poisson paradigm is also called the law of rare events. The interpretation of “rare” is that the $p_{j}$ are small, not that $\lambda$ is small. For example, in the email example, the low probability of getting an email from a specific person in a particular hour is offset by the large number of people who could send you an email in that hour.

In the examples we gave above, the number of events that occur isn’t exactly Poisson because a Poisson random variable has no upper bound, whereas how many of $A_{1},\ldots,A_{n}$ occur is at most $n$, and there is a limit to how many chocolate chips can be crammed into a cookie. But the Poisson distribution often gives good approximations. Note that the conditions for the Poisson paradigm to hold are fairly flexible: the $n$ trials can have different success probabilities, and the trials don’t have to be independent, though they should not be very dependent. So there are a wide variety of situations that can be cast in terms of the Poisson paradigm. This makes the Poisson a popular model, or at least a starting point, for data whose values are nonnegative integers (called count data in statistics).

###### Example 4.7.4 (Balls in boxes).

There are $k$ distinguishable balls and $n$ distinguishable boxes. The balls are randomly placed in the boxes, with all $n^{k}$ possibilities equally likely. Problems in this setting are called occupancy problems, and are at the core of many widely used algorithms in computer science.

(a) Find the expected number of empty boxes (fully simplified, not as a sum).

(b) Find the probability that at least one box is empty. Express your answer as a sum of at most $n$ terms.

(c) Now let $n=1000,\,k=5806$. The expected number of empty boxes is then approximately $3$. Find a good approximation as a decimal for the probability that at least one box is empty. The handy fact $e^{3}\approx 20$ may help.

Solution:

(a) Let $I_{j}$ be the indicator r.v. for the $j$th box being empty. Then

$E(I_{j})=P(I_{j}=1)=\left(1-\frac{1}{n}\right)^{k}.$

By linearity,

$E\left(\sum_{j=1}^{n}I_{j}\right)=\sum_{j=1}^{n}E(I_{j})=n\left(1-\frac{1}{n}\right)^{k}.$

(b) The probability is $1$ for $k<n$. In general, let $A_{j}$ be the event that box $j$ is empty. By inclusion-exclusion,

$P(A_{1}\cup A_{2}\cup\cdots\cup A_{n})$ $=\sum_{j=1}^{n}(-1)^{j+1}\binom{n}{j}P(A_{1}\cap A_{2}\cap\cdots\cap A_{j})$
$=\sum_{j=1}^{n-1}(-1)^{j+1}\binom{n}{j}\left(1-\frac{j}{n}\right)^{k}.$

Expectation

(c) The number $X$ of empty boxes is approximately $\operatorname{Pois}(3)$, since there are a lot of boxes but each is very unlikely to be empty; the probability that a specific box is empty is $(1-\frac{1}{n})^{k}=\frac{1}{n}\cdot E(X)\approx 0.003$. So

$P(X\geq 1)=1-P(X=0)\approx 1-e^{-3}\approx 1-\frac{1}{20}=0.95.\qed$

Poisson approximation greatly simplifies obtaining a good approximate solution to the birthday problem discussed in Chapter 1, and makes it possible to obtain good approximations to various variations which would be hard to solve exactly.

###### Example 4.7.5 (Birthday problem continued).

If we have $m$ people and make the usual assumptions about birthdays, then each pair of people has probability $p=1/365$ of having the same birthday, and there are ${m\choose 2}$ pairs. By the Poisson paradigm the distribution of the number $X$ of birthday matches is approximately $\operatorname{Pois}(\lambda)$, where $\lambda={m\choose 2}\frac{1}{365}$. Then the probability of at least one match is

$P(X\geq 1)=1-P(X=0)\approx 1-e^{-\lambda}.$

For $m=23$, $\lambda=253/365$ and $1-e^{-\lambda}\approx 0.500002$, which agrees with our finding from Chapter 1 that we need 23 people to have a 50-50 chance of a matching birthday.

Note that even though $m=23$ is fairly small, the relevant quantity in this problem is actually ${m\choose 2}$, which is the total number of “trials” for a successful birthday match, so the Poisson approximation still performs well. ∎

###### Example 4.7.6 (Near-birthday problem).

What if we want to find the number of people required in order to have a 50-50 chance that two people would have birthdays within one day of each other (i.e., on the same day or one day apart)? Unlike the original birthday problem, this is difficult to obtain an exact answer for, but the Poisson paradigm still applies. The probability that any two people have birthdays within one day of each other is $3/365$ (choose a birthday for the first person, and then the second person needs to be born on that day, the day before, or the day after). Again there are ${m\choose 2}$ possible pairs, so the number of within-one-day matches is approximately $\operatorname{Pois}(\lambda)$ where $\lambda={m\choose 2}\frac{3}{365}$. Then a calculation similar to the one above tells us that we need $m=14$ or more. This was a quick approximation, but it turns out that $m=14$ is the exact answer! ∎

###### Example 4.7.7 (Birth-minute and birth-hour).

There are 1600 sophomores at a certain college. Throughout this example, make the usual assumptions as in the birthday problem.

(a) Find a Poisson approximation for the probability that there are two sophomores who were born not only on the same day of the year, but also at the same hour and the same minute (e.g., both sophomores were born at 8:20 pm on March 31, not necessarily in the same year).

(b) With assumptions as in (a), what is the probability that there are four sophomores who were born not only on the same day, but also at the same hour (e.g., all were born between 2 pm and 3 pm on March 31, not necessarily in the same year)?

Give two different Poisson approximations for this value, one based on creating an indicator r.v. for each quadruplet of sophomores, and the other based on creating an indicator r.v. for each possible day-hour. Which do you think is more accurate?

*Solution*:

(a) This is the birthday problem, with $c=365\cdot 24\cdot 60=525600$ categories rather than 365 categories. Let $n=1600$. Creating an indicator r.v. for each pair of sophomores, by linearity the expected number of pairs born on the same day-hour-minute is

$\lambda_{1}={n\choose 2}\frac{1}{c}.$

By Poisson approximation, the probability of at least one match is approximately

$1-\exp(-\lambda_{1})\approx 0.9122.$

This approximation is very accurate: typing pbirthday(1600, classes=365*24*60) in R yields 0.9125.

(b) Now there are $b=365\cdot 24=8760$ categories. Let’s explore two different methods of Poisson approximation.

*Method 1*: Create an indicator for each set of 4 sophomores. By linearity, the expected number of sets of 4 sophomores born on the same day-hour is

$\lambda_{2}={n\choose 4}\frac{1}{b^{3}}.$

Poisson approximation gives that the desired probability is approximately

$1-\exp(-\lambda_{2})\approx 0.333.$

*Method 2*: Create an indicator for each possible day-hour. Let $I_{j}$ be the indicator for at least 4 people having been born on the $j$th day-hour of the year (ordered chronologically), for $1\leq j\leq b$. Let $p=1/b$ and $q=1-p$. Then

$E(I_{j})$ $=$ $P(I_{j}=1)$
$=$ $1-P(\mbox{at most 3 people born on the $j$th day-hour})$
$=$ $1-q^{n}-npq^{n-1}-{n\choose 2}p^{2}q^{n-2}-{n\choose 3}p^{3}q^{n-3}.$

The expected number of day-hours on which at least 4 sophomores were born is

$\lambda_{3}=b\cdot E(I_{1}),$

with $E(I_{1})$ as above. We then have the Poisson approximation

$1-\exp(-\lambda_{3})\approx 0.295.$

The command pbirthday(1600, classes = 8760, coincident=4) in R gives that the correct answer is 0.296. So Method 2 is more accurate than Method 1.

An intuitive explanation for why Method 1 is less accurate is that there is a more substantial dependence in the indicators in that method. For example, being given that sophomores 1, 2, 3, 4 share the same birth day-hour greatly increases the chance that sophomores 1, 2, 3, 5 share the same birth day-hour. In contrast, knowing that at least 4 sophomores were born on a specific day-hour provides very little information about whether at least 4 were born on a different specific day-hour. ∎

### 4.8 Connections between Poisson and Binomial

The Poisson and Binomial distributions are closely connected, and their relationship is exactly parallel to the relationship between the Binomial and Hypergeometric distributions that we examined in the previous chapter: we can get from the Poisson to the Binomial by *conditioning*, and we can get from the Binomial to the Poisson by *taking a limit*.

Our results will rely on the fact that the sum of independent Poissons is Poisson, just as the sum of independent Binomials is Binomial. We’ll prove this result using the law of total probability for now; in Chapter 6 we’ll learn a faster method that uses a tool called the moment generating function. Chapter 13 gives further insight into these results.

###### Theorem 4.8.1 (Sum of independent Poissons).

If $X\sim\mathrm{Pois}(\lambda_{1})$, $Y\sim\mathrm{Pois}(\lambda_{2})$, and $X$ is independent of $Y$, then $X+Y\sim\mathrm{Pois}(\lambda_{1}+\lambda_{2})$.

###### Proof.

To get the PMF of $X+Y$, condition on $X$ and use the law of total probability:

$P(X+Y=k)$ $=\sum_{j=0}^{k}P(X+Y=k|X=j)P(X=j)$
$=\sum_{j=0}^{k}P(Y=k-j)P(X=j)$
$=\sum_{j=0}^{k}\frac{e^{-\lambda_{2}}\lambda_{2}^{k-j}}{(k-j)!}\frac{e^{-\lambda_{1}}\lambda_{1}^{j}}{j!}$
$=\frac{e^{-(\lambda_{1}+\lambda_{2})}}{k!}\sum_{j=0}^{k}\binom{k}{j}\lambda_{1}^{j}\lambda_{2}^{k-j}$
$=\frac{e^{-(\lambda_{1}+\lambda_{2})}(\lambda_{1}+\lambda_{2})^{k}}{k!}.$

Introduction to Probability

The last step used the binomial theorem. Since we've arrived at the  $\mathrm{Pois}(\lambda_1 + \lambda_2)$  PMF, we have  $X + Y\sim \mathrm{Pois}(\lambda_1 + \lambda_2)$ .

The story of the Poisson distribution provides intuition for this result. If there are two different types of events occurring at rates  $\lambda_{1}$  and  $\lambda_{2}$ , independently, then the overall event rate is  $\lambda_{1} + \lambda_{2}$ .

Theorem 4.8.2 (Poisson given a sum of Poissons). If  $X \sim \operatorname{Pois}(\lambda_1)$ ,  $Y \sim \operatorname{Pois}(\lambda_2)$ , and  $X$  is independent of  $Y$ , then the conditional distribution of  $X$  given  $X + Y = n$  is  $\operatorname{Bin}(n, \lambda_1 / (\lambda_1 + \lambda_2))$ .

Proof. Exactly as in the corresponding proof for the Binomial and Hypergeometric, we use Bayes' rule to compute the conditional PMF  $P(X = k|X + Y = n)$ :

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {P (X + Y = n | X = k) P (X = k)}{P (X + Y = n)} \\ = \frac {P (Y = n - k) P (X = k)}{P (X + Y = n)}. \\ \end{array}
$$

Now we plug in the PMFs of  $X$ ,  $Y$ , and  $X + Y$ ; the last of these is distributed  $\mathrm{Pois}(\lambda_1 + \lambda_2)$  by the previous theorem. This gives

$$
\begin{array}{l} P (X = k | X + Y = n) = \frac {\left(\frac {e ^ {- \lambda_ {2}} \lambda_ {2} ^ {n - k}}{(n - k) !}\right) \left(\frac {e ^ {- \lambda_ {1}} \lambda_ {1} ^ {k}}{k !}\right)}{\frac {e ^ {- (\lambda_ {1} + \lambda_ {2})} (\lambda_ {1} + \lambda_ {2}) ^ {n}}{n !}} \\ = \binom {n} {k} \frac {\lambda_ {1} ^ {k} \lambda_ {2} ^ {n - k}}{(\lambda_ {1} + \lambda_ {2}) ^ {n}} \\ = \binom {n} {k} \left(\frac {\lambda_ {1}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {k} \left(\frac {\lambda_ {2}}{\lambda_ {1} + \lambda_ {2}}\right) ^ {n - k}, \\ \end{array}
$$

which is the  $\mathrm{Bin}(n,\lambda_1 / (\lambda_1 + \lambda_2))$  PMF, as desired.

Conversely, if we take the limit of the  $\operatorname{Bin}(n,p)$  distribution as  $n\to \infty$  and  $p\rightarrow 0$  with  $np$  fixed, we arrive at a Poisson distribution. This provides the basis for the Poisson approximation to the Binomial distribution.

Theorem 4.8.3 (Poisson approximation to Binomial). If  $X \sim \operatorname{Bin}(n, p)$  and we let  $n \to \infty$  and  $p \to 0$  such that  $\lambda = np$  remains fixed, then the PMF of  $X$  converges to the  $\operatorname{Pois}(\lambda)$  PMF. More generally, the same conclusion holds if  $n \to \infty$  and  $p \to 0$  in such a way that  $np$  converges to a constant  $\lambda$ .

This is a special case of the Poisson paradigm, where the  $A_{j}$  are independent with the same probabilities, so that  $\sum_{j=1}^{n} I(A_{j})$  has a Binomial distribution. In this special case, we can prove that the Poisson approximation makes sense just by taking a limit of the Binomial PMF.

Expectation

Proof. We will prove this for the case that $\lambda = np$ is fixed while $n\to \infty$ and $p\rightarrow 0$, by showing that the $\operatorname {Bin}(n,p)$ PMF converges to the $\mathrm{Pois}(\lambda)$ PMF. For $0\leq k\leq n$

$$
\begin{array}{l}
P (X = k) = \binom {n} {k} p ^ {k} (1 - p) ^ {n - k} \\
= \frac {n (n - 1) \dots (n - k + 1)}{k !} \left(\frac {\lambda}{n}\right) ^ {k} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k} \\
= \frac {\lambda^ {k}}{k !} \frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \left(1 - \frac {\lambda}{n}\right) ^ {n} \left(1 - \frac {\lambda}{n}\right) ^ {- k}.
\end{array}
$$

Letting $n\to \infty$ with $k$ fixed,

$$
\begin{array}{l}
\frac {n (n - 1) \dots (n - k + 1)}{n ^ {k}} \rightarrow 1, \\
\left(1 - \frac {\lambda}{n}\right) ^ {n} \rightarrow e ^ {- \lambda}, \\
\left(1 - \frac {\lambda}{n}\right) ^ {- k} \rightarrow 1,
\end{array}
$$

where the $e^{-\lambda}$ comes from the compound interest formula from Section A.2.5 of the math appendix. So

$$
P (X = k) \rightarrow \frac {e ^ {- \lambda} \lambda^ {k}}{k !},
$$

which is the $\operatorname{Pois}(\lambda)$ PMF.

This theorem implies that if $n$ is large, $p$ is small, and $np$ is moderate, we can approximate the $\operatorname{Bin}(n,p)$ PMF by the $\operatorname{Pois}(np)$ PMF. The main thing that matters here is that $p$ should be small; in fact, the result mentioned after the statement of the Poisson paradigm says in this case that the error in approximating $P(X \in B) \approx P(N \in B)$ for $X \sim \operatorname{Bin}(n,p), N \sim \operatorname{Pois}(np)$ is at most $\min(p, np^2)$.

Example 4.8.4 (Visitors to a website). The owner of a certain website is studying the distribution of the number of visitors to the site. Every day, a million people independently decide whether to visit the site, with probability $p = 2 \times 10^{-6}$ of visiting. Give a good approximation for the probability of getting at least three visitors on a particular day.

Solution:

Let $X \sim \operatorname{Bin}(n, p)$ be the number of visitors, where $n = 10^6$. It is easy to run into computational difficulties or numerical errors in exact calculations with this distribution since $n$ is so large and $p$ is so small. But since $n$ is large, $p$ is small, and $np = 2$ is moderate, $\operatorname{Pois}(2)$ is a good approximation. This gives

$$
P (X \geq 3) = 1 - P (X &lt; 3) \approx 1 - e ^ {- 2} - e ^ {- 2} \cdot 2 - e ^ {- 2} \cdot \frac {2 ^ {2}}{2 !} = 1 - 5 e ^ {- 2} \approx 0. 3 2 3 3,
$$

which turns out to be extremely accurate.