import psycopg2
import random

def inject_data(name='Nik'):
    conn_fly = psycopg2.connect("dbname='fly' host='localhost' user='postgres' password='somePassword'")
    conn_hotel = psycopg2.connect("dbname='hotel' host='localhost' user='postgres' password='somePassword'")
    conn_account = psycopg2.connect("dbname='account' host='localhost' user='postgres' password='somePassword'")

    this_id = random.randint(0, 100)
    conn_fly.tpc_begin(conn_fly.xid(this_id, 'transaction', 'conn fly'))
    conn_hotel.tpc_begin(conn_hotel.xid(this_id, 'transaction ID', 'conn hotel'))
    conn_account.tpc_begin(conn_account.xid(this_id, 'transaction ID', 'conn account'))

    curr_fly = conn_fly.cursor()
    curr_hotel = conn_hotel.cursor()
    curr_account = conn_account.cursor()

    curr_fly.execute("""INSERT INTO booking(booking_id, client_name, fly_number, "from", "to", date) VALUES (%s, %s, %s, %s, %s, %s);""",
                     (random.randint(0, 1000), name, 'KLM 1382', 'KBP', 'AMS', '01/05/2015'))
    curr_hotel.execute("""INSERT INTO booking(booking_id, client_name, hotel_name, arrival, departure) VALUES (%s, %s, %s, %s, %s);""",
                       (random.randint(0, 1000), name, 'Hilton', '01/05/2015', '07/05/2015'))
    curr_account.execute("UPDATE account SET amount = amount - 100 WHERE client_name=%s", (name, ))

    try:
        conn_fly.tpc_prepare()
        conn_hotel.tpc_prepare()
        conn_account.tpc_prepare()
    except psycopg2.DatabaseError as e:
        print('error', e)
        conn_fly.tpc_rollback()
        conn_hotel.tpc_rollback()
        conn_account.tpc_rollback()
    else:
        print('finished')
        conn_fly.tpc_commit()
        conn_hotel.tpc_commit()
        conn_account.tpc_commit()

    conn_fly.close()
    conn_hotel.close()
    conn_account.close()
if __name__ == "__main__":
    inject_data()