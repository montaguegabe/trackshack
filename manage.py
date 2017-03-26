#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
from raygun4py import raygunprovider

def handle_exception(exc_type, exc_value, exc_traceback):
    print('Exception sent to Raygun')
    key = os.getenv('RAYGUN_APIKEY')
    sender = raygunprovider.RaygunSender(key)
    sender.send_exception(exc_info=(exc_type, exc_value, exc_traceback))

    sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = handle_exception

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tracktalk.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
