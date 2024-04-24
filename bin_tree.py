class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_tree(root, level=0, prefix="Root:"):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left is not None:
            print_tree(root.left, level + 1, 'L-- ')
        if root.right is not None:
            print_tree(root.right, level + 1, 'R-- ')


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        self.graph[node1].append(node2)

    def __str__(self):
        result = ""
        for node in self.graph:
            result += str(node) + " -> " + ", ".join(str(neighbor) for neighbor in self.graph[node]) + "\n"
        return result


if __name__ == '__main__':
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
