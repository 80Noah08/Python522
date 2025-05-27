# CNUM – код клиента
# NAME – имя заказчика
# CITY - город проживания клиента (заказчика)
# RATING - рейтинг клиента (покупателя)
# KOD - код продавца (менеджера)
# SUM – сумма
# CITY_2 – город, куда поставляют товар
# Prod – Товар
# REM - ремарка, примечание, пояснение
#
# =====================================
#
# 1. В какие города фирма поставляет товар.
#
# Select CITY2
# From ZAKAZ
#
# 2. В каких городах проживают заказчики.
#
# Select CITY
# From ZAKAZ
#
# 3. Какие заказчики обслуживаются менеджером с номером 1005.
#
# Select CNUM, NAME, KOD
# From ZAKAZ
# Where KOD is 1005
#
# 4. Вывести только тех заказчиков, рейтинг которых более 380.
#
# Select  NAME, RATING
# From ZAKAZ
# Where RATING > 380
#
# 5. Определите тех заказчиков в ремарках, о которых ничего не сказано.
#
# Select  NAME, REM
# From ZAKAZ
# Where REM is NULL
#
# 6. Выведите коды тех продавцов, которые имеют сумму заказа более 4000.
#
# Select  KOD, SUM
# From ZAKAZ
# Where SUM > 4000
#
# 7. Вывести тех заказчиков, сумма заказа которых менее 1000 и они не живут в Иркутске.
#
# Select  CNUM, NAME, SUM, CITY
# From ZAKAZ
# Where SUM < 1000 and CITY  is not 'Иркутск'
#
# 8. Вывести всех заказчиков, рейтинг которых от 100 до 270.
#
# Select   NAME, RATING
# From ZAKAZ
# Where RATING Between 100 and 270
#
# 9. Выведите фамилии, код, город проживания, тех заказчиков, которые поставляют товар не в тот город, в котором они проживают.
#
# Select   NAME, CNUM, CITY, CITY2
# From ZAKAZ
# Where CITY is not CITY2
#
# 10. Вывести код  всех продавцов рейтинг заказчиков, которых менее 200 или больше 350.
#
# Select   KOD, NAME, Rating
# From ZAKAZ
# Where RATING < 200 or RATING > 350
#
# 11. Вывести фамилии и товар всех заказчиков, которые заказали обеденные столы.
#
# Select   NAME, Prod
# From ZAKAZ
# Where Prod is 'столы обеденные'
#
# 12. Вывести фамилии заказчиков, в состав которых входит две буквы а и более.
#
# Select   NAME
# From ZAKAZ
# Where NAME Glob "*[Аa]*[Аа]*"
#
# 13. Определите коды тех продавцов, фамилии заказчиков которых начинаются на К (вывести фамилию заказчика и номер продавца).
#
# Select   NAME, KOD
# From ZAKAZ
# Where NAME Glob "К*"
#
# 14. Определите коды продавцов, которые продают стулья в Химках.
#
# Select KOD, Prod, CITY2
# From ZAKAZ
# Where Prod is 'стулья' and CITY2 = 'Химки'
#
# 15. Вывести всех заказчиков, которые проживают в Химках и продают товар там же, при этом сумма их заказа от 1000 до 1750.
#
#  NAME, CITY, CITY2, SUM
# From ZAKAZ
# Where CITY is'Химки' and CITY = CITY2 and SUM Between 1000 and 1750
#
# 16. Определить коды всех продавцов, которые не продают сейфы.
#
# Select KOD, Prod
# From ZAKAZ
# Where Prod is not 'сейфы'
#
# 17. Выведите список заказанных диванов на сумму большую 4000.
#
# Select Prod, SUM
# From ZAKAZ
# Where Prod is 'диваны' and SUM > 4000
#
# 18. Выведите фамилии тех заказчиков, которые купили стульев на сумму большую 1200.
#
# Select NAME, Prod, SUM
# From ZAKAZ
# Where Prod is 'стулья' and SUM > 1200
#
# 19. Определите фамилии тех продавцов, которые не живут в Иркутске и имеют рейтинг менее 200 пунктов.
#
# Select NAME, CITY, RATING
# From ZAKAZ
# Where CITY is not 'Иркутск' and RATING < 200
#
# 20. Написать запрос, который выводит фамилии заказчиков, которые имеют льготы на доставку.
#
# Select NAME, REM
# From ZAKAZ
# Where REM Like "льготная доставка"
#
# 21. Выведите фамилии продавцов, сумма заказа которых превышает 14000 тысяч и живут они не в Москве или Липецке.
#
# Select NAME, CITY, SUM
# From ZAKAZ
# Where SUM > 14000 and CITY is not 'Москва' and CITY is not 'Липецк'