# Тестовое задание для Ipavlov
[![flake8](https://github.com/MigAru/fast_api_test_ipavlov/actions/workflows/flake8.yml/badge.svg?branch=main)](https://github.com/MigAru/fast_api_test_ipavlov/actions/workflows/flake8.yml)

## О проекте
Данный проект был сделан в качестве тестового задания для компании Ipavlov.
В проекте были реализованы 3 эднпоинта по архитектуре REST на базе фреймворка FastAPI

## Установка
Для запуска проета нужно скачать и установить Docker и Docker-compose по [мануалу](https://docs.docker.com/desktop/) с официального источника
___

## Запуск
Для того чтобы запустить проект
```sh
$ docker-compose up -d --build
```
Применить миграции
```sh
$ docker-compose exec backend aerich upgrade
```
___
## Доступные Url после запуска
[Документация](http://127.0.0.1:8000/docs) и [эндпоинты items](http://127.0.0.1:8000/items)