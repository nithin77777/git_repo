from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
from tabulate import tabulate
from flask import Flask
import pandas as pd

load_dotenv()
API_KEY=os.getenv("API_KEY")
print(API_KEY)

# Query For Getting Video Insights

query=build("youtube" , "v3" , developerKey=API_KEY).videos().list(part="snippet,contentDetails,statistics" ,
                                                                   id="sm5VIsISMHE")
rest=query.execute()
# print(rest)
youtube_insights_dict=dict()

print(rest['items'][0]['statistics'])

youtube_insights_dict['Channel_id']=rest['items'][0]['snippet']['channelId']

youtube_insights_dict['Title']=rest['items'][0]['snippet']['title']

youtube_insights_dict['Published_Date']=rest['items'][0]['snippet']['publishedAt']

youtube_insights_dict['Video_Description']=rest['items'][0]['snippet']['description']

youtube_insights_dict['Definition']=rest['items'][0]['contentDetails']['definition']

youtube_insights_dict['dimension']=rest['items'][0]['contentDetails']['dimension']

youtube_insights_dict['LicensedOrNo']=rest['items'][0]['contentDetails']['licensedContent']

youtube_insights_dict['viewCount']=rest['items'][0]['statistics']['viewCount']

youtube_insights_dict['likeCount']=rest['items'][0]['statistics']['likeCount']

youtube_insights_dict['favourites']=rest['items'][0]['statistics']["favoriteCount"]

youtube_insights_dict['comments']=rest['items'][0]['statistics']['commentCount']

data=pd.DataFrame(youtube_insights_dict , index=[0])
data.to_csv('./ytVideo.csv')

app=Flask(__name__)


@app.route("/")
def Index():
    return "<a href='http://127.0.0.1:1000/youtubeVideoAnalytics'>http://127.0.0.1:1000/youtubeVideoAnalytics</a>"


Index()


@app.route("/youtubeVideoAnalytics")
def yt_Video():
    import pandas as pd
    return youtube_insights_dict


yt_Video()

if __name__ == "__main__":
    print("Done")
    app.run(port=1000 , host="0.0.0.0")
# ----------------------------------------------------------------------------------------------

# queryTwo = build("youtube" , "v3" , developerKey=API_KEY)
