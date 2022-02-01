import requests  # allows us to make a request (think of this as a browser)
import hashlib  # Pokedex_png module for hashing!


# Notes on # 2
# url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'  # Hashed Password
# we'll use first 5 letters of hashed password of our original password using SHA1 Hash Generator
# res = requests.get(url)
# print(res)  # <Response [400]> is not good. Usually means something's not right with the API.
# <Response [200]> is OK

# 2
# checking password if it exists in API response
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error Fetching: {res.status_code}, check the api and try again")
    return res


# 3
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())  # wrapping this in a tuple
    # in the loop 'line' will get separated when it encounters a ':'

    for h, count in hashes:  # here h means the tails that matched the first5_char and count is how many times found
        if h == hash_to_check:
            return count
    return 0


# 1 converting the password to sha1 hashed password in hexadecimal with uppercase letters
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(response)  # <response[200]>
    return get_password_leaks_count(response, tail)


# 4
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probably change your password")
        else:
            print(f"{password} was not found. Carry On!")
    return 'done'


# 5
# try to take arguments from a text file
# only run this file if its the main file being run from the command line not if its being imported!
if __name__ == '__main__':
    with open('pass.txt', 'r') as check_pass:
        passes = check_pass.read().split()  # .split() will split the texts when it finds a whitespace
        main(passes)
