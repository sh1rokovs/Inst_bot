from instapy import InstaPy

session = InstaPy(username="", password="")
session.login()

custom_list = [""]
session.unfollow_users(amount=84, custom_list_enabled=True,
                       custom_list=custom_list, custom_list_param="nonfollowers",
                       style="RANDOM", unfollow_after=55*60*60, sleep_delay=600)
