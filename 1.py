import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType

# Функция для отправки сообщения в ВКонтакте
def send_message(vk_session, peer_id, message):
    vk_session.method('messages.send', {'peer_id': peer_id, 'message': message, 'random_id': 0})

# Ваш токен доступа ВКонтакте
token = 'My_token'

# Инициализация сессии ВКонтакте
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

# Получение Long Poll сервера
longpoll = VkLongPoll(vk_session)

# Основной цикл обработки событий
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Получаем текст сообщения
        message_text = event.text.lower()

        # Проверяем, содержится ли ключевое слово в сообщении
        keywords = ['нужна', 'нужны', 'девочка', 'девушки', 'девушка', 'девочки', 'привет', 'hi']
        if any(keyword in message_text for keyword in keywords):
            send_message(vk_session, event.peer_id, '+')
            time.sleep(10)  # Задержка в 30 секунд после отправки сообщения
