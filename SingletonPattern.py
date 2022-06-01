"""
Making a class singleton in Python
"""

class TransactionProcess:

	__instance = None

	# This method is used to get an instance of the class
	@staticmethod
	def getInstance():

		if TransactionProcess.__instance == None:
			raise Exception("please create the object with the constructor first!")

		return TransactionProcess.__instance


	def __init__(self,type):

		if TransactionProcess.__instance != None:
			raise Exception("Object already exists! Use getInstance method!")

		self.type = type

		TransactionProcess.__instance = self


UPI = TransactionProcess("UPI")
obj = TransactionProcess.getInstance()
print(obj.type)
