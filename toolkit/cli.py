
import argparse
from .protocol import run_protocol_audit

def main():
    parser = argparse.ArgumentParser(description="CTF Protocol Analysis Toolkit")
    sub = parser.add_subparsers(dest="command")

    proto = sub.add_parser("protocol-audit")
    proto.add_argument("--host")
    proto.add_argument("--port", type=int)
    proto.add_argument("--script")
    proto.add_argument("--replay")
    proto.add_argument("--fuzz", action="store_true")

    args = parser.parse_args()

    if args.command == "protocol-audit":
        run_protocol_audit(args)

if __name__ == "__main__":
    main()
