from flask import Flask, render_template, request
import pypyodbc as odbc
import pandas as pd

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'}

# Server Connection 
server = 'cloudsqlserver01.database.windows.net'
database = 'DemoDB'
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:cloudsqlserver01.database.windows.net,1433;Database=DemoDB;Uid=RohithGurram;Pwd={Demodbgrr@#4};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)


@app.route('/')
def earthquakedata():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT * FROM dbo.bonusquiztb")

    #if resultValue > 0:
    data = cur.fetchall()
    return render_template('earthquakedata.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)