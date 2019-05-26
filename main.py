import tweepy
from keys import *
import time

#OAuth process
def authentication(consumer_token, consumer_secret, access_token, access_token_secret):
    global auth
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

def answer_mentions():
    print("Retrieving mentions...")

    since_id = get_last_id()
    mentions = api.mentions_timeline(since_id, tweet_mode='extended')

    for tweet in reversed(mentions):
        update_last_id(tweet.id)
        if "#help" in tweet.full_text.lower():
            print("#help found in tweet. Answering...")
            b = '\U0001F605'
            api.update_status(f"@{tweet.author.screen_name} I don't do anything yet \U0001F605", tweet.id)
        else:
            print("No keywords found in this tweet")

    print("All mentions adressed.")

def update_last_id(new_id):
    print("Updating ID...")
    file = open("last_id.txt", 'r')
    old_id = file.read()
    file.close()
    if new_id > int(old_id):
        file = open("last_id.txt", 'w')
        file.write(str(new_id))
        file.close()
        print("ID updated.")
    else:
        print("Given ID older than existing ID.")

def get_last_id():
    file = open('last_id.txt')
    id = file.read()
    return int(id)

def sleep(sleeptime):
    print(f"Waiting {sleeptime} seconds...")
    time.sleep(sleeptime)

authentication(consumer_token, consumer_secret, access_token, access_token_secret)

api = tweepy.API(auth)

while True:
    answer_mentions()
    sleep(15)

print("THE END")
