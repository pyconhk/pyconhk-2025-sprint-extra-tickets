import os
import subprocess
import textwrap
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

KEY_PART_A = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu45PzGP"
KEY_PART_B = "XNEnPL<name>HWWHKR0qjz2ak5I5wQAwjDnaHrj7q82OQ3d03GSdwIg+SWFNluQbKc4aEYQHtHafLM17"
KEY_PART_C = "WwlWwQ7OpUPMmUGsIyzG/fBA6Z+ELIgKi8RE9HhMvGvV{missing_char}"
KEY_PART_D = "efFofbTg4PixSaXVcJ07htZOpdfHqeNOcKlGcgK{0}cfxsu/pOZ+G3Z6QEuHdoF9hrkWK3fwCTOLkvbD4E1OmWU"
KEY_PART_E = "6q6x+9ls2dupgJRPYcPtBlJwCwgTnKvTVEPcmC9RP99XVdIQ1EsciD6ye/IzwRLRwTggvU3MsI8/F6X7OKky9CoKg4832MGwYeGUf8iA2yHj+"
REVERSED_KEY_PART_F = "BAQADIQFw6TsacXFOuiVmKA"

def create_public_key(*key_parts: str):
    first_key_part, second_key_part, *rest_key_parts = key_parts
    second_key_part = second_key_part.replace("<name>", Path(__file__).stem.replace("e","").upper())
    key_str = "".join([first_key_part, second_key_part, *rest_key_parts])

    return textwrap.dedent(
        f"""
        -----BEGIN PUBLIC KEY-----
        {key_str}
        -----END PUBLIC KEY-----
        """
    ).strip()


@contextmanager
def set_encrypted_environment(public_key: str):
    """Encrypts ENV_CONST with the public key and sets it as an environment variable."""
    
    public_key_obj = serialization.load_pem_public_key(public_key.encode())
    env_const = ""
    env_const_indices = [11, 174, 16, 205, 81, 89, 18, 99, 73, 84, 165, 114, 41, 81, 149, 132]
    for index in env_const_indices:
        env_const += public_key[index]
    
    encrypted = public_key_obj.encrypt(
        env_const.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    with patch.dict(os.environ, {"CTF_ENV": encrypted.hex()}):
        yield

####### Main Challenge Code, don't touch the code above! #######

def main():
    
    key_part_c_missing_char = 'W'
    
    public_key = create_public_key(
        (                                       #? How can the public key be reconstructed if the first argument is a tuple?
            KEY_PART_A,
            KEY_PART_B 
        ),
        KEY_PART_C.format(<ans>),               #? Fill in the missing character
        KEY_PART_D.format(f'{<ans>:X}'),        #? What anniversary is PyConHK 2025? Fill in the missing number
        KEY_PART_E,
        <ans>                                   #? We need a 'unreversed' REVERSED_KEY_PART_F here
    )

    with set_encrypted_environment(<ans>):      #? Please fill in the missing argument

####### Main Challenge Code, don't touch the code below! #######

        subprocess.run("./encryptor") 

if __name__ == "__main__":
    main()
