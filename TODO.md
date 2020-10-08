# To-do
* Clean up wait_for stuff in base.py

# Done
* Get the server running on port 80 instead of 8080
* Get rid of Django dev server, and put something that can handle real workloads (i.e. Nginx and Gunicorn)
* Get DEBUG=False into settings.py
* Make ALLOWED_HOSTS less permissive
* Set a unique SECRET_KEY
* Systemd config file so the web server starts automatically on server reboot
* remove hardcoded URLs from views.py
* remove hardcoded URLs from forms in list.html and home.html
* valid input so there are no blanks
* Remove duplication of validation logic in views
* Send emails
* Generating and recognising unique tokens
* How to authenticate someone in Django
* What steps will the user have to go through
