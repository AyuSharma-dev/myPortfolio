import sqlite3

class reviewObj:
    def __init__(self, data):
        print(data[0])
        self.email = data[0]
        self.name = data[1]
        self.title = data[2]
        self.review = data[3]
        self.image = data[4]

def createTable():
    sql_create_review_table = """ CREATE TABLE IF NOT EXISTS reviews (
                                    Email text PRIMARY KEY,
                                    Name text NOT NULL,
                                    Title text NOT NULL,
                                    Review text NOT NULL,
                                    Image text
                                    ); """

def updateData():
    sql = ''' UPDATE reviews
              SET image = ?
              WHERE email = ?'''
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, review )
    c.commit()

def insertData( review ):
    sql = ''' INSERT INTO reviews(Name,Email,Title,Review,Image)
              VALUES(?,?,?,?,?) '''
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, review )
    conn.commit()


def queryData():
    conn = sqlite3.connect( 'database\database.db' )
    print(conn)
    sql = 'SELECT * FROM reviews'
    c = conn.cursor()
    print(c)
    c.execute(sql)
    rows = c.fetchall()
    reviews = [] 
    for row in rows:
        reviews.append( reviewObj( row ) )
    return reviews
