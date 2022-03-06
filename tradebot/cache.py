from redis.client import Redis

CACHE_PREFIX = "TRDBT"


class CacheClient:
    def __init__(self):
        self._client: Redis = self._setup()

    def get(self, key):
        self._client.get(self._get_composite_key(key))

    def set(self, key, value, **kwargs):
        self._client.set(self._get_composite_key(key), value, **kwargs)

    def delete(self, *args):
        self._client.delete(self._get_composite_key(*args))

    def _setup(self) -> Redis:
        return Redis(host="127.0.0.1", port=6379)

    def _get_composite_key(self, key):
        return CACHE_PREFIX + key


local_cache = CacheClient()
