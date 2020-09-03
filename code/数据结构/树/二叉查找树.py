class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, val_list=[]):
        self.root = None
        for val in val_list:
            self.insert(val)

    def insert(self, data):
        pass

    def search(self):
        pass

    def delete(self):
        pass

    def __del(self):
        pass


    def get_min(self):
        pass

    def get_max(self):
        pass




if __name__ == '__main__':
    pass
