# -*- coding: utf-8 -*-
# @Author: p-chambers
# @Date:   2016-11-28 17:12:38
# @Last Modified by:   p-chambers
# @Last Modified time: 2016-11-28 17:26:00
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))