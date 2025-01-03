<p align="center">
  <a href="README.ru.md"><img src="https://img.shields.io/badge/Русский-Readme-blue" alt="Russian" /></a>&nbsp;&nbsp;
  <a href="README.md"><img src="https://img.shields.io/badge/English-Readme-blue" alt="English" /></a>&nbsp;&nbsp;
  <img src="https://visitor-badge.laobi.icu/badge?page_id=White-Tiger-PX.set-random-wallpaper-from-folders" alt="visitors" />&nbsp;&nbsp;
  <img src="https://img.shields.io/github/stars/White-Tiger-PX/set-random-wallpaper-from-folders?style=social" alt="GitHub stars" />
</p>

# set-random-wallpaper-from-folders

Этот скрипт позволяет установить случайное изображение из заданного списка папок в качестве обоев рабочего стола. Он поддерживает фильтрацию по расширению файлов и включает опцию поиска в подкаталогах.

## Особенности

- Выбирает случайное изображение из одной или нескольких указанных папок.
- Поддерживает фильтрацию по расширению файлов.
- Опция включения или исключения подкаталогов в поиске.
- Автоматически устанавливает выбранное изображение в качестве обоев рабочего стола.

## Поддерживаемые операционные системы

Этот скрипт предназначен специально для Windows. Он использует библиотеку ctypes для взаимодействия с Windows API и установки обоев рабочего стола.

## Установка

### Настройка папок с изображениями

- Откройте файл `config.py`.
- Замените пути в списке `FOLDERS` на директории, содержащие ваши изображения.
- Для каждой папки вы можете указать, включать ли подкаталоги в поиск, установив `include_subfolders` в `True` или `False`.

### Автоматическое выполнение скрипта

Чтобы скрипт выполнялся автоматически при запуске системы, настройте задачу в **Планировщике заданий Windows**:

1. Откройте **Планировщик заданий**, найдя его в меню Пуск (или нажмите `Win + R`, введите `taskschd.msc` и нажмите Enter).
2. Нажмите на **Создать задачу** в правой панели.
3. Укажите имя для вашей задачи (например, "Установить случайные обои").
4. Перейдите на вкладку **Триггеры** и нажмите **Создать**.
   - Установите параметр **Начать задачу** на **При входе в систему**, чтобы задача запускалась при каждом входе в систему.
   - Опционально, установите флажок **Повторять задачу каждые** и укажите интервал (например, каждый час), если хотите, чтобы задача выполнялась периодически.
5. Перейдите на вкладку **Действия**, нажмите **Создать** и выберите **Запуск программы**.
6. Выберите исполнимый файл Python. По умолчанию он находится по следующему пути:
   `C:\Users\ВАШЕ_ИМЯ_ПОЛЬЗОВАТЕЛЯ\AppData\Local\Programs\Python\ВАША_ВЕРСИЯ_python\python.exe`.
7. В поле **Добавить аргументы** укажите полный путь к вашему скрипту. Например:
   `(C:\путь\к\вашему\set_random_wallpaper_from_folders.py)`
   *(Убедитесь, что путь заключён в кавычки, если он содержит пробелы.)*
8. Нажмите **ОК**, чтобы сохранить задачу.

<div style="justify-content: space-between; align-items: center;">
  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - Triggers.png" alt="Task Scheduler - Triggers" width="75%" />
  </div>

  <div style="text-align: center;">
    <img src="Task Scheduler - General.png" alt="Task Scheduler - General" width="75%" />
  </div>
</div>
