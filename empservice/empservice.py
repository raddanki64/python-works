from flask import Flask
from flask import Response
from flask import request, jsonify
from functools import wraps
import json
import psycopg2
import logging
import os


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger("my-logger")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'


import cityservice


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

log.info("Connected to the database")


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            #data = jwt.decode(token, app.config['SECRET_KEY'])
            #current_user = Users.query.filter_by(public_id=data['public_id']).first()
            current_user = "joe"
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator


@app.route('/employees', methods=['GET'])
#@token_required
def get_all_employess():
    reply = Response()
    reply.headers["Access-Control-Allow-Origin"] = "*"
    reply.status = 200
    reply.content_type = 'application/json'

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.\"Employees\" ORDER BY id ASC;")
    records = cursor.fetchall()

    print("Total rows are:  ", len(records))

    reply.response = json.dumps(records)
    cursor.close()

    return reply


@app.route('/employee', methods=['POST'])
def add_employee():
    print(request.data)
        
    reply = Response()
    reply.headers["Access-Control-Allow-Origin"] = "*"
    reply.status = 200
    reply.content_type = 'application/json'

    insert_stmt = "INSERT INTO public.\"Employees\" (id, first_name, last_name) VALUES (%s,%s,%s)"
    record_to_insert = (request.json['id'], request.json['first_name'],  request.json['last_name'])

    cursor = conn.cursor()
    cursor.execute(insert_stmt, record_to_insert)

    conn.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into Employees table")
    
    return reply


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()