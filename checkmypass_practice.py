# import modules
import hashlib
import requests


# pass password to a function to convert into sha1password + hexadecimal + uppercase
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # split them in first5_char and a tail
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return password_leaked_or_not(response, tail)


# pass the first5_char to a response api function to get a response of 200 then return the response
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        print(f"Error Fetching {res.status_code}. Check the api and try again")
    else:
        return res


# then pass the response and the tail to a function to know if passwords leaked or not
def password_leaked_or_not(hashes, hash_to_check):
# wrap the response in a tuple, assign it to a variable, do a for loop and split the sentences when it encounters a ':'
    all_hash = (line.split(':') for line in hashes.text.splitlines())

# do another for loop to see if the tail matches any of the tuple variable, if not return 0 or else return the count
    for h, count in all_hash:
        if h == hash_to_check:
            return count
    return 0


# return the response to a main function which takes passwords as parameters.
def main(args):
    # do a for loop to loop through the passwords by passing them in pwned_api_check function which returns the count
    for password in args:
        count = pwned_api_check(password)
        # Do a if else statement to print if a password is usable or not
        if count:
            print(f"{password} was found {count} times... you should probably change your password")
        else:
            print(f"{password} was not found. Carry On!")
    return 'done'


# under __name__ == '__main__' open a text file to read the passwords within and pass it to the main function as a var
if __name__ == '__main__':
    with open(r"C:\Users\User\PycharmProjects\Scripting With Python\email playground\password playground\pass.txt",
              'r') as check_pass:
        passes = check_pass.read().split()
        main(passes)
