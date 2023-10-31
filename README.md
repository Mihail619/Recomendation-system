# Рекомендательная система.
Проект представляет собой рекомендадтельную систему основанную на истории взаимодействия пользователей со статьями.

В ходе проекта для всех статей из базы данных определяется верояность того, что пользователь лайкнет их. 
Из всех статей выбирается N заданное количествой, которые будут рекомендованы пользователю.
Матетематическая частьвыполнена при помощи python (scikitlearn, catboost, roberta-base). Демо версия Backend страницы сделана при помощи фреймворка Fast API.

Это первая версия системы.

## Запуск приложения
Для запуска приложения необходимо:
1. Скопировать репозиторий к себе на пк в <своя дирректория>.
2. В терминале установить текущую дирректорию как <своя дирректория>\Recomendation-system\scr
3. В терминале выполнить команду python main.py
После запуска убедиться что напечатаны сообщения: "Модель загружена!" и 
4. В браузере ввести URL http://127.0.0.1:8000/?id=<USER_id>&limit=<limit>, 
где USER_id - id юзера, для которого необходимо вывести список рекомендаций,
limit - количество рекомендаций.
