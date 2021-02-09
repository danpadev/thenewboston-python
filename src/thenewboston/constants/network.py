HTTP = 'http'
HTTPS = 'https'

PROTOCOL_CHOICES = [
    (HTTP, HTTP),
    (HTTPS, HTTPS),
]

PROTOCOL_LIST = [HTTP, HTTPS]

BANK = 'BANK'
CONFIRMATION_VALIDATOR = 'CONFIRMATION_VALIDATOR'
PRIMARY_VALIDATOR = 'PRIMARY_VALIDATOR'

ACCOUNT_FILE_HASH_LENGTH = 64
BALANCE_LOCK_LENGTH = 64
BLOCK_IDENTIFIER_LENGTH = 64
HEAD_HASH_LENGTH = 64
SIGNATURE_LENGTH = 128
VERIFY_KEY_LENGTH = 64

MIN_POINT_VALUE = 1
MAX_POINT_VALUE = 281474976710656

ACCEPTED_FEES = [BANK, PRIMARY_VALIDATOR]
