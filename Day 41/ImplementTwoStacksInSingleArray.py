class Stack:

	def __init__(self, n):

		self.capacity = n
		self.A = [None] * n
		self.top1 = -1
		self.top2 = n

	# Function to insert a given element into the first stack
	def push1(self, key):

		# check if the list is full
		if self.top1 + 1 == self.top2:
			print("Stack Overflow")
			exit(-1)

		self.top1 = self.top1 + 1
		self.A[self.top1] = key

	# Function to insert a given element into the second stack
	def push2(self, key):

		# check if the list is full
		if self.top1 + 1 == self.top2:
			print("Stack Overflow")
			exit(-1)

		self.top2 = self.top2 - 1
		self.A[self.top2] = key

	# Function to pop an element from the first stack
	def pop1(self):

		# if no elements are left in the list
		if self.top1 < 0:
			print("Stack UnderFlow")
			exit(-1)

		top = self.A[self.top1]
		self.top1 = self.top1 - 1
		return top

	# Function to pop an element from the second stack
	def pop2(self):

		# if no elements are left in the list
		if self.top2 >= self.capacity:
			print("Stack UnderFlow")
			exit(-1)

		top = self.A[self.top2]
		self.top2 = self.top2 + 1
		return top


if __name__ == '__main__':

	first = [10, 50, 2, 6, 12]
	second = [6, 7, 8, 9, 10]

	stack = Stack(len(first) + len(second))

	[stack.push1(i) for i in first]
	[stack.push2(j) for j in second]

	print("Popping element from the first stack  :", stack.pop1())
	print("Popping element from the second stack :", stack.pop2())
