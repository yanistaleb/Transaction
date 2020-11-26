import pyodbc 
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=LAPTOP-1MKAJNIV\MSSQLSERVER02;'
                        'Database=transactions_test;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()

    cursor.execute('select * from Fournisseurs')
    for row in cursor:
        print(row)

    cursor.execute("""update Fournisseurs set NomF = 'thomas',VilleF = 'Nice', AdrF= 'rue de nice',TelF = 'NNNNNNNN' where Idf = 7 """)

    conn.commit()
    cursor.execute('select * from Fournisseurs')

    for row in cursor:
        print(row)
    #conn.close()
except :
    print("Database Update Failed !: {}")
    conn.rollback()

conn.close()
