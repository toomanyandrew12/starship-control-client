# Authentication provider contract

Starship Control Client keeps authentication provider selection outside the
core package. Each deployment installs one distribution that registers a
callable in the `starship.auth` entry-point group.

The callable receives the application name and returns a mapping containing a
non-empty `token` plus an optional `enabled` flag. Providers may read
`STARSHIP_API_KEY` and `STARSHIP_CLIENT_ID` and may validate those values with
their credential issuer before returning.

Provider distributions and issuer endpoints are selected by deployment
operators; this repository does not maintain a global allowlist.
