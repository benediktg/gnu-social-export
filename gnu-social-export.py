import argparse
import os

import requests
from dotenv import load_dotenv


def main():
    ap = argparse.ArgumentParser(
        description='Export the list of followed users from GNU social',
    )
    ap.add_argument(
        '-e', '--envfile',
        nargs='?',
        default='.env',
    )
    ap.add_argument(
        '-o', '--outfile',
        nargs='?',
        default='following_accounts.csv',
    )
    args = ap.parse_args()
    load_dotenv(args.envfile)
    hostname = os.environ['GNU_SOCIAL_HOST']
    username = os.environ['GNU_SOCIAL_USER']
    password = os.environ['GNU_SOCIAL_PASS']

    r = requests.get(
        '{host}/api/statuses/friends.json'.format(host=hostname),
        auth=(username, password),
    )
    accounts = {
        '{}@{}\n'.format(
            account['screen_name'],
            account['statusnet_profile_url'].split('/')[2],
        )
        for account in r.json()
    }

    with open(args.outfile, 'w') as f:
        f.writelines(accounts)


if __name__ == '__main__':
    main()
