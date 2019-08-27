#Бандитское тестирование

## Введение
### Цель статьи
### Оглавление

## Конверсии бандиты против аб
### Принцип работы бандита
Бандитское тестирование - это особый вид АБ-тестирования, при котором мы начинаем использовать информацию об успешности
вариантов рассылок в тот момент, когда узнаем о ней, а не откладываем до конца АБ-теста.

В начале рассылки, пока нет информации о конверсиях, мы рассылаем варианты 50/50.
В момент, когда приходят первые отклики, мы меняем эту пропорцию в пользу варианта, который показывает себя лучше.
И чем больше наша уверенность в превосходстве одного варианта над другим, тем большую часть писем мы шлем с этим вариантом.

Это позволяет получить из больше конверсий из рассылки, чем при использовании классического АБ-теста.

### Конверсии
* Конверсии в одинаковых условиях, таблица плюс словами это лучше, это хуже (Пример с результатом, сравниваем с оптимальным размером АБ-теста)
* Еще несколько примеров, таблица слева оптимальный аб, справа бандит

## Принцип работы АБ-тестирования
При использовании классических АБ-тестов для увеличения конверсий из рассылки варианты рассылки сначала сравниваются (собственно, проводится АБ-тест, шлем 50/50), и только потом знания какой вариант лучше используются (выбирается лучший вариант и рассылаем оставшиеся письма с ним).

В отличие от классических АБ-тестов, бандитские АБ-тесты используют отклик на рассылку сразу как она приходит.
Чем лучше показывает себя вариант по сравнению с другими, тем с больше мы выставляем вероятность, что следующее письмо уйдет именно с этим вариантом.
Вначале мы шлем варианты 50/50, но как только один вариант показывает себя лучше другого, мы начинаем слать на него все большую и большую часть траффика.

Это приводит к тому, что мы начинаем пользоваться информацией о том, какой вариант лучше с самого начала рассылки и рассылка приносит больше конверсий.

* вероятности вариантов меняются динамически
* чем больше уверенность, тем больше доля писем
* когда 99% уверены, что вариант лучший - шлем на него 99%
* если варианты одинаковые - шлем 50/50

## Бандитское тестирование проще запускать
* меньше настроек при лучшем результате
* не нужно думать о размере АБ теста
* не нужно угадывать, какой будет процент конверсий у вариантов

## Бандитское тестирование должно быть встроено в рассыльщик, его нельзя запустить "на коленке"
* рассыльщик должен собирать отклики и динамически менять доли вариантов
* для этого у него должен быть функционал
* чтобы запустить "на коленке", нужно самостоятельно написать механизм распределения по вариантам и перераспределять адресатов по вариантам не реже, чем раз в час
* нужно ограничивать скорость отправки писем, иначе все уйдет до получения первого отклика, 50/50

## Лучше работает на сайте, хуже конверсиями из писем в заказы - чем быстрее отклик, тем лучше
* если отклик запаздывает на 2 часа, то и вероятности обновляются на 2 часа позже
* с классическими аб тестами это можно побороть если быстро отправить все письма для аб и подождать отклик
* проблема не возникает в триггерной рассылке