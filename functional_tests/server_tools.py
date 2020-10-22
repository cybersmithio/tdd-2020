from fabric.api import run, env
from fabric.context_managers import settings, shell_env


def _get_manager_dot_py(host):
    return f'~/sites/{host}/virtualenv/bin/python ~/sites/{host}/manage.py'


def reset_database(username, host):
    manage_dot_py = _get_manager_dot_py(host)
    print(f"reset_database: Connecting to staging server with string {username}@{host}")
    #with settings(host_string=f'{username}@{host}'):
    #with settings(user=username):
    with settings(user=username, host_string=host, key_filename='superlists-staging_key.pem', warn_only=True):
        run(f'{manage_dot_py} flush --noinput')


def _get_server_env_vars(host):
    env_lines = run(f'cat ~/sites/{host}/.env').splitlines()
    return dict(l.split('=') for l in env_lines if l)


def create_session_on_server(username, host, email):
    manage_dot_py = _get_manager_dot_py(host)
    print(f"create_session_on_server: Connecting to staging server with string {username}@{host}")
    #with settings(host_string=f'{username}@{host}'):
    with settings(user=username, host_string=host, key_filename='superlists-staging_key.pem'):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f'{manage_dot_py} create_session {email}')
            return session_key.strip()
