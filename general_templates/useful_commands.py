
# 1. Turns list of chars to string
res = ['a', 'b']
print(''.join(res))

# 2. Sort a dictionary by its value
sorted(num_to_count, key= lambda k: -num_to_count[k])

# 3. The width of binary tree
'''
height = self.getHeight(root)
width = 2 ** height - 1
def getHeight(self, root):
    if not root:
        return 0
    return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
'''

# 4. [[''] * width] * height will gives you inappropriate reference use the bottom one instead
# Correct: [[''] * width for i in range(height)]

