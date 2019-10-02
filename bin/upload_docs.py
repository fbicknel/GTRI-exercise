#!/usr/bin/env python

import argparse
import requests

def get_args():
    global args
    parser =  argparse.ArgumentParser()
    parser.add_argument('--file', help='Select a file to upload')
    parser.add_argument('--url', default='http://localhost:4242',
                        help='Give a URL to use for the server')
    args = parser.parse_args()
    return args

def get_stream_type(file):
    '''
    Send a file to the server and let it figure out what the type is
    '''
    global args
    operation='detect/stream'
    url = f'{args.url}/{operation}'
    files = {'file': open(file, 'rb')}
    try:
        r = requests.put(url=url,
                        files=files,
                        )
    except Exception as e:
        print(f'Well, drat. This came back: {e}')
        exit(1)
        if r.status_code != 200:
            raise ValueError(f'Failed to get file type: \
                             {r.reason} ({r.status_code})')
    return r.text

def get_document(operation='tika', file=None, type=None):
    global args
    url = f'{args.url}/{operation}'
    headers = {'Content-type': type}
    try:
        files = {'file': open(file, 'rb')}
    except TypeError:
        print('get_document called with no file?')
        exit(1)
    except FileNotFoundError:
        print(f'I wasn\'t able to find this file: {file}')
        exit(1)
    except Exception as e:
        print(f"oh, foo: {e}")
        raise
    try:
        response = requests.put(url=url,
                                files=files,
                                headers=headers,
                                )
    except Exception as e:
        print(f'Well, THAT didn\'t go well: {e}')
        raise
    if response.status_code != 200:
        raise ValueError(f"Server responded with an error: \
                         {response.reason} ({response.status_code})")
    print('This was the server\'s response:')
    print(response.text)

if __name__ == '__main__':
    options = get_args()
    stream_type = get_stream_type(file=options.file)
    get_document(file=options.file, type=stream_type)
