#-*- coding: utf-8 -*-
#!/usr/bin/python
import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print "BASE_DIR : %s" % BASE_DIR
sys.path.append(BASE_DIR+"/auction")

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from django.conf import settings
from django.contrib.auth.models import User

from account.models import Account
from core.models import Stuff, Deal

from django.templatetags.static import static

stuff = Stuff(name           = "7개월간 코딩만한 크고 가벼운 노트북",
              start_price    = "550000",
              min_diff_price = "1000",
              img_url        = static("img/acer.png"),
              detail         = "15.6인치 1920x1080 2.0Kg i7-4500U (1.8GHz) 8GB GT750M")

stuff.save()
