import hashlib

def get_user_input():
    _input = input("Provide a string: >")
    return _input

def encode_input(_input):
    e_input = _input.encode()
    return e_input

def generate_hash(e_input):
    _hash = hashlib.sha256()
    _hash.update(e_input)
    return _hash

def print_hash(_hash):
    print(_hash.hexdigest())

def main():
    _input = get_user_input()
    e_input = encode_input(_input)
    _hash = generate_hash(e_input)
    print_hash(_hash)

if __name__ == "__main__":
    main()