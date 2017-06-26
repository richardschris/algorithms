class HashMap():
    def __init__(self, size=1024):
        self.size = size
        self.map = [None] * size

    def add(self, key, value):
        self._check_size()
        map_val = self.map[hash(key) % self.size]
        if map_val is not None and (key, value) not in map_val:
            self.map[hash(key) % self.size].append((key, value))
        elif map_val is not None and (key, value) in map_val:
            return self
        else:
            self.map[hash(key) % self.size] = [(key, value)]
        return self

    def get(self, key):
        self._check_size()
        map_val = self.map[hash(key) % self.size]
        if map_val is None:
            raise ValueError('Invalid key!')
        else:
            for k, v in map_val:
                if k == key:
                    return v
        raise ValueError('Invalid key!')

    def _check_size(self):
        if None in self.map:
            return
        else:
            new_size = self.size * 2
            temp_map = [None] * new_size
            for hashed_key in self.map:
                for k, v in hashed_key:
                    new_map_val = temp_map[hash(k) % new_size]
                    if new_map_val is not None and v not in new_map_val:
                        temp_map[hash(k) % new_size].append((k, v))
                    elif new_map_val is not None and v in new_map_val:
                        continue
                    else:
                        temp_map[hash(k) % new_size] = [(k, v)]
            self.map = temp_map
            self.size = new_size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.add(key, value)