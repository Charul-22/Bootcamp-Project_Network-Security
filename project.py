import hashlib

str=input("input: ")
print("\n")

result = hashlib.md5(str.encode())
print("The MD5 hash for "+str+" is: "+result.hexdigest())

result = hashlib.sha256(str.encode())
print("The SHA256 hash for "+str+" is: "+result.hexdigest())

result = hashlib.sha1(str.encode())
print("The SHA1 hash for "+str+" is: "+result.hexdigest())

