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