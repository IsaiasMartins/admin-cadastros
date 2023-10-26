import mysql.connector
from dotenv import load_dotenv
import os

def connect_mysql_dev():

    load_dotenv()

    con = mysql.connector.connect(
        host=os.environ['HOST'],
        database=os.environ['DATABASE'],
        user=os.environ['USER'],
        password=os.environ['PASSWORD']
    )
    
    return con