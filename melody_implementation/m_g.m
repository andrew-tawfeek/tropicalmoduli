(* The below code is an implementation by Melody Chan (Brown University) in Mathematica for computing M_g *)
(* Sourced from https://www.math.brown.edu/mchan2/torelli/m_g *)

<<Combinatorica`

(* GENUS *) genus = 5;

maxcells=Table[0,{10}];

(* MAKE CYCLE FROM LIST OF MULTIPLICITIES *)
cycle[l_]:=Module[{ret, len, i,j},
 len = Length[l];
 ret = EmptyGraph[1];
 For[i=1, i<len, i++,
	ret = AddVertex[ret];
	For[j=1, j<=l[[i]], j++,
		ret = AddEdge[ret, {i,i+1}];
	];
 ];
 For[j=1, j<=l[[len]], j++,
	ret = AddEdge[ret, {1,len}];
 ];
 ret
]

(* MAKE PATH FROM LIST OF MULTIPLICITIES *)
path[l_]:=Module[{ret, len, i,j},
 len = Length[l];
 ret = EmptyGraph[1];
 For[i=1, i<=len, i++,
	ret = AddVertex[ret];
	For[j=1, j<=l[[i]], j++,
		ret = AddEdge[ret, {i,i+1}];
	];
 ];
 ret
]

(* ADD "LOLLIPOPS" AT GIVEN LIST OF VERTICES *)
loll[g_,l_]:=Module[{i, len, ret, newv},
 len=Length[l];
 ret=g;
 For[i=1,i<=len,i++,
	ret = AddVertex[ret];
	newv = V[ret];
	ret = AddEdge[ret, {l[[i]], newv}];
	ret = AddEdge[ret, {newv, newv}];
 ];
 ret
]

(* MAXIMAL CELLS OF M_ 2 *)
maxcells[[2]] = {
FromAdjacencyMatrix[{{0,3},{3,0}}],
FromAdjacencyMatrix[{{1,1},{1,1}}]
};

(* MAXIMAL CELLS OF M_ 3 *)
maxcells[[3]] = {
CompleteGraph[4],
FromUnorderedPairs[{{1,2},{1,2},{3,4},{3,4},{1,3},{2,4}}],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,3},{3,4},{4,4}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,3},{3,4},{4,4}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,4},{3,3},{4,4}}]
};

(* MAXIMAL CELLS OF M_4 *)
maxcells[[4]] = {
FromUnorderedPairs[{{1,2},{2,3},{3,4},{1,4},{1,5},{3,5},{2,6},{4,6},{5,6}}],
GraphProduct[CompleteGraph[2],CompleteGraph[3]],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,4},{3,5},{4,5},{3,6},{4,6},{5,6}}],
FromUnorderedPairs[{{1,2},{1,2},{3,4},{5,6},{5,6},{1,3},{3,5},{2,4},{4,6}}],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6},{5,6}}],
FromUnorderedPairs[{{1,2},{1,2},{2,3},{3,4},{3,4},{4,5},{5,6},{5,6},{1,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,4},{3,5},{4,5},{3,6},{4,6},{5,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,4},{3,4},{3,5},{4,6},{5,6},{5,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{3,4},{3,4},{4,5},{5,6},{5,6},{2,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,3},{3,4},{4,5},{4,6},{5,6},{5,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,4},{3,4},{3,5},{4,5},{5,6},{6,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{4,4},{4,5},{5,6},{2,5},{3,6},{3,6}}],
FromUnorderedPairs[{{1,1},{2,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6},{5,6}}],
FromUnorderedPairs[{{1,1},{1,2},{2,3},{2,3},{3,4},{4,5},{4,5},{5,6},{6,6}}],
FromUnorderedPairs[{{1,1},{2,2},{3,3},{1,4},{2,5},{3,6},{4,5},{5,6},{4,6}}],
FromUnorderedPairs[{{1,1},{2,2},{1,3},{2,3},{3,4},{4,5},{4,5},{5,6},{6,6}}],
FromUnorderedPairs[{{1,1},{2,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,5},{6,6}}]
};

(* MAXIMAL CELLS OF M_5 *)
maxcells[[5]] = {
AddEdges[Cycle[8],{{1,6},{2,5},{3,7},{4,8}}],
(k2=CompleteGraph[2]; GraphProduct[k2,k2,k2]),
AddEdges[Cycle[8],{{1,6},{2,7},{3,5},{4,8}}],
AddEdges[Cycle[8],{{1,5},{2,8},{3,7},{4,6}}],
AddEdges[Cycle[8],{{1,3},{2,4},{5,7},{6,8}}],
AddEdges[cycle[{2,1,1,1,1,1,1,1}], {{3,6},{4,7},{5,8}}],
AddEdges[cycle[{2,1,1,1,1,1,1,1}], {{3,6},{4,8},{5,7}}],
AddEdges[cycle[{2,1,1,1,1,1,1,1}], {{3,5},{4,7},{6,8}}],
AddEdges[cycle[{2,1,1,1,1,1,1,1}], {{3,8},{4,6},{5,7}}],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,3},{3,4},{4,5},{4,8},{5,6},{5,7},{6,7},{6,8},{7,8}}],
AddEdges[cycle[{2,1,1,1,2,1,1,1}], {{3,7},{4,8}}],
AddEdges[cycle[{2,1,1,1,2,1,1,1}], {{3,8},{4,7}}],
AddEdges[cycle[{2,1,1,2,1,1,1,1}], {{3,7},{6,8}}],
AddEdges[cycle[{2,1,2,1,1,1,1,1}], {{5,7},{6,8}}],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,3},{3,4},{4,5},{4,6},{5,6},{5,7},{6,8},{7,8},{7,8}}],
FromUnorderedPairs[{{1,2},{1,2},{3,4},{3,4},{5,6},{5,6},{1,7},{2,8},{3,7},{4,8},{5,7},{6,8}}],
AddEdges[cycle[{2,1,1,2,1,2,1,1}], {{3,8}}],
FromUnorderedPairs[{{1,2},{1,2},{1,3},{2,3},{3,4},{4,5},{4,8},{5,6},{5,6},{6,7},{7,8},{7,8}}],
AddEdges[path[{2,1,1,2,1,1,2}], {{1,3},{6,8}}],
cycle[{2,1,2,1,2,1,2,1}],
loll[AddEdges[Cycle[7],{{2,5},{3,6},{4,7}}] ,{1}],
loll[AddEdges[Cycle[7],{{2,6},{3,5},{4,7}}] ,{1}],
loll[AddEdges[Cycle[7],{{2,4},{3,6},{5,7}}] ,{1}],
loll[AddEdges[Cycle[7],{{2,7},{3,5},{4,6}}] ,{1}],
loll[AddEdges[cycle[{1,1,1,2,1,1,1}],{{2,6},{3,7}}] ,{1}],
loll[AddEdges[cycle[{1,1,2,1,1,1,1}],{{2,6},{5,7}}] ,{1}],
loll[AddEdges[cycle[{1,1,1,2,1,1,1}],{{2,7},{3,6}}] ,{1}],
loll[AddEdges[cycle[{1,2,1,1,1,1,1}],{{4,6},{5,7}}] ,{1}],
loll[AddEdges[path[{2,1,1,1,1,1}],{{4,6},{3,7},{5,7}}] ,{1}],
loll[AddEdges[path[{1,1,1,1,1,2}],{{1,3},{2,4},{5,7}}] ,{1}],
loll[AddEdges[path[{1,1,2,1,1,2}],{{2,7},{1,5}}] ,{1}],
loll[AddEdges[cycle[{1,1,2,1,1,2,1}],{{2,5}}] ,{1}],
loll[AddEdges[cycle[{1,1,2,1,2,1,1}],{{2,7}}] ,{1}],
loll[AddEdges[path[{1,2,1,1,1,2}],{{1,4},{5,7}}] ,{1}],
loll[AddEdges[path[{2,1,1,1,2,1}],{{3,7},{4,7}}] ,{1}],
loll[AddEdges[path[{2,1,1,1,1,2}],{{1,3},{5,7}}] ,{4}],
loll[cycle[{1,2,1,2,1,2,1}] ,{1}],
loll[AddEdges[path[{2,1,1,2,1,2}],{{3,7}}] ,{1}],
loll[AddEdges[path[{2,1,2,1,1,2}],{{5,7}}] ,{1}],
loll[AddEdges[Cycle[6], {{2,5},{3,6}}], {1,4}],
loll[AddEdges[Cycle[6], {{2,5},{4,6}}], {1,3}],
loll[AddEdges[Cycle[6], {{2,6},{3,5}}], {1,4}],
loll[AddEdges[Cycle[6], {{4,6},{3,5}}], {1,2}],
loll[AddEdges[path[{1,1,1,1,1}], {{4,6},{3,5},{2,6}}], {1,1}],
loll[FromUnorderedPairs[{{1,2},{1,2},{1,5},{2,3},{3,4},{3,6},{4,5},{5,6}}],{4,6}],
loll[AddEdges[cycle[{1,1,2,1,1,1}], {{2,5}}], {1,6}],
loll[AddEdges[cycle[{1,1,1,2,1,1}], {{2,6}}], {1,3}],
loll[AddEdges[path[{1,1,1,2,1}], {{2,6},{3,6}}], {1,1}],
loll[AddEdges[path[{1,1,1,1,2}], {{1,3},{4,6}}], {1,2}],
loll[AddEdges[path[{1,1,1,1,2}], {{1,3},{2,4}}], {1,6}],
loll[cycle[{1,1,2,1,2,1}],{1,2}],
loll[cycle[{1,2,1,1,2,1}],{1,4}],
loll[AddEdges[path[{1,1,2,1,2}], {{2,6}}], {1,1}],
loll[AddEdges[path[{2,1,1,2,1}], {{3,6}}], {1,6}],
loll[AddEdges[path[{1,2,1,1,2}], {{4,6}}], {1,1}],
loll[AddEdges[path[{2,1,1,1,2}], {{4,6}}], {1,3}],
loll[path[{2,1,2,1,2}], {1,6}],
loll[FromUnorderedPairs[{{1,4},{1,5},{2,4},{2,5},{3,4},{3,5}}],{1,2,3}],
loll[AddEdges[Cycle[5], {{3,5}}], {1,2,4}],
loll[AddEdges[path[{1,1,1,1}], {{2,4},{3,5}}], {1,1,5}],
loll[cycle[{1,1,1,2,1}],{1,2,3}],
loll[AddEdges[path[{1,2,1,1}], {{1,4}}], {1,5,5}],
loll[AddEdges[path[{1,1,1,2}], {{3,5}}], {1,1,2}],
loll[AddEdges[path[{2,1,1,1}], {{3,5}}], {1,4,5}],
loll[path[{1,2,1,2}],{1,1,5}],
loll[path[{2,1,1,2}],{1,3,5}],
loll[Cycle[4],{1,2,3,4}],
loll[AddEdges[path[{1,1,1}], {{2,4}}], {1,1,3,4}],
loll[path[{1,1,2}],{1,1,2,4}],
loll[path[{1,2,1}],{1,1,4,4}],
loll[path[{1,1}],{1,1,2,3,3}]
};

degseq[g_] := Module[{A,n,i,j},
 A = ToAdjacencyMatrix[g];
 n = Length[A];
 Sort[Table[Sum[A[[i,j]],{j,1,n}]+A[[i,i]],
 {i, n}]]
 ]

makeobj[g_]:= {g, Table[0,{V[g]}] }

(* Make an undirected adjacency matrix into a list of directed edges *)
edges[m_]:=Module[{i,j,k,ret},
        ret={};
        For[i=1,i<=Length[m],i++,
                For[j=i,j<=Length[m],j++,
                        For[k=1,k<=m[[i,j]],k++,
                                ret = Append[ret, i->j]
                        ];
                ];
        ];
        ret
]

contract[g_,l_,k_]:=Module[{gnew,lnew,v,w,A,p,i,brk,last},
 lnew=l;
 A=ToAdjacencyMatrix[g];
 p = ToUnorderedPairs[g];
 {v,w}=Sort[ Edges[g][[k]] ];
 last=V[g];
 If[v==w,
        (* THEN DELETE THE LOOP AND ADD 1 TO WEIGHT AT V *)
        A[[v,v]]--; gnew = FromAdjacencyMatrix[A]; lnew[[v]]++;,
        (* ELSE DELETE ONE COPY OF THE EDGE... *)
         brk = 0; i = 1;
         While[brk ==0,
                 If [p[[i]] == {v,w},
                         p = Drop[p,{i,i}];
                         brk = 1;,
                         i++;
                 ];
         ];
         (* THEN REPLACE W->V, LAST->W *)
         For[i=1,i<=Length[p],i++,
                 If[p[[i]][[1]] == w, p[[i]][[1]]=v, Null];
                 If[p[[i]][[2]] == w, p[[i]][[2]]=v, Null];
                 If[p[[i]][[1]] == last, p[[i]][[1]]=w, Null];
                 If[p[[i]][[2]] == last, p[[i]][[2]]=w, Null];
         ];
        gnew= FromUnorderedPairs[p];
        (* AND EDIT LNEW: V GETS V+W, W GETS LAST, LAST GETS REMOVED *)
        lnew[[v]] = lnew[[v]] + lnew[[w]];
        lnew[[w]] = lnew[[  Length[lnew]  ]];
        lnew = Delete[lnew, Length[lnew]];
 ];
 If[Length[lnew] == V[gnew], Null, Print ["FAIL",g,l,gnew,lnew];Pause[1];];
 {gnew,lnew}
]

isoq[g1_,l1_,g2_,l2_] := Module[{ret, ps, I,i},
        ret = False;
        If [ (degseq[g1]==degseq[g2]) && (Sort[l1]==Sort[l2]),
                (* CHECK IF THERE IS AN ISO, SET RET = TRUE IF SO *)
                ps = Permutations[V[g1]];
                For[i = 1, i<=Length[ps], i++,
                        If[ IsomorphismQ[g1,g2,ps[[i]] ] && Permute[ l2,ps[[i]]                                              ] == l1,
                        ret = True, Null        ];
                ];
                (* OTHERWISE, RET REMAINS 0 *)
                Null;
        ];
        ret
]

(* MAKE THE MAXIMAL CELLS MARKED GRAPHS *)
vli={};
For[i=1,i<=Length[maxcells[[genus]]],i++,
        vli = Append[vli, makeobj[maxcells[[genus]][[i]]]];
];



poset=EmptyGraph[Length[vli]];
i=1;
(* FOR EACH VERTEX IN POSET... *)
While[i<=V[poset],
        {gr, li} = vli[[i]];
        (* COMPUTE ITS CONTRACTIONS ONE BY ONE... *)
        For[k=1,k<=M[gr],k++,
                {grnew,linew} = contract[gr,li,k];
                (* FOR EACH CONTRACTION, IS IT ISOMORPHIC TO A KNOWN VERTEX? *)
                flag = 1; j = 1;
                While[flag==1 && j <= V[poset],
                        {g3,l3} = vli[[j]];
                        (* IF YES , ADD EDGE *)
                        If[isoq[grnew,linew, g3,l3],
                                (* ADD AN EDGE IF THERE ISNT ONE... *)
                                If[MemberQ[Edges[poset], {i,j}], Null,
                                        poset = AddEdge[poset, {i,j}];
                                ];
                                (* ...AND STOP LOOKING *)
                                flag = 0;,
                                Null;
                        ];
                        j++;
                ];
                If[flag==1,
                        poset = AddVertex[poset];
                        poset = AddEdge[poset, {i, V[poset]}];
                        vli = Append[vli, {grnew, linew}],
                        Null;
                ];
        ];
        i++;
];

(* MAKE GRAPHICS FOR EACH VERTEX OF THE POSET *)
vscale=10;
vli2={};
For[i=1,i<=Length[vli],i++,
    vli2=Append[vli2, GraphPlot[edges[ToAdjacencyMatrix[vli[[i]][[1]]]],ImageSize->80,MultiedgeStyle->0.3,SelfLoopStyle->1,PlotStyle->{Blue},VertexRenderingFunction->({Black,Inset[vli[[i,2]][[#2]],#1+{0.1,0}]} &)]];
    ];
(* THE BOTTOM VERTEX SHOULD DISPLAY A NUMBER AND NOT THE EMPTY GRAPH *)
vli2[[ Length[vli2] ]] = vli[[ Length[vli] ]][[2]][[1]];

(* COMPUTE VERTEX COORDINATES BY HAND *)

(* FIRST MAKE A LIST OF NUMBERS OF EDGES *)
numedges=Table[0,{Length[vli]}];
For[i=1,i<=Length[vli],i++,
        numedges[[i]] = M[vli[[i]][[1]] ];
];
(* NOW COORDINATES *)
coords=Table[0,{Length[vli]}];
howmanysofar=Table[0,{M[vli[[1]][[1]]]+1}]; (* Ith entry tells us how many graphs with i-1 edges we have encountered *)
For[i=1,i<=Length[vli],i++,
        coords[[i]] = i->{(-1)*Length[Position[numedges, numedges[[i]]]]+2*howmanysofar[[ numedges[[i]]+1 ]], 2*numedges[[i]]*vscale};
        howmanysofar[[ numedges[[i]]+1 ]]++;
];
GraphPlot[edges[ToAdjacencyMatrix[poset]],VertexRenderingFunction->({White,Disk[#1,.5],Black,Inset[vli2[[#2]],#1]} &),VertexCoordinateRules->coords]
