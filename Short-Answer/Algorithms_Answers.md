#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The run time of this function will increase exponentially given increases in the size of the inputs. The while loop will not be satisfied until our 'a' value is sufficiently high. Thus, the time complexity of this function is described as O(n^2)


b) For this code snippet, it appears at first glance that this could be O(log n) given the while loop's 'j' value. However, the function header contains a for loop that must iterate through every value in range n making the overall function's time complexity to be O(n).

c) The output of this function increases by the same amount (2) given each additional bunny. Therefore, the time complexity of the function is O(n).

## Exercise II

For this problem I am assuming that their is an optimal floor f that can be found that reduces the amount of eggs thrown / broken. I would first split the entire building in half and throw an egg from that floor. If it is broken, I would split the lower half of the building into another half and repeat the process. If the egg is not broken, we would split the upper half of the split building and repeat the process. We do this until an optimal floor f is found.

This solution is an example of a binary search tree with O(log n) time complexity.