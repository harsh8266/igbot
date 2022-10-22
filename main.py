
import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot()
bot.login(username="artistharsh8233", password="101KingArtist101")



for hashtag in args.hashtags:
  users = bot.get_hashtag_users(hashtag)
  bot.follow_users(users)
bot.logout()
