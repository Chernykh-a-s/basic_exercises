"""
Пожалуйста,
приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

# 1. Вывести айди пользователя, который написал больше всех сообщений.
def is_user_with_max_messages(messages):
    #  1. Generate a list of unique id of users who have sent messages
    user_id_list_who_sent_messages = []
    for message in messages:
        user_id_list_who_sent_messages.append(message["sent_by"])
    unique_user_id_list_who_sent_messages = list(set(user_id_list_who_sent_messages))

    #  2. Generate a list of dictionaries with users id and sum of messages sent by them
    user_id_sum_of_messages = []
    for user_id in unique_user_id_list_who_sent_messages:
        user_id_sum_of_messages.append({
            "user_id": user_id,
            "sum_of_messages_sent_by": user_id_list_who_sent_messages.count(user_id),
        })

    #  3. Find the maximum number of messages sent
    max_sum_of_messages_sent_by = max(user_id_sum_of_messages, key=lambda x: x['sum_of_messages_sent_by'])[
        'sum_of_messages_sent_by']

    #  4. Making a list of the users id with the maximum number of messages
    users_id_with_max_messages = []
    for user_id in user_id_sum_of_messages:
        if user_id['sum_of_messages_sent_by'] == max_sum_of_messages_sent_by:
            users_id_with_max_messages.append(user_id['user_id'])

    return users_id_with_max_messages


# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def is_user_with_max_reply_messages(messages):
     #  1. Формируем список id сообщений на которые отвечали -> уникальные
     messages_id_that_were_replied = []
     for message in messages:
         if message["reply_for"] != [] and message["reply_for"] is not None:
            messages_id_that_were_replied.append(message["reply_for"])

     unique_messages_id_that_were_replied = set(messages_id_that_were_replied)

     #  2. Формируем список словарей: id сообщения, кол-во сообщений-ответов на это сообщение
     messages_id_that_were_replied_with_sum_of_answers = []
     for message_id in unique_messages_id_that_were_replied:
         messages_id_that_were_replied_with_sum_of_answers.append({
             "message_id": message_id,
             "number_of_answers": messages_id_that_were_replied.count(message_id),
         })
     print(messages_id_that_were_replied_with_sum_of_answers)

     #  3. Выводим id сообщения с максимальным количеством ответов на него
     message_id_with_max_sum_of_answers = max(messages_id_that_were_replied_with_sum_of_answers, key=lambda x: x[
         "number_of_answers"])
     print(f'айди сообщения sum = {message_id_with_max_sum_of_answers}')

     #  4. Кладем в пременную id сообщения с максимальным количеством ответов на него
     message_id_with_max_sum_of_answers_var = message_id_with_max_sum_of_answers['message_id']
     print(f'айди сообщения = {message_id_with_max_sum_of_answers_var}')

     #  5. Формируем словарь из id сообщений и id пользователей-отправителей этих сообщений
     messages_id_and_users_id_sent_by = {}
     for message in messages:
        messages_id_and_users_id_sent_by[message["id"]] = message["sent_by"]
     print(f'Словарь = {messages_id_and_users_id_sent_by}')

     #  6. Выводим id пользователя на сообщения которого больше всего отвечали

     return messages_id_and_users_id_sent_by[message_id_with_max_sum_of_answers_var]

if __name__ == "__main__":
    messages = generate_chat_history()
    print(is_user_with_max_messages(messages))
    print(is_user_with_max_reply_messages(messages))