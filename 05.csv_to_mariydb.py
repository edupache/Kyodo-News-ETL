# Fifth Stage
# Main goal: to make the connection to the mariadb database with all the parameters needed for it. Then I create
# a table inside the 'CIP_Project' database. And finally I push the data contained in the 'Kyodo_articles_cleaned-csv'
# file into the table 'kyodo_articles'.

# Author: Eduardo Pacheco Ardon - 24.5.2022

import mariadb
import sys

# Connecting to mariadb with the needed credentials and parameters
try:
    conn = mariadb.connect(
        user='admin',
        password='$1223',
        host='localhost',
        port=3306,
        database='CIP_Project'
    )
except mariadb.Error as e:
    print(f'Error connecting to MariaDB Platform: {e}')
    sys.exit(1)

# Getting the cursor
cur = conn.cursor()

# Setting a new table in the database named 'kyodo articles'
try:
    cur.execute("CREATE OR REPLACE TABLE kyodo_articles(\
    title VARCHAR(200), datetime VARCHAR(30), description VARCHAR(400), paragraph TEXT,\
    channels VARCHAR(200), author VARCHAR(100), url VARCHAR(200), PRIMARY KEY(title));")
    print('The table was successfully created.')
except mariadb.Error as e:
    print(f'Error: {e}')

# Pushing the data from the file 'Kyodo_articles_cleaned.csv' into 'kyodo_articles' table
try:
    cur.execute("LOAD DATA LOCAL INFILE\
    '/home/student/Cloud/Owncloud/Institution/SyncVM/CIP_F22/Pycharm/CIP_Project/Kyodo_articles_cleaned.csv'\
    INTO TABLE kyodo_articles FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS\
    (title, datetime, description, paragraph, channels, author, url);")
    conn.commit()
    print('The data was successfully uploaded.')
except mariadb.Error as e:
    print(f'Error: {e}')

conn.close()





