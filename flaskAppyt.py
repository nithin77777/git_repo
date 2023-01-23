from public_yt import *
from flask import Flask

app=Flask(__name__)


@app.route("/")
def yt_insights():
    return youtube_insights_dict


@app.route("/insta_analytics")
def insta_analytics():
    pass


@app.route("/fb_analytics")
def facebook_insights():
    pass


# hello_world()

if __name__ == "__main__":
    app.run()
