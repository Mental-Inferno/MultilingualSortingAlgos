# A quick lesson on how the algorithms work

## MergeSort
- MergeSort is recursive, meaning it calls itself
- It is a divide-and-conquer algorithm
- It is a very efficient algorithm for large data sets

#### Big O Analysis
- Merge Sort does log n merge steps as each merge step doubles the list size
- It does n work for each merge step as it looks at every item
- It runs in **O(n logn)**

## QuickSort
- QuickSort is recursive
- It is a divide-and-conquer algorithm
- It is a very efficient algorithm for large data sets

#### Big O Analysis
- Worst case is **O(n^2)**
- Average case is **O(n logn)**
- Performance largely depends on the pivot selection