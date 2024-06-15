from dotenv import load_dotenv
import os

load_dotenv()

open_datasets_username = os.getenv("OPEN_DATASETS_USERNAME")
open_datasets_key = os.getenv("OPEN_DATASETS_KEY")

print('open_datasets_username', open_datasets_username)
print('open_datasets_key', open_datasets_key)
