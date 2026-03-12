import socket

def start_server(handle_command):

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:

        client, addr = s.accept()
        request = client.recv(1024).decode()

        if "move/?cmd=" in request:
            cmd = request.split("move/?cmd=")[1].split(" ")[0]
            print("Received command:", cmd)
            handle_command(cmd)

        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.close()
