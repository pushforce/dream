import os

BADLISTED_WORDS_URL = os.getenv('BADLISTED_WORDS_URL', 'http://localhost:8018')
SPACY_NOUNPHRASES_URL = os.getenv('SPACY_NOUNPHRASES_URL', 'http://localhost:8006')
PG_URL = os.getenv('PG_URL', 'postgresql+asyncpg://postgres:postgres@localhost/test')
