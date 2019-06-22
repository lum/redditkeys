#!/usr/bin/env python

import argparse
import json
import logging
import praw
import prawcore
import requests
import sys

BASE_URL = 'https://keybase.io/_/api/1.0/user/discover.json'

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='android:com.example.myredditapp:v1.2.3 (by /u/kemitche)')


def retrieve_reddit_posts(subreddit, number, live=None):
    if live:
        try:
            # The skip_existing=True option will only retrieve new submissions starting when the stream is created.
            for submission in reddit.subreddit(subreddit).stream.submissions(
                                                            skip_existing=True):
                user_fingerprint = retrieve_user_info(submission.author.name)
                if user_fingerprint:
                    print("Reddit Username: {} Post Title: {} Keybase Key Fingerprint: {}"
                          .format(submission.author.name.encode('utf-8'),
                                  submission.title.encode('utf-8'),
                                  user_fingerprint))
        except praw.exceptions.APIException as e:
            print("Reddit API error: {}".format(e))
        except praw.exceptions.APIException as e:
            print("Reddit API error: {}".format(e))
        except prawcore.exceptions.ResponseException as e:
            print("Unathorized Reddit API Access")
        except prawcore.exceptions.Redirect as e:
            print("Unknown subreddit name: {}".format(subreddit))
    else:
        try:
            for submission in reddit.subreddit(subreddit).new(limit=number):
                user_fingerprint = retrieve_user_info(submission.author.name)
                if user_fingerprint:
                    print("Reddit Username: {} Post Title: {} Keybase Key Fingerprint: {}"
                          .format(submission.author.name.encode('utf-8'),
                                  submission.title.encode('utf-8'),
                                  user_fingerprint))
        except praw.exceptions.APIException as e:
            print("Reddit API error: {}".format(e))
        except praw.exceptions.APIException as e:
            print("Reddit API error: {}".format(e))
        except prawcore.exceptions.ResponseException:
            print("Unathorized Reddit API Access")
        except prawcore.exceptions.Redirect:
            print("Unknown subreddit name: {}".format(subreddit))


def retrieve_user_info(username):
    logging.debug("Looking up username: {}".format(username))
    try:
        response = requests.get(BASE_URL + "?reddit=" + username)
    except requests.exceptions.RequestException as e:
        logging.info("Connectivity Error: {}".format(e))
        sys.exit(1)

    try:
        data = json.loads(response.text)
    except ValueError:
        logging.debug("JSON Parsing error")

    if not isinstance(data, dict):
        logging.debug("Expected a dict object")

    try:
        keybase_match = data['matches']['reddit'][0][0]
    except IndexError:
        logging.debug("User doesn't have a reddit username match in Keybase")
        return

    try:
        public_key = keybase_match['public_key']['key_fingerprint']
        return public_key
    except:
        logging.debug("No public key fingerprint")
        return

def main(subreddit, last, live):
    retrieve_reddit_posts(subreddit, last, live)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initializes redditkeys")
    parser.add_argument("subreddit",
                        help="Name of Reddit subreddit to search for new posts")
    parser.add_argument("--last",
                        help="The number of new posts to lookup from subreddit",
                        type=int)
    parser.add_argument("--live",
                        help="Continously stream new posts from subreddit",
                        action="store_true",
                        default=False)
    parser.add_argument("-v", "--verbose", help="Increase log verbosity",
                        action="store_true")
    options = parser.parse_args()
    if options.last and options.live:
        print("Choose only one option between --live or --last")
        sys.exit(1)
    elif not options.last and not options.live:
        print("You must specify one of --live or --last")
        sys.exit(1)
    elif options.verbose:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)-15s %(levelname)s: %(message)s')
    else:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)-15s %(levelname)s: %(message)s')
    main(options.subreddit, options.last, options.live)
