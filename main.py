from node import Node, LinkedList
from custom_array import Array
from stack import Queue, Stack
from bin_tree import Graph, TreeNode, print_tree
from sorts import bubble_sort, merge_sort

if __name__ == '__main__':
    arr = Array(5)
    arr[0] = 10
    arr[1] = 25
    arr[2] = 30
    arr[3] = 80
    arr[4] = 50
    print("Array:", arr)

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print("Stack:", stack)

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue:", queue)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Binary Tree:")
    print_tree(root)


    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    print("Graph:")
    print(graph)

    print("Bubble Sort")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    sorted_arr = bubble_sort(arr.copy())
    print("Sorted Array:", sorted_arr, "\n")

    print("Merge Sort")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original Array:", arr)
    merge_sort(arr)
    print("Sorted Array", arr, "\n")
