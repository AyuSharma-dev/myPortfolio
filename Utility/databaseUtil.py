import csv

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


##Following method updates the Password for username ( Not in use )
#def updateData( newPassword, username ):
    


##Following method inserts the Reviews in database
def insertData( review ):
    with open('static/docs/reviews.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow( review )


##Following method queries the Auth values from Database
def getUserPass():
    with open('static/docs/auth.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        auth = authObj( list(reader)[0] )
        return auth


##Following method queries the Reviews from Database
def queryData():
    with open('static/docs/reviews.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        reviews = []
        idNum = 0
        for row in reader:
            print('row')
            row += idNum,
            reviews.append( reviewObj( row ) )
            idNum += 1
        return reviews


##Following method deletes a Review from Database
# def deleteReviewRecord( email ):
#     sql = 'DELETE FROM reviews WHERE Email = ?;'
#     conn = sqlite3.connect( 'database\database.db' )
#     c = conn.cursor()
#     c.execute( sql, (email,) )
#     conn.commit()
    