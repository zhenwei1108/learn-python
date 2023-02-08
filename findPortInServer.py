import socket
import time


for i in range(8000,65535):
    socket_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try:
    socket_socket.settimeout(0.1)
    ex = socket_socket.connect_ex(("192.168.126.7", i))
    if ex == 0:
        print("ok:" + str(i))
    socket_socket.close()
    # socket_socket.shutdown(1)
# except BaseException as e:
#     print(str(e))
