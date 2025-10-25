import argparse
from pylognet.server import LoggingService


parser = argparse.ArgumentParser(description="Run the FastAPI application.")
parser.add_argument(
    "-p",
    "--port",
    type=int,
    default=9000,
    help="Port to run the FastAPI application on",
)
args = parser.parse_args()

if __name__ == "__main__":
    service = LoggingService()
    service.run(port=args.port)
