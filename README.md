# DeepAlgebra
Automating LaTeX understanding after https://arxiv.org/abs/1610.01044

The first step is to implement an enhanced semantic tagger which will annotate .tex files (from the Stacks Project). The idea is to use both rule-based approach and machine learning methods like Word2Vec. 

New mathematical concepts are TYPEs. Particular realization of a given TYPE is a VARIABLE (VAR). 

E.g. "Let $X$ be a scheme", here "X" is VAR of TYPE "scheme".

We use spaCy for semantic tagging. With the first iteration we would like to take a mathematical paper in .tex and output another .tex file with all the mathematical terms correctly identified either as TYPE or VAR. On top of that we want to create a graph of knowledge, which would show all the connections between different types. Nodes would be types and edges would go from node A to node B, whenever node B is a sub-type of node A, e.g. node A = "group", node B = "algebraic group".

