"""
Diamond problem in multiple inheritance
"""


class A:
	def test(self):
		print("function inside class A")


class B(A):
	pass
	def test(self):
		print("function inside clas B")


class C(A):
	def test(self):
		print("function inside clas C")


class D(B, C):
	pass


objD = D()
objD.test()  # TODO: It will first check class B, then class C and finally will check the class A
