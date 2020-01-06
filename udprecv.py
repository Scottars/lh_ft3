self.ip_port = ('192.168.0.3', 32768)
#
# self.ip_port = ('127.0.0.1', 44233)
BUFSIZE = 1024
self.udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

self.udp_server_client.bind(self.ip_port)
print('we have bind this ip')

while True:
    if flagthreadstop:
        self.udp_server_client.close()
        break


    else:
        global msg
        msg, addr =self.udp_server_client.recvfrom(BUFSIZE)
        # print("recv", msg, addr)
        # self.trigger.emit()
