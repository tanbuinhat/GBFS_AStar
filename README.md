# GBFS_AStar


* Based on the graph with given weight, find the shortest path according to the corresponding algorithm from start to finish vertex.

* The results returned by each algorithm are as follows
  1. GBFS: total heuristic on the path from origin to destination vertex. 
  2. A *: total length of the path from the origin to the destination vertex (does not contain heuristic)

The program reads from the file "input. txt" (according to the structure of the given input. txt file) and outputs the result as the cost of the corresponding algorithm to the "output. txt" file.



Input and output


Description:
* The first line contains 2 integers N and M are the number of vertices and the number of edges of the graph. 
* The next M lines give edge information of the graph, each line contains 3 numbers i, j, k representing the edge connecting from vertex i to vertex j with weight k. 
* The next N lines each contain a number x that is the heuristic value h (x). 
* The last line contains 2 integers u and v corresponding to the beginning and the end of the vertex. 

Sample GBFS algorithm:


<img width="631" alt="Screen Shot 2021-03-19 at 10 34 48" src="https://user-images.githubusercontent.com/60350737/111728205-fca7d580-889e-11eb-88f5-b98932a006a2.png">


Sample A* algorithm:




<img width="631" alt="Screen Shot 2021-03-19 at 10 36 02" src="https://user-images.githubusercontent.com/60350737/111728290-23fea280-889f-11eb-856f-1584e4d25521.png">
