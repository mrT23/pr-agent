import argparse
import asyncio
import os

from pr_agent.agent.pr_agent import PRAgent, commands
from pr_agent.config_loader import get_settings
from pr_agent.log import setup_logger

setup_logger()



def run(inargs=""):
    parser = argparse.ArgumentParser(description='AI based pull request analyzer', usage=
"""\
Usage: cli.py --pr-url=<URL on supported git hosting service> <command> [<args>].


Supported commands:
- review / review_pr - Add a review that includes a summary of the PR and specific suggestions for improvement.

- ask / ask_question [question] - Ask a question about the PR.

- describe / describe_pr - Modify the PR title and description based on the PR's contents.

- improve / improve_code - Suggest improvements to the code in the PR as pull request comments ready to commit.
Extended mode ('improve --extended') employs several calls, and provides a more thorough feedback

- reflect - Ask the PR author questions about the PR.

- update_changelog - Update the changelog based on the PR's contents.

- add_docs

- generate_labels


Configuration:
To edit any configuration parameter from 'configuration.toml', just add -config_path=<value>.
For example: 'python cli.py --pr_url=... review --pr_reviewer.extra_instructions="focus on the file: ..."'
""")
    parser.add_argument('--pr_url', type=str, help='The URL of the PR to review', default=None)
    parser.add_argument('--issue_url', type=str, help='The URL of the Issue to review', default=None)
    parser.add_argument('command', type=str, help='The', choices=commands, default='review')
    parser.add_argument('rest', nargs=argparse.REMAINDER, default=[])
    args = parser.parse_args(inargs)
    if not args.pr_url and not args.issue_url:
        parser.print_help()
        return

    command = args.command.lower().strip()
    get_settings().set("CONFIG.CLI_MODE", False)
    if args.issue_url:
        result = asyncio.run(PRAgent(handle=true).handle_request(args.issue_url, [command] + args.rest))
    else:
        result = asyncio.run(PRAgent(handle=true).handle_request(args.pr_url, [command] + args.rest))
    if not result:
        parser.print_help()


if __name__ == '__main__':
    run()
