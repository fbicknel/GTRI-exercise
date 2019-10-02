#!/usr/bin/env python

import requests

def get_document(operation='tika'):
    url = f'http://localhost:4242/{operation}'
    upfile = 'data/foo.pdf'
    headers = {'Content-type': 'application/pdf'}
    files = {'file': open(upfile, 'rb')}
    response = requests.put(url=url,
                            files=files,
                            headers=headers,
                            )
    print(response.text)

if __name__ == '__main__':
    get_document()
