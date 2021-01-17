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


#Following method deletes a Review from Database
def deleteReviewRecord( email ):
    lines = list()
    with open('static/docs/reviews.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            if row[0] == email:
                lines.remove(row)

    with open('static/docs/reviews.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        for row in lines:
            if any(field.strip() for field in row):
                writer.writerow(row)
        