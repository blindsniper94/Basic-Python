import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT)")
    conn.commit()
conn.close()


import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT,\
        col_filetype TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('drill.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for file in fileList:
    if file.endswith(".txt"):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files( col_filename ) VALUES (?)", (file,))
            conn.commit()
conn.close()



