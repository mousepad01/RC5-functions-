from RC5 import RC5_key_generator, RC5_block_decryptor, RC5_block_encryptor
import secrets


key = secrets.randbits(4096)

s_k = RC5_key_generator(key, 128, 100, 512)

msg = 'hai ca merge !!! voi mai testa !'

encrypted = RC5_block_encryptor(msg, s_k, 128, 100)

print(encrypted)

decr = RC5_block_decryptor(encrypted, s_k, 128, 100)

print(decr)

