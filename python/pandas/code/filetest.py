import os
import numpy as np
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.types import CHAR, INT

connect_info = 'mysql+pymysql://root:Zhouhao96!@localhost:3306/jeecg-boot?charset=utf8'
engine = create_engine(connect_info)  # use sqlalchemy to build link-engine


path = "D://grain//data"
files = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) ]


csvfiles = [x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x)) and os.path.splitext(x)[1] == '.csv']
excelfiles = [x for x in os.listdir(path) if
              os.path.isfile(os.path.join(path, x)) and os.path.splitext(x)[1] == '.xlsx']

for x in files:
    fpath=os.path.join(path,x)
    print(fpath)
    if os.path.splitext(x)[1] == '.csv':
        df = pd.read_csv(fpath)
    elif os.path.splitext(x)[1] == '.xlsx':
        df = pd.read_excel(fpath)
    else:
        print("其他文件类型 "+os.path.splitext(x)[1] )
        continue
    tableName = os.path.splitext(x)[0].lower()
    tableName="grain_"+tableName
    df.to_sql(name=tableName, con=engine, if_exists='replace', )




# fpath = os.path.join(path, "库区表.csv")
# df = pd.read_csv(fpath)
# print(df)
# df.to_sql(name='test1', con=engine, if_exists='append', )
