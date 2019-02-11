import praw
import datetime as dt
import random
import time

def get_fact():
    fact = random.choice(list(open('alpaca_facts.txt')))

    text = f"""Hello there! I am a bot raising awareness of Alpacas

Here is an Alpaca Fact:

{fact}

______
| [Info](https://github.com/soham96/AlpacaBot/blob/master/README.md)
| [Code](https://github.com/soham96/AlpacaBot)
| [Feedback](http://np.reddit.com/message/compose/?to=JustAnAlpacaBot&subject=Feedback)
| [Contribute Fact](http://np.reddit.com/message/compose/?to=JustAnAlpacaBot&subject=Fact)
____


If you liked this fact, consider donating [here](https://github.com/soham96/AlpacaBot/blob/master/README.md)"""
    
    return text

def get_comments():
    print(time.time())

    try:
        for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
            if comment.author == 'JustAnAlpacaBot':
                continue
            if 'alpaca' in comment.body.lower():
                    reply_alpaca(comment.id, 'comment')
                    print(time.time())
    except:
        pass
        

def reply_alpaca(post_id, post_type):
    
    if post_type=='post':
        submission=reddit.submission(id=post_id)
        try:
            submission.reply(get_fact())
            print(f"Commented on {post_type} {post_id} and url {submission.permalink}")
        except:
            time.sleep(600)
            submission.reply(get_fact())
            print(f"Commented on {post_type} {post_id} and url {submission.permalink}")
    
    if post_type=='comment':
        comment=reddit.comment(id=post_id)
        try:
            comment.reply(get_fact())
            print(f"Commented on {post_type} with {post_id} and url {comment.permalink}")
        except:
            print(f"Could not comment {post_id}")

def main(reddit):
    while True:
        get_comments()

if __name__ == "__main__":
    reddit=praw.Reddit(client_id='your_client_id',
                        client_secret='your_secret',
                        user_agent='Alpaca Facts by u/JustAnAlpacaBot',
                        username='JustAnAlpacaBot',
                        password='my_password')
    
    main(reddit)
