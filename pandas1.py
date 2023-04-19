from app import app
from config import  mysql
from flask import flash, request ,Response ,render_template , url_for , send_file
import pandas as pd
   
@app.route('/pandas1')
def my_functions():
    try:
        conn = mysql.connect()

        #cursor = conn.cursor(pymysql.cursors.DictCursor)
        #cursor.execute ('select * from students')
        #data = cursor.fetchall()

        query = 'select * from students'
        my_data=pd.read_sql(query , conn)

        print(f"My Data : {my_data}") 
        return f"File downloaded {my_data.to_excel('my_filepanda21.xlsx')}"
    except Exception as e:
        return f"There is an Error {e}"
 
if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))