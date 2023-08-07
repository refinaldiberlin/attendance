# import uuid
# import psutil
# from datetime import datetime

# # datetime object containing current date and time
# now = datetime.now()
 
# # dd/mm/YY H:M:S
# timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

# def get_mac_address():
#     try:
#         # Get a list of all network interfaces on the system
#         interfaces = psutil.net_if_addrs()

#         for interface_name, interface_addresses in interfaces.items():
#             for address in interface_addresses:
#                 # Check if the address family is MAC address
#                 if address.family == psutil.AF_LINK:
#                     return address.address
#     except Exception as e:
#         print("Error:", e)

#     return None

# if __name__ == "__main__":
#     mac_address = get_mac_address()
#     if mac_address:
#         print("MAC Address:", mac_address)
#         print("Accessed at:", timestamp)
#     else:
#         print("MAC Address not found.")

# import subprocess

# wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
# data = wifi.decode('utf-8')
# print(data)
# if "school_wifi_name" in data:
#     print("connected to speccific wifi")
# else:
#     print("not connected")
# 8c:dc:02:9b:cf:9a
# c6:7d:16:15:86:f6


from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def g(num):
    for i in range(num):
        print(1)
 
def f(num):
    for i in range(num):
        print(2)

# if __name__ == '__main__':
#     info('main line')
p1 = Process(target=g, args=(10,)) 
p2 = Process(target=f, args=(10,))

p1.start()
p2.start()

p1.join()
p2.join()

# import threading
 
 
# def print_cube(num):
#     for i in range(num):
#         print(1)
 
# def print_square(num):
#     for i in range(num):
#         print(2)
 
 
# if __name__ =="__main__":
#     # creating thread
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
 
#     # starting thread 1
#     t1.start()
#     # starting thread 2
#     t2.start()
 
#     # wait until thread 1 is completely executed
#     t1.join()
#     # wait until thread 2 is completely executed
#     t2.join()
 
#     # both threads completely executed
#     print("Done!")
    