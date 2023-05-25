import { createGraph, createAdjacencyMatrix, createAdjacencyList, IGraph, INode, IEdge } from './GraphUtils.js'

const N_NODES = 5
const MAX_EDGES = 6

const graph: IGraph = createGraph(N_NODES, MAX_EDGES)


const prim_mst = (graph: IGraph) => {
  // WARN: STEP 0
  // Inizializzo un grafo vuoto che rappresentera' l'mst
  const mst: IGraph = {
    nodes: [],
    edges: []
  }

  // WARN: STEP 1
  // get random node from graph
  const uniqueNodes: Set<number> = new Set<number>()
  const startNode: INode = graph.nodes[Math.floor(Math.random() * graph.nodes.length)]
  uniqueNodes.add(startNode.id)

  // add startNode to mst
  mst.nodes.push(startNode)
  console.log(`start node: ${startNode.id}`)

  // WARN: STEP 2
  // Considero i nodi adiacenti al nodo di partenza
  // Fra questi, scelgo quello con peso minore

  // Per facilitare questa ricerca uso una lista di adiacenza
  const nearestNodes: number[] = createAdjacencyList(graph)[startNode.id]
  console.log(`nearest nodes: ${nearestNodes}`)

  // dei nodi vicini prendo il nodo con peso minore
  let minWeight: number = Infinity
  let selectedNode: number = -1
  for (let i = 0; i < nearestNodes.length; i++) {
    // get distance from startNode and from nearestNode
    const distance: number = createAdjacencyMatrix(graph)[startNode.id][nearestNodes[i]]
    if (distance < minWeight) {
      minWeight = distance
      selectedNode = nearestNodes[i]
    }

  }

  console.log(`selected node: ${selectedNode}`)

  mst.nodes.push(graph.nodes[selectedNode])
  mst.edges.push({
    from: startNode.id,
    to: selectedNode,
    weight: minWeight
  })

  uniqueNodes.add(selectedNode)

  // WARN: STEP 3
  // Considero i nodi adiacenti ai nodi gia' facente parte dell'mst
  // Fra questi, scelgo quello con peso minore
  // Ripeto fino a quando non ho aggiunto tutti i nodi



  const uniqueNearesNodes: Set<number> = new Set<number>()

  uniqueNodes.forEach(node => {
    const nearestNodes: number[] = createAdjacencyList(graph)[node]
    nearestNodes.forEach(nearestNode => {
      uniqueNearesNodes.add(nearestNode)
    })
  })


  uniqueNodes.forEach(node => {
    uniqueNearesNodes.delete(node)
  })

  console.log(uniqueNearesNodes)
  // ora devo trovarer il nodo con peso minore



  return mst
}

console.log(graph)
// console.log(createAdjacencyMatrix(graph))
console.log(createAdjacencyList(graph))

console.log(prim_mst(graph))

