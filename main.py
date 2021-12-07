
from client import Client

if __name__ == '__main__':

    ip = 'http://45.143.139.222'

    client = Client(ip)

    client.setToken("semen", "mypassowrd")
    print(client.addTodo("new todo for semen"))
    print(client.getTodos())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
