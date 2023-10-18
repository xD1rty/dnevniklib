---
description: Как создать, как получить данные?
---

# Работа с классом Student

Самый главный класс в библиотеке - класс Student

Он отвечает за данные юзера (ученика)

Для импорта этого класса и его инициализации надо ввести

```python
from dnevniklib.student import Student

student = Student(token="")
```

К сожалению, функцию получения токена мы напишем позже, надо подождать

Пока наш класс Student возвращает

```
first_name - имя
middle_name - отчество
last_name - фамилия
birthdate - дата рождения
email - эл. почта
person_id - id персоны (нужен для получения дз)
school_id - id школы
age - возраст
sex - пол ("male", "female")
login - логин ученика
class_name - имя класса
```
