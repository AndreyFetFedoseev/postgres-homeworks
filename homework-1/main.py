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
        with open('north_data/customers_data.csv', newline='') as file:
            csv_file = csv.reader(file)
            i = 0
            for row in csv_file:
                if i != 0:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
                i += 1

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', newline='') as file:
            csv_file = csv.reader(file)
            i = 0
            for row in csv_file:
                if i != 0:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
                i += 1

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('north_data/orders_data.csv', newline='') as file:
            csv_file = csv.reader(file)
            i = 0
            for row in csv_file:
                if i != 0:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", row)
                i += 1
