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


