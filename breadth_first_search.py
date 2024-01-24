class Node:
    def __init__(self,key:str):
        self.key = key
        self.children = []


def create_tree():
    root = Node("5")
    child_1 = Node("3")
    child_2 = Node("7")
    root.children.append(child_1)
    root.children.append(child_2)
    child3 = Node("2")
    child4 = Node("4")
    child_1.children.append(child3)
    child_1.children.append(child4)
    child5 = Node("8")
    child_2.children.append(child5)
    child4.children.append(child5)

    return root


def breadth_first_traversal(root:Node):
    queue = [root]
    visited = [root.key]
    while queue:
        node = queue.pop(0)
        print(node.key)
        for child in node.children:
            if child.key not in visited:
                queue.append(child)
                visited.append(child.key)



def main():

    root = create_tree()
    """
    result for breadth first search traversal should be ---> 5 3 7 2 4 8
    """
    breadth_first_traversal(root)


main()