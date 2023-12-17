import sqlite3

def mysql(user,pwd):
    class main():
        def display(self,user,pwd):
             connetion = sqlite3.Connection('mydatabase.db')
             cursor = connetion.cursor()
             check_U = cursor.execute(f'''
                                       SELECT USER_NAME FROM DATA_SET WHERE "{user}" IN (SELECT USER_NAME FROM DATA_SET);
                                      ''').fetchall()
             if len(check_U)!=0 :
                 check_P = cursor.execute(f'''
                                       SELECT USER_PASSWORD FROM DATA_SET WHERE "{pwd}" IN (SELECT USER_PASSWORD FROM DATA_SET);
                                      ''').fetchall()
                 if len(check_P)!=0 :
                     return True
                 else:
                     return False
             else:
                 return False
             
    ob = main()   
    if ob.display(user,pwd) :
        return True
    else:
        return False   
     
def register(user,pwd,email):
    class re_data():       
        def register(self,user,pwd,email):
             connetion = sqlite3.Connection('mydatabase.db')
             cursor = connetion.cursor()
             cursor.execute(''' 
                            CREATE TABLE IF NOT EXISTS DATA_SET(USER_NAME TEXT,USER_PASSWORD TEXT,USER_EMAIL TEXT);
                            ''')
             check_U = cursor.execute(f'''
                                       SELECT USER_NAME FROM DATA_SET WHERE "{user}" IN (SELECT USER_NAME FROM DATA_SET);
                                      ''').fetchall()
             if len(check_U)==0:
                 cursor.execute(f''' 
                                 INSERT INTO DATA_SET(USER_NAME,USER_PASSWORD,USER_EMAIL) VALUES("{user}","{pwd}","{email}");
                                 ''')
                 connetion.commit()
                 return True
             else:       
                 return False                      
    
    ob = re_data()
    if ob.register(user,pwd,email):
        return True
    else:
        return False