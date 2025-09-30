import argparse
import os
import pathlib
import base64

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--order-id")
    parser.add_argument("--key-path")
    args = parser.parse_args()

    order_id = (args.order_id or input("Order id: ")).strip()
    private_key_path = pathlib.Path(
        args.key_path or input("Private Key Path: ").strip()
    )

    private_key = serialization.load_pem_private_key(
        private_key_path.read_bytes(),
        password=None,
        backend=default_backend(),
    )

    os.makedirs("tickets", exist_ok=True)
    tickets_dir = pathlib.Path("tickets")
    tickets_dir.mkdir(parents=True, exist_ok=True)

    order_id_file = tickets_dir / f"{order_id}.txt"

    order_id_signature = private_key.sign(
        order_id.encode(),
        ec.ECDSA(hashes.SHA256()),
    )

    order_id_file.write_text(base64.b64encode(order_id_signature).decode())
    print(
        f"Generated {str(order_id_file)}. Now you can create Pull Request to submit your ticket!"
    )


if __name__ == "__main__":
    raise SystemExit(main())
