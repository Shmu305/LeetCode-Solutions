https://emre.me/categories/#coding-patterns - educative.io 'sneak peak' of each pattern

https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed - broad overview of classic patterns

https://seanprashad.com/leetcode-patterns/ - WebSite based on educative.io course 

https://github.com/SeanPrashad/leetcode-patterns - more tips/tricks for pattern recognition including solutions 

https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU - Blind 75 list - The most important list?

# LeetCode-Solutions
A place to store LeetCode solutions to help track my progress and consistency. This repo is focused on learning all the LC patterns/tricks. Nearly all the problems on LC can be solved by knowing about 16 different patterns. Multiple questions are solved with the same patterns. 

*Solutions are done in Python because Python is by far the best interview language since it is less wordy than other languages. For example, let's compare creating a map in Java vs Python.
    
    Java...
    Map<String, String> myMap  = new HashMap<String, String>()
    
    Python...
    myMap = {}
    
As you can see, it saves a lot of time knowing python and interviews are timed!
    

# BFS...
In BFS, we start by pushing the root node into a queue. Then, we remove an element(node) from the front of the queue. For every node removed from the queue, we add all its children to the back of the same queue. We keep on continuing this process till the queue becomes empty. In this way, we can traverse the given tree on a level-by-level basis.
If you look at my solutions under the BFS folder, you will see that each problem has an identical solution. Depending on the question asked, only slight modifications were needed. 

# Sliding Window
A sliding window is an abstract concept commonly used in array/string problems. A window is a range of elements in the array/string which usually defined by the start and end indices. The idea is to increase the window until contraints are met. Then remove the first elements in the window while the contrains are still met and 'slide' the window-start up for each index thats removed.
