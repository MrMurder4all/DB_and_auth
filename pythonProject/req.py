import requests

# URL страницы для авторизации
login_url = 'https://auth.mail.ru/login'

# Данные для авторизации
data = {
    'login': 'kozirev.fa@bk.ru',   # Ваш логин
    'password': '23062002Fe',     # Ваш пароль
}

# Заголовки, чтобы имитировать запрос с браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

# Создаем сессию
session = requests.Session()

# Отправляем POST-запрос с данными для авторизации
response = session.post(login_url, data=data, headers=headers)

# Проверка успешности авторизации
if response.ok:
    print("Авторизация успешна!")
else:
    print("Ошибка авторизации.")

#Можно проверить содержимое страницы, чтобы удостовериться
#print(response.text)
