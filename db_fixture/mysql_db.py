import pymysql.cursors
import os
import configparser as cparser

# ======== Reading db_config.ini setting ===========
base_dir=str(os.path.dirname(os.path.dirname(__file__)))
base_dir=base_dir.replace('\\','/')
file_path=base_dir+"db_config.ini"

cf=cparser.ConfigParser()
cf.read(file_path)
host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf",'port')
db=cf.get("mysqlconf","db_name")
user=cf.get("mysqlconf",'user')
password=cf.get("mysqlconf","password")


# ======== MySql base operating ===================
class DB:
    def __int__(self):
        try:
            self.connetion=pymysql.connect(host=host,
                                           user=user,
                                           password=password,
                                           db=db,
                                           charset='utf8mb4',
                                           cursorclass='pymysql.cursors.DictCursor')
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    #清除数据
    def clear(self,table_name):
        real_sql='delete from'+table_name+";"
        with self.connetion.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)

        self.connetion.commit()



    #插入sql语句
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"
        key=','.join(table_data.keys())
        value=','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value+ ")"
        print(real_sql)
        with self.connetion.cursor() as cursor:
            cursor.execute(real_sql)





