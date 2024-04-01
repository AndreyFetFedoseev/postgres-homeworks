import csv
import psycopg2


conn_params = {
  "host": "localhost",
  "database": "north",
  "user": "postgres",
  "password": "catonnameG@v1"
}


# with psycopg2.connect(**conn_params) as conn:
#     with conn.cursor() as cur:
#         with open('customers_data.csv', newline='') as file:
#             csv_file = csv.reader(file)
#             i = 0
#             for row in csv_file:
#                 if i != 0:
#                     print(row)
#                     cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
#                 i += 1

with psycopg2.connect(host='localhost', database='north', user='postgres', password='catonnameG@v1') as conn:
    with conn.cursor() as cur:
        # cur.execute("INSERT INTO north VALUES (%s, %s)", (1, "Test"))
        cur.execute("SELECT * FROM customers")

        rows = cur.fetchall()
        for row in rows:
            print(row)
