import sqlite3
try:
	times = int(raw_input('How many cities do you want to see?\n'))
except ValueError,e:
	print 'This error has been launched:\n'+str(e)
	exit()
cities = []
for i in range(times):
  city = raw_input("Add the city:")
  cities.append(city)
print cities

# save cities in database
conn = sqlite3.connect('myPlaces.sqlite')
cur = conn.cursor()
conn.text_factory = str
cur.execute('''CREATE TABLE IF NOT EXISTS Cities
  (name TEXT UNIQUE)''')
#INTEGER PRIMARY KEY AUTOINCREMENT

for elem in cities:
	cur.execute('INSERT OR IGNORE INTO Cities(name) VALUES(?)',(elem,) )

conn.commit()

cur.execute('SELECT DISTINCT name FROM Cities')
rows = cur.fetchall()
cur.close()
print '\n'
print rows
print rows[1][0]

fhand = open('myPlaces.js','w')
fhand.write("cities = [ ['City','Name']")


for elem in rows:
  fhand.write(",\n['"+elem[0]+"','"+elem[0]+"']")
fhand.write('];')
fhand.close()