import json
from datetime import datetime
import calendar
import random
import time

import boto3
from faker import Faker

my_stream_name = 'playground-analytics-events'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

fake = Faker()

def put_to_stream(payload):
    print(payload)

    put_response = kinesis_client.put_record(
		StreamName=my_stream_name,Data=json.dumps(payload),PartitionKey=event_id)
    print(put_response)

while True:
    event_id = str(random.randint(1, 1000))
    event_timestamp = calendar.timegm(datetime.utcnow().timetuple())

    payload = {
        'lesson_id': fake.numerify(text='########'),
        'lesson_rank': random.randint(1, 3),
        'class_id': fake.numerify(text='######'),
        'class_sku': fake.numerify(text='######'),
        'event_type': 'completed-lession',
        'timestamp': str(event_timestamp),
        'event_id': event_id
    }

    put_to_stream(payload)

    print("wait for 2 secs...")
    time.sleep(2)
