#!/usr/bin/env bash
cd k8s/
gsed -i "s/<PROJECT_ID>/$PROJECT_ID/g" *
gsed -i "s/<IMAGE>/$IMAGE/g" *
gsed -i "s/<TAG>/$GITHUB_SHA/g" *
gsed -i "s/<PRAW_CLIENT_ID>/$PRAW_CLIENT_ID/g" *
gsed -i "s/<PRAW_CLIENT_SECRET>/$PRAW_CLIENT_SECRET/g" *
gsed -i "s/<PRAW_PASSWORD>/$PRAW_PASSWORD/g" *
gsed -i "s/<PRAW_USER_AGENT>/$PRAW_USER_AGENT/g" *