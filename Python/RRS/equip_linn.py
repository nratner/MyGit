import urllib
from bs4 import BeautifulSoup



# Make some fresh tables using executescript()
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Track;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );
# ''')


fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'linnrrsdbs_subset.xml'

hand = open(fname).read()



def lookup(d, td):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'td' :
            found = True
    return None

soup = BeautifulSoup(hand, "html.parser")
all = soup.findall('tbody')
print 'Article count:', len(all)
for entry in all:
    if ( lookup(entry, 'Equipment ID:') is None ) : continue

    field = soup.find(text="Field:").child
    location = soup.find(text="Location:").child
    equipid = soup.find(text="Equipment ID:").child
    inspector = soup.find(text="Inspector:").child
    comments = soup.find(text="Comments:").child
    upipeid = soup.find(text="UltraPipe Unit ID").child
    upipecircuit = soup.find(text="UltraPipe Circuit").child


    if equipid is None :
        continue

    print equipid, upipeid, field, location, inspector, upipecircuit

    # cur.execute('''INSERT OR IGNORE INTO Artist (name)
    #     VALUES ( ? )''', ( artist, ) )
    #
    # cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    # artist_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR IGNORE INTO Genre (name)
    #            VALUES ( ? )''', (genre,))
    #
    # cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    # genre_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
    #     VALUES ( ?, ? )''', ( album, artist_id ) )
    # cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    # album_id = cur.fetchone()[0]
    #
    # cur.execute('''INSERT OR REPLACE INTO Track
    #     (title, album_id, genre_id, len, rating, count)
    #     VALUES ( ?, ?, ?, ?, ?, ? )''',
    #     ( name, album_id, genre_id, length, rating, count ) )
    #
    # conn.commit()
