"""Command line entry point for the Finesse toolkit."""

from __future__ import annotations

import argparse


def main() -> None:
    """Parse command line arguments and dispatch commands."""

    parser = argparse.ArgumentParser(description="Finesse FSM toolkit")
    parser.parse_args()
    print("Finesse CLI is not yet implemented.")


if __name__ == "__main__":
    main()
