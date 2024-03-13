import pymysql.cursors

def connection_mysql ():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 passwd='',
                                 database='dbapi',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    return connection