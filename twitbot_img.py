import os
import random

import config

def process_tweet(tweet_id, tweet_text, mentions, api):
    tweet_img = None
    for image, keywords in config.images.iteritems():
        for keyword in keywords:
            # this is highly inefficient
            if keyword in tweet_text:
                tweet_img = image
                break

    if config.default_random and tweet_img is None:
        # we choose a random image
        tweet_img = random.choice(config.images.keys())

    if tweet_img:
        tweet_img = os.path.join(config.image_folder, tweet_img)
        content = '%s %s' % (' '.join(mentions), tweet_text)
        api.update_with_media(tweet_img,
            status=content,
            in_reply_to_status_id=tweet_id)
