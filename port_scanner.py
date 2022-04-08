import socket
import threading
from queue import Queue
def portscan(port):
    try:
        #it will try to make a connection to every port that you will specify,
        sock  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((Target,port))
        return True # its exist on the target machine
    except:
        return False# its not exist on the target machine.
def fill_queue(port_list): #filling queue
    for port in port_list:
        queue.put(port)#the first port is the first to be scanned, taking list and filling it into a queue
def worker(): #the methods of the threads
    while not queue.empty(): # if there is any port in the queue
        port = queue.get() # getting the next port on the list
        if portscan(port): # if it's open
            print(f"port {port} is open!") # we will print it and add it to open port lists
            open_ports.append(port)

queue = Queue() # defining a queue
open_ports = []
Target = input("insert your target ip address")
user_scan_begin = int(input("[*]Start Port: "))  # begin from port
user_scan_ending = int(input("[*]End Port: "))  # to port
user_thread = input("Number of threads, [S] to skip: ")  # how many threads we want.
if user_thread == "S" or user_thread == "skip":
    user_thread = 10
else:
    user_thread = int(user_thread)
print("     /|\         ")
print("    / | \        ")
print("   /  |  \       ")
print("  /   |   \      ")
print("[+]scanning[+]   ")
print("  \   |   /      ")
print("   \  |  /       ")
print("    \ | /        ")
print("     \|/         \n")
port_list = range(user_scan_begin,user_scan_ending)
fill_queue(port_list)
thread_list = []
for t in range(user_thread):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)
    thread.start()
for thread in thread_list:
    thread.join()
print("open port are:",open_ports)