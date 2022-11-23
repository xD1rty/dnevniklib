# Библиотека для автоматизированного сбора информации из Дневника МЭШ ```dnevniklib 0.2```

 На данном этапе вход в Дневник через библиотеку доступен !!!ТОЛЬКО!!! по токену аунтефикации, что в последующих версиях пофиксится

### Код для получения имени профиля
```python 
import dnevniklib
user = dnevniklib.User(token="<TOKEN>")
print(user.first_name)
```

### Код для получения оценок
```python
import dnevniklib
user = dnevniklib.User(token="<TOKEN>")
marks = dnevniklib.Marks(user.session, user.token, user.id)
print(marks.get_marks_by_data("2022-11-16"))
```
# P.S: дату во всех примерах вводим форматом ```%Y-%m-%d```

### Код для получения Д/З 
```python
import dnevniklib
user = dnevniklib.User(token="<TOKEN>")
homeworks = dnevniklib.Homeworks(user.session, user.token, user.id)
print(homeworks.get_homeworks_by_data("2022-11-16"))
```

### Код для получения данных школы
```python
import dnevniklib
user = dnevniklib.User(token="<TOKEN>")
school_ = dnevniklib.School(user.session, user.token)
print(school_.get_info_about_school())
```

# Как получить токен ?
<html>
<img src="./screenshots/1.png" alt="drawing" width="200"/> 
</html>

### Заходим на сайт mos.ru

<html>
<img src="./screenshots/2.png" alt="drawing" width="200"/> 
</html>

### Входим в аккаунт на сайт mos.ru

<html>
<img src="./screenshots/3.png" alt="drawing" width="200"/> 
</html>

### Заходим в консоль разработчика

<html>
<img src="./screenshots/4.png" alt="drawing" width="200"/> 
</html>

### Находим файлы куки

<html>
<img src="./screenshots/5.png" alt="drawing" width="200"/> 
</html>

### Находим куки с ключом aupd_token - он является токеном авторизации

# Профит!! 

# Изменения в новой версии:
 - ## Добавили новые поля в класс User
 - ## Добавили класс ошибки DnevnikLibError
 - ## Добавили функцию, упрощающую ввод даты в классе User (get_date_in_format) 
 - ## Добавили инструкцию на получение токена (вход по логину и паролю будет позже)

## По поводу багов обращаться к создателю