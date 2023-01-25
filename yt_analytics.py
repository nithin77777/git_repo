import os
from builtins import print
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from tabulate import tabulate
import pandas as pd
import pymysql
from flask import Flask

pymysql.install_as_MySQLdb()
# import psycopg2 as ps
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import os
import urllib3

os.chdir('/Users/nithinsaikrishna/PycharmProjects/pythonProject/yt_api/')

SCOPES=['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME='youtubeAnalytics'
API_VERSION='v2'
CLIENT_SECRETS_FILE='yt_test_client.json'


def get_service():
    flow=InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE , SCOPES)

    credentials=flow.run_console()
    return build(API_SERVICE_NAME , API_VERSION , credentials=credentials)


def execute_api_request(client_library_function , **kwargs):
    response=client_library_function(**kwargs).execute()
    return response


def create_table(table , headers=None):
    if headers:
        headerstring="\t{}\t" * len(headers)
        print(headerstring.format(*headers))

    rowstring="\t{}\t" * len(table[0])

    for row in table:
        print(rowstring.format(*row))


if __name__ == '__main__':
    youtubeAnalytics=get_service()
    result=execute_api_request(
        youtubeAnalytics.reports().query ,
        ids='channel==MINE' ,
        startDate='2022-04-01' ,
        endDate='2023-01-20' ,
        metrics='estimatedMinutesWatched,views,likes,subscribersGained,shares,annotationClickThroughRate,averageViewDuration,videosAddedToPlaylists' ,
        dimensions='day' ,
        sort='day'
        # filters='relatedToVideoId==1'
        # type='video'
    )
    headers=['date' , 'estimatedMinutesWatched' , 'views' , 'likes' , 'subscribersGained' , "shares" ,
             "annotationClickThroughRate" , "averageViewDuration" , "videosAddedToPlaylists"]
    # print(result['kind'])
    print(result)
    print(type(result))
    create_table(result['rows'] , headers=headers)
    print(tabulate(result['rows'] , headers=headers , tablefmt="pretty"))
# Adding a Block of code for getting a list of columns

i=0
cols=list()
for c in result['columnHeaders']:
    cols.append(c['name'])
    i+=1

# Creating Dataframe with data as result['rows'] and setting the parameters as previously created list 'cols'
data=pd.DataFrame(result['rows'] , columns=cols)
data.to_csv(
    './yt_analytics.csv')  # Exporting dataframe into csv file and naming it as "yt_analytics.csv" as it contains analytical data

appOne=Flask(__name__)


@appOne.route("/")
def Index():
    return "<a href='http://127.0.0.1:1300/youtube_userInsights'>http://127.0.0.1:1300/youtube_userInsights</a>"


Index()


@appOne.route("/youtube_userInsights")
def yt_insights():
    return tabulate(result['rows'] , headers=headers , tablefmt="pretty")


yt_insights()

if __name__ == '__main__':
    print("YOUTUBE ANALYTICS CODE COMPLETE !!\n CHECK THE .csv FILE!!")
    appOne.run(port=1300 , host="0.0.0.0")
