import csv
import psycopg2


conn_params = {
  "host": "localhost",
  "database": "north",
  "user": "postgres",
  "password": "catonnameG@v1"
}


with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('customers_data.csv', newline='') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                cur.execute("INSERT INTO north VALUES (%s, %s, %s)", row)
