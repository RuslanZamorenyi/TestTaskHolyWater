import MySQLdb


def db_connect():
    connect = MySQLdb.connect(host='127.0.0.1', user='root', passwd='admin', db='flask')
    return connect

import json
import requests

url = "https://us-central1-passion-fbe7a.cloudfunctions.net/dzn54vzyt5ga/installs"
headers = {
    "Authorization": "gAAAAABmAv9NX8rIApw6q-sUsLbLcrr4aWSg7QwxtcUAhJn3fK8KdiYx6nHozJkRQqabo2junrIi6gcJLwmsBCIIcW3Z4voAFO3K0CfFchhf24Yv9ea1o4-nqfklRDdn4b8hiedUPnbQuK6jrcaqFflOFUhQBQQpXQ=="
}

date = "2024-02-26"

response = requests.post(url, headers=headers, params={"date": date})
data = response.json()

# Отримання списка записів
records = data['records']
data_list = json.loads(records)
# print(records)
for record in data_list:
    marketing_id = record.get("marketing_id")
    location = record.get("name")
    channel = record.get("channel")
    medium = record.get("medium")
    campaign = record.get("campaign")
    keyword = record.get("keyword")
    ad_content = record.get("ad_content")
    ad_group = record.get("ad_group")
    landing_page = record.get("landing_page")

    sql_query = """INSERT INTO table_costs (marketing_id, location, channel, medium, campaign, keyword, ad_content, ad_group, landing_page) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (marketing_id, location, channel, medium, campaign, keyword, ad_content, ad_group, landing_page)
    print(values)

    with db_connect().cursor() as connection:
        connection.execute(sql_query, values)
        db_connect().commit()



