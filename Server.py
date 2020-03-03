import socket
import  sys


def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 8090
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error : " + str(msg))


def socket_bind():
    try:
        global host
        global port
        global s
        print("binding to port : "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error : " + str(msg))
        socket_bind()


def socket_accecept():
    conn, adress=s.accept()
    print("connection deails : ip :" + adress[0] + ": port :" + str(adress[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accecept()


main()
