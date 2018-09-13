# spectral_embedding

Weighted spectral embedding of graphs

This repository contains the implementation in Python of weighted spectral embedding, as described in the paper:

Weighted spectral embedding of graphs, by Thomas Bonald, Alexandre Hollocou, Marc Lelarge, Allerton 2018.


## Getting started

```python
from spectral_embedding import *

spectral = SpectralEmbedding()
```

Import a toy graph:

```python
import networkx as nx

graph = nx.karate_club_graph()
adjacency = nx.to_scipy_sparse_matrix(graph)
```

Spectral embedding

```python
spectral.fit(adjacency)
embedding = spectral.embedding_
```

## Experiments

Experiments on real datasets are available as a Jupyter notebook:

```python
example.ipynb
```

## License

Released under the 3-clause BSD license.

