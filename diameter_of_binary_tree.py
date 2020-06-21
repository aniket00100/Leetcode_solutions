class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

    def print_inorder(self, root, node_list):
        if not root:
            return
        self.print_inorder(root.left, node_list)
        node_list.append(root)
        self.print_inorder(root.right, node_list)
        return node_list


class Solution:

    def diameter_of_binary_tree(self, root):
        return self.over_each_node(root, [])

    def over_each_node(self, root, node_list):
        if not root:
            return
        self.over_each_node(root.left, node_list)
        node_list.append(root)
        self.over_each_node(root.right, node_list)

        max_diameter = self.calculate_diameter(node_list[0])
        for i in range(1, len(node_list)):
            diameter = self.calculate_diameter(node_list[i])
            if diameter > max_diameter:
                max_diameter = diameter
        return max_diameter

    def calculate_diameter(self, root):
        left = right = 0
        if root.left:
            left = self.depth_of_sub_tree(root.left)
        if root.right:
            right = self.depth_of_sub_tree(root.right)
        return left + right

    def depth_of_sub_tree(self, node, depth = 0):
        if node == None:
            return depth
        return max(self.depth_of_sub_tree(node.left, depth + 1), self.depth_of_sub_tree(node.right, depth + 1))




root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(8)
root.left.right.left.left = TreeNode(9)
root.left.right.left.right = TreeNode(10)
root.left.right.left.right.left = TreeNode(11)
root.right = TreeNode(3)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.left.right.left = TreeNode(14)
root.right.left.right.right = TreeNode(15)
root.right.left.right.right.right = TreeNode(17)
root.right.left.right.right.left = TreeNode(16)
root.right.left.right.right.left.left = TreeNode(18)

# print(root.print_inorder(root, []))

ans = Solution()
print(ans.diameter_of_binary_tree(root))