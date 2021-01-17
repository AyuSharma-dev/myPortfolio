import sqlite3

##Review class with all required Fields
class reviewObj:
    def __init__(self, data):
        print(data[0])
        self.email = data[0]
        self.name = data[1]
        self.title = data[2]
        self.company = data[3]
        self.review = data[4]
        self.image = data[5]
        self.id = data[6]


##Auth object class with Username and Password fields
class authObj:
    def __init__(self, data):
        self.username = data[0]
        self.password = data[1]


##Following method creates the Reviews datatable ( Used once )
def createTable():
    sql_create_review_table = """ CREATE TABLE IF NOT EXISTS reviews (
                                    Email text PRIMARY KEY,
                                    Name text NOT NULL,
                                    Title text NOT NULL,
                                    Company text NOT NULL,
                                    Review text NOT NULL,
                                    Image text
                                    ); """
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql_create_review_table )
    conn.commit()


##Following method creates the Auth datatable ( Used once )
def createAuthTable():
    sql_create_auth_table = """ CREATE TABLE IF NOT EXISTS auth (
                                    Username text PRIMARY KEY,
                                    Password_hash text NOT NULL
                                    ); """
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql_create_auth_table )
    conn.commit()


##Following method inserts the username and password values( Used once )
def insertUserNamePassword():
    sql = ''' INSERT INTO auth(Username,Password_hash)
              VALUES(?,?) '''
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, ( 'portfolioUser@sf.com', "b'gAAAAABgAr08c0VWa5WMAnI3smwOOelf1qmr8S-cMPatfNf22lHvHyZVPGYA3AKnr9HWmPhp4C8D2UNxIf67Nuw0f9OVqENxvw=='" ) )
    conn.commit()


##Following method updates the Password for username ( Not in use )
def updateData( newPassword, username ):
    sql = ''' UPDATE auth
              SET Password_hash = ?
              WHERE Username = ?'''
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, (newPassword, username) )
    conn.commit()


##Following method inserts the Reviews in database
def insertData( review ):
    sql = ''' INSERT INTO reviews(Name,Email,Title,Company,Review,Image)
              VALUES(?,?,?,?,?,?) '''
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, review )
    conn.commit()


##Following method queries the Auth values from Database
def getUserPass():
    conn = sqlite3.connect( 'database\database.db' )
    sql = 'SELECT * FROM auth'
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    auth = authObj( rows[0] )
    return auth


##Following method queries the Reviews from Database
def queryData():
    conn = sqlite3.connect( 'database\database.db' )
    sql = 'SELECT * FROM reviews'
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    reviews = [] 
    l = list(range(0, len(rows) ))
    for row in rows:
        if l:
            row += l.pop(),
        reviews.append( reviewObj( row ) )
    return reviews


##Following method deletes a Review from Database
def deleteReviewRecord( email ):
    sql = 'DELETE FROM reviews WHERE Email = ?;'
    conn = sqlite3.connect( 'database\database.db' )
    c = conn.cursor()
    c.execute( sql, (email,) )
    conn.commit()
    