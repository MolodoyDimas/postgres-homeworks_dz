import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='65900')
try:
    with conn:
        with conn.cursor() as cur:
            with open('../homework-1/north_data/orders_data.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                for row in reader:
                    cur.execute(f'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (row[0],
                                                                                    row[1],
                                                                                    row[2],
                                                                                    row[3],
                                                                                    row[4]))
                cur.execute('SELECT * FROM orders')
                # data = cur.fetchall()
                # for x in data:
                # print(x)
finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='65900')
try:
    with conn:
        with conn.cursor() as cur:
            with open('../homework-1/north_data/employees_data.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                for row in reader:
                    cur.execute(f'INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', (row[0],
                                                                                           row[1],
                                                                                           row[2],
                                                                                           row[3],
                                                                                           row[4],
                                                                                           row[5]))
                cur.execute('SELECT * FROM employees')
                # data = cur.fetchall()
                # for x in data:
                # print(x)
finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='65900')
try:
    with conn:
        with conn.cursor() as cur:
            with open('../homework-1/north_data/customers_data.csv', 'r', encoding='utf-8') as csvfile:
                with open('../homework-1/north_data/orders_data.csv', 'r', encoding='utf-8') as csvfile2:
                    reader = csv.reader(csvfile)
                    next(reader)
                    for row in reader:
                        csvfile2.seek(0)
                        reader2 = csv.reader(csvfile2)
                        next(reader2)
                        for x in reader2:
                            if row[0] in x:
                                cur.execute(f'INSERT INTO customers VALUES (%s, %s, %s, %s)', (row[0],
                                                                                               row[1],
                                                                                               row[2],
                                                                                               x[0]))

                cur.execute('SELECT * FROM customers')
                data = cur.fetchall()
                for x in data:
                    print(x)
finally:
    conn.close()
