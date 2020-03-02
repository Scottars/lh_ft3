import socket

import struct


msg = '02:00:00:0c:4e:00:00:00:00:00:12:e5:54:ca:1c:9b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:43:ab:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:6a:bb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:91:cb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:b8:db:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:df:eb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:06:fb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:2e:0b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:0:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:55:1b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:7c:2b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:a3:3b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:ca:4b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21'





#
# ip_port = ('192.168.0.3', 32768)
ip_port = ('127.0.0.1', 44233)

BUFSIZE = 1024
udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

import time
msg = '00:00:00:0c:4e:00:00:00:00:00:12:e5:54:ca:1c:9b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:43:ab:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:6a:bb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:91:cb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:b8:db:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:ca:df:eb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:06:fb:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:2e:0b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:0:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:55:1b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:7c:2b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:a3:3b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21:54:cb:ca:4b:05:64:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:04:b5:04:b5:75:c7:4d:b8:00:00:0f:08:f6:c5:00:0e:00:00:01:d2:01:d2:2d:9d:8b:a6:00:00:0f:08:b5:a5:00:0e:00:00:fb:43:fb:43:89:73:16:2d:00:00:0f:08:26:21'

shuzus=msg.split(':')
data=[]
for shuzu in shuzus:
    data.append(int(('0x'+ shuzu),16))
databytes=b''
for i in data:
    databytes =databytes + struct.pack('B',i)
while True:
    time.sleep(0.001)
    print('we are sending ')

    if not msg:
        continue
    udp_server_client.sendto(databytes, ip_port)

    # back_msg, addr = udp_server_client.recvfrom(BUFSIZE)
    # print(back_msg.decode('utf-8'), addr)