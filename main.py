import time
import os

from internet_speed_twitter import InterSpeedTwitter

PROMISED_DOWN = 200
PROMISED_UP = 50

email_input = os.environ.get('EMAIL')
password_input = os.environ.get('PASSWORD')

speed_twitter = InterSpeedTwitter()
time.sleep(5)
speed_twitter.get_internet_speed()
speed_twitter.tweet_at_provider(email_input, password_input)

# result-data-large number result-data-value download-speed
# result-data-large number result-data-value upload-speed


