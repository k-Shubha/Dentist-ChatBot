import os
from os.path import join, dirname
from dotenv import load_dotenv  # need to `pip install -U python-dotenv`

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
print(dotenv_path)

# Load file from the path.
load_dotenv(dotenv_path)

# Accessing variables.
ACCOUNT_SID = 'ACf11ed3930668c68e3ea357bb6543902e'
AUTH_TOKEN = '012d8bd5856136d5fac10fc05514bd1d'