# -*- encocding: utf-8 -*-
from __future__ import unicode_literals
import os

# App mount point, if the environment variable 'OABOT_DEV' is defined then
# mount the application on '/', otherwise mount it under '/oabot'
OABOT_APP_MOUNT_POINT = '/oabot'
if os.environ.get('OABOT_DEV', None) is not None:
    # Mount point is '/'
    OABOT_APP_MOUNT_POINT = ''

OABOT_USER_AGENT = 'OAbot/1.0 (+http://enwp.org/WP:OABOT)'

# the bot will not make any changes to these templates
excluded_templates = ['cite arxiv', 'cite web', 'cite news', 'cite book']

# Set the API key for the Zotero endpoint here.
# This Zotero endpoint is just a version of 
# https://github.com/zotero/translation-server
# protected by an API key (otherwise it would allow
# anyone use it to query any website, which is dangerous)
#
# Ask for an API key at  dev @ dissem . in
# 
ZOTERO_CACHE_API_KEY = open('zotero_cache_key.txt','r').read().strip()
if not ZOTERO_CACHE_API_KEY:
    raise ValueError('Please provide a Zotero cache API key '+
                    '(email dev @ dissem . in to get one.)')


# PDFbox location.
# this is necessary to run CiteSeerX's PDF classification
# heuristics, to check that full texts look legit.
# Download it from http://pdfbox.apache.org/
PDFBOX_JAR_PATH = 'resources/pdfbox-app-2.0.3.jar'
FILTER_JAR_PATH = 'resources/classifier.jar'
FILTER_ACL_PATH = 'resources/acl'
FILTER_TRAIN_DATA_PATH = 'resources/train_str_f43_paper.arff'

