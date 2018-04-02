# encoding = utf-8
from queue import Queue

class TreeNode():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class BinaryTree():
	def __init__(self, root=None):
		self.root = root


	def breathSearch(self):
		if (self.root == None):
			return None
		
		queue = Queue()
		# 首先把根节点放到队列
		queue.put(self.root)

		# 队列不为空， 遍历左右节点
		while queue.empty is not True:
			node = queue.get()
			print(str(node.val))
			if (node.left != None):
				queue.put(node.left)
			if (node.right != None):
				queue.put(node.right)


if  __name__ == '__main__':
	rootNode = TreeNode(50)
	rootNode.left = TreeNode(20, TreeNode(30), TreeNode(40))
	rootNode.right = TreeNode(60, right=TreeNode(70))

	tree = BinaryTree(rootNode)
	tree.breathSearch()
