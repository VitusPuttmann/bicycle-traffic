"""
Function for signing a manifest with a private key.
"""

import base64
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import load_pem_private_key
import json
import os


def sign_manifest(manifest: dict) -> dict:
    """
    Adds a detached Ed25519 signature over the canonical manifest JSON.
    """

    payload = json.dumps(
        {k: v for k, v in manifest.items() if k != "signature"},
        sort_keys=True,
        ensure_ascii=False
    ).encode()

    key_b64 = os.getenv("MANIFEST_SIGNING_KEY")
    if not key_b64:
        raise RuntimeError("MANIFEST_SIGNING_KEY environment variable not set")
    private_key = load_pem_private_key(base64.b64decode(key_b64), password=None)

    sig = private_key.sign(payload)
    manifest["signature"] = {
        "algorithm": "Ed25519",
        "value": base64.b64encode(sig).decode(),
        "key_id": "manifest_signing.pub",
    }

    return manifest
