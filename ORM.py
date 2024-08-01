import sqlite3
from user_obj import User
from mmm_obj import MMM_Obj
from requirements import SkillRequirements

class ORM:

    def __init__(self, db_name):
        self._database = sqlite3.connect(db_name)
        self._cursor = self._database.cursor()
        self.gen_db()
    
    def __del__(self):
        self._database.close()
    
    def gen_db(self):
        self._cursor.execute("DROP TABLE IF EXISTS Requirements")
        self._cursor.execute("""
                       CREATE TABLE IF NOT EXISTS Requirements
                       (id int primary key, Attack int, Strength int, Defense int, Ranged int, 
                       Prayer int, Magic int, Runecraft int, Hitpoints int, Crafting int,
                       Mining int, Smithing int, Fishing int, Cooking int, 
                       Firemaking int, Woodcutting int, Agility int, Herblore int, 
                       Thieving int, Fletching int, Slayer int, Farming int, 
                       Construction int, Hunter int)
                       """)
        self._cursor.execute("DROP TABLE IF EXISTS MMM")
        self._cursor.execute("""
                       CREATE TABLE IF NOT EXISTS MMM
                       (id int primary key ,Method text, Profit int,
                       Time boolean, Requirements_id int,
                       FOREIGN KEY(Requirements_id)
                       REFERENCES Requirements(id)) 
                       """)
        self._cursor.execute("DROP TABLE IF EXISTS Users")
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS Users 
                             (id int primary key, Name varchar(12), 
                             Reqs_id int, 
                             FOREIGN KEY(Reqs_id) REFERENCES Requirements(id))""")
        self._database.commit()     
        
    def gen_db_data(self):
        self._cursor.execute("""INSERT INTO Requirements VALUES (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)""")
        self._cursor.execute("""INSERT INTO Requirements VALUES (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)""")
        self._cursor.execute("""INSERT INTO Requirements VALUES (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)""")
        self._cursor.execute("""INSERT INTO MMM VALUES (1, 'Killing Green Dragons', 2300000, 1, 1)""") 
        self._cursor.execute("""INSERT INTO MMM VALUES (2, 'Farming Kuwarms', 1000000, 0, 1)""")   
        self._cursor.execute("""INSERT INTO Users VALUES (1, 'squidman2023', 3)""")
        self._database.commit()
    
    def get_user(self, name):
        user = self._cursor.execute(f"SELECT * FROM Users WHERE Name = '{name}'").fetchone()
        reqs = self._cursor.execute(f"SELECT * FROM Requirements WHERE id = {user[2]}").fetchone()
        return User(user[1],SkillRequirements(reqs[1],reqs[2],reqs[3],reqs[4],reqs[5],reqs[6],reqs[7],reqs[8],reqs[9],reqs[10],reqs[11],reqs[12],reqs[13],reqs[14],reqs[15],reqs[16],reqs[17],reqs[18],reqs[19],reqs[20],reqs[21],reqs[22],reqs[23]))
   
    def get_method(self, id):
        method = self._cursor.execute(f"SELECT * FROM MMM WHERE id = {id}").fetchone()
        reqs = self._cursor.execute(f"SELECT * FROM Requirements WHERE id = {method[4]}").fetchone()
        return MMM_Obj(method[1], method[2], method[3], SkillRequirements(reqs[1],reqs[2],reqs[3],reqs[4],reqs[5],reqs[6],reqs[7],reqs[8],reqs[9],reqs[10],reqs[11],reqs[12],reqs[13],reqs[14],reqs[15],reqs[16],reqs[17],reqs[18],reqs[19],reqs[20],reqs[21],reqs[22],reqs[23]))

    def get_method_by_user(self, userobj):
        method = self._cursor.execute(f"SELECT * FROM MMM WHERE Requirements_id = {userobj.reqs.id}").fetchall()    
        temp = []
        for each in method:
            reqs = self._cursor.execute(f"SELECT * FROM Requirements WHERE id = {each[4]}").fetchone()
            temp.append(MMM_Obj(each[1], each[2], each[3],SkillRequirements(reqs[1],reqs[2],reqs[3],reqs[4],reqs[5],reqs[6],reqs[7],reqs[8],reqs[9],reqs[10],reqs[11],reqs[12],reqs[13],reqs[14],reqs[15],reqs[16],reqs[17],reqs[18],reqs[19],reqs[20],reqs[21],reqs[22],reqs[23])))
        return temp
    def add_user(self, name, reqsid):
        self._cursor.execute(f"INSERT INTO Users VALUES ({self._cursor.lastrowid+1}, '{name}', {reqsid})")        
        return self._cursor.lastrowid
    def add_method(self, method, profit, time, reqsid):
        self._cursor.execute(f"INSERT INTO MMM VALUES ({self._cursor.lastrowid+1}, '{method}', {profit}, {time}, {reqsid})")
        return self._cursor.lastrowid
    def add_requirement(self, reqs_list):
        self._cursor.execute(f"INSERT INTO MMM VALUES ({self._cursor.lastrowid+1},'{reqs_list[0]}',{reqs_list[1]}','{reqs_list[2]}', {reqs_list[3]},'{reqs_list[4]}','{reqs_list[5]}', '{reqs_list[6]}','{reqs_list[7]}', {reqs_list[8]},'{reqs_list[9]}','{reqs_list[10]}', '{reqs_list[11]}','{reqs_list[12]}', {reqs_list[13]},'{reqs_list[14]}','{reqs_list[15]}', '{reqs_list[16]}','{reqs_list[17]}', {reqs_list[18]},'{reqs_list[19]}','{reqs_list[20]}', '{reqs_list[21]}', '{reqs_list[22]}')")
        
    def edit_user(self, id, name, reqsid):
        self._cursor.execute(f"UPDATE Users SET name = '{name}', Reqs_id = {reqsid} WHERE id = {id}")
        return self._cursor.lastrowid

    def edit_method(self, id, method, profit, time, reqsid):
        self._cursor.execute(f"UPDATE MMM SET method = '{method}', profit = {profit}, time = {time}, Requirements_id = {reqsid} WHERE id = {id}")
        return self._cursor.lastrowid

    def edit_requirement(self, id, reqs_list):
        self._cursor.execute("""UPDATE Requirements SET Attack = '{reqs_list[0]}', Strength = '{reqs_list[1]}', Defense = '{reqs_list[2]}', Ranged = '{reqs_list[3]}',
                             Prayer = '{reqs_list[4]}', Magic = '{reqs_list[5]}', Runecraft = '{reqs_list[6]}', Hitpoints = '{reqs_list[7]}', Crafting = '{reqs_list[8]}',
                             Mining = '{reqs_list[9]}', Smithing = '{reqs_list[10]}', Fishing = '{reqs_list[11]}', Cooking = '{reqs_list[12]}', Firemaking = '{reqs_list[13]}',
                             Woodcutting = '{reqs_list[14]}', Agility = '{reqs_list[15]}', Herblore = '{reqs_list[16]}', Thieving = '{reqs_list[17]}', Fletching = '{reqs_list[18]}',
                             Slayer = '{reqs_list[19]}', Farming = '{reqs_list[20]}', Construction = '{reqs_list[21]}', Hunter = '{reqs_list[22]}' WHERE id = {id}""")
        return self._cursor.lastrowid
    
    def del_user(self, id):
        self._cursor.execute(f"DELETE FROM Users WHERE id = {id}")
        return self._cursor.lastrowid
    def del_method(self, id):
        self._cursor.execute(f"DELETE FROM MMM WHERE id = {id}")
        return self._cursor.lastrowid
    def del_requirement(self, id):
        self._cursor.execute(f"DELETE FROM Requirements WHERE id = {id}")
        return self._cursor.lastrowid
    