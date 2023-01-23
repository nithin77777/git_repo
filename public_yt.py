from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

load_dotenv()
API_KEY=os.getenv("API_KEY")
print(API_KEY)

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
