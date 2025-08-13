"""
Range Queries
implement a class for range queries
This class will handle range queries on an array, allowing for efficient updates and queries.
It supports:
- Point updates: Update a single element in the array.
- Range queries: Query the sum of elements in a specified range.
- Lazy propagation: Efficiently handle updates and queries on ranges.
The class uses a segment tree with lazy propagation to achieve efficient updates and queries.
The segment tree is built from the input array, and it allows for both point updates and range queries.
The lazy propagation technique is used to delay updates to segments of the tree until necessary, improving
performance for multiple updates and queries.
"""
# def min
# def max

# binary indexed trees