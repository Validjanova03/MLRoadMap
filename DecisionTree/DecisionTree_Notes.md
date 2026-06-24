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


