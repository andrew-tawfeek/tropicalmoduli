which layer of m_g,n is the widest one? (math result? matroid top-heavy? check m_g,n geometry of varieties)


current desired algoirthms:
sorting algorithms: as we generate each level, sort them so the isomorphism check has to check less things (i.e. we want clever isomorphism checks)
top down algoriithms
combing top-down and bottom-up


(done -- tried, but didn't have significant gains)
(small difference (e.g. 11 mins vs 12 mins), zawad has committed this to leave in)
before automorphism check:
- check vertex counts
- check edge counts
- bite the bullet: call the function
 
(done)
adopt in pickling in python

(still todo)
add into current algorithms: keep count running of how many times isomorphism-check is being called

**Question** (important for top-down):

Given trees $T_1$ and $T_2$, how do we characterize when
$$T_1 \cup \{e\} \cong T_2 \cup \{e'\}$$
for edges $e,e'$ connecting pairs of vertices?

**Conjecture:** When $n=0$ in $\mathcal{M}_{g,n}^\text{trop}$, the widest level of the poset is $2g-1$.



ALSO TODO:
- start up overleaf
- upload photos to gdrive from meeting