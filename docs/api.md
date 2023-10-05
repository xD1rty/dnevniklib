https://school.mos.ru/v3/userinfo <br>
GET запрос на получение данных об ученике, ничего не передается, только в Authorization хендлере токен.

https://school.mos.ru/api/family/web/v1/schedule?student_id=STUDENT_ID&date=DATE <br>
GET запрос на получение расписания в школе на какой-то промежуток времени. 

https://school.mos.ru/api/family/web/v1/homeworks?from=DATE&to=DATE&student_id=USER_ID <br>
GET запрос на получение домашнего задания на какой-то промежуток времени
В хендлерах Authorization передаем токен, а в X-Mes-Subsystem передаем familyweb.

https://dnevnik.mos.ru/core/api/student_profiles/USER_ID <br>
GET запрос на получение данных студента (его имя, фамилия, имя классного руководителя, person_id и тд тп.)

https://school.mos.ru/api/family/web/v1/programs/parallel_curriculum/570008?student_id=USER_ID <br>
GET запрос на получение данных об учебных часах на весь учебный год на все предметы. В хендреры принимает X-Mes-Subsystem (familyweb), Auth-Token, Authorization.