import sqlite3

sql_create_review_table = """ CREATE TABLE IF NOT EXISTS reviews (
                                    Email text PRIMARY KEY,
                                    Name text NOT NULL,
                                    Title text NOT NULL,
                                    Company text NOT NULL,
                                    Review text NOT NULL,
                                    Image text
                                ); """

sql_create_auth_table = """ CREATE TABLE IF NOT EXISTS auth (
                                    Username text PRIMARY KEY,
                                    Password_hash text NOT NULL
                                    ); """

conn = sqlite3.connect( 'database\database.db' )
c = conn.cursor()
c.execute( sql_create_review_table )
c.execute( sql_create_auth_table )
conn.commit()
