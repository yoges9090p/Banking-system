import mysql.connector


class Mybanking:
    def __init__(self,db_name):
        self.db_name = db_name
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mynewpassword',
            port= 3306,
            database=db_name
        )
        self.mycursor = self.mydb.cursor()
    def tuplefetcher(self,query):
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def tupleinserter(self,mytuple):
        self.mycursor.execute(f"INSERT INTO customer (customer_id, customer_name, customer_email, customer_phone, "
                              f"customer_dob, customer_pass,current_balance) VALUES {mytuple};")
        self.mydb.commit()

    def ifalreadytaken(self,query_name,query):
        fetcher_query = f"SELECT * FROM customer WHERE {query_name} = {query};"
        if self.tuplefetcher(fetcher_query) == []:
            return 0
        else:
            return 1

    def currentcustomerid(self):
        query =  """SELECT customer_id FROM customer ORDER BY customer_id DESC LIMIT 1;"""
        return self.tuplefetcher(query)[0][0]

    def currentbalance(self,extra_query,email_address,password):
        fetch_query = f"""SELECT {extra_query} FROM customer WHERE customer_email={email_address} AND customer_pass={password};"""
        received_output = self.tuplefetcher(fetch_query)
        if received_output == []:
            return None
        else:
            return int(self.tuplefetcher(fetch_query)[0][0])

    def updatebalance(self,current_customer_id,new_balance):
        self.mycursor.execute(f"""UPDATE customer SET current_balance = {new_balance} WHERE customer_id = {current_customer_id};""")
        self.mydb.commit()
