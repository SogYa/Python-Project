import socket
import threading
import time

key = 8194  # ключь для шифровки данных

shutdown = False
join = False


def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)

                # получение сообщений от  других пользователей, расшифровка сообщения от других пользователей
                decrypt = ""
                k = False
                for i in data.decode("utf-8"):
                    if i == ":":
                        k = True
                        decrypt += i
                    elif k == False or i == " ":
                        decrypt += i
                    else:
                        decrypt += chr(ord(i) ^ key)
                print(decrypt)

                time.sleep(0.2)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())  # ip локальной сети
port = 0  # т.к клиент подключается к сети, а не создает ее

server = ("192.168.220.1", 90)# переменная меняется в зависимости от ip сервера

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # TCP/IP
s.bind((host, port))
s.setblocking(0)

alias = input("Name: ")

rT = threading.Thread(target=receving, args=("RecvThread", s))  # многопоточность которая обробатывается TCP/IP
rT.start()

while not shutdown:

    # отправка сообщения на сервер,когда пользователь пресоеденился к чату

    if not join:
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
        join = True
    else:

        # если пользователь пресоеденился к чату, то он отправляет сообщения

        try:
            message = input("Enter -> ")

            # шифровка сообщения
            crypt = ""
            for i in message:
                crypt += chr(ord(i) ^ key)
            message = crypt

            # если отпровляеться пустое сообщение, то на сервер ничего не приходит

            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)

            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

rT.join()
s.close()
