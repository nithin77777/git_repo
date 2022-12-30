import os
from builtins import print
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from tabulate import tabulate
import pandas as pd
import pymysql

pymysql.install_as_MySQLdb()
# import psycopg2 as ps
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import chardet

os.chdir('./')

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'client_secret_desktop_temp.json'


def get_service():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)

    credentials = flow.run_console()
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def execute_api_request(client_library_function, **kwargs):
    response = client_library_function(
        **kwargs
    ).execute()
    return response


def create_table(table, headers=None):
    if headers:
        headerstring = "\t{}\t" * len(headers)
        print(headerstring.format(*headers))

    rowstring = "\t{}\t" * len(table[0])

    for row in table:
        print(rowstring.format(*row))


if __name__ == '__main__':
    youtubeAnalytics = get_service()
    result = execute_api_request(
        youtubeAnalytics.reports().query,
        ids='channel==MINE',
        startDate='2022-04-01',
        endDate='2022-12-20',
        metrics='views,likes,comments',
        dimensions='day',
        sort='day'
    )
    headers = ['views', 'likes', 'comments']
    # create_table(result['rows'], headers=headers)
    print(tabulate(result['rows'], headers=headers, tablefmt="pretty"))

# Adding a Block of code for getting a list of columns
i = 0
cols = list()
for c in result['columnHeaders']:
    cols.append(c['name'])
    i += 1

# Creating Dataframe with data as result['rows'] and setting the parameters as previously created list 'cols'
data = pd.DataFrame(result['rows'], columns=cols)
data.to_csv(
    'yt_analytics.csv')  # Exporting dataframe into csv file and naming it as "yt_analytics.csv" as it contains analytical data

if __name__ == '__main__':
    print("ALL WENT WELL YOUTUBE ANALYTICS CODE COMPLETE !!\n CHECK THE .csv FILE!!")

    # Pushing yt_analytics.csv to MySQL database
    # import pymongffo

    # os.chdir('/Users/nithinsaikrishna/Downloads/')

    file = 'yt_analytics.csv'
    with open(file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(100000))
    print(result)

    dataset = pd.read_csv('yt_analytics.csv')  # encoding='unicode_escape'
    # dataset.replace(to_replace=' ',value='NULL',inplace=True)
    print(dataset)
    # dataset.to_csv('power_consumption_v1.csv', encoding='utf-8')

    db = create_engine("mysql://root:mnsk1315@127.0.0.1:3306/youtube_report", echo=True)
    connection = db.connect()
    dataset.to_sql(name='analytics', con=connection, if_exists='replace', index=False)
    connection.close()

    file = 'yt_analytics.csv'
    with open(file, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(100000))
    print('After conversion the file type is: ', result)
