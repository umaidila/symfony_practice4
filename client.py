import requests
import json
import re


class Client:

    def __init__(self):
        self.url = 'http://91.203.192.213'
        self.token = "none"

    def register(self, username, password):
        creds = {"username": username, "password": password}
        r = requests.post(f'{self.url}/register', data=creds)
        jsonData = json.loads(r.text)
        if jsonData["status"] != 200:
            return {'Error': jsonData['errors']}
        else:
            return {'Success': f'User {username}  was successfully created'}

    def setToken(self, username, password):
        creds = {"username": username, "password": password}
        r = requests.post(f'{self.url}/api/login_check', json=creds)
        jsonData = json.loads(r.text)
        if r.status_code != 200:
            return {'Error': jsonData["message"]}
        else:
            self.token = jsonData["token"]
            return {'Success': 'Token was successfully set'}

    def getTodos(self):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/todo', headers={'Authorization': f'Bearer {self.token}'})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        jsonData = json.loads(r.text)
        return jsonData

    def getTodo(self, id):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/todo/{id}', headers={'Authorization': f'Bearer {self.token}'})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        jsonData = json.loads(r.text)
        if r.status_code == 404:
            return {'Error': jsonData['errors']}
        return jsonData

    def addTodo(self, name):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.post(f'{self.url}/api/todo', headers={'Authorization': f'Bearer {self.token}'},
                          json={'name': name})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        else:
            return {'Success': 'Post added successfully'}

    def addFile(self, filename):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        myfile = {'file': open(filename, 'rb')}
        r = requests.post(f'{self.url}/api/file', headers={'Authorization': f'Bearer {self.token}'},
                          files=myfile)
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        if r.status_code != 200:
            return {'Error': 'Upload error'}
        else:
            return {'Success': 'File was successfully uploaded'}

    def getFiles(self):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/file', headers={'Authorization': f'Bearer {self.token}'})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        jsonData = json.loads(r.text)
        return jsonData

    def getFile(self, id):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.get(f'{self.url}/api/file/{id}', headers={'Authorization': f'Bearer {self.token}'})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        d = r.headers['content-disposition']
        fname = re.findall("filename=(.+)", d)[0]
        open(fname, 'wb').write(r.content)
        return f'file {fname} was downloaded'

    def delFile(self, id):
        if self.token == "none":
            return {'Error': 'You need to set token first'}
        r = requests.delete(f'{self.url}/api/file/{id}', headers={'Authorization': f'Bearer {self.token}'})
        if r.status_code == 401:
            return {'Error': 'Invalid JWT token'}
        if r.status_code == 404:
            return {'Error': 'File not found'}
        else:
            return {'Success': 'File deleted successfully'}
