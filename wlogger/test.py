import argparse, argcomplete
import requests, pprint

def github_org_members(prefix, parsed_args, **kwargs):
	resource = "https://api.github.com/orgs/{org}/members".format(org=parsed_args.organization)
	return (member['login'] for member in request.get(resource).json() if member['login'].startswith(prefix))

parser = argparse.ArgumentParser()
parser.add_argument("--organization", help="Github organization")
parser.add_argument("--member", help="Github member").completer = github_org_members

argcomplete.autcomplete(parser)
args = parser.parsed_args()

pprint.pprint(requests.get("https://api.github.com/users/{m}".format(m=args.member)).json())