import hashlib

class Hashing:
	def __init__(self,user_input_location:str,mode:str):
		self.location_of_file = user_input_location
		self.hash_mode = mode
