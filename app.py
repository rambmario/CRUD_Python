from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL

app=Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = '192.168.64.2'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema2122'
mysql.init_app(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')

    sql="INSERT INTO `empleados`(`id`, `nombre`, `correo`, `foto`) VALUES (NULL,'mario','mario@gmail.com','foto.jpg')"
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    return render_template('empleados/index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)

