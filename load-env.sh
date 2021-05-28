#!/usr/bin/env bash
cd k8s/
sed -i "s/<PROJECT_ID>/$PROJECT_ID/g" *
sed -i "s/<IMAGE>/$IMAGE/g" *
sed -i "s/<TAG>/$GITHUB_SHA/g" *
sed -i "s/<PRAW_CLIENT_ID>/$PRAW_CLIENT_ID/g" *
sed -i "s/<PRAW_CLIENT_SECRET>/$PRAW_CLIENT_SECRET/g" *
sed -i "s/<PRAW_PASSWORD>/$PRAW_PASSWORD/g" *
sed -i "s/<PRAW_USER_AGENT>/$PRAW_USER_AGENT/g" *