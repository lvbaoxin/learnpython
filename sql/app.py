import pymysql


def connect_db():
    db = pymysql.connect(host='localhost', user="root", password='745458741', charset='utf8')
    cursor = db.cursor()
    cursor.execute('select version()')
    data = cursor.fetchone()

    print('数据库版本为{}'.format(data))
    db.close()


def create_db():
    db = pymysql.connect(host='localhost', user='root', password='745458741', charset='utf8')
    cursor = db.cursor()
    cursor.execute('create database if not EXISTS pythontest')
    db.close()


def create_table():
    db = pymysql.connect(host="localhost", user='root', password='745458741', database='pythontest', charset='utf8')
    cursor = db.cursor()
    cursor.execute('drop table if exists student')
    sql = '''
    create table student(
    id int PRIMARY KEY,
    name char(20) not null,
    age int,
    sex char(1),
    class int
    )
    '''
    cursor.execute(sql)
    db.close()


def insert_db():
    db = pymysql.connect(host='localhost', user='root', password='745458741', database='pythontest', charset='utf8')
    cursor = db.cursor()
    sql = "insert into student(id,name,age,sex,class)" \
          "values(%s,'%s',%s,'%s',%s)" % (3, 'wangwu', 22, 'M', 1)
    cursor.execute(sql)
    db.commit()
    db.close()



if __name__ == '__main__':
    insert_db()
