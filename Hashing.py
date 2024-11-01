#Hashing_api

import hashlib

class Hashing:
    def __init__(self, user_input_location: str, hash_input : str):
        self.location_of_file = user_input_location  # Indicates where the file is located
        self.hash_input = hash_input.strip()  # Location of the hash file
        self.hash_mode = self.auto_detect_hash_mode(hash_input)  # Automatically detect the hash mode
        self.hash_output = []
        self.hash_dict = \
        {'md5':hashlib.md5,
        'sha1':hashlib.sha1,
        'sha224':hashlib.sha224,
        'sha256_all':[hashlib.sha256,hashlib.sha3_256],
        'sha384_all':[hashlib.sha384,hashlib.sha3_384],
        'sha512_all':[hashlib.sha512,hashlib.sha3_512],
        'No_valid':self.no_valid_len} #This is hash table dictionary
    
    @staticmethod 
    def auto_detect_hash_mode(hash_value): #This is a static method, as it applies to all objects universally and not to each object specifically. 
        """Auto-detect the hash mode based on the length of the hash value."""
        hash_length = len(hash_value)
        if hash_length == 32:
            return 'md5'
        elif hash_length == 40:
            return 'sha1'
        elif hash_length == 56:
            return 'sha224'
        elif hash_length == 64:
            return 'sha256_all'
        elif hash_length == 96:
            return 'sha384_all'
        elif hash_length == 128:
            return 'sha512_all'
        else:
            return "No_valid"
            
    def no_valid_len(self):
      #Raises error if the inputed hash is incorrect
      raise Exception('Incorrect hash value')
      
    def chunk_file(self,hashfunc):
        #It reads file as chunked it will help to reduce the memory consumption for larger files
        for i in hashfunc:
            temp_hash = i()
            with open(self.location_of_file, 'rb') as fi:
              while True:
                chunk = fi.read(4096)
                if not chunk:
                  break
                temp_hash.update(chunk)
              self.hash_output.append(temp_hash)
              
    def compute_hash(self):
        #Computing hashes based on its type
        hashfunc = self.hash_dict.get(self.hash_mode)
        if type([]) == type(hashfunc):
            self.chunk_file(hashfunc)
        else:
            self.chunk_file(list([hashfunc]))
        return self.hash_output

    def check_hash(self,computed_hash):
      #Validating hashes
      for i in computed_hash:
        if i.hexdigest() == self.hash_input:
          return True
      return False
    
    def verify_hash(self):
        #Verify and validate the hash
        computed_hash = self.compute_hash()
        if str(computed_hash) == type(''):
          return computed_hash
        else:
          return self.check_hash(computed_hash)

obj = Hashing('/home/kali/projects/CheckSumr/README.md',
'1'*56) #Use case: first param describe the file location second param describe the hash of file 
print(obj.verify_hash())