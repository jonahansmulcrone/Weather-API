import os
import sys
import sqlite3
import csv

"""
In this homework, you are allowed to work in pairs, please get your API ready and use it in this code.
 

# Student Name 1: Brian Sung
# Student Name 2: Emmanuel Obikwelu
# Student Name 3: Jonah Mulcrone

# Additional comment for this program, any bugs or creative functions?


"""

class saving2Database():
    """
    Feel free to add more methods in this class
    
    """
    def __init__(self, keyWord, recordLimit, output):
        """
        This is the constructor, you can initialize any objects here
        keyWord would be the topic you are going to search through the database, it can be a list if you want to search multiple topics
        recordLimit is used for testing, if you want your program quit once you reach the recordLimit of database. Don't forget the close and save your data into the database. If it is -1, your program will keep running, but you should save your data every 1000 records, just in case your data gets lost
        output would be the path of your sqlite3 database and the data will be saved there
        """
        # set up the mysqlite3 db connection 
        con = sqlite3.connect(output)
        cur = con.cursor()


        # initialize the table for the database
        self.initTable()
        for row in cur.execute('SELECT * FROM weather WHERE city = ?', (keyWord,)):
            print(row)
        con.commit()  # save (commit) the changes
        con.close()
        pass
    
    def initTable(self):
        """
        Discuss and think about what kind of table you want to create for your database, like the weather, the location, and others? also think about the size of the column, you may need to find out the maximum length for each feature
        """

        con = sqlite3.connect('weather.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE Weather (city text, time text,  temperature text, humidity text, wind_speed text, wind_deg text, visibility text)''')


        with open('weather_data.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO Weather VALUES (?, ?, ?, ?, ?, ?, ?)",(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        con.commit()
        con.close()
        pass

 

# example code that you can run and test 
# for testing you can use 1000, and the topic can be different
key = sys.argv[1]
myt = saving2Database(key, 1000, "weather.db")
#print(myt)