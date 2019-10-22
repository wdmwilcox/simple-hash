import hashlib
from random import randint

def get__user_input():
    _input = input("Enter a string \n")
    return _input

def hash_input(_input):
    _input = _input.encode()
    _hash = hashlib.sha256()
    _hash.update(_input)
    _hash = _hash.hexdigest()
    return _hash

def check_valid_hash(hash_input):
    nonce = 0
    checksum = ""
    counter = 0
    while checksum[:4] != "0000":
        nonce = randint(1,1000000)
        combined = str(hash_input) + str(nonce)
        _combined = combined.encode()
        _hash = hashlib.sha256()
        _hash.update(_combined)
        checksum = _hash.hexdigest()
        counter += 1
    return nonce, counter

def main():
    _input = get__user_input()
    _hash = hash_input(_input)
    nonce, counter = check_valid_hash(_hash)
    print(f"Valid nonce is {nonce}")
    print(f"Found in {counter} tries")

if __name__ == "__main__":
    main()
        
