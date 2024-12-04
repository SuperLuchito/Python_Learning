import hashlib

example_1 = 121
example_2 = 1234


def isPalindrome(num):
    
    num_str = str(num)
    hash_object = hashlib.sha256(num_str.encode())
    hash_value = hash_object.hexdigest()
    
    new_num_str = ''
    
    for item in num_str[::-1]:
        new_num_str += item
    
    new_hash_object = hashlib.sha256(new_num_str.encode())
    new_hash_value = new_hash_object.hexdigest()
    
    if hash_value == new_hash_value:
        return True
    else:
        return False


print(isPalindrome(example_1))