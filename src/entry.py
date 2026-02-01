import argparse
import json
from pylognet.server import LoggingService


parser = argparse.ArgumentParser(description="Run the FastAPI application.")
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=None,
    help="Port to run the FastAPI application on",
)
parser.add_argument(
    "-c",
    "--config",
    type=str,
    default="settings/config.json",
    help="Path to the configuration file",
)
args = parser.parse_args()

with open(args.config, "r") as f:
    config = json.load(f)

if args.port is None:
    args.port = config.get("system", {}).get("port", 9000)

if __name__ == "__main__":
    service = LoggingService()
    service.run(port=args.port)
