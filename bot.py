import praw
import os
import datetime as dt
import random
import time

def get_fact():
    fact=random.choice(list(open('alpaca_facts.txt')))

    text=("Hello there! I am a bot raising awareness of Alpacas"
        "\n \n Here is an Alpaca Fact:"
        f"\n \n {fact}"
        "\n \n ______ \n \n"
        "| [Info](https://github.com/soham96/AlpacaBot/blob/master/README.md)"
        "| [Code](https://github.com/soham96/AlpacaBot)"
        "| [Feedback](http://np.reddit.com/message/compose/?to=JustAnAlpacaBot&subject=Feedback)"
        "| [Contribute Fact](http://np.reddit.com/message/compose/?to=JustAnAlpacaBot&subject=Fact)"
        "\n \n ###### You don't get a fact, you earn it. If you got this fact then AlpacaBot thinks you deserved it!")

    return text

def get_comments():
    print(time.time())

    try:
        subreddit=reddit.subreddit('all')
        for comment in subreddit.stream.comments(skip_existing=False):
            if comment.author == 'JustAnAlpacaBot':
                continue
            if 'alpaca' in comment.body.lower():
                    reply_alpaca(comment)
                    print(time.time())
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(e)        

def reply_alpaca(comment):
    try:
        comment.reply(get_fact())
        print(f"Commented on {comment.id} and url {comment.permalink}")
    except:
        print(f"Could not comment {comment.id}")

def main(reddit):
    while True:
        get_comments()

if __name__ == "__main__":
    print(os.getenv('PRAW_CLIENT_ID'))
    print(os.getenv('PRAW_CLIENT_SECRET'))
    reddit=praw.Reddit(client_id=os.getenv('PRAW_CLIENT_ID'),
                        client_secret=os.getenv('PRAW_CLIENT_SECRET'),
                        user_agent=os.getenv('PRAW_USER_AGENT'),
                        username='JustAnAlpacaBot',
                        password=os.getenv('PRAW_PASSWORD'))
    
    main(reddit)
