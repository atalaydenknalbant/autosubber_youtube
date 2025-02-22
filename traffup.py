from selenium_codes import sub4sub_websites_selenium as sws
from configparser import ConfigParser


config_object = ConfigParser()
config_object.read("config.ini")
userinfo = config_object["USERINFO"]

required_dict = {
    "yt_email": userinfo["youtube_email"],
    "chrome_userdata_directory": userinfo["chrome_userdata_directory"],
    "chrome_profile_name": userinfo["chrome_profile_name"],
    "yt_channel_id": userinfo["youtube_channel_id"],
    "email_traffup": userinfo["traffup_email"],
    "pw_traffup": userinfo["traffup_password"],
    "yt_useragent": userinfo["youtube_useragent"],
    "github_token": userinfo["github_token"]
}

if __name__ == "__main__":
    sws.traffup_functions(required_dict)