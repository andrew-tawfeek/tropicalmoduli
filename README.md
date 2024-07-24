# Tropical Moduli Project
This repository is dedicated to computing the cells/graphs within the moduli space of tropical curves $\mathcal{M}_{g,n}^\text{trop}$. 

This research project is being run by the participants of the University of Washington's [Tropical Geometry Seminar](https://www.atawfeek.com/moduli).

---

## Current Goals:
- [ ] Compute the $f$-vector of the poset being output by the current implementation of $\mathcal{M}_{g,n}^\text{trop}$ and check against Theorem 2.12 of Melody's paper[^5]
- [ ] Can we implement a dynamic-approach to the computation, using the observation that $\mathcal{M}_{g,n}^\text{trop}$ admits a stratification by lower moduli $g$ and $n$? (Also, can we find an explicit source for this as a mathematical statement? Maybe in this[^6]?)
- [ ] Implement top-down approach to computation (e.g. by generating all maximal first, then contracting).
- [ ] Write-in a SageMath to/from Python translation (particularly cleanly between `networkx` and `graphs` for tropical curves) to expand compatibility between platforms (and to assist with later work, e.g. matroids...).
- [ ] Look into UW mathematics department/general usage computing cluster usage for large-scale computation of poset to store for future-use/offer publicly.
- [ ] Continue research into what aspects of the package are worthwhile developing based on most-recent publications (e.g. cohomology direction of cone complexes? etc. -- find and compile sources).


---

## Future Questions/Directions:
- Using Sage's **convex rational polyhedral cone** package (paired with **toric plotter**) we could potentially display $\mathcal{M}_{g,n}^\text{trop}$ as a generalized cone complex and have this interplay nicely with the poset of dual grpahs.
- Can we extend the code to interact well with the matroid perspective[^4] of tropical geometry, perhaps with the aid of Sage's already well-developed **matroid package**?
- Following up on the cone complexes: we should then be able to compute the _link_ $\Delta_{g,n}$ of the cone complex -- potentially paving the way towards cohomology[^3]...
- **(Hard)** What can we do towards extending our work to compactifications of other moduli spaces, such as K3 surfaces?[^1][^2]


[^1]: Ranganathan, Dhruv. "[Tropical Geometry: Forwards and Backwards](https://www.ams.org/notices/202307/rnoti-p1048.pdf)." Notices of the AMS 70.7 (2023).
[^2]: Alexeev, Valery, and Philip Engel. "[Compact moduli of K3 surfaces](https://arxiv.org/pdf/2101.12186)." Annals of Mathematics 198.2 (2023): 727-789.
[^3]: Chan, Melody, Søren Galatius, and Sam Payne. "[Tropical curves, graph complexes, and top weight cohomology of $\mathcal{M}_g$](https://arxiv.org/pdf/1805.10186
)." Journal of the American Mathematical Society 34.2 (2021): 565-594.
[^4]: Ardila, Federico. "[The geometry of matroids](https://www.ams.org/journals/notices/201808/rnoti-p902.pdf)." Notices of the AMS 65.8 (2018).
[^5]: Chan, Melody. "[Combinatorics of the tropical Torelli map](https://arxiv.org/pdf/1012.4539)." Algebra & Number Theory 6.6 (2012): 1133-1169.
[^6]: Arbarello, Enrico, Maurizio Cornalba, and Phillip A. Griffiths. Geometry of algebraic curves: volume II with a contribution by Joseph Daniel Harris. Springer Berlin Heidelberg, 2011.

## Relevant Documentation Links:
- [graph theory](https://doc.sagemath.org/html/en/reference/graphs/index.html)
- [convex rational polyhedral cones](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/cone.html#sage.geometry.cone.Cone)
- [toric plotter](https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/toric_plotter.html)
- [matroid theory](https://doc.sagemath.org/html/en/reference/matroids/index.html)


## Various helpful links:
- [Tropical Geometry Seminar](https://www.atawfeek.com/moduli)
- [Coding Project Homepage](https://www.atawfeek.com/coding-project)
- [Google Drive](https://drive.google.com/drive/folders/1hSjcd7dVly7yk6G-xA1ltIPTIa-PhVPd?usp=sharing) (UW-email required)
- [Zulip Chat](https://uwtropgeo.zulipchat.com/) (UW-email required)

---

