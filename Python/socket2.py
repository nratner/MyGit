import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('linn.inspectiondates.com/', 80))
mysock.send('GET http://linn.inspectiondates.com/index.php?option=com_content&view=article&id=1139&Itemid=547 HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()