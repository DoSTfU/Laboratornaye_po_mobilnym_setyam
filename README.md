# Лабораторная работа №1 "Обработка и тарификация CDR (Call Detail Record)"
Последовательность действий:

Примечание: данная программа написана на языке Python версии 3. Для ее функционирования необходимо установить дистрибутив для работы с Python версии 3.
Для установки на UNIX необходимо воспользоваться командой sudo apt-get install python3 . Для установки на Windows необходимо скачать файл установки с официального сайта https://www.python.org/downloads/ и установить к себе на компьютер.

1) Загрузить и разархивировать папку с файлами к данной ЛР

2) Установить библиотеку pandas в директорию python, с которой работает Пользователь. Команды для установки:
а) Для UNIX (вводить в терминале): pip3 install pandas (для Python v.3)
	Примечание: При отсутствии вспомогательных пакетов для нормального функционирования данной библиотеки, в окно терминала возможно будет выведено сообщение об ошибке с просьбой установить необходимые пакеты. Данные пакеты устанавливаются в привилегированном режиме с помощью команды sudo apt install packet_name , где packet_name - имя требуемого пакета. После завершения установок необходимо будет повторить установку библиотеки pandas
б) Для Windows: Необходимо скачать и установить дистрибутив Anacondas по ссылке https://www.continuum.io/downloads 
После скачивания установить с помощью мастера установки. После чего нужная библиотека pandas будет установлена. Если же ее там не будет, то возможно ее установить отдельно с помощью пакетного менеджера, который входит в состав Anaconda, который называется conda. Для этого в терминале необходимо перейти в каталог [Anaconda install path]\Scripts\ . Далее следует ввести команду conda install pandas , после чего все будет установлено. Или же можно воспользоваться менеджером пакетов Python, для этого необходимо ввести одну из команд pip, указанных в пункте "а"

3) Далее в терминале необходимо перейти в директорию с файлами для данной ЛР и запустить ее следующим образом:
а) Для UNIX: python3 cdr.py
б) Для Windows: cdr.py
