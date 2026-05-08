class TimeMap:

    def __init__(self):
        self.storage = {}
        self.ts = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.storage:
            self.storage[key][timestamp] = value
            self.ts[key].append(timestamp)
        else:
            self.storage[key] = {}
            self.storage[key][timestamp] = value
            self.ts[key] = []
            self.ts[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        print("GET KEY:", key, "AT TS:", timestamp)
        if key not in self.storage:
            return ""

        if timestamp in self.storage[key]:
            return self.storage[key][timestamp]
        
        ts = self.ts[key]
        max_ts = ts[-1]
        if timestamp > max_ts:
            return self.storage[key][max_ts]
        
        min_ts = ts[0]
        if timestamp < min_ts:
            return ""

        l = 1
        r = len(ts)
        while l <= r:
            i = (l + r) // 2
            if l == r:
                if timestamp == ts[l]:
                    return self.storage[key][ts[l]]
                if timestamp > ts[l]:
                    return self.storage[key][ts[l]]
                elif timestamp < ts[l]:
                    return self.storage[key][ts[l-1]]
            if timestamp > ts[i]:
                if r - l == 1:
                    l = r
                else:
                    l = i

            elif timestamp < ts[i]:
                r = i










