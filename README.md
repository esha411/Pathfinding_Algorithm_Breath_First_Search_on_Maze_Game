# ✨ Pathfinding in Strategy Games and Maze Solving Using Breath First Search Algorithm

How can we determine the shortest path between two points? 

In computing, solving issues like these is very common. 
In a video game, an opponent AI must be able to identify the player's destination quickly.
You need Google Maps to find the quickest route to your destination. 
Here, The goal is to simply navigate a maze.

Pathfinding could be used to give answers to the question “How do I get from source to destination?”. In most cases, the path from source (current point) to the destination (next point) could possibly include several different solutions, but if possible, the solution needs to cover the following goals:

1.The way to get from source A to destination B.

2.The way to get around obstacles in the way.

3.The way to find the shortest possible path.

4.The way to find the path quickly.

## 🌟 Breath First Search Algorithm

Pathfinding requires significant amount of resources especially in movement intensive games. For that reason, an efficient and inexpensive approach is needed.

Breadth-First search is widely used in pathfinding and graph traversal. This algorithm will be used to find the shortest path between two points on the image. The proposed methodology is shown in Figure.



Breadth-First search algorithm uses First-In-First-Out queue. This algorithm involves visiting nodes one at a time. 

This Breadth-First search algorithm visits nodes in the order of their distance from the source node, where distance is measured as the number of traversed edges.
