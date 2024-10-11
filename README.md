# enjoypro - тестовое задание

## Требования для запуска

- **Docker**
- **Docker Compose**

## Запуск приложения

```bash
git clone https://github.com/2rage/test_asignment_enjoypro
cd test_asignment_enjoypro
docker-compose up --build
```

Теперь приложение доступно по адресу http://localhost:8000

## Доступные страницы приложения

- Страница авторизации: **/login/**
- Список вопросов для пользователей: **/quiz/questions/**
- Страница вопроса с ответами: **/quiz/questions/<int:pk>/**
- Админка: **/admin-panel/**
- Создание пользователя (для администраторов): **/admin/create_user/**
- Редактирование вопросов и ответов: **/admin/edit_question/<int:pk>/**
- Статистика пользователей: **/admin/statistics/**


## Для тестирования

### Параметры для админского аккаунта: 

**enjoypro** – логин

**enjoy271828** – пароль


### Параметры для обычного аккаунта:

**enjoyuser** – логин

**enjoy271828** – пароль


## Примеры работы приложения

<img src="/misc/images/image.png" width="650">
<img src="/misc/images/image2.png" width="650">
<img src="/misc/images/image3.png" width="650">
<img src="/misc/images/image4.png" width="650">
<img src="/misc/images/image5.png" width="650">
<img src="/misc/images/image6.png" width="650">
<img src="/misc/images/image7.png" width="650">