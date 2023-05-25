
export interface IGraph {
  nodes: INode[],
  edges: IEdge[],
}

export interface INode {
  id: number,
  label?: string,
}

export interface IEdge {
  from: number,
  to: number,
  weight: number,
}






export const createAdjacencyMatrix = (graph: IGraph): number[][] => {
  const matrix: number[][] = []
  for (let i = 0; i < graph.nodes.length; i++) {
    matrix[i] = [] // create row
    for (let j = 0; j < graph.nodes.length; j++) {
      matrix[i][j] = 0 // create column
    }
  }
  graph.edges.forEach(edge => {
    matrix[edge.from][edge.to] = edge.weight
    matrix[edge.to][edge.from] = edge.weight
  })
  return matrix
}

export const createAdjacencyList = (graph: IGraph): number[][] => {
  const list: number[][] = [] // create list
  for (let i = 0; i < graph.nodes.length; i++) {
    list[i] = [] // create row
  }
  graph.edges.forEach(edge => {
    list[edge.from].push(edge.to)
    list[edge.to].push(edge.from)
  })
  return list
}

export const createGraph = (n_nodes: number, n_edges: number): IGraph => {
  const nodes: INode[] = []
  const edges: IEdge[] = []

  // create nodes
  for (let i = 0; i < n_nodes; i++) {
    nodes.push({
      id: i,
      label: `Node ${i}`
    })
  }

  // create edges
  while (edges.length < n_edges) {
    const from = Math.floor(Math.random() * n_nodes)
    const to = Math.floor(Math.random() * n_nodes)
    const weight = Math.floor(Math.random() * 9 + 1)

    const skip = edges.some((edge) => {
      if (edge.from === from && edge.to === to) return true

      else if (edge.from === to && edge.to === from) return true

      else if (from === to) return true

    })
    if (!skip)
      edges.push({
        from,
        to,
        weight
      })
  }

  const graph: IGraph = {
    nodes,
    edges
  }

  return graph
}
