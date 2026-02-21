# Python-Exercises
A repository created for practice exercises that are not part of a big project, to help me track my progress.

---

## Binary Search
A search method that efficiently finds the position of a target value in a **sorted** array by repeatedly dividing the search interval in half.<br>
It's complexity is \(O(\log n)\).<br>

Also created a recursive binary search function.<br>
This code helped me better understand divide-and-conquer thinking and practice basic Big O notation.

---

## Interpolation search
A search method that improves on binary search for **sorted (best for uniformly distributed)** arrays by estimating target location, instead of always checking the middle. <br>

This code helped me practice reasoning about index formulas, and compare its behavior to binary search in different input cases.

---

## Bubble Sort
A sort method that gets an array and goes over it cell by cell each time comparing it to the next one and swapping them if needed. <br>
It's complexity is \(O(\log n^2)\).<br>

The second method implimented in this code contains a bollean variable that tracks if changes were made.<br>
This is useful in cases of already sorted input, where the complexity will be \(O(\log n)\). <br>

This code helped me understand complexity in edge cases (and how to plan accordingly to have more efficient code)

---

## Selection Sort
A sort method that goes over an array, finds the location of the minimum value and places it at the index of the current iteration (starting at the lowest index and iterating forward).<br>

This method has a complexity of \(O(\log n^2)\). It's potential advantage over the bubble sort is that is uses less swapping actions.<br>

This code helped me compare two different sort methods and their advantages over one another.
