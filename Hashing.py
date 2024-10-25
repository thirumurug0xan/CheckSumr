import hashlib

class Hashing:
	def __init__(self,user_input_location:str,user_hash:str,mode:str):
		self.location_of_file = user_input_location #inducates where the file located
		self.hash_mode = mode
		self.hash_value = user_hash
	def sha256(self,loc):
		return #some boolean
	def sha512(self,loc):
		#some hashlib fuction
	def md5(self,loc):
		#some hashlib function
	def sha384(self,loc):
		#some hashlib function
