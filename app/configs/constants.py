import os 

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_QUEUE = os.getenv('REDIS_QUEUE', 'default')
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL', '')
