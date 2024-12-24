from dotenv import load_dotenv

load_dotenv(verbose=True)


import os
import json
from kafka import KafkaProducer

def send_data(topic:str, data:list):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    try:
        producer.send(topic, value=data)
        producer.flush()
        print('Data sent successfully')
    except Exception as e:
        print(f'Error sending data: {e}')
    finally:
        producer.close()

