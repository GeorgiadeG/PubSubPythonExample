from asyncio import futures
import os
from google.cloud import pubsub_v1

credential_path = './pk-python.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/temp-347914/topics/tempChannel'

data = 'simple text test1'
data = data.encode('utf-8')

future = publisher.publish(topic_path, data)
print(future.result())