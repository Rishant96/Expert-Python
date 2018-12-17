import time
import hashlib
import pickle


cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.shal(key).hexdigest()


def memorize(duration=10):
    def _memorize(function):
        def __memorize(*args, **kwargs):
            key = compute_key(function, args, kwargs)

            # do we have it already ?
            if (key in cache and
                    not is_obsolete(cache[key], duration)):
                print('we got a winner')
                return cache[key]['value']

            # computing
            result = function(*args, **kwargs)
            # storing the result
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result
        return __memorize
    return _memorize
