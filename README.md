# Binary-Search

## Recursive Binary Search without List Slicing</font>

The binary search algorithm in the textbook uses Python list slicing as part of the recursive divide-and-conquer approach it uses to solve the searching problem.

This is inefficient, as a new copy of the original input list is made at each recursive call. Albeit, the new list is reduced in size by alist//2 each time `binary_search` is recursively executed.

Replace the use of list slicing with a technique that eliminates the unnecessary list copying. Recall that you will need to pass the list along with the starting and ending index values for the sublist. 
