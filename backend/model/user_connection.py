import psycopg
import json

credentials = "/home/juan/Documentos/FastAPI_PostgreSQL/config.json"

with open(credentials, "r") as config_file:
    config = json.load(config_file)
    print(config)

dbname = config["dbname"]
user =  config["user"]
password = config["password"]
host = config["host"]
port = config["port"]

class Userconnection():
    conn = None
    def __init__(self) :
        try:
            self.conn = psycopg.connect(f"dbname={dbname} user={user} password={password} host={host} port={port}")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()
    
    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                            SELECT * FROM "user"
                        """)
            return data.fetchall()
    
    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                            SELECT * FROM "user" WHERE id = %s
                        """, (id, ))
            return data.fetchone()

 
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                            INSERT INTO "user" (name, phone) VALUES (%(name)s, %(phone)s)
                        """, data)
            self.conn.commit()
    

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                    UPDATE "user" SET name=%(name)s, phone=%(phone)s WHERE id =%(id)s
                """, data)
            self.conn.commit()

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                DELETE FROM "user" WHERE id = %s
            """, (id, ))
        self.conn.commit()
    

    def __def__(self):
        self.conn.close()
