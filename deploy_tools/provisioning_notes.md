Provisioning a new site
=======================

## Required packages:
* nginx
* Python 3.6
* virtualenv + pip
* Git

on Ubuntu:
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.6 python3.6-venv nginx git

## Nginx Virtual Host config
* see nginx.tempalte.config
* replace DOMAIN with superlists-staging.cybersmith.io
* replace USER with username that will run all this

## Systemd service
* see gunicorn-systemd.template.service
* replace DOMAIN with superlists-staging.cybersmith.io
* replace USER with username that will run all this

## Folder structure:

Assume we have a user account at /home/USER

/home/USER
    sites
        DOMAIN1
            .env
            db.sqlite3
            manage.py
            static
            virtualenv
            etc
        DOMAIN2
            .env
            db.sqlite3
            manage.py
            static
            virtualenv
            etc
