# GNU social export

Python script which allows to export a list of followed users. This list can be imported to Mastodon.

## Setup & usage

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env  # and edit the .env file
python gnu-social-export.py > friends.csv       # for the list of the users you are following
python gnu-social-export.py -f > followers.csv  # for the list of your followers
```

