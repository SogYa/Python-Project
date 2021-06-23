import socket
import sys
import time
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import time

import serverQt
import clientQt
from serverQt import *

str_ = ''


class ExampleApp(QMainWindow, serverQt.Ui_Server):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def ref(self):
        self.close()

    def print(self, str):
        self.textBrowser.append(str)


def main():
    app = QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp

    host = socket.gethostbyname(socket.gethostname())  # содержиит в себе ip на котором поднят сервер
    port = 90  # порт на которм сейчас ничего не запущено

    clients = []  # список клиентов подключенных к серверу

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # содержит в себе сокеты, TCP/IP. Протокол TCP/IP
    s.bind((host, port))  # создание хоста и порта

    quit = False  # для того чтоб цикл прекратился
    window.print("Server start\n" + "Start at ip: " + host)
    window.show()  # Показываем окно
    app.exec_()

    while not quit:
        try:

            data, addr = s.recvfrom(1024)  # 1024байт - сервер может приинять.
            # data - сообщение, которое отпровляет пользователь. addr - личный адрес пользователя

            if addr not in clients:  # если адрес не находится в списке, то его добовляют в список
                clients.append(addr)  #

            ItsaTime = time.strftime("%Y-%m-%d %H:%M", time.localtime())  # для отслеживания

            print("[" + addr[0] + "] = [" + str(addr[1]) + "] = [" + ItsaTime + "]" + "\nLogin:",
                                      end="")  # пишет информацию
            print(data.decode('utf-8'))  # декодируем сообщение, отправленное клиентом
            # app.print(data.decode('utf-8'))

            for client in clients:
                if addr != client:  # проверка на  дублирование сообщения у отправителя
                    s.sendto(data, client)  # отправка сообщений
                    window.textBrowser.reload()
        except:

            print("\n Server stopped")
            quit = True
            window.close()

    s.close()


if __name__ == '__main__':
    main()
