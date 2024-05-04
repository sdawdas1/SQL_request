import sqlite3

conn = sqlite3.connect('electronic_magazin.db')
cursor = conn.cursor()


cursor.execute('''

SELECT customers.customer_id, customers.first_name, customers.last_name, COUNT(orders.order_id) AS order_count
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.first_name, customers.last_name
ORDER BY customers.customer_id;
''')
sdf = cursor.fetchall()
print(sdf)

conn.commit()
conn.close()

