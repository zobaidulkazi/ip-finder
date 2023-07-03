import socket

print('''
\033[1m _____       ______ _           _           \033[0m
\033[1m|_   _|      |  ___(_)         | |          \033[0m
\033[1m  | | _ __   | |_   _ _ __   __| | ___ _ __ \033[0m
\033[1m  | || '_ \  |  _| | | '_ \ / _` |/ _ \ '__|\033[0m
\033[1m _| || |_) | | |   | | | | | (_| |  __/ |   \033[0m
\033[1m \___/ .__/  \_|   |_|_| |_|\__,_|\___|_|   \033[0m
\033[1m     | |                                    \033[0m
\033[1m     |_|                                    \033[0m

\033[1;33m    @@@@@@@ Tool Name ::IP Finder  @@@@@@@\033[0m
\033[0;36m        Why This tool :: IP Finder is a simple command-line tool written in\033[0m
\033[0;36m        Python/JavaScript that allows you to retrieve your \033[0m
\033[0;36m        private and public IP addresses.\033[0m
\033[0;36m        Contact with Me : \033[4;34m[GitHub](https://github.com/zobaidulkazi)\033[0m
\033[0;31m    @@@ Don't try to copy this project. \033[0m
\033[0;31m    All rights reserved by @zobaidulkazi.\033[0m

\033[1m1. Private IP\033[0m
\033[1m2. Public IP\033[0m
\033[1m3. Exit\033[0m
''')


# # fast function is hear get_private_ip()
# def get_private_ip():
#     hostname = socket.gethostname()
#     ip = socket.gethostbyname(hostname)
#     return ip
# # 2nd function is grt_public_ip
# def get_public_ip():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.connect(("8.8.8.8", 80))
#     ip = sock.getsockname()[0]
#     sock.close()
#     return ip

# print("My IP Finder")

# while True:
#     print("\n1. My Private IP")
#     print("2. My Public IP")
#     print("3. Exit")

#     choice = input("Enter Your Choice Number: ")

#     if choice == "1":
#         private_ip = get_private_ip()
#         print("Your private IP is:", private_ip)

#     elif choice == "2":
#         public_ip = get_public_ip()
#         print("Your public IP is:", public_ip)

#     elif choice == "3":
#         print("Exiting the program...")
#         break

#     else:
#         print("Invalid choice. Please try again.zk")




import socket

# Function to get the private IP
def get_private_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

# Function to get the public IP
def get_public_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("8.8.8.8", 80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip

# Styling variables
HEADER = '\033[95m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

# color variables

GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'

print(f"{HEADER}{BOLD}My IP Finder{END}")

while True:
    print("\n1. My Private IP")
    print("2. My Public IP")
    print("3. Exit")
    print("..............................")

    choice = input(f"{HEADER} {YELLOW}Enter Your Choice Number: {END} ")

    if choice == "1":
        private_ip = get_private_ip()
        print(f"\n{BOLD} {GREEN} Your private IP is:{END}", private_ip)

    elif choice == "2":
        public_ip = get_public_ip()
        print(f"\n{BOLD}{GREEN}Your public IP is:{END}", public_ip)

    elif choice == "3":
        print(f"\n{BOLD} {RED}Exiting the program...{END}")
        break

    else:
        print(f"\n{BOLD} {RED}Invalid choice. Please try again.{END}")
