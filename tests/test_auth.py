"""Tests for the provider-discovery boundary."""

import unittest
from unittest.mock import patch

import app


class MissingProviderTest(unittest.TestCase):
    @patch.object(app, "entry_points", return_value=[])
    def test_missing_provider_is_explicit(self, _entry_points) -> None:
        with self.assertRaisesRegex(RuntimeError, "AuthConfig not found"):
            app.load_auth_config()


if __name__ == "__main__":
    unittest.main()
