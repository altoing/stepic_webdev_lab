#!/usr/bin/env python
import MySQLdb
db = MySQLdb.conect(host="localhost", user="root")
cursor =db.cursor()