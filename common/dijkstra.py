#sponsored by chatGPT
# Hey, can you give a python implementation of dijkstra's algortihm?
# Input is a dictionary of nodes: dictionary of edges (node: distance), start node and end node
import heapq

def dijkstra(graph, start, end):
  # initialize distances from start node to all other nodes
  distances = {node: float("inf") for node in graph}
  distances[start] = 0

  # initialize a set of visited nodes
  visited = set()

  # initialize a priority queue of distances
  # we use a priority queue so that we can always get the smallest
  # distance in O(1) time
  queue = []
  heapq.heappush(queue, [distances[start], start])

  while queue:
    # get the smallest distance from the queue
    current_distance, current_node = heapq.heappop(queue)

    # if we have reached the end node, we can stop
    if current_node == end:
      break

    # if we have already visited this node, we can skip it
    if current_node in visited:
      continue

    # mark the current node as visited
    visited.add(current_node)

    # check the distances to each neighbor
    for neighbor, edge_distance in graph[current_node].items():
      # if the distance to the neighbor is shorter using the current node,
      # update the distance for the neighbor
      if distances[neighbor] > current_distance + edge_distance:
        distances[neighbor] = current_distance + edge_distance

        # add the neighbor to the queue with the updated distance
        heapq.heappush(queue, [distances[neighbor], neighbor])

  # return the final distances to the end node
  return distances[end]


def dijkstra_path(graph, start, end):
    # Set of unvisited nodes
    unvisited = set(graph.nodes())
    # Set of visited nodes
    visited = set()
    # Set of distances from start to each node
    distances = {node: float('inf') for node in unvisited}
    # Set of previous nodes on the shortest path from start to each node
    previous = {node: None for node in unvisited}

    # Set the distance from start to the start node to be 0
    distances[start] = 0

    # Loop until there are no more unvisited nodes
    while unvisited:
        # Get the unvisited node with the smallest distance from start
        current = min(unvisited, key=lambda node: distances[node])

        # If the current node is the end node, we have found the shortest path
        if current == end:
            break

        # Mark the current node as visited
        visited.add(current)
        unvisited.remove(current)

        # Update the distances of the unvisited neighbors of the current node
        for neighbor, distance in graph[current].items():
            if neighbor in visited:
                continue

            new_distance = distances[current] + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    # Build the shortest path from start to end
    path = []
    current = end

    while current:
        path.append(current)
        current = previous[current]

    # Reverse the path to get the start-to-end path
    return list(reversed(path))
