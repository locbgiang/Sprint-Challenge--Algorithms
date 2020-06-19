#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n)
    Justify: a grows at n^2 
            it will takes n-time to reach n^3

b)
    O(n^2)
    Justify:  the for loop cost n-time
                the while loop cost another n-time 
            total time = n^2 

c)
    O(n)
    Justify: recursive here will take linear time
    A better solution is if we just take bunnies * 2 instead, we will have constant rt O(1)

## Exercise II

This is a binary search problem.  Drop the egg from middle of the building 

if the egg breaks move to the middle of the bottom half 
(top of the building now is the middle - 1), 

if it doesnt break move to the middle of the top half, 
(bottom of the building now is middle)

repeat until you find f when f+1 breaks the egg and f doesnt

O(log n)
