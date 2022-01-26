from client import Client

if __name__ == '__main__':
    client = Client()

    print(client.setToken("semen", "password"))
    print(client.getFiles())

    print(client.addFile('main.html'))

    print(client.getFile(12))
    # print(client.delFile(12))

