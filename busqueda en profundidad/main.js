const grafo = [1, 2, 3, 4, 5, 6];

const visitado = Array.from(grafo, (i) => false);

function depthFirstSearch(graph, i) {
  visitado[i] = true;
  console.log(`${graph[i]} visitado`);
  for (let j = 0; j < graph.length; j++) {
    if (visitado[j] == false) {
      console.log(`${graph[j]} no visitado`)
      depthFirstSearch(graph, j);
    }
  }
}
console.log(grafo);
depthFirstSearch(grafo, 0);
console.log(visitado);