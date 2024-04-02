import csv
import psycopg2

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "catonnameG@v1"
}


def insert_table(params, url, table):
    """
    Функция для заполнения таблиц в PostgresSQL
    """
    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            with open(url, newline='') as file:
                csv_file = csv.reader(file)
                i = 0
                for row in csv_file:
                    arguments = '%s, ' * (len(row) - 1) + '%s'
                    if i != 0:  # Для пропуска первой строки(оглавления) в файле csv
                        cur.execute(f"INSERT INTO {table} VALUES ({arguments})", row)
                    i += 1


insert_table(conn_params, 'north_data/customers_data.csv', 'customers')
insert_table(conn_params, 'north_data/employees_data.csv', 'employees')
insert_table(conn_params, 'north_data/orders_data.csv', 'orders')
