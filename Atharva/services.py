import pymysql

class FilmOperations:
    def searchfilmsongenre(self, gen):
        dic = {}
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            curs.execute("SELECT * FROM films WHERE genre = '%s'" % gen)
            data = curs.fetchall()
            dic['searchresult'] = data
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            dic['searchresult'] = []
        finally:
            if con:
                con.close()  # Ensure the connection is always closed
        return dic

    def addnewfilmtodb(self, nm, yr, gn, ln, rt):
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            curs.execute(
                "INSERT INTO films(filmname, relyear, genre, language, imdbrating) VALUES ('%s', %d, '%s', '%s', %.1f)" %
                (nm, yr, gn, ln, rt)
            )
            con.commit()
            return 'New film added successfully'
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            return 'Error adding film'
        finally:
            if con:
                con.close()  # Ensure the connection is always closed

    def retrieveallfilmsdata(self):
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            curs.execute("SELECT * FROM films")
            data = curs.fetchall()
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            data = []
        finally:
            if con:
                con.close()  # Ensure the connection is always closed
        return data

    def findfilmsonlang(self, lang):
        dic = {}
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            curs.execute("SELECT * FROM films WHERE language = '%s'" % lang)
            data = curs.fetchall()
            dic['language'] = lang
            dic['searchresult'] = data
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            dic['searchresult'] = []
        finally:
            if con:
                con.close()  # Ensure the connection is always closed
        return dic

    def deletefilm(self, fid):
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            cnt = curs.execute("DELETE FROM films WHERE filmid = %d" % fid)
            con.commit()
            if cnt == 1:
                return "success"
            else:
                return "failed"
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            return "failed"
        finally:
            if con:
                con.close()  # Ensure the connection is always closed

    def authenticate(self, uid, psw):
        con = None  # Initialize the connection variable
        try:
            con = pymysql.connect(
                host='mysql-1a7c146b-demo07python.c.aivencloud.com',
                port=13875,
                user='avnadmin',
                password='AVNS_1oOjGTIkf6chPnto32M',
                database='demopython'
            )
            curs = con.cursor()
            curs.execute(
                "SELECT * FROM users WHERE userid = '%s' AND pswd = '%s'" % (uid, psw)
            )
            data = curs.fetchone()
            if data:
                return "success"
            else:
                return "failed"
        except pymysql.MySQLError as e:
            print(f"Error occurred: {e}")
            return "failed"
        finally:
            if con:
                con.close()  # Ensure the connection is always closed
