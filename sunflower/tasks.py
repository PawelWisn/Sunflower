import sunflower.wsgi  # sets up settings
from invoke import task
from django.core.management import call_command
import subprocess
import time
from django.core.management.base import CommandError


@task
def run_api(c, port="8000", db_port="5432"):
    wait_for_database_setup(db_port)
    call_command("migrate")
    create_superuser()
    call_command("runserver", f"0.0.0.0:{port}")


def create_superuser():
    try:
        call_command("createsuperuser", "--noinput")
    except CommandError:
        print("Superuser already exists")


def wait_for_database_setup(db_port="5432"):
    while subprocess.run(
        ["nc", "-z", "db", db_port], stdout=subprocess.PIPE
    ).returncode:
        pass
