# eric's relay.sh workflow repo

This repo is synced to my [Relay.sh](https://relay.sh/) account via webhook.

PRs that merge workflows/*.yaml to the `main` branch are automatically synced
to the service, so I can keep things in git without having to sync a bunch of
files around.

This happens via github actions, which you can see in the [.github/workflows]
directory. 

There is an equivalent relay workflow in [workflows/relay-update-on-commit.yaml]

![Relay.sh](https://github.com/puppetlabs/relay/raw/master/docs/relay-logo.svg?sanitize=true)
