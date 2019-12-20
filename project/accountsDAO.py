import mysql.connector
import config as cfg
class AccountsDAO:
    db=""
    def __init__(self): 
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        #user="root", password blank
        database=cfg.mysql['database']
        )
    
    def getOne(self):
        cursor = self.db.cursor()
        sql="select * from accounts"
        cursor.execute(sql)
        results = cursor.fetchone()
        #returnArray = []
        #print(results)
        #for result in results:
            #print(result)
            #returnArray.append(self.convertToDictionary(result))

        return results
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into accounts (username, password,email) values (%s,%s,%s)"
        cursor.execute(sql, values)

        self.db.commit()
        return cursor.lastrowid

    def convertToDictionary(self, result):
        colnames=['id','username','password','email']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
accountsDAO = AccountsDAO()