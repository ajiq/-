import sys
import base64
import argparse

def main():
    parser = argparse.ArgumentParser(description='Base64 decoder with streaming or buffered mode.')
    parser.add_argument('--stream', action='store_true', help='Enable streaming mode')
    args = parser.parse_args()

    if args.stream:
        buffer = b''
        while True:
            chunk = sys.stdin.buffer.read(1024)
            if not chunk:
                break
            buffer += chunk
            while len(buffer) >= 4:
                group, buffer = buffer[:4], buffer[4:]
                sys.stdout.buffer.write(base64.b64decode(group))
        if buffer:
            sys.stdout.buffer.write(base64.b64decode(buffer))
    else:
        data = sys.stdin.buffer.read()
        sys.stdout.buffer.write(base64.b64decode(data))

if __name__ == '__main__':
    main()
