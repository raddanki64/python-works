from flask import Response
import json
import boto3

from empservice import app
from empservice import log

@app.route('/cities', methods=['GET'])
def get_all_cities():
    reply = Response()
    reply.headers["Access-Control-Allow-Origin"] = "*"
    reply.status = 200
    reply.content_type = 'application/json'

#client = boto3.client('DynamoDB', aws_access_key_id='ny5xji', aws_secret_access_key='ld3eff', region_name='***')


    ddb = boto3.resource('dynamodb',
                        region_name='us-east-1',
                        aws_access_key_id="AKIAQWKJFYS2Q6NBMIWH",
                        aws_secret_access_key="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")

    print(list(ddb.tables.all()))
    log.info("Established dynamo boto resource")





    #cities = ddb.Table('MiddlesexCounty')
    #print(cities.creation_date_time)


#cursor = client.cursor()
#cursor.execute("SELECT * FROM public.\"Employees\" ORDER BY id ASC;")
#records = cursor.fetchall()

#print("Total rows are:  ", len(records))

    reply.response = json.dumps("connected to cloud dynamodb")
#cursor.close()

    return reply
