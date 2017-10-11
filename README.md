# deep-algebra
Automatic LaTeX understanding (and more) based on https://przchojecki.github.io/deepalgebra/

The first step is to implement an enhanced semantic tagger which will annotate .tex files (from the Stacks Project). We start with a rule based approach to look for new definitions.

New mathematical concepts are TYPES. Particular realization of a given TYPE is a VARIABLE (VAR). 

E.g. "Let $X$ be a scheme", here "X" is VAR of TYPE "scheme".

We use spaCy for semantic tagging.

