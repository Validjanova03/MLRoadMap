Decision Tree - The mental model. A dicision tree is just a game of 20 questions. Every split is a Yes/No questions. It keep asking untill each group is pure.
Purity is measured with GINI IMPURITY or ENTROPY
Key Terms:
Root Node - Very first split
Internal node - any split in the middle
Leaf node - final answer, no more split
Depth - How many splits deep you go
Pure Node - All one class(perfect), all Yes/No
Branches - A subsection of the entire tree (also known as a sub-tree)
Maximum Depth - Maximum number of branches between the top and the lower end

IMAGE





How to evaluate the purity of leaf or decide when to stop?
On Categorical variables: Entropy and Information Gain (IG)
On Continious variables: Reduction in variance
We need always low impurity: Gini = 0.00
Gini: Asks "If i randomly pick 2 candies from this bowl, what is chance they are different olours?"
High Chance = Messy = High Gini
Low Chance = Organised = Low Gini
Gini = 1 -(p_red^2 + p_blue^2)
p_red = 3/4 = 0.75 
p_blue = 1/4 = 0.25
Gini = 1 - (0.75^2 + 0.25^2) = 1 - (0.5625 + 0.0625) = 1 - 0.625 = 0.375
0.375 - moderately impure - not terrible, but not very clean eaither.(A Decision tree would continiue split)
Entopy: Entropy = -(p_red log2(p_red)) - p_blue

Pure bowl(all red): Entopy = 0.00
50/50 bowl: Entropy = 1.00 (worst)
3 red, 1 blue: Entropy = 0.81 (still not good) 


Information Gain (IG)
How much did this split clean up the mess?
Before split we have one bowl(messy). After the split we have 2 smaller bowls. If the two smaller bowls are cleaner than the original that split was useful.
IG = Gini(Before) - Average_Gini(after)

If IG is High - Split cleaned up alot -> Good split
If IG is Low - Split barely helped -> Bad split
Example: We have dataset of 10 samples, 6 Red , 4 Blue
Parent Gini(Before): p_red = 6/10, p_blue = 4/10
Gini(Parent) = 1 - (0.6^2 + 0.4^2) = 1 - (0.36 + 0.16) = 0.48
Split into 2 child nodes
* Child A: 4 Red, 1 Blue
Gini(A) = 1 - (4/5^2 + 1/5^2) = 1 - (0.64 + 0.04) = 0.32

* Child B: 2 Red, 3 Blue
Gini B: 1 - (2/5^2 + 3/5^2) = 1 - (0.4^2 + 0.6^2) = 1 - (0.16 + 0.36) = 0.48

Weighted average Gini (After):
WG(After) = 5/10 * 0.32 + 5/10 * 0.48 = 0.16 + 0.24 = 0.40
IG:
IG = 0.48 - 0.40 = 0.08 -> reduced impurity a little but not dramatically
We need higher IG





