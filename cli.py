import argparse
from pprint import pprint

from web import get_data, get_token

parser = argparse.ArgumentParser()
parser.add_argument("--username", type=str, help="SRM netID username")

parser.add_argument("--password", type=str, help="SRM password")

args = parser.parse_args()
token = get_token(username=args.username, password=args.password)
data = get_data(token_dict=token)

pprint(data)
