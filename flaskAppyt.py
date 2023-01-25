import requests
import tabulate
from tabulate import tabulate
import pandas as pd

access="EAAHScwZCDx5YBAMPPCzGwbDZAwW9pC4yWdBV16BloL1MCZAvZAbSamFxBbaAmF0u6RhuIjdv2EzQ5ynqYouToavirsushQ0x3MvuREW1zooKBVS8mRKBMzSyEZBfwfMyopoUrAipRwdr2o5R8K0b5AFAdTWYSug75uE1DU8oN0RidmNc9Iv3b7wrQP7iZBiuVRVoARcCjLPvsWZCFEhL2qK6juRPnFNaGYZD"

page=requests.get(
    url="https://graph.facebook.com/v15.0/me?fields=picture%2cabout%2Cid%2Cname%2Cemails%2Cfan_count%2Cfollowers_count%2Cband_interests%2Cbio%2Cbirthday%2Cphotos%2Calbums%2Ccontact_address%2Cbusiness%2Cconnected_instagram_account%2Cengagement%2Cvideos&access_token=" + access)
pageAbout=dict(page.json())
print(pageAbout)

instagramUser=requests.get(
    "https://graph.facebook.com/v15.0/17841456927336966?fields=biography%2Cid%2Cig_id%2C%20followers_count%2C%20follows_count%2Cmedia_count%2Cname%2C%20profile_picture_url%2Cusername%2Cwebsite%20&access_token=" + access)
instagramUser=instagramUser.json()
print(instagramUser)

instagramMedia=requests.get(
    "https://graph.facebook.com/v15.0/17841456927336966?fields=business_discovery.username(capnxtglobaltech)%7Bfollowers_count%2Cmedia_count%2Cmedia%7D&access_token=" + access)
instagramMedia=instagramMedia.json()
print(instagramMedia)

# Getting media infor with media ID instagram
mediaId=requests.get(
    "https://graph.facebook.com/v15.0/17963395772279635?fields=caption%2Cid%2Cig_id%2Cis_comment_enabled%2Clike_count%2Ccomments_count%2Cmedia_url%2Cowner%2Ctimestamp%2Cmedia_type%2Cpermalink&access_token=EAAHScwZCDx5YBAFWep5wIUznNtjEWCUYjbRIGlRQjDlmknuSiNx92LZAaD28GgKZBWwvKWZCX0TzCzePaKAZANypE4KCOg9IgVPf3NiCwynYVEmyZBhNR6v2WmTmy9PZA53mjdfz07qD5S79oJpFnWLZAsMX732iUZAFvGvbI2hQJI9aMclMx1p1VL5PNwFAM6ruV0f17ZAWrrBDBtQmDwOiWRlNPumyTVKy4ZD")
mediaId=mediaId.json()
print(mediaId)

# Getting Ad_set insights
AdaccountInsights=requests.get(
    "https://graph.facebook.com/v15.0/act_1823690511319599/insights?fields=impressions%2Creach%2Caccount_id%2Caccount_name%20&date_preset=last_14d&access_token=" + access)
AdaccountInsights=AdaccountInsights.json()
print(AdaccountInsights)
# Post Insights
PostInsights=requests.get(
    "https://graph.facebook.com/v15.0/17905768403704595/insights?metric=impressions%2Creach%2Clikes%2C%20comments%2C%20shares%2C%20total_interactions%2C%20follows%2C%20profile_visits%2C%20profile_activity%2Cengagement&access_token=EAAHScwZCDx5YBAFWep5wIUznNtjEWCUYjbRIGlRQjDlmknuSiNx92LZAaD28GgKZBWwvKWZCX0TzCzePaKAZANypE4KCOg9IgVPf3NiCwynYVEmyZBhNR6v2WmTmy9PZA53mjdfz07qD5S79oJpFnWLZAsMX732iUZAFvGvbI2hQJI9aMclMx1p1VL5PNwFAM6ruV0f17ZAWrrBDBtQmDwOiWRlNPumyTVKy4ZD")
PostInsights=PostInsights.json()
print(PostInsights)

# Ad Insights Based on Campaign ID
facebookAdInsights=requests.get(
    "https://graph.facebook.com/v15.0/23852588885780572/insights?fields=website_ctr%2Cupdated_time%2Csocial_spend%20%2Cspend%2Coptimization_goal%20%2Cgender_targeting%20%2Cfull_view_impressions%2C%20full_view_reach%20%2Cfrequency%2Ccreated_time%2Ccpm%2Ccpp%2Cctr%2C%20cost_per_unique_inline_link_click%20%2Ccost_per_unique_click%20%2Ccost_per_ad_click%2Cimpressions%2Creach%2Ccpc%2Caccount_currency%2Caccount_name%2Cad_id%2Cad_name%2Cage_targeting%2Ccampaign_id%2Ccampaign_name%2C%20clicks%2Cconversion_values%2Cconversions%2Cconverted_product_quantity%2Cconverted_product_value&access_token=EAAHScwZCDx5YBAMPPCzGwbDZAwW9pC4yWdBV16BloL1MCZAvZAbSamFxBbaAmF0u6RhuIjdv2EzQ5ynqYouToavirsushQ0x3MvuREW1zooKBVS8mRKBMzSyEZBfwfMyopoUrAipRwdr2o5R8K0b5AFAdTWYSug75uE1DU8oN0RidmNc9Iv3b7wrQP7iZBiuVRVoARcCjLPvsWZCFEhL2qK6juRPnFNaGYZD")
facebookAdInsights=facebookAdInsights.json()
print(facebookAdInsights)

appflask=Flask(__name__)

appflask.route("/")


def endPoints():
    return "<h>hi</h>"


endPoints()

if __name__ == "__main__":
    print("Done !! CHeck Output!!")
