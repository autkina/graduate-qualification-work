import logging
import mysql.connector
from mysql.connector import Error

class db:
    isc = False #Is Connected?
    conn = None
    cursor = None

    @classmethod
    def connect(cls):
        # ѕараметры подключени€
        host = '82.202.156.82'
        database = 'mbio'
        user = 'BISuser'
        password = 'psu_bio'
        port=3306
        try:
            cls.conn = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if cls.conn.is_connected():
                cls.cursor = cls.conn.cursor()
                cls.isc = True
                return cls.conn
            else:
                return None
        except Error as e:
            logging.error('Error while connecting to SQL Server', e)
            return None


    @classmethod
    def select_all(cls, table): #поиск по любой таблице
        if cls.isc:
            request_to_read_data = f'SELECT * FROM {table}'
            cls.cursor.execute(request_to_read_data)
            data = cls.cursor.fetchall()
            logging.info(f'Select is done')
            for d in data:
                print(d)

    @classmethod
    def insert_stdnt(cls, data): #регистраци€ студента
        if cls.isc:        
            request_to_read_data = f'SELECT key_user, login FROM BISUser WHERE login = "{data[0]}" and passw = "{data[1]}";'
            print(request_to_read_data)
            cls.cursor.execute(request_to_read_data)
            dataf = cls.cursor.fetchone()
            print('dataf', dataf)
            if (dataf != None):
                login = dataf[1]
                login += login[0]
                print(login)
                data_to_ins = (login, data[1], 1)
            else:
                data_to_ins = (data[0], data[1], 1 )
            cls.cursor.execute('INSERT INTO BISUser (login,passw,key_type) VALUES (%s, %s, %s);', (data_to_ins))
            cls.conn.commit()
            return data_to_ins[0]
        else:
            return False
        

    @classmethod
    def insert_grp(cls, data): #регистраци€ группы
        if cls.isc:
            request_to_read_grp = f'SELECT key_group FROM UserGroup WHERE name_gr = "{data[1]}";'
            cls.cursor.execute(request_to_read_grp)
            data_grp = cls.cursor.fetchone()
            if data_grp == None:
                data_to_ins = (data[0], data[1], 1)
                cls.cursor.execute('INSERT INTO UserGroup (key_lect,name_gr,isActive) VALUES (%s, %s, %s);', (data_to_ins))
                cls.conn.commit()
                return True

    @classmethod
    def grp_stdn(cls, data): #добавление студента в группу
        if cls.isc:        
            request_to_read_std = f'SELECT key_user FROM BISUser WHERE login = "{data[1]}";'
            cls.cursor.execute(request_to_read_std)
            data_std = cls.cursor.fetchone()
            if data_std:
                request_to_read_grp = f'SELECT key_group FROM UserGroup WHERE name_gr = "{data[0]}";'
                cls.cursor.execute(request_to_read_grp)
                data_grp = cls.cursor.fetchone()
                data_to_ins = (data_grp[0], data_std[0])
                
                request_to_read_connect = f'SELECT key_group, key_user FROM Connect_UserGroup WHERE key_group = {data_grp[0]} and key_user = {data_std[0]};'
                cls.cursor.execute(request_to_read_connect)
                data_conn = cls.cursor.fetchone()
                if data_conn == None:
                    print('INSERT INTO Connect_UserGroup (key_group,key_user) VALUES (%s, %s);', (data_to_ins))
                    cls.cursor.execute('INSERT INTO Connect_UserGroup (key_group,key_user) VALUES (%s, %s);', (data_to_ins))
                    cls.conn.commit()
                    return True
            else:
                return False

    @classmethod
    def find_stdnt(cls, data): #поиск пользовател€ по логину и паролю
        if cls.isc:        
            print(data)
            request_to_read_data = f'SELECT key_user, key_type FROM BISUser WHERE login = "{data[0]}" and passw = "{data[1]}";'
            print(request_to_read_data)
            cls.cursor.execute(request_to_read_data)
            dataf = cls.cursor.fetchone()
            print('dataf', dataf)
            return dataf
    
    @classmethod
    def find_groups(cls): #поиск группы, если она ещЄ активна
        equest_to_read_grps = f'SELECT name_gr FROM UserGroup where isActive = 1;'
        cls.cursor.execute(equest_to_read_grps)
        data_grps = cls.cursor.fetchall()
        result = []
        for row in data_grps:
            group_str = row[0]
            result.append(group_str)
        print(result)
        return result
        
    @classmethod
    def find_modules(cls): #поиск модул€ с закрытым доступом
        equest_to_read_grps = f'SELECT name_mod FROM Module where isLimitAccess = 1;'
        cls.cursor.execute(equest_to_read_grps)
        data_grps = cls.cursor.fetchall()
        print(data_grps[0])
        result = []
        for row in data_grps:
            group_str = row[0]
            result.append(group_str)
        print(result)
        return result
        
    @classmethod
    def find_modules_access(cls, data): #поиск доступных и недоступных дл€ пользовател€ модулей
        equest_to_read_acc = f"""select isAccessOpened from Connect_GroupModule
                                join UserGroup on (UserGroup.key_group = Connect_GroupModule.key_group)
                                join Connect_UserGroup on (Connect_UserGroup.key_group = UserGroup.key_group)
                                join BISUser on (BISUser.key_user = Connect_UserGroup.key_user)
                                where BISUser.login = '{data[0]}' order by Connect_GroupModule.key_module;"""
        cls.cursor.execute(equest_to_read_acc)
        data_acc = cls.cursor.fetchall()
        if data_acc:
            print(data_acc[0])
            result = []
            for row in data_acc:
                acc_str = row[0]
                result.append(acc_str)
            print(result)
        else:
            result = None
        return result
    
    @classmethod
    def check_state(cls, data): #проверка статуса доступа к модулю у группы
        if cls.isc:        
            print(data)
            request_to_read_datagr = f'SELECT key_group FROM UserGroup WHERE name_gr = "{data[0]}";'
            cls.cursor.execute(request_to_read_datagr)
            datagr = cls.cursor.fetchone()
            print('datagr', datagr)
            request_to_read_datamd = f'SELECT key_mod FROM Module WHERE name_mod = "{data[1]}";'
            cls.cursor.execute(request_to_read_datamd)
            datamd = cls.cursor.fetchone()            
            print('datamd', datamd)
            request_to_read_dataacc = f'SELECT isAccessOpened FROM Connect_GroupModule WHERE key_group = {datagr[0]} and key_module = {datamd[0]};'
            cls.cursor.execute(request_to_read_dataacc)
            dataacc = cls.cursor.fetchone()
            return dataacc[0]
        
    @classmethod
    def change_state(cls, data): #смена статуса доступа к модулю у группы
        if cls.isc:        
            print(data)
            request_to_read_datagr = f'SELECT key_group FROM UserGroup WHERE name_gr = "{data[0]}";'
            cls.cursor.execute(request_to_read_datagr)
            datagr = cls.cursor.fetchone()
            print('datagr', datagr)
            request_to_read_datamd = f'SELECT key_mod FROM Module WHERE name_mod = "{data[1]}";'
            cls.cursor.execute(request_to_read_datamd)
            datamd = cls.cursor.fetchone()            
            print('datamd', datamd)            
            request_to_read_dataacc = f'UPDATE Connect_GroupModule SET isAccessOpened = {data[2]} WHERE key_group = {datagr[0]} and key_module = {datamd[0]};'
            cls.cursor.execute(request_to_read_dataacc)
            cls.conn.commit()    

    @classmethod
    def load_module(cls, id): #загрузка kv-файла модул€
        if cls.isc:
            request_to_read_data = f'SELECT text_mod FROM Module WHERE id_mod = {id}'
            cls.cursor.execute(request_to_read_data)
            data = cls.cursor.fetchone()
            logging.info(f'load module is done')
            return data[0]

    @classmethod 
    def makeareq(cls, str): #дл€ любого запроса
        if cls.isc:
            res = cls.cursor.execute(f'{str}').fetchone()[0]
            return res

    @classmethod
    def FindFeat(cls, Feat_name): #дл€ поиска параметров по имени
        if cls.isc:
            result = cls.cursor.execute(
                f'select key_feat, name_feat from Feature where name_feat = "{Feat_name}"').fetchall()[0]
            return result