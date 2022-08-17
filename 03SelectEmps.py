import pymysql

con=pymysql.connect(host='bkcbsppidpkn3d1gddmo-mysql.services.clever-cloud.com',user='uvx7nsdewz01hhtf',password='MlQRAIuOANmNYCkOY6vM',database='bkcbsppidpkn3d1gddmo')
curs=con.cursor()
curs.execute("select * from emp")
data=curs.fetchall()
print(data)
con.close()