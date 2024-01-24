class Node:
    def __init__(self,key):
        self.key = key
        self.children = {}
        self.distance = float('infinity')


def dijiskira(root:Node):
    root.distance = 0
    queue = [root]
    while queue:
        current_node = queue.pop(0)
        for child in current_node.children:
            new_distance = current_node.distance + current_node.children[child]
            if new_distance < child.distance:
                child.distance = new_distance
                queue.append(child)


def main():
    root = Node('a')
    child_1 = Node('b')
    child_2 = Node('c')
    root.children[child_1] = 6
    root.children[child_2] = 3
    # child_3 = Node('c')
    child_4 = Node('d')
    child_5 = Node('e')
    child_1.children[child_2] = 1
    child_1.children[child_4] = 2
    child_2.children[child_1] = 4
    child_2.children[child_4] = 8
    child_2.children[child_5] = 2
    child_4.children[child_5] = 9
    child_5.children[child_4] = 7

    dijiskira(root)
    print(child_1.distance)
    print(child_2.distance)
    print(child_4.distance)
    print(child_5.distance)




main()