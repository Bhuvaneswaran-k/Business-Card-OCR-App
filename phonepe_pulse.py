import glob
import pandas as pd
import re
from sqlalchemy import create_engine
import streamlit as st
import mysql.connector

mydatabase=mysql.connector.connect(
host="localhost",
user="root",
port="3306",
password="",
)
mycursor= mydatabase.cursor(buffered=True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_pulse")
mydatabase.commit()
mycursor.close()

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="",
                               db="12345"))


def aggtransyear():
    for i in path:
        DF = pd.read_json(i)
        j = DF.loc["transactionData", "data"]
        j = pd.json_normalize(j, record_path=['paymentInstruments'], meta=["name"])
        result = re.search(r'\d{4}', i)
        j["Year"] = result.group()
        splt_lst = i.split("\\")
        for x in splt_lst:
            result = re.search(r'.json$', x)
            if result != None:
                x = x.split(".")
                j["Quater"] = x[0]
        global agg_yr
        agg_yr = pd.concat([agg_yr, j], ignore_index=True)


def aggtransstate():
  for i in path:
    DF = pd.read_json(i)
    j = DF.loc["transactionData","data"]
    j = pd.json_normalize(j,record_path=['paymentInstruments'],meta=["name"])
    result = re.search(r'\d{4}',i)
    j["Year"] = result.group()
    splt_lst = i.split("\\")
    j["State"]= splt_lst[13]
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        j["Quater"] = x[0]
        global agg_state
    agg_state = pd.concat([agg_state,j],ignore_index=True)


def agguseryear():
  for i in path:
    DF = pd.read_json(i)
    b = DF.loc["usersByDevice","data"]
    if b == None:
      continue
    b = pd.json_normalize(b)
    c = DF.loc["aggregated","data"]
    if c == None:
      continue
    c = pd.json_normalize(c)
    result = re.search(r'\d{4}',i)
    b["Year"] = c["Year"]= result.group()
    splt_lst = i.split("\\")
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        b["Quater"] = c["Quater"] = x[0]
    output = pd.concat([b,c])
    global user_data_year
    user_data_year = pd.concat([user_data_year,output],ignore_index=True)


def agguserstate():
  for i in path:
    DF = pd.read_json(i)
    b = DF.loc["usersByDevice","data"]
    if b == None:
      continue
    b = pd.json_normalize(b)
    c = DF.loc["aggregated","data"]
    if c == None:
      continue
    c = pd.json_normalize(c)
    result = re.search(r'\d{4}',i)
    b["Year"] = c["Year"]= result.group()
    splt_lst = i.split("\\")
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        b["Quater"] = c["Quater"] = x[0]
    output = pd.concat([b,c])
    global user_state
    user_state = pd.concat([user_state,output],ignore_index=True)


def mapyear():
  for i in path:
   DF = pd.read_json(i)
   a = DF.loc["hoverDataList","data"]
   a = pd.json_normalize(a, record_path=["metric"],meta=["name"])
   a.columns = ["Type","Count","Amount","City"]
   result = re.search(r'\d{4}',i)
   a["Year"] = result.group()
   splt_lst = i.split("\\")
   for x in splt_lst:
     result = re.search(r'.json$',x)
     if result != None:
       x = x.split(".")
       a["Quater"] = x[0]
       global map_yr
   map_yr = pd.concat([map_yr,a],ignore_index=True)


def mapstate():
  for i in path:
    DF = pd.read_json(i)
    a = DF.loc["hoverData","data"]
    a = pd.DataFrame(a)
    a = a.transpose()
    a.reset_index(inplace=True)
    a.columns=["City","RegUser","AppOpens"]
    result = re.search(r'\d{4}',i)
    a["Year"] = result.group()
    splt_lst = i.split("\\")
    a["State"] = splt_lst[14]
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"] = x[0]
        global map_state
    map_state = pd.concat([map_state,a],ignore_index=True)


def mapuseryr():
  for i in path:

    DF = pd.read_json(i)

    a = DF.loc["hoverData","data"]
    a = pd.DataFrame(a)
    a = a.transpose()
    a.reset_index(inplace=True)
    a.columns=["City","RegUser","appopens"]
    result = re.search(r'\d{4}',i)
    a["Year"] = result.group()
    splt_lst = i.split("\\")
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"] = x[0]
        global map_user_yr
    map_user_yr = pd.concat([map_user_yr,a],ignore_index=True)


def toptransyear():
  for i in path:
    DF = pd.read_json(i)
    a = DF.loc["districts","data"]
    a = pd.json_normalize(a)
    a.columns = ["Districts","Total","Count","Amount"]
    b = DF.loc["pincodes","data"]
    b= pd.json_normalize(b)
    b.columns = ["Pincode","Total","Count","Amount"]
    c = DF.loc["states","data"]
    c = pd.json_normalize(c)
    c.columns=["State","Total","Count","Amount"]
    result = re.search(r'\d{4}',i)
    a["Year"] = b["Year"] = c["Year"]= result.group()
    splt_lst = i.split("\\")
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"] = b["Quater"] = c["Quater"] = x[0]
    output = pd.concat([a,b,c])
    global top_trans_year
    top_trans_year = pd.concat([top_trans_year,output],ignore_index=True)


def toptransstate():
  for i in path:
    DF = pd.read_json(i)
    a = DF.loc["districts","data"]
    a = pd.json_normalize(a)
    a.columns = ["Districts","Total","Count","Amount"]
    b = DF.loc["pincodes","data"]
    b= pd.json_normalize(b)
    b.columns = ["Pincode","Total","Count","Amount"]
    result = re.search(r'\d{4}',i)
    a["Year"] = b["Year"] = result.group()
    splt_lst = i.split("\\")
    a["State"] = b["State"]= splt_lst[13]
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"] = b["Quater"] = x[0]
    output = pd.concat([a,b])
    global top_trans_state
    top_trans_state = pd.concat([top_trans_state,output],ignore_index=True)


def topuseryear():

  for i in path:
    DF = pd.read_json(i)
    a = DF.loc["districts","data"]
    a = pd.DataFrame(a)
    a.columns = ["District","DistrictRegUser"]
    b = DF.loc["pincodes","data"]
    b= pd.DataFrame(b)
    b.columns = ["Pincode","PincodeRegUser"]
    c = DF.loc["states","data"]
    c = pd.DataFrame(c)
    c.columns=["State","StateRegUser"]
    result = re.search(r'\d{4}',i)
    a["Year"] = b["Year"] = c["Year"]= result.group()
    splt_lst = i.split("\\")
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"]=b["Quater"] = c["Quater"] = x[0]
    output = pd.concat([a,b,c])
    global top_user_year
    top_user_year = pd.concat([top_user_year,output],ignore_index=True)


def topuserstate():
  for i in path:
    DF = pd.read_json(i)
    a = DF.loc["districts","data"]
    a = pd.DataFrame(a)
    a.columns = ["District","DistrictRegUser"]
    b = DF.loc["pincodes","data"]
    b= pd.DataFrame(b)
    b.columns = ["Pincode","PincodeRegUser"]
    result = re.search(r'\d{4}',i)
    a["Year"] = b["Year"] = result.group()
    splt_lst = i.split("\\")
    a["State"] = b["State"]= splt_lst[13]
    for x in splt_lst:
      result = re.search(r'.json$',x)
      if result != None:
        x = x.split(".")
        a["Quater"] = b["Quater"] = x[0]
    output = pd.concat([a,b])
    global top_user_state
    top_user_state = pd.concat([top_user_state,output],ignore_index=True)

path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\aggregated\transaction\country\india\*\*.json", recursive = True)
agg_yr = pd.DataFrame()
aggtransyear()

path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\aggregated\transaction\country\india\state\*\*\*.json", recursive = True)
agg_state = pd.DataFrame()
aggtransstate()

path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\aggregated\user\country\india\*\*.json", recursive = True)
user_data_year=pd.DataFrame()
agguseryear()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\aggregated\user\country\india\state\*\*\*.json", recursive = True)
user_state=pd.DataFrame()
agguserstate()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\map\transaction\hover\country\india\*\*.json", recursive = True)
map_yr=pd.DataFrame()
mapyear()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\map\transaction\hover\country\india\state\*\*\*.json", recursive = True)
map_yr=pd.DataFrame()
mapyear()
map_trans_state=map_yr



path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\map\user\hover\country\india\*\*.json", recursive = True)
map_user_yr=pd.DataFrame()
mapuseryr()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\map\user\hover\country\india\state\*\*\*.json", recursive = True)
map_state=pd.DataFrame()
mapstate()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\top\transaction\country\india\*\*.json", recursive = True)
top_trans_year=pd.DataFrame()
toptransyear()



path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\top\transaction\country\india\state\*\*\*.json", recursive = True)
top_trans_state= pd.DataFrame()
toptransstate()




path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\top\user\country\india\*\*.json", recursive = True)
top_user_year= pd.DataFrame()
topuseryear()


path = glob.glob(r"C:\Users\kbuva\OneDrive\Desktop\github_clone\pulse\data\top\user\country\india\state\*\*\*.json", recursive = True)
top_user_state = pd.DataFrame()
topuserstate()



# Insert whole DataFrame into MySQL
agg_yr.to_sql('agg_yr', con = engine, if_exists = 'replace')
agg_state.to_sql('agg_state', con = engine, if_exists = 'replace')
user_data_year.to_sql('user_data_year', con = engine,if_exists = 'replace')
user_state.to_sql('user_state', con = engine, if_exists = 'replace')
map_yr.to_sql('map_yr', con = engine, if_exists = 'replace')
map_state.to_sql('map_state', con = engine, if_exists = 'replace')
map_user_yr.to_sql('map_user_yr', con = engine,if_exists = 'replace')
map_trans_state.to_sql('map_trans_state', con = engine,if_exists = 'replace')
top_trans_year.to_sql('top_trans_year', con = engine,if_exists = 'replace')
top_trans_state.to_sql('top_trans_state', con = engine,if_exists = 'replace')
top_user_year.to_sql('top_user_year', con = engine, if_exists = 'replace')
top_user_state.to_sql('top_user_state', con = engine,if_exists = 'replace')

