from redis.client import Redis

CACHE_PREFIX = "TRDBT"


class CacheClient:
    def __init__(self):
        self._client: Redis = self._setup()

    def get(self, key):
        self._client.get(self._get_composite_key(key))

    def set(self, key, value):
        self._client.set(self._get_composite_key(key), value)

    def delete(self, key):
        self._client.delete(self._get_composite_key(key))

    def _setup(self) -> Redis:
        return Redis(host="127.0.0.1", port=6379)

    def _get_composite_key(self, key):
        return CACHE_PREFIX + key


local_cache = CacheClient()
