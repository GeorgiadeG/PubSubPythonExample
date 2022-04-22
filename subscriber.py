from asyncio import futures
import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credential_path = './pk-python.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

timeout = 5.0

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/temp-347914/subscriptions/tempChannel-sub'

def callback(message):
    print('Received message: {}'.format(message))
    print('Message data: {}'.format(message.data))
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print('Listening for messages on {}..\n'.format(subscription_path))

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()