FROM python:3.9-slim

# Copy local code to the container image.
COPY . /src
WORKDIR /src

RUN env
ARG PRAW_CLIENT_ID
# ENV PRAW_CLIENT_SECRET=${{PRAW_CLIENT_SECRET}}
ARG PRAW_PASSWORD=${PRAW_PASSWORD}
# ENV PRAW_USER_AGENT=${PRAW_USER_AGENT}
ARG PRAW_USER_AGENT="Some Agent"
RUN env
# Install Python Requirements
RUN pip install -r requirements.txt

# Run the service
CMD python bot.py
