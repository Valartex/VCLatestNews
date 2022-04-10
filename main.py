import requests
from pprint import pprint
import config


def get_latest_news():
    response = requests.get("https://api.vc.ru/v1.9/timeline/index/recent?count=1")

    if response.status_code != 200:
        raise Exception("Не удалось получить последнюю новость!")

    json_data = response.json()
    latest_news = json_data["result"][0]
    news_title = latest_news["title"]
    news_url = latest_news["url"]
    link = f'<a href="{news_url}">{news_title}</a>'

    return link


def send_message_to_channel(text):
    bot_token = config.bot_token
    channel_id = config.channel_id

    url = "https://api.telegram.org/bot"
    url += bot_token
    method = url + "/sendMessage"

    response = requests.post(method, data={
        "chat_id": channel_id,
        "text": text,
        "parse_mode": "HTML"
        })

    if response.status_code != 200:
        raise Exception("Не удалось отправить новость в канал!")


if __name__ == '__main__':
    latest_news = get_latest_news()
    send_message_to_channel(latest_news)

