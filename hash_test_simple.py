import hashlib

_input = input("Provide a string: >")
e_input = _input.encode()
_hash = hashlib.sha256()
_hash.update(e_input)
print(_hash.hexdigest())

