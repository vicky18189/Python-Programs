from simple_salesforce import Salesforce
import requests
import pandas as pd
from io import StringIO

sf = Salesforce(username='vikram.singh@exxatsystems.com',password='Ankur_89', security_token='tqltENQ4S9GcUO0MERrrnCQby')


sf_instance = 'https://exxat.lightning.force.com/' #Your Salesforce Instance URL
reportId = '00O7F00000AxpA1UAJ' # add report id
export = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
sfUrl = sf_instance + reportId + export
response = requests.get(sfUrl, headers=sf.headers, cookies={'sid': sf.session_id})
download_report = response.content.decode('utf-8')
df1 = pd.read_csv(StringIO(download_report))

df1.to_csv(r'C:\Users\vikram.singh\Documents\my_data.csv', index=False)