#Importing required packages
import pypyodbc as odbc
import pandas as pd
from credentials import username, password

# Server Connection 
server = 'cloudsqlserver01.database.windows.net'
database = 'DemoDB'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cloudsqlserver01.database.windows.net,1433;Database=DemoDB;Uid=RohithGurram;Pwd={Demodbgrr@#4};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)

# Data Retrieval
sql = '''
    SELECT * FROM dbo.bonusquiztb where id = 'us6000jp76';
'''
cursor = conn.cursor()
cursor.execute(sql)
dataset = cursor.fetchall()
print(dataset)

columns = [column[0] for column in cursor.description] 
df = pd.DataFrame(dataset, columns=columns)
print(df)

for x in dataset:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_html('templates/base.html')