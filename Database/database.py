import sqlite3
from database2 import Dalibai

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS sample (Firstname text, Surname text, DoB text, Occupation text, Age integer)""")
conn.commit()

# c.execute("INSERT INTO sample VALUES ('Musa', 'Haruna', '24/5/2000', 'Programmer', 21)")
# c.execute("INSERT INTO sample VALUES ('John', 'Tech', '24/5/2000', 'Manomir', 21)")
# c.execute("INSERT INTO sample VALUES ('Halima', 'Zakariyya', '24/5/2000', 'Dinki', 21)")
# c.execute("INSERT INTO sample VALUES ('Baje', 'Tech', '24/5/2000', 'Ethical Hacker', 21)")
# c.execute("INSERT INTO sample VALUES ('Yusuf', 'Mandawari', '24/5/2000', 'Tailor', 21)")
# conn.commit()

dalibi_1 = Dalibai('Bilkisu', 'Muhammad', '24/10/2000','Daliba', 21)
dalibi_2 = Dalibai('Suleiman', 'Muhammad', '24/1/2005','Dan kasuwa', 16)

c.execute("INSERT INTO sample VALUES (?, ?, ?, ?, ?)", (dalibi_1.Firstname, dalibi_1.Surname, dalibi_1.DoB, dalibi_1.Occupation, dalibi_1.Age))
conn.commit()

c.execute("INSERT INTO sample VALUES (:Firstname, :Surname, :DoB, :Occupation, :Age)", {'Firstname': dalibi_2.Firstname, 'Surname': dalibi_2.Surname, 'DoB': dalibi_2.DoB, 'Occupation': dalibi_2.Occupation, 'Age': dalibi_2.Age})
conn.commit()

c.execute("SELECT * FROM sample WHERE Surname='Muhammad' ")
print(c.fetchall())
conn.commit()
conn.close()


















































