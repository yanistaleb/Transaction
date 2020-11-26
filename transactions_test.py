import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-1MKAJNIV\MSSQLSERVER02;'
                      'Database=transactions_test;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute('select * from Fournisseurs')
for row in cursor:
    print(row)

####################TRANSACTION####################
cursor.execute("""update Fournisseurs set NomF = 'Jhon',VilleF = 'Nen-York', AdrF= 'BRONX',TelF = 'OOOOOOOO' where Idf = 4 """)
cursor.execute("""update Fournisseurs set NomF = 'David',VilleF = 'los-Angeles',AdrF = 'beverly-hills',TelF = 'MMMMMMMM' where Idf = 5 """)
cursor.execute("""update Fournisseurs set NomF = 'Lewis',VilleF = 'Tizi-Ouzou',AdrF = 'Boghni',TelF = 'PPPPPPPP'  where Idf = 6 """)
conn.commit()
cursor.execute('select * from Fournisseurs')
print('______________________________________________________________')

for row in cursor:
    print(row)
conn.close()
