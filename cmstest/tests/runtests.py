#!/usr/bin/python

import os, sys

APPDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
APPNAME = os.path.basename(APPDIR)
TESTMODULE = '.'.join([APPNAME, 'tests'])

os.environ['DJANGO_SETTINGS_MODULE'] = '.'.join([TESTMODULE, 'settings'])
sys.path.append(os.path.dirname(APPDIR))

import django
from django.conf import settings
from django.test.utils import get_runner

if hasattr(django, 'setup'):
    django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner(verbosity=1)
kwargs = {}
if TestRunner.__name__ == 'DjangoTestSuiteRunner':
    from unittest import TestLoader
    kwargs['extra_tests'] = TestLoader().discover(TESTMODULE)
failures = test_runner.run_tests([APPNAME,], **kwargs)
if failures:
    sys.exit(bool(failures))
