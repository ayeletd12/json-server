class BasePost:
    def __init__(self, uID, cid, ctitle, cbody):
        self.userId = uID
        self.id = cid
        self.title = ctitle
        self.body = cbody


url = "https://jsonplaceholder.typicode.com/posts"
import requests
import json

r = requests.get(url)

result = json.loads(r.text)

postDict = {}

for res in result:
    newBP = BasePost(res['userId'], res['id'], res['title'], res['body'])
    postDict[res['id']] = newBP

print(postDict)