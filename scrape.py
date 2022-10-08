import twint
import os
import nest_asyncio
import sys

def search(subj: str, username:str):

    c = twint.Config()
    c.Username = "barackobama"
    c.Custom["tweet"] = ["tweet"]
    c.Store_json = True
    c.Hide_output = True
    open('tweets.txt', 'w').close()
    c.Output = "tweets.txt"
    c.Limit = 10000
    c.Popular_tweets = True
    c.Search = subj

    twint.run.Search(c)

    return c.Username

def searchE():

    c = twint.Config()
    c.Username = "elonmusk"
    c.Custom["tweet"] = ["tweet"]
    c.Store_json = True
    c.Hide_output = True
    open('tweets.txt', 'w').close()
    c.Output = "tweets.txt"
    c.Limit = 10000
    c.Popular_tweets = True

    twint.run.Search(c)

    return c.Username



if __name__ == "__main__":
    if len(sys.argv) == 2:
        subj = sys.argv[1]
        username = sys.argv[2]
        search(subj, username)
    else:
        searchE()