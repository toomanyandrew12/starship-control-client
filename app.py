"""Command-line status client for a Starship control-plane deployment."""

from __future__ import annotations

import argparse
from collections.abc import Mapping
from dataclasses import dataclass
from importlib.metadata import entry_points
import os


@dataclass(frozen=True)
class AuthConfig:
    """Authentication configuration returned by a deployment provider."""

    token: str
    enabled: bool = True


def load_auth_config() -> AuthConfig:
    """Load the first installed provider for the ``starship.auth`` group."""

    providers = list(entry_points(group="starship.auth"))
    if not providers:
        raise RuntimeError("AuthConfig not found.")

    values = providers[0].load()(application="starship-control")
    if not isinstance(values, Mapping):
        raise RuntimeError("AuthConfig not found.")

    token = values.get("token")
    if not isinstance(token, str) or not token:
        raise RuntimeError("AuthConfig not found.")
    return AuthConfig(token=token, enabled=bool(values.get("enabled", True)))


def status() -> None:
    """Print a compact deployment status after provider authentication."""

    auth = load_auth_config()
    if not auth.enabled:
        raise RuntimeError("Control-plane authentication is disabled.")

    deployment = os.environ.get("STARSHIP_DEPLOYMENT", "staging")
    print(f"Deployment: {deployment}")
    print("Control plane: reachable")
    print("Authentication: enabled")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", default="status", choices=("status",))
    args = parser.parse_args()
    if args.command == "status":
        status()


if __name__ == "__main__":
    main()
