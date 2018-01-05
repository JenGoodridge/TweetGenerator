# Tweet Generator
Generates new tweets by feeding a Twitter user's timeline through a Markov chain.

## Dependencies
Requires Python 3 and the [Twitter](http://mike.verdone.ca/twitter/) and [Requests](http://python-requests.org) libraries.

## Setup
Requires a `config.py` to be created in the project directory containing

```python
CONSUMER_KEY    = <Twitter consumer key>
CONSUMER_SECRET = <Twitter consumer secret>
```

in order to authenticate with the Twitter API.

## Running
Can be run with `python3 GenerateTweet.py`. The first time the tool runs, it will perform the OAuth dance, and will save the fetched credentials to `~/.jtwitter`.

# Next Steps

1. Further cleanup of the project
2. Improvements to the interface — allowing command-line arguments to specify what Twitter profile to generate from (currently hard-coded), multiple Twitter timelines, etc.
