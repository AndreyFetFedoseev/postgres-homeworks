import json
import sqlite3
import psycopg2

from config import config


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'my_new_db'

    params = config()

    conn = None

    create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")

                suppliers = get_suppliers_data(json_file)
                print([sup.get('products') for sup in suppliers])
                insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")

                add_foreign_keys(cur, json_file)
                print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""

    conn = psycopg2.connect(dbname='youtube', **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(f'DROP DATABASE IF EXISTS {db_name}')
    with conn.cursor() as cur:
        cur.execute(f'CREATE DATABASE {db_name}')
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""
    with open(script_file, 'r') as file:
        file_sql = file.read()
        cur.execute(file_sql)


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""
    cur.execute("""
        CREATE TABLE suppliers (
            suppliers_id SERIAL PRIMARY KEY,
            company_name VARCHAR(255),
            contact VARCHAR(255),
            address VARCHAR(255),
            phone TEXT,
            fax TEXT,
            homepage VARCHAR(255)
        )
    """)


def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    with open(json_file, 'r') as file:
        data_json = json.load(file)
        return data_json


def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""
    for sups in suppliers:
        cur.execute("""
            INSERT INTO suppliers (company_name, contact, address, phone, fax, homepage)
            VALUES (%s, %s, %s, %s, %s, %s)
        """,
                    (sups.get('company_name'), sups.get('contact'), sups.get('address'), sups.get('phone'),
                     sups.get('fax'), sups.get('homepage'))
                    )


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    with open(json_file, 'r') as f:
        data_suppliers = json.load(f)
        for supplier in data_suppliers:
            if products.product_name in [prod for prod in supplier.get('product')]:
                cur.execute("""
                ALTER TABLE products ADD CONSTRAINT fk_products_suppliers FOREIGN KEY (product_name) REFERENCES suppliers(suppliers_id)
                WHERE suppliers.company_name=  
                """)


if __name__ == '__main__':
    main()
