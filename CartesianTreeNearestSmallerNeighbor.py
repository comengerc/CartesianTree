
# Advanced Data Structures Project #1

# Osman Mantıcı 

def read_file(file_name):
    return list(  # put it into an array
        map(int,  # casting string to int
            open(file_name, 'r').read().replace(',', '').split())  # read input file as splitted by spaces
    )


def findMinIndex(inorder, firstIndex, lastIndex):
    minIndex = firstIndex  # default min value is firstIndex, if there is no minimum value, min is first item
    for i in range(firstIndex + 1, lastIndex + 1):  # search rest of array
        if inorder[minIndex] > inorder[i]:
            minIndex = i
    return minIndex


class CartesianNode:  # node class
    def __init__(self, value, index, inherited=None, leftChild=None, rightChild=None):  # constructor function
        self.value = value
        self.leftChild = leftChild  # default null
        self.rightChild = rightChild  # default null
        self.index = index  # 1-a,index value is assigned when node created, its obvious, no necessary to calculate later
        self.inherited = inherited  # 1-b default null


def inorderTraversal(root, list):  # left-root-right
    if root is None:
        return

    inorderTraversal(root.leftChild, list)
    if root.inherited is None:  # "inherited"  keeps value that its nearest smaller index
        print("-", end=', ')
    else:
        print(list[root.inherited], end=', ')
    inorderTraversal(root.rightChild, list)


def inheritedTraversalLeftNearest(root):
    if root is None:
        return

    if root.rightChild is not None:  # index value of root is equal to inherited value of right child of root
        root.rightChild.inherited = root.index
        inheritedTraversalLeftNearest(root.rightChild)
    if root.leftChild is not None:  # inherited value of root is equal to inherited value of left child of root
        root.leftChild.inherited = root.inherited
        inheritedTraversalLeftNearest(root.leftChild)


def inheritedTraversalRightNearest(root):
    if root is None:
        return

    if root.rightChild is not None:  # inherited value of root is equal to inherited value of right child of root
        root.rightChild.inherited = root.inherited
        inheritedTraversalRightNearest(root.rightChild)
    if root.leftChild is not None:  # index value of root is equal to inherited value of left child of root
        root.leftChild.inherited = root.index
        inheritedTraversalRightNearest(root.leftChild)


def constructTree(inorder, firstIndex, lastIndex):  # first parameter list always same, not divided any time
    if lastIndex < firstIndex:
        return None

    index = findMinIndex(inorder, firstIndex, lastIndex)  # index of smallest value, smallest will be root soon

    root = CartesianNode(inorder[index], index)  # min heap property, its root

    root.rightChild = constructTree(inorder, index + 1, lastIndex)  # right subtree of current root, it is also a root
    root.leftChild = constructTree(inorder, firstIndex, index - 1)  # left subtree of current root, it is also a root

    return root


def main():
    input_inorder = read_file('ads_input.txt')  # reading input file in to an array
    root = constructTree(input_inorder, 0, len(input_inorder) - 1)  # constructing tree
    # by giving that list with first last indexes

    inheritedTraversalLeftNearest(root)  # starting from the root inherit values assigned to each node
    print("Nearest left smaller values: ", end='')
    inorderTraversal(root, input_inorder)  # print in-order

    print()
    inheritedTraversalRightNearest(root)  # starting from the root inherit values assigned to each node
    print("Nearest right smaller values: ", end='')
    inorderTraversal(root, input_inorder)  # print in-order


main()
