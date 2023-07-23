import requests
import json
import pandas as pd
from sqlalchemy import create_engine
from config import BASE_URL
import datetime

now = str(datetime.datetime.now())[:19]

def insert(table_name):
    url = f'{BASE_URL}itfcd'
    
    file_path = 'C:/app/toy/'
    file_name = '데이터.xlsx'
    df = pd.read_excel(f'{file_path}{file_name}', sheet_name=table_name)
    df['created_at'] = now
    df['updated_at'] = now
    
    print(df)
    engine = create_engine('mysql+pymysql://root:eoqkr123@localhost:3306/booksen?charset=utf8')
    conn = engine.connect()
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

if __name__ == '__main__':
    insert('complete')