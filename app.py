import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parents.settings")  # change "myproject" to your project name
    sys.argv = ["manage.py", "runserver", "127.0.0.1:8000"]  # default host:port
    execute_from_command_line(sys.argv)
