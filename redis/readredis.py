import redis
import time
import datetime
import json

redisConnection = None


REDIS_HOST='100.98.26.42'
REDIS_PORT=6379
REDIS_DB=0

def startRedisConnection():
    redisConnection = redis.StrictRedis()

def pushMessage(session,message,channel='channel_console'):
    redisConnection = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)

    time.sleep(1)

    comment_json = {
        'message': message,
        'submit_date': str(datetime.datetime.now()),
        'session_id':session}

    redisConnection.publish(channel,json.dumps(comment_json))


def readMessage():
    redisConnection = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB)

    time.sleep(1)

    pubsub = redisConnection.pubsub()
    pubsub.subscribe('channel_console')


    #print 'Listening to {channel}'.format(**locals())
    for item in pubsub.listen():
	print item
    

   




if __name__ == '__main__':
	
	readMessage()	

