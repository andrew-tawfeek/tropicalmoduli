# Tropical Moduli Project
This repository is dedicated to computing the cells/graphs within the moduli space of tropical curves $\mathcal{M}_{g,n}^\text{trop}$. 

This research project is being run by the participants of the University of Washington's [Tropical Geometry Seminar](https://www.atawfeek.com/moduli).

---

## Questions/Directions:
- Using Sage's **convex rational polyhedral cone** package (paired with **toric plotter**) we could potentially display $\mathcal{M}_{g,n}^\text{trop}$ as a generalized cone complex and have this interplay nicely with the poset of dual grpahs.
- Following up on the above: assuming an implementation of the above, we should then be able to compute the _link_ $\Delta_{g,n}$ of the cone complex -- potentially paving the way towards cohomology[^3]...
- Can we extend the code to interact well with the matroid perspective[^4] of tropical geometry, perhaps with the aid of Sage's already well-developed **matroid package**?
- **(Hard)** What can we do towards extending our work to compactifications of other moduli spaces, such as K3 surfaces?[^1][^2]


[^1]: Ranganathan, Dhruv. "[Tropical Geometry: Forwards and Backwards](https://www.ams.org/notices/202307/rnoti-p1048.pdf)." NOTICES OF THE AMERICAN MATHEMATICAL SOCIETY 70.7 (2023).
[^2]: Alexeev, Valery, and Philip Engel. "[Compact moduli of K3 surfaces](https://arxiv.org/pdf/2101.12186)." Annals of Mathematics 198.2 (2023): 727-789.
[^3]: Chan, Melody, Søren Galatius, and Sam Payne. "[Tropical curves, graph complexes, and top weight cohomology of $\mathcal{M}_g$](https://arxiv.org/pdf/1805.10186
)." Journal of the American Mathematical Society 34.2 (2021): 565-594.
[^4]: Ardila, Federico. "[The geometry of matroids](https://www.ams.org/journals/notices/201808/rnoti-p902.pdf)." Notices of the AMS 65.8 (2018).

## SageMath Documentation Links:
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

