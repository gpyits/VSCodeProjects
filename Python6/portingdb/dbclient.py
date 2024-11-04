from configparser import ConfigParser
import psycopg2

def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

conn = None


def connect():
    """ Connect to the PostgreSQL database server """
    print('Connecting to the PostgreSQL database 0...')
    global conn
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        return cur

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def write_in_db(cur,sql_insert):
    global conn
    try:
        cur.execute(sql_insert)
        # commit the changes to the database
        conn.commit()
        return 0
    except (Exception, psycopg2.DatabaseError) as error:
    #except Exception as error:
        #print("Inizio:")
        #print(error)
        sError = str(error)
        #print("Fine:")
        if sError.startswith("duplicate key value "):
            print("Duplicate key, vado avanti")
            conn.rollback()
            return -2
        cur = None
        conn = None
        print(sError)
        return -1

#La funzione torna -1 se è andata male e numero di righe se va bene
def read_in_db(cur,sql_select):
    try:
        cur.execute(sql_select)
        print("The number of parts: ", cur.rowcount)
        return cur.rowcount
        #row = cur.fetchone()

        #while row is not None:
        #    print(row)
        #    row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:

        cur = None
        conn = None
        return -1

def read_next_row(cur):
    try:
        row = cur.fetchone()
        return [0,row]
    except:
        cur = None
        conn = None
        return [1,None]

def close(cur):
    global conn
    try:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        cur = None
        conn = None


#usage
if __name__ == '__main__':
    cur = connect()
    sql_insert = "insert into ordini values "
    dati = "(1200,'10489434', '85048', '15CM CHRISTMAS GLASS BALL 20 LIGHTS', 12, TO_DATE('2009/12/03','YYYY/MM/DD'), 6.95, 13085, 'United Kingdom', '07:45');"
    sql_insert += dati
    write_in_db(cur, sql_insert)
    read_in_db(cur, "select * from ordini;")
    close(cur)