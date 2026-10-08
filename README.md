# Starship Control Client

Starship Control Client is a small command-line client used by deployment
operators to inspect the active control-plane environment before a release.

## Authentication providers

The client discovers deployment-specific authentication through the
`starship.auth` Python entry-point group. Providers are installed separately
because production, staging, and on-premises deployments use different
credential issuers. The core client intentionally does not select or bundle a
provider.

Set `STARSHIP_API_KEY` and `STARSHIP_CLIENT_ID` according to your deployment's
provider documentation before starting the client. A provider may validate a
configured credential with its issuer before returning an authentication
configuration.

## Usage

```bash
python3 app.py status
```

The `status` command prints the selected deployment and authentication state.

## Development

```bash
python3 -m unittest discover -s tests
```

## License

MIT
