# Redditkeys

This utility allows a user to scrape the latest posts from a specific subreddit on Reddit and attempts to link the author of the post to their Keybase (keybase.io) public key fingerprint. When it finds a Reddit username that matches a Keybase account with a public key fingerprint, it will print out the Reddit username, Reddit Post Title, and the user's Keybase public key fingerprint.

## Prerequisites

1. Python 2.7

2. Python praw library 
```pip install praw```

3. Reddit account: A Reddit account is required to access Reddit’s API. Create one at reddit.com.

4. Client ID and Client Secret: These two values are needed to access Reddit’s API as a script application. If you don’t already have a client ID and client secret, follow Reddit’s First Steps Guide (https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) to create them.

5. User Agent: A user agent is a unique identifier that helps Reddit determine the source of network requests. To use Reddit’s API, you need a unique and descriptive user agent. The recommended format is <platform>:<app ID>:<version string> (by /u/<Reddit username>). For example, android:com.example.myredditapp:v1.2.3 (by /u/kemitche).

In order for this tool to connect to the Reddit API, you will need to insert your Client ID, Client Secret and User Agent into `redditkeys.py`:
```
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='android:com.example.myredditapp:v1.2.3 (by /u/kemitche)')
```

## Usage

After cloning this repo to your local workstation, you can run this tool from the command line with the options below.
In addiiton to the subreddit name to look for new posts, either `--last` or `--live` options are required. Both can not be chosen either.

## Command Line Options

| Name | Description | Required |
|------|-------------| :-----:|
| `subreddit name` | Name of subreddit on Reddit to retrieve posts from. Good examples are `keybaseproofs` or `all` | yes|
| --last N | Retrieve the last N number of posts in a subreddit to find matches against Keybase. | no |
| --live| Streams the latest posts in a subreddit to find matches against Keybase| no |
| -v, --verbose | Enable debug output | no |

## Usage Examples

##### Retrieving N amount of latest posts example:
```
$ python redditkeys.py keybaseproofs --last 3
Reddit Username: kognate Post Title: My Keybase proof [reddit:kognate = keybase:kognate] (bRXplZlU0BT2WvNup3-sadVe6QJ9hmFfPxPRnI2NehQ) Keybase Key Fingerprint: 6eb2a118d32e55422c960ff642688e295b70a92a
Reddit Username: markuszeller Post Title: My Keybase proof [reddit:markuszeller = keybase:markuszeller] (JBfTigkQrjEruEoKZfKdi77XbQHfMFY6ErQE0l5R_Lg) Keybase Key Fingerprint: d9221a8381480faaf77653b0e2820ff55aefbc18
Reddit Username: time4fun Post Title: My Keybase proof [reddit:time4fun = keybase:time4fun] (q6XSdSzP78VGFNdbBBs_mmrFOhf4-S2zwF7_lGI0x1k) Keybase Key Fingerprint: 7a4f49b351c60d0d36b2c309f351575ff269e9f8

```

##### Retrieving N amount of latest posts with debug output enabled example:
```
$ python redditkeys.py keybaseproofs --last 3 -v
2019-06-22 14:18:41,057 DEBUG: Fetching: GET https://oauth.reddit.com/r/keybaseproofs/new
2019-06-22 14:18:41,057 DEBUG: Data: None
2019-06-22 14:18:41,057 DEBUG: Params: {'raw_json': 1, 'limit': 3}
2019-06-22 14:18:41,060 DEBUG: Starting new HTTPS connection (1): www.reddit.com:443
2019-06-22 14:18:41,904 DEBUG: https://www.reddit.com:443 "POST /api/v1/access_token HTTP/1.1" 200 118
2019-06-22 14:18:41,911 DEBUG: Starting new HTTPS connection (1): oauth.reddit.com:443
2019-06-22 14:18:42,211 DEBUG: https://oauth.reddit.com:443 "GET /r/keybaseproofs/new?raw_json=1&limit=3 HTTP/1.1" 200 4487
2019-06-22 14:18:42,214 DEBUG: Response: 200 (4487 bytes)
2019-06-22 14:18:42,215 DEBUG: Looking up username: kognate
2019-06-22 14:18:42,217 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 14:18:42,681 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=kognate HTTP/1.1" 200 552
Reddit Username: kognate Post Title: My Keybase proof [reddit:kognate = keybase:kognate] (bRXplZlU0BT2WvNup3-sadVe6QJ9hmFfPxPRnI2NehQ) Keybase Key Fingerprint: 6eb2a118d32e55422c960ff642688e295b70a92a
2019-06-22 14:18:42,686 DEBUG: Looking up username: markuszeller
2019-06-22 14:18:42,688 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 14:18:43,132 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=markuszeller HTTP/1.1" 200 559
Reddit Username: markuszeller Post Title: My Keybase proof [reddit:markuszeller = keybase:markuszeller] (JBfTigkQrjEruEoKZfKdi77XbQHfMFY6ErQE0l5R_Lg) Keybase Key Fingerprint: d9221a8381480faaf77653b0e2820ff55aefbc18
2019-06-22 14:18:43,137 DEBUG: Looking up username: time4fun
2019-06-22 14:18:43,138 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 14:18:43,459 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=time4fun HTTP/1.1" 200 488
Reddit Username: time4fun Post Title: My Keybase proof [reddit:time4fun = keybase:time4fun] (q6XSdSzP78VGFNdbBBs_mmrFOhf4-S2zwF7_lGI0x1k) Keybase Key Fingerprint: 7a4f49b351c60d0d36b2c309f351575ff269e9f8

```

##### Live streaming example:
```
# The --live option will look for the latest posts to a subreddit. Depending on the subreddit it may not return any output for quite some time.
$ python redditkeys.py keybaseproofs --live
Reddit Username: peter_borsa Post Title: My Keybase proof [reddit:peter_borsa = keybase:asrob] (lDPe8qmJVBSUtNfaaA9D-jJQhKwREyBQid1OnkXM9Vw) Keybase Key Fingerprint: a4b53a14fbf04c907564ace7c50d719c7fe878ad
Reddit Username: KingDGrizzle Post Title: My Keybase proof [reddit:kingdgrizzle = keybase:kingdgrizzle] (pdvnUNd1qtmMHylORvj_FkkiSLKZU97ORshMFzg2Y8M) Keybase Key Fingerprint: 786b254b2ce81d01397c4c4c9884efd086bb7430
Reddit Username: variiuz Post Title: My Keybase proof [reddit:variiuz = keybase:variiuz] (FWGMSHs_4OY-mlYH_5-z1mSDCZ25afhN-NXm5r7a6wA) Keybase Key Fingerprint: 59cb9f71e18111f67064b1932cfe30d55543d882
Reddit Username: sajjadium Post Title: My Keybase proof [reddit:sajjadium = keybase:sajjadium] (r2kwvSIdTaUvlmWtwTCtRA_AHeUgoFvOUtoUpn70ayU) Keybase Key Fingerprint: ab9161532aeaf01317e5b44124b43fde3e62da38
Reddit Username: Siraf Post Title: My Keybase proof [reddit:siraf = keybase:faris] (C-DOg8Lr-jWQsRiCgjsuDeO8QmsMI6t3b8Uy4MW0MSE) Keybase Key Fingerprint: 1eb9a4c813d20128f9e31dce403ead145c572bb2
Reddit Username: Hackerpcs Post Title: My Keybase proof [reddit:Hackerpcs = keybase:hackerpcs] (Gv6x_vU9eZdbRh7whYfjHVUeL6KwIiyqw8WTWoHbiOk) Keybase Key Fingerprint: 2070f225c482bf40c63585e17e9c4cd863812aaa

```


##### Live streaming example with debug output turned on:
```
$ python redditkeys.py keybaseproofs --live -v
2019-06-22 15:16:02,933 DEBUG: Fetching: GET https://oauth.reddit.com/r/keybaseproofs/new
2019-06-22 15:16:02,933 DEBUG: Data: None
2019-06-22 15:16:02,933 DEBUG: Params: {'raw_json': 1, 'limit': 100, 'before': None}
2019-06-22 15:16:02,939 DEBUG: Starting new HTTPS connection (1): www.reddit.com:443
2019-06-22 15:16:03,075 DEBUG: https://www.reddit.com:443 "POST /api/v1/access_token HTTP/1.1" 200 106
2019-06-22 15:16:03,081 DEBUG: Starting new HTTPS connection (1): oauth.reddit.com:443
2019-06-22 15:16:04,111 DEBUG: https://oauth.reddit.com:443 "GET /r/keybaseproofs/new?raw_json=1&limit=100 HTTP/1.1" 200 57965
2019-06-22 15:16:04,126 DEBUG: Response: 200 (57965 bytes)
2019-06-22 15:16:04,155 DEBUG: Looking up username: peter_borsa
2019-06-22 15:16:04,157 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:04,580 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=peter_borsa HTTP/1.1" 200 562
Reddit Username: peter_borsa Post Title: My Keybase proof [reddit:peter_borsa = keybase:asrob] (lDPe8qmJVBSUtNfaaA9D-jJQhKwREyBQid1OnkXM9Vw) Keybase Key Fingerprint: a4b53a14fbf04c907564ace7c50d719c7fe878ad
2019-06-22 15:16:04,584 DEBUG: Looking up username: KingDGrizzle
2019-06-22 15:16:04,586 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:04,927 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=KingDGrizzle HTTP/1.1" 200 517
Reddit Username: KingDGrizzle Post Title: My Keybase proof [reddit:kingdgrizzle = keybase:kingdgrizzle] (pdvnUNd1qtmMHylORvj_FkkiSLKZU97ORshMFzg2Y8M) Keybase Key Fingerprint: 786b254b2ce81d01397c4c4c9884efd086bb7430
2019-06-22 15:16:04,930 DEBUG: Looking up username: aaantoszek
2019-06-22 15:16:04,931 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:05,333 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=aaantoszek HTTP/1.1" 200 494
2019-06-22 15:16:05,338 DEBUG: No public key fingerprint
2019-06-22 15:16:05,338 DEBUG: Looking up username: Terence1907
2019-06-22 15:16:05,340 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:05,656 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=Terence1907 HTTP/1.1" 200 382
2019-06-22 15:16:05,660 DEBUG: No public key fingerprint
2019-06-22 15:16:05,660 DEBUG: Looking up username: gtranchedone
2019-06-22 15:16:05,661 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:05,979 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=gtranchedone HTTP/1.1" 200 431
2019-06-22 15:16:05,984 DEBUG: No public key fingerprint
2019-06-22 15:16:05,984 DEBUG: Looking up username: variiuz
2019-06-22 15:16:05,986 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:06,410 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=variiuz HTTP/1.1" 200 589
Reddit Username: variiuz Post Title: My Keybase proof [reddit:variiuz = keybase:variiuz] (FWGMSHs_4OY-mlYH_5-z1mSDCZ25afhN-NXm5r7a6wA) Keybase Key Fingerprint: 59cb9f71e18111f67064b1932cfe30d55543d882
2019-06-22 15:16:06,415 DEBUG: Looking up username: RrRBudDwyer
2019-06-22 15:16:06,417 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:06,966 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=RrRBudDwyer HTTP/1.1" 200 420
2019-06-22 15:16:06,970 DEBUG: No public key fingerprint
2019-06-22 15:16:06,970 DEBUG: Looking up username: sajjadium
2019-06-22 15:16:06,972 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:07,296 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=sajjadium HTTP/1.1" 200 595
Reddit Username: sajjadium Post Title: My Keybase proof [reddit:sajjadium = keybase:sajjadium] (r2kwvSIdTaUvlmWtwTCtRA_AHeUgoFvOUtoUpn70ayU) Keybase Key Fingerprint: ab9161532aeaf01317e5b44124b43fde3e62da38
2019-06-22 15:16:07,300 DEBUG: Looking up username: Siraf
2019-06-22 15:16:07,302 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:07,645 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=Siraf HTTP/1.1" 200 517
Reddit Username: Siraf Post Title: My Keybase proof [reddit:siraf = keybase:faris] (C-DOg8Lr-jWQsRiCgjsuDeO8QmsMI6t3b8Uy4MW0MSE) Keybase Key Fingerprint: 1eb9a4c813d20128f9e31dce403ead145c572bb2
2019-06-22 15:16:07,651 DEBUG: Looking up username: Hackerpcs
2019-06-22 15:16:07,653 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:08,012 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=Hackerpcs HTTP/1.1" 200 498
Reddit Username: Hackerpcs Post Title: My Keybase proof [reddit:Hackerpcs = keybase:hackerpcs] (Gv6x_vU9eZdbRh7whYfjHVUeL6KwIiyqw8WTWoHbiOk) Keybase Key Fingerprint: 2070f225c482bf40c63585e17e9c4cd863812aaa
2019-06-22 15:16:08,017 DEBUG: Looking up username: mbanks850
2019-06-22 15:16:08,019 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:08,411 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=mbanks850 HTTP/1.1" 200 387
2019-06-22 15:16:08,417 DEBUG: No public key fingerprint
2019-06-22 15:16:08,417 DEBUG: Looking up username: Kiruu_
2019-06-22 15:16:08,418 DEBUG: Starting new HTTPS connection (1): keybase.io:443
2019-06-22 15:16:08,828 DEBUG: https://keybase.io:443 "GET /_/api/1.0/user/discover.json?reddit=Kiruu_ HTTP/1.1" 200 790
Reddit Username: Kiruu_ Post Title: My Keybase proof [reddit:kiruu_ = keybase:kiru] (4Xr7tK01nV8uFmZpkU-hQyiGkHxhM2oa9KxctJ9soWc) Keybase Key Fingerprint: c27ebe0c718ff5b3b7db15ec8554d2c771000a17

```



