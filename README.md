# eric's relay.sh workflow repo

This repo is synced to my [Relay.sh](https://relay.sh/) account via webhook.

PRs that merge workflows/*.yaml to the `main` branch are automatically synced
to the service, so I can keep things in git without having to sync a bunch of
files around.

The Ourobouros workflow that makes this happen is itself stored in the repo
at workflows/relay-update-on-commit.yaml. Feel free to use it if you want!

![Relay.sh](https://github.com/puppetlabs/relay/raw/master/docs/relay-logo.svg?sanitize=true)
