# tdd-2020
My project as I work through the Test-Driven Development with Python by Harry Percival

#Environment
* Django 1.11
* Windows 10
* Visual Studio redistributable https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
* Gecko driver https://github.com/mozilla/geckodriver/releases/
* Python 3.6
    * Selenium 3

# To run dev server in Linux enviornment:
set -a ; source .env ; set +a; python manage.py runserver


# To run dev server in Windows environment:
.env.bat
python manage.py runserver

# To run functional tests in staging in Windows environment:
set STAGING_SERVER=superlists-staging.cybersmith.io
set STAGING_SERVER_USERNAME=*******
set TEST_EMAIL=***************
python manage.py test functional_tests
set STAGING_SERVER=

