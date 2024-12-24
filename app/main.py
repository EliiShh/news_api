import os

from app.kafka_publisher.producer import send_data
from app.repository.api_repo import fetch_articles
from app.services.groq_service import get_all_news_obj
import time


if __name__ == "__main__":
    list_before = []
    batch = fetch_articles()
    while True:
        filtered_list = [item for item in batch if item not in list_before]
        events = get_all_news_obj(filtered_list)
        topic_name = os.environ['TOPIC_EMAILS_NAME']
        send_data(topic_name, events)
        time.sleep(120)
        batch = fetch_articles()



