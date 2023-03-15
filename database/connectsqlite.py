import sys
import os
import sqlite3

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
sys.path.append("..")


class ConnectSqlite:

    def __init__(self, dbName):
        """
        初始化连接--使用完记得关闭连接
        :param dbName: 连接库名字，注意，以'.db'结尾
        """
        self._conn = sqlite3.connect(dbName)
        self._cur = self._conn.cursor()
        self._time_now = "[" + sqlite3.datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S') + "]"

    def close_con(self):
        """
        关闭连接对象--主动调用
        :return:
        """
        self._cur.close()
        self._conn.close()

    def create_tabel(self, sql):
        """
        创建表初始化
        :param sql: 建表语句
        :return: True is ok
        """
        try:
            self._cur.execute(sql)
            self._conn.commit()
            return True
        except Exception as e:
            print(self._time_now, "[CREATE TABLE ERROR]", e)
            return False

    def drop_table(self, table_name):
        """
        删除表
        :param table_name: 表名
        :return:
        """
        try:
            self._cur.execute('DROP TABLE {0}'.format(table_name))
            self._conn.commit()
            return True
        except Exception as e:
            print(self._time_now, "[DROP TABLE ERROR]", e)
            return False

    def fetchall_table(self, sql, limit_flag=True):
        """
        查询所有数据
        :param sql:
        :param limit_flag: 查询条数选择，False 查询一条，True 全部查询
        :return:
        """
        try:
            self._cur.execute(sql)
            war_msg = self._time_now + ' The [{}] is empty or equal None!'.format(sql)
            if limit_flag is True:
                r = self._cur.fetchall()
                return r if len(r) > 0 else None
            elif limit_flag is False:
                r = self._cur.fetchone()
                return r if len(r) > 0 else None
        except Exception as e:
            print(self._time_now, "[SELECT TABLE ERROR]", e)

    def insert_facedata_table(self, insert_list):
        """
        插入/更新表记录
        :param insert_list:
        :return:0 or err
        """
        try:
            sql = "INSERT INTO face_data (id,name,face_img,change_time,label) values (NULL,?,?,?,?);"
            print(sql)
            self._cur.execute(sql,insert_list)
            self._conn.commit()
            return 0
        except Exception as e:
            err = self._time_now + "[INSERT/UPDATE TABLE ERROR]"+ str(e)
            print(err)
            return err

    def insert_checkin_table(self, insert_list):
        """
        插入/更新表记录
        :param insert_list:
        :return:0 or err
        """
        try:
            sql = "INSERT INTO re_record (student_id,name,checkin_time,id) values (?,?,?,NULL);"
            print(sql)
            self._cur.execute(sql, insert_list)
            self._conn.commit()
            return 0
        except Exception as e:
            err = self._time_now + "[INSERT/UPDATE TABLE ERROR]" + str(e)
            print(err)
            return err

    def return_all_face(self):
        sql = """SELECT * FROM face_data;"""

        face_data = self.fetchall_table(sql)
        face_list = []
        if face_data != None:
            for i in face_data:
                face_list.append(i)
            return face_list
        else:
            return face_list

    def return_all_checkin_record(self):
        sql = """SELECT * FROM re_record;"""

        face_data = self.fetchall_table(sql)
        check_list = []
        if face_data != None:
            for i in face_data:
                check_list.append(i)
            return check_list
        else:
            return check_list

    def return_all_sid(self):
        sql = """SELECT student_id FROM face_data;"""

        student_id = self.fetchall_table(sql)
        id_list = []
        if student_id != None:
            for i in student_id:
                id_list.append(str(i[0]))
            return id_list
        else:
            return id_list

    def return_face_photo(self):
        sql = """SELECT face_img FROM face_data;"""

        face_img = self.fetchall_table(sql)
        face_list = []
        for i in face_img:
            face_list.append(i[0])
        return face_list

    def insert_table_many(self, sql, value):
        """
        插入多条记录
        :param sql:
        :param value: list:[(),()]
        :return:
        """
        try:
            self._cur.executemany(sql, value)
            self._conn.commit()
            return True
        except Exception as e:
            print(self._time_now, "[INSERT MANY TABLE ERROR]", e)
        return False

    # 载入已录入信息的函数
    def load_registered_data(self):

        sql = """SELECT student_id,name,face_data FROM face_data;"""

        info = self.fetchall_table(sql)
        if info != None:
            student_info_all = []
            for i in info:
                face_data = i[2]
                face_data = list(map(float, face_data.split('\n')))
                # print(len(face_data))
                student_info = {'sid': i[0], 'name': i[1], 'feature': face_data}
                student_info_all.append(student_info)
            return student_info_all
        else:
            return None
        

    def insert_update_table(self, sql):
        """
        插入/更新表记录
        :param sql:
        :return:
        """
        try:
            self._cur.execute(sql)
            self._conn.commit()
            return 0
        except Exception as e:
            err = self._time_now + "[INSERT/UPDATE TABLE ERROR]" + str(e)
            print(err)
            return err

    def update_face_table(self,modify_list):
        print(modify_list)
        sql_update = "UPDATE face_data SET student_id='{0}',name='{1}' WHERE id={2}".format(modify_list[0],modify_list[1], modify_list[2])
        print(sql_update)
        return self.insert_update_table(sql_update)

    def update_checkin_table(self, modify_list,id):
        print(modify_list)
        sql_update = "UPDATE re_record SET name='{0}',student_id='{1}',checkin_time='{2}' WHERE id={3}".format(modify_list[0], modify_list[1], modify_list[2], id)


        print(sql_update)
        return self.insert_update_table(sql_update)

    def delete_table(self, sql):
        """
        删除表记录
        :param sql:
        :return: True or False
        """
        try:
            if 'DELETE' in sql.upper():
                self._cur.execute(sql)
                self._conn.commit()
                return 0
            else:
                err = self._time_now + "[EXECUTE SQL IS NOT DELETE]"
                return err
        except Exception as e:
            err = self._time_now + "[DELETE TABLE ERROR]" + str(e)
            return err

    def delete_face_table(self,id):
        sql = "DELETE FROM face_data WHERE id='{0}';".format(id)
        return self.delete_table(sql)

    def delete_checkin_table(self,id):
        sql = "DELETE FROM re_record WHERE id='{0}';".format(id)
        print(sql)
        return self.delete_table(sql)