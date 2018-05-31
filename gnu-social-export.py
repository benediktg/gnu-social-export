import argparse
import os
import sys

import requests
from dotenv import load_dotenv


def main():
    ap = argparse.ArgumentParser(
        description='Export the list of followed users from GNU social',
    )
    ap.add_argument(
        '-e', '--envfile', nargs='?', default='.env',
        help='path to the environment file')
    ap.add_argument(
        '-f', '--followers', action='store_true',
        help='export list of followers instead of friends')
    args = ap.parse_args()
    load_dotenv(args.envfile)
    apiroot = os.environ['GNU_SOCIAL_HOST'] + '/api/'
    credentials = (os.environ['GNU_SOCIAL_USER'],
                   os.environ['GNU_SOCIAL_PASS'])
    pagesize = 100
    resource = 'followers' if args.followers is True else 'friends'

    r = requests.get(
        apiroot + 'statuses/user_timeline.json', auth=credentials)
    page_count = r.json()[0]['user'][resource + '_count'] // pagesize + 1
    e_print('will make {} requests'.format(page_count))

    accounts = []
    for i in range(1, page_count + 1):
        r = requests.get(
            '{}statuses/{}.json?count={}&page={}'.format(
                apiroot, resource, pagesize, i),
            auth=credentials)
        accounts += [
            '@'.join([
                account['statusnet_profile_url'].split('/')[-1].lstrip('@'),
                account['statusnet_profile_url'].split('/')[2],
            ])
            for account in r.json()
        ]
        e_print('request #{} processed'.format(i))

    e_print('finished')
    for acc in accounts:
        print(acc)


def e_print(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if __name__ == '__main__':
    main()
