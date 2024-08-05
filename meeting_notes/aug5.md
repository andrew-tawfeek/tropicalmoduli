# August 5, 2024

**Goals for the day:**
- Finish the top down algorithm
- Have an API convert between Sage and Python
- Work towards Cone Complexes for $\mathcal{M}_{g,n}^\text{trop}$ in Sage
- Create output table for the $\mathcal{M}_{g,n}^\text{trop}$'s we can compute
- Organize meeting notes
- Set up an Overleaf for keeping track of sources/conjectures/proofs etc.

**Big Question:** Given two tropical graphs $(G,w)$ and $(G',w')$, is there a right notion of morphism between the two such that the contracted edges map to eachother? More specifically, _how can we characterize on a single layer when two graphs will contract to the same graph on the next layer?_

- Aside observation: we should study the first (bottom) two layers of $\mathcal{M}_{g,n}^\text{trop}$ to obseve this -- as every graph on that layer will neccesary contract to the same graph (singleton) below.

- See photos on GDrive...

- Relevant scribble (clean up later):
> say we generated the top layer
>
> for each graph, we need to look at every possible list of contractions that bring us down
> 
> the problem is, downstairs, we then have to delete duplicates by checking isomorphisms
> 
> 
> ----
> 
> going back to the first step, how do we produce all possible contractions such that, there, there are no duplicates?
> 
> 
> --
> 
> for each pair of vertices (including same vertex and itself), contract edge, add it to list of outputs
> 
> --- 
> 
> we came up with a SLIGHTLY better way
> 
> look at a graph and calculate its set of automorphisms
> partition the set of vertices under it's orbit under the isomorphisms
> 
> e.g. consider an automorphism that sends vertex A to vertex B, so A and B are indistinguishable as far as the graph structure is concerned
> so  both those contractions connecting to A/B would yield isomorphic  graphs downstairs following contractions
> 
> going further.......!!
> 
> if we do these for all four graphs/on a level...