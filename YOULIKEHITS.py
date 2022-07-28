from selenium_codes import sub4sub_websites_selenium as sws
from configparser import ConfigParser
import os

heroku = "not available"
try:
    heroku = os.environ['HEROKU']
    print("Running HEROKU Version")
except KeyError:
    print("Running Local Version")
    pass

# Heroku
if heroku == "available":
    required_dict = {
        "yt_pw": os.environ["youtube_password"],
        "yt_email": os.environ["youtube_email"],
        "yt_channel_id": os.environ["youtube_channel_id"],
        "username_youlikehits": os.environ["youlikehits_username"],
        "pw_youlikehits": os.environ["youlikehits_password"],
        "yt_useragent": os.environ["youtube_useragent"],
        "github_token": os.environ["github_token"]
    }
# config.ini
else:
    config_object = ConfigParser()
    config_object.read("config.ini")
    userinfo = config_object["USERINFO"]

    required_dict = {
        "yt_pw": userinfo["youtube_password"],
        "yt_email": userinfo["youtube_email"],
        "yt_channel_id": userinfo["youtube_channel_id"],
        "username_youlikehits": userinfo["youlikehits_username"],
        "pw_youlikehits": userinfo["youlikehits_password"],
        "yt_useragent": userinfo["youtube_useragent"],
        "github_token": userinfo["github_token"]
    }

if __name__ == "__main__":
    sws.youlikehits_functions(required_dict)
