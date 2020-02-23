#!/usr/bin/env python3

import connexion
import os

from openapi_server import encoder


def main():
    port = int(os.environ.get("PORT", 8080))
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'LoL prediction'},
                pythonic_params=True)
    app.run(port=port)


if __name__ == '__main__':
    main()
