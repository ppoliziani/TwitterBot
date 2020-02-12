import tweepy
import time
import datetime
import os

MINUTE = 60
FIVE_MINS = 60 * 5
TWENTY_MINS = 60 * 20
HOUR = 60 * 60
DAY = 60 * 60 * 24


def repeated():

    while True:
        os.system("java -jar processing-py.jar processing.py")
        # daily upload -> img_path = (str(datetime.datetime.now().date()) + ".jpg")
        img_path = ("Pictures\ " + str(datetime.datetime.now().time().strftime('%H:%M')) + ".jpg").replace(":", "-")
        api.update_with_media(img_path, "Created at " + str(datetime.datetime.now().time().strftime('%H:%M')))
        time.sleep(TWENTY_MINS)


def main():

    with open("keys.txt", "r+") as keyFile:
        for line in keyFile:
            if line[0] == "!":
                apikey = line[1:len(line) - 1]
            elif line[0] == "@":
                apikeysecret = line[1:len(line) - 1]
            elif line[0] == "#":
                accesstoken = line[1:len(line) - 1]
            elif line[0] == "$":
                accesstokensecret = line[1:len(line)]

    print(apikey)
    print(apikeysecret)
    print(accesstoken)
    print(accesstokensecret)

    twitter_auth_keys = {
        "consumer_key": apikey,
        "consumer_secret": apikeysecret,
        "access_token": accesstoken,
        "access_token_secret": accesstokensecret
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )
    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )

    global api
    api = tweepy.API(auth)

    # print("Filename: " + str(datetime.datetime.now().date()) + ".jpg")
    print(("Pictures\ " + str(datetime.datetime.now().time().strftime('%H:%M')) + ".jpg").replace(":", "-"))

    repeated()


main()



"""
victims = ["Dan", "Mish", "Land", "Ran", "Mash", "Nal", "Bert", "Felice", "Dave"]
    insults = ["dumb", "stupid", "moronic", "not right in the head", "not gonna succeed"]
    # tweet = ""
    previous = ""
    while True:
        tweet = ("" + str(victims[random.randint(0, len(victims) - 1)]) + " is " + str(insults[random.randint(0, len(insults) - 1)]))
        if tweet == previous:
            print(tweet + " and " + previous + " are the same, trying again:")
            tweet = ("" + str(victims[random.randint(0, len(victims) - 1)]) + " is " + str(
                insults[random.randint(0, len(insults) - 1)]))
        print(tweet)
        previous = tweet
        # status = api.update_status(status=tweet)
        # tweet = tweet[:-1]
        time.sleep(60)
"""
