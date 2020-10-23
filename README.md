# LeetCode-Solutions
A place to store LeetCode solutions to help track my progress and consistency. This repo is focused on learning all the LC patterns/tricks. Nearly all the problems on LC can be solved by knowing about 14 different patterns. Multiple questions are solved with the same patterns. 

##BFS...
In BFS, we start by pushing the root node into a queuequeue. Then, we remove an element(node) from the front of the queuequeue. For every node removed from the queuequeue, we add all its children to the back of the same queuequeue. We keep on continuing this process till the queuequeue becomes empty. In this way, we can traverse the given tree on a level-by-level basis.
