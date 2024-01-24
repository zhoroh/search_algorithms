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


def depth_first_search_traversal(node:Node,visited:set):
    if node.key not in visited:
        print(node.key)
        visited.add(node.key)
        for child in node.children:
            depth_first_search_traversal(child,visited)
    



def main():
    root = create_tree()
    visited = set()
    """
    result for breadth first search traversal should be ---> 5 3 2 4 8 7
    """
    depth_first_search_traversal(root,visited)

main()