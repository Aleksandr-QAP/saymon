Вспомогательные файлы
-----

[pages/locator.py](pages/locator.py) содержит набор локаторов.

[pages/settings.py](pages/settings.py) содержит необходимые для тестирования переменные.

[conftest.py](conftest.py) набор фикстур.

---
Локальное тестирование
-----

[local_tests](local_tests) содержит тесты, используемые для локального запуска.

[local_tests/test_saymon.py](local_tests/test_saymon.py) содержит набор тестов:
1) [test_base] Сценарий, описанный в тестовом задании.


Запуск Теста
----------------

1) Установить все зависимости:

    ```bash
    pip3 install -r requirements
    ```

2) Загрузить Selenium WebDriver  https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)

3) Добавляем вебдрайверу права на исполнение:

   ```bash
    sudo chmod +x ./chrome-linux64/chrome
    ```
    
4) Запуск теста:

    ```bash
    python3 -m pytest --html=report_saymon.html --self-contained-html -v --driver Chrome --driver-path ./local_tests/chrome-linux64/chrome ./local_tests/test_saymon.py 
    ```
   
Замечание:
~/chrome указывает на путь к файлу Selenium WebDriver, загруженному и разархивированному в шаге #2.

---
Тестирование в GitLab CI
-----

[tests](tests) содержит тесты, используемые для запуска в GitLab.

[tests/test_saymon.py](tests/test_saymon.py) содержит набор тестов:
1) [test_base] Сценарий, описанный в тестовом задании.


Запуск Теста
----------------

1) Загрузить Docker-image selenium/standalone-chrome:

   ```bash
       docker pull selenium/standalone-chrome
   ```

2) Запустить локально контейнер Selenium WebDriver:

   ```bash
       docker run --rm -it -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:latest
   ```

3) Запустить сборочную линию в GitLab-CI

PS: Возможен локальный запуск теста с использованием remote_browser:

   ```bash
       python3 -m pytest --html=report_saymon.html --self-contained-html -v --driver Chrome tests/test_saymon.py 
   ```