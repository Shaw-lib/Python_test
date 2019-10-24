def time_count(key: str, limit: int, seconds: int) -> (bool, int):
    """
    限制指定时间内最多执行多少次
    :param key: 缓存key
    :param limit: 限制次数
    :param seconds: 多少秒内
    :return: 是否超过限制， 下次重试时间
    """
    times = cache.get(key, 0)
    if times >= limit:
        return False, cache.ttl(key)
    elif times == 0:
        cache.set(key, times + 1, seconds)
    else:
        cache.set(key, times + 1, cache.ttl(key))
    return True, 0
