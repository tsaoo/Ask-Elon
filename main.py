from sys import argv
from scrape import search, searchE
from markov import markovData
import subprocess

def main(subj: str, username: str) -> str:
    if len(subj) > 2:
        search(subj, username)
    else:
        searchE()

    #parseData()
    cmd = "parse.cpp"
    subprocess.call(["g++", cmd])
    subprocess.call("./a.out")

    tweet = markovData()

    return(tweet)

if __name__ == "__main__":
    main(argv[1])