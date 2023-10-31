import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
print(MEDIA_ROOT)
