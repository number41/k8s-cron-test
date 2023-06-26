import logging
import argparse
import time
import random

def parse_args():
    parser = argparse.ArgumentParser(description="dumb program")
    parser.add_argument("--verbose",help="Debug logging")

    return parser.parse_args()


def init_logging(args):
    level = logging.INFO
    if args.verbose:
        level = logging.DEBUG
    logging.basicConfig(level=level, format="%(asctime)s [%(levelname)s] %(message)s")


def do_stuff(args):
    start = time.monotonic()

    logging.info("Starting application")
    logging.debug("Running application with debug on")
    time.sleep(random.randint(0,3))

    logging.warning("Warning about something, I guess")
    time.sleep(random.randint(0,3))

    logging.error("Oh snap, stuff is going down")
    time.sleep(random.randint(0,3))

    logging.info("OK, we're all good")

    end = time.monotonic()
    logging.info("Finished in %s seconds", end-start)


def main():
    args = parse_args()
    init_logging(args)

    do_stuff(args)


if __name__ == "__main__":
    main()