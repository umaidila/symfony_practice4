
from client import Client

if __name__ == '__main__':

    client = Client()

    print(client.setToken("semen", "password"))
    print(client.getFiles())
    print(client.delFile(4))
    print(client.getFiles())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
