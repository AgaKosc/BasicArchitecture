import pymysql


class Database:

    def __init__(self):
        self.cnx = None

    def connect(self, dbSetting):
        self.cnx = pymysql.connect(user=dbSetting["user"], passwd=dbSetting["password"],
                                   host=dbSetting["host"], port=dbSetting["port"], db=dbSetting["name"])

    def processSqlQuery(self, sqlQuery, update=False):
        cursor = self.cnx.cursor()
        cursor.execute(sqlQuery)
        if update:
            self.cnx.commit()
        records = [record for record in cursor]
        cursor.close()
        return records

    def disconnect(self):
        self.cnx.close()
