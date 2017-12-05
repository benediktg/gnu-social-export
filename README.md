# GNU social export

Python script which allows to export a list of followed users. This list can be imported to Mastodon.

## Usage

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.sample .env  # and edit the .env file
python gnu-social-export.py
```
