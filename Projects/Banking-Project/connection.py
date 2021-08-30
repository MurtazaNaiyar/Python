__author__ = 'user'

import cx_Oracle
import os
#you must have Oracle database userId and password for connection from database.

con = cx_Oracle.connect('hr/manager@xe')
cur = con.cursor()
