'''二叉树-广度优先遍历'''


class Node(object):  # 创建节点，每个节点有两个子节点
    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None


class Tree(object):  # 创建树
    def __init__(self):
        self.root = None

    def add(self, item):  # 添加元素
        node = Node(item)
        if self.root is None:   # 设置根节点
            self.root = node
            return
        queue = [self.root]
        while queue:  # 只要队列不为空
            cur_node = queue.pop(0)  # 读取当前节点
            if cur_node.left is None:  # 判断当前节点的左子节点是否为空
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:  # 判断当前节点的右子节点是否为空
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breath_travel(self):  # 广度优先遍历
        if self.root is None:
            return
        queue = [self.root]
        while queue:  # 当队列存在时
            cur_node = queue.pop(0)
            print(cur_node.item, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)  # 添加左子元素
            if cur_node.right is not None:
                queue.append(cur_node.right)  # 添加右子元素

    def pre_order(self, node):  # 先序遍历
        if node == None:
            return
        print(node.item, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):  # 中序遍历
        if node == None:
            return
        self.in_order(node.left)
        print(node.item, end=' ')
        self.in_order(node.right)
        return '->'.join(node.item)

    def post_order(self, node):  # 后序遍历
        if node == None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.item, end='—>')


if __name__ == '__main__':
    tree = Tree()
    for i in range(10):
        tree.add(i)
    tree.breath_travel()  # 0 1 2 3 4 5 6 7 8 9
    print('')
    tree.pre_order(tree.root)  # 0 1 3 7 8 4 9 2 5 6
    print('')
    tree.in_order(tree.root)  # 7 3 8 1 9 4 0 5 2 6
    print('')
    tree.post_order(tree.root)  # 7 8 3 9 4 1 5 6 2 9
