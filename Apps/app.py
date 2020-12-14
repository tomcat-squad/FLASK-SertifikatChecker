from flask import Flask, render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)

'''
DATABASE MYSQL
'''
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcat_sertifikat'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check/<int:ID>', methods=['GET'])
def check(ID):
    conn = mysql.connection
    cur = conn.cursor()
    cur.execute("SELECT * FROM validasi WHERE id=%s;" %(ID))
    result_data = cur.fetchall()
    return render_template('ajax_data.html', data=result_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')