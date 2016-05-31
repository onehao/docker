


from flask import Flask
from redis import Redis
import pymongo

app = Flask(__name__)
#redis = Redis(host='mongo', port=6379)
conn = pymongo.MongoClient("mongo",27017)
db = conn.test
welinfo = db.welinfo
#u = dict(name="welinfo",message=0)
db.welinfo.insert({"welinfo":0})

@app.route('/')
def hello():
    #redis.incr('hits')
    user = db.welinfo.find_one()#{"name","welinfo"})
    print(user)
    user['welinfo'] +=1
    db.welinfo.save(user)
    return 'Hello Mihcael! I have been seen %s times.' % user['welinfo']#redis.get('hits')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
