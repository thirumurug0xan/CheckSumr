from Hashing import Hashing
from GUI import *

obj = Hashing('./README.md','1'*64)
print(obj.verify_hash())