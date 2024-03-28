import MySQLdb
import json
import requests


def db_connect():
    connect = MySQLdb.connect(host='127.0.0.1', user='root', passwd='admin', db='flask')
    return connect


url = "https://us-central1-passion-fbe7a.cloudfunctions.net/dzn54vzyt5ga/orders"
headers = {
    "Authorization": "gAAAAABmAv9NX8rIApw6q-sUsLbLcrr4aWSg7QwxtcUAhJn3fK8KdiYx6nHozJkRQqabo2junrIi6gcJLwmsBCIIcW3Z4voAFO3K0CfFchhf24Yv9ea1o4-nqfklRDdn4b8hiedUPnbQuK6jrcaqFflOFUhQBQQpXQ=="
}

date = "2024-02-27"

response = requests.post(url, headers=headers, params={"date": date})
data = response.json()
print(data)
# data = response.json()

# records = data['records']
print(response.text)

# url = "https://us-central1-passion-fbe7a.cloudfunctions.net/dzn54vzyt5ga//orders"
# headers = {
#     "Authorization": "gAAAAABmAu3nKRFHOeSP_HntvgO_N6WqGGDm8v0JJVhF6nFZXVRdO6MsVd7Ur7B9xz323CDT5E0qaE-A3f17MVlVb40vxQXVE2qEOw60YjZY2BlPHjke-Pqc0YdnUtnWALrtqOq9r5N023j_zITCpxiE79MQNVgYIw=="
# }
#
#
# response = requests.post(url, headers=headers, params={"date": date})
# data = response.json()
#
# print(data)

# values_list = []
# data_list = json.loads(records)
#
# for record in data_list:
#     marketing_id = record.get("marketing_id")
#     location = record.get("name")
#     channel = record.get("channel")
#     medium = record.get("medium")
#     campaign = record.get("campaign")
#     keyword = record.get("keyword")
#     ad_content = record.get("ad_content")
#     ad_group = record.get("ad_group")
#     landing_page = record.get("landing_page")
#
#     values = (marketing_id, location, channel, medium, campaign, keyword, ad_content, ad_group, landing_page)
#     values_list.append(values)
#
# sql_query = """INSERT INTO table_costs (marketing_id, location, channel, medium, campaign, keyword, ad_content, ad_group, landing_page)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
# print(values_list)
#
#
# with db_connect() as connection:
#     with connection.cursor() as cursor:
#         cursor.executemany(sql_query, values_list)
#     connection.commit()



