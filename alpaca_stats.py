import praw
import datetime as dt
import random
import time
from multiprocessing import Process
import datetime
import pickle

## SET BACKEND
import matplotlib as mpl
mpl.use('TkAgg')

from matplotlib import pyplot as plt
plt.style.use('seaborn-pastel')
from collections import Counter
import seaborn as sns


def number_of_daily_comments():

    with open('obj/' + 'comment_info_dict' + '.pkl', 'rb') as f:
        comment_info_dict=pickle.load(f)
    dates=[]
    amt=[]
    upv=[]
    
    for k, v in comment_info_dict.items():
        dates.append(k)
    
    dates=sorted(dates)
    for date in dates:
        amt.append(comment_info_dict[date]["no_of_comments"])
        upv.append(comment_info_dict[date]["upvotes"])
    
    # import ipdb; ipdb.set_trace()

    dates=[date[5:] for date in dates]
    
    fig, ax1 = plt.subplots()
    ax1.plot(dates, amt, 'bo-', linewidth=2)
    ax1.set_xticklabels(dates, rotation = 45)
    ax1.tick_params(axis='y', labelcolor='b')
    ax1.set_ylabel('No. of Daily Comments', color='b')

    ax2 = ax1.twinx()

    ax2.plot(dates, upv, 'r^-.')
    ax2.set_ylabel('No. of Daily Upvotes', color='r')
    ax2.set_xticklabels(dates, rotation = 45)
    ax2.tick_params(axis='y', labelcolor='r')

    fig.tight_layout()
    # plt.annotate('Bot stopped without me knowing', xy=('01-28', 0), arrowprops=dict(facecolor='black', width=2, headlength=8, headwidth=8), xytext=(12, 50))
    # plt.annotate('Banned from: \n r/Gaming, \n r/LifeProTips, \n r/KemonoFriends, \n r/Rpdrcringe', xy=('01-21', comment_info_dict['2019-01-21']["upvotes"]), arrowprops=dict(facecolor='black', width=2, headlength=8, headwidth=8), xytext=(0, 1500))
    plt.title('Breakdown by Comments')
    plt.show()


def main(reddit):
    
    dates=[]
    for comment in reddit.redditor('JustAnAlpacaBot').comments.top(limit=None):
        dates.append(datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d'))
    
    print(f"Total Comments = {len(dates)}")
    dates=list(set(dates))
    dates.extend(['2019-01-28', '2019-01-29', '2019-01-30', '2019-01-31'])
    dates=sorted(dates)
    print(f"Total dates: {len(dates)}")

    comment_info_dict={
            '2019-01-28':{
                "no_of_comments": 0,
                "upvotes": 0
            },
            '2019-01-29':{
                "no_of_comments": 0,
                "upvotes": 0
            },
            '2019-01-30':{
                "no_of_comments": 0,
                "upvotes": 0
            },
            '2019-01-31':{
                "no_of_comments": 0,
                "upvotes": 0
            }}

    subreddit=[]
    subreddit_upvotes={}
    upvote_sum=0
    for comment in reddit.redditor('JustAnAlpacaBot').comments.top(limit=None):
        date=datetime.datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d')    
    
        if date in comment_info_dict:
            no_of_comments=comment_info_dict[date]["no_of_comments"]+1
            upvotes=comment_info_dict[date]["upvotes"]+comment.score
            subreddit_id=comment.subreddit.display_name
            subreddit.append(subreddit_id)

            comment_info_dict[date]={
                "no_of_comments": no_of_comments,
                "upvotes": upvotes
            }

            if subreddit_id in subreddit_upvotes:
                sr_upvotes=subreddit_upvotes[subreddit_id]+comment.score
                subreddit_upvotes[subreddit_id]=sr_upvotes
                upvote_sum=upvote_sum+comment.score
            else:
                subreddit_upvotes[subreddit_id]=comment.score
                upvote_sum=upvote_sum+comment.score

        else:
            no_of_comments=1
            upvotes=comment.score
            subreddit_id=comment.subreddit.display_name
            subreddit.append(subreddit_id)
            
            if subreddit_id in subreddit_upvotes:
                sr_upvotes=subreddit_upvotes[subreddit_id]+comment.score
                subreddit_upvotes[subreddit_id]=sr_upvotes
            else:
                subreddit_upvotes[subreddit_id]=comment.score
            upvote_sum=upvote_sum+comment.score

            comment_info_dict[date]={
                "no_of_comments": no_of_comments,
                "upvotes": upvotes
            }
    
    with open('obj/comment_info_dict.pkl', 'wb') as f:
        pickle.dump(comment_info_dict, f, pickle.HIGHEST_PROTOCOL)

    with open('obj/subreddit.pkl', 'wb') as f:
        pickle.dump(subreddit, f, pickle.HIGHEST_PROTOCOL)

    with open('obj/subreddit_upvotes.pkl', 'wb') as f:
        pickle.dump(subreddit_upvotes, f, pickle.HIGHEST_PROTOCOL)

    number_of_daily_comments(comment_info_dict)
    
    print(Counter(subreddit))
    print(comment_info_dict)
    print(subreddit_upvotes)
    print(f"Sum = {upvote_sum}")

def pie_upvotes():

    with open('obj/' + 'subreddit_upvotes' + '.pkl', 'rb') as f:
        subreddit_upvotes=pickle.load(f)
    
    import operator
    sorted_d = sorted(subreddit_upvotes.items(), key=operator.itemgetter(1), reverse=True)

    shown_sum=0
    total_sum=0

    labels=[]
    sizes=[]

    for i, val in enumerate(sorted_d):
        
        sr, up=val
        total_sum=total_sum+up
        if i<9:
            labels.append(f"r/{sr}: {up} upvotes")
            sizes.append(up)
            shown_sum=shown_sum+up
    
    labels.append(f'Others: {total_sum-shown_sum} upvotes')
    sizes.append(total_sum-shown_sum)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=45)
    #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.text(0.5, 0.05,f'Most Upvoted Subreddits \n Total Upvotes: {total_sum}', ha='center')
    plt.title(f'Breakdown by Subreddits')
    plt.show()

def pie():

    with open('obj/' + 'subreddit' + '.pkl', 'rb') as f:
        subreddit=pickle.load(f)
    


    subreddit=dict(Counter(subreddit))
    import operator

    sorted_d = sorted(subreddit.items(), key=operator.itemgetter(1), reverse=True)

    shown_sum=0
    total_sum=0

    labels=[]
    sizes=[]

    for i, val in enumerate(sorted_d):
        
        sr, up=val
        total_sum=total_sum+up
        if i<9:
            labels.append(f"r/{sr}: {up} comments")
            sizes.append(up)
            shown_sum=shown_sum+up
    
    labels.append(f'Others: {total_sum-shown_sum} \n comments')
    sizes.append(total_sum-shown_sum)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=120)
    #ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    fig1.text(0.5, 0.05,f'Subreddits Most Commented on \n Total Comments: {total_sum}', ha='center')
    # plt.title(f'Breakdown by Subreddits')
    plt.show()

if __name__ == "__main__":
    reddit=praw.Reddit(client_id='my_client',
                        client_secret='my_secret',
                        user_agent='Alpaca stats by u/JustAnAlpacaBot',
                        username='JustAnAlpacaBot',
                        password='mypass')
    
    # number_of_daily_comments()
    pie()
