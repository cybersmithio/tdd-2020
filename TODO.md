# To-do
* valid input so there are no blanks or duplicates
* remove hardcoded URLs from views.py
* remove hardcoded URLs from forms in list.html and home.html


# Done
* Get the server running on port 80 instead of 8080
* Get rid of Django dev server, and put something that can handle real workloads (i.e. Nginx and Gunicorn)
* Get DEBUG=False into settings.py
* Make ALLOWED_HOSTS less permissive
* Set a unique SECRET_KEY
* Systemd config file so the web server starts automatically on server reboot