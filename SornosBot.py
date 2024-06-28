import requests

TOKEN = 'ТОКЕН БОТА'
CHAT_ID = 'ID чата'

message = "ПеКарня включилась."

def send_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

if __name__ == "__main__":
    response = send_message(TOKEN, CHAT_ID, message)
    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print("Ошибка при отправке сообщения")
