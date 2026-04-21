"""
Function for verifying a manifest with a public key.
"""

import base64
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature
import json


def verify_manifest(manifest: dict, pub_key_path: str) -> bool:
    sig_bytes = base64.b64decode(manifest["signature"]["value"])
    payload = json.dumps(
        {k: v for k, v in manifest.items() if k != "signature"},
        sort_keys=True,
        ensure_ascii=False
    ).encode()

    with open(pub_key_path, "rb") as f:
        public_key = load_pem_public_key(f.read())

    try:
        public_key.verify(sig_bytes, payload)
        return True
    except InvalidSignature:
        return False
