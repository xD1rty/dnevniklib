# Библиотека для автоматизированного сбаро информации из Дневника МЭШ ```dnevniklib```

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

## Данная библиотека - является выплеском адреналина 7-ми классника.
## По поводу багов обращаться к создателю