#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import django
from django.conf import settings


sys.path.insert(0, abspath(dirname(__file__)))


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.auth',
            'django.contrib.admin',
            'email_log',
            'email_log.tests',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        EMAIL_LOG_BACKEND = 'django.core.mail.backends.locmem.EmailBackend',
        ROOT_URLCONF='email_log.tests.urls',
    )


def runtests():
    if hasattr(django, 'setup'):
        django.setup()
    try:
        from django.test.runner import DiscoverRunner
    except:
        from django.test.simple import DjangoTestSuiteRunner
        failures = DjangoTestSuiteRunner(failfast=False).run_tests(['tests'])
    else:
        failures = DiscoverRunner(failfast=False).run_tests(
            ['email_log.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    runtests()
