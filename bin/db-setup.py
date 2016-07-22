#!/usr/bin/env python
from argparse import ArgumentParser
import subprocess
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'csa.settings'
django.setup()
from csa.models.user import User, UserProfile
from csa.models.core import ProductCategory, ProductMeasureUnit


def test_data():
    ProductMeasureUnit.objects.bulk_create([
        ProductMeasureUnit(name='κιλό'),
        ProductMeasureUnit(name='μάτσο')
    ])

    ProductCategory.objects.bulk_create([
        ProductCategory(name='Λαχανικά'),
        ProductCategory(name='Φρούτα'),
        ProductCategory(name='Μεταποιημένα')
    ])

    ProductCategory.objects.create(
        name='Ντομάτες',
        parent=ProductCategory.objects.get(name='Λαχανικά'))

    password = 'p4ssw0rd'
    admin = User.objects.create_user(
        username='admin',
        email='csa@example.com',
        password=password,
        first_name='CSA',
        last_name='Διαχειρηστής')

    consumer = User.objects.create_user(
        username='consumer',
        email='consumer@example.com',
        password=password,
        first_name='Τάκης',
        last_name='Σουπερμαρκετάκης')
    UserProfile.objects.create(
        user=consumer,
        phone_number='+306976823542')

    producer = User.objects.create_user(
        username='producer',
        email='producer@example.com',
        password=password,
        first_name='Βάσω',
        last_name='Παρασύρη')
    UserProfile.objects.create(
        user=producer,
        phone_number='+306976823542')





parser = ArgumentParser(description='CSA database setup tool')
parser.add_argument('--drop', action='store_true', help='drop tables')
parser.add_argument('--init', action='store_true', help='creates tables and initialize')
parser.add_argument('--test-data', action='store_true', help='add test data')

args = parser.parse_args()

if args.drop:
    subprocess.check_call(
        './manage.py sqlflush | ./manage.py dbshell',
        shell=True)

if args.init:
    for cmd in [
            './manage.py makemigrations --no-input',
            './manage.py makemigrations csa --no-input',
            './manage.py migrate --no-input'
    ]:
        subprocess.check_call(cmd, shell=True)

if args.test_data:
    test_data()
