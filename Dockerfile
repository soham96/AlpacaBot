FROM python:3.9-slim

# Copy local code to the container image.
COPY . /src
WORKDIR /src

# Install Python Requirements
RUN pip install -r requirements.txt

# Run the service
CMD python bot.py
