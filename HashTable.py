#Nikita Lesenkovs 231RDB359 8.GR.
class HashTable:
    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def delete(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                del bucket[i]
                return

    def find(self, key):
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if key == k:
                return v
        return "not found"


def phone_book_manager(queries):
    phone_book = HashTable()
    results = []

    for query in queries:
        parts = query.split()
        command = parts[0]
        number = parts[1]

        if command == "add":
            name = parts[2]
            phone_book.add(number, name)
        elif command == "delete":
            phone_book.delete(number)
        elif command == "find":
            result = phone_book.find(number)
            results.append(result)

    return results

queries = [
    "add 911 police",
    "add 76213 Mom",
    "add 17239 Bob",
    "find 76213",
    "find 910",
    "find 911",
    "delete 910",
    "delete 911",
    "find 911",
    "find 76213",
    "add 76213 daddy",
    "find 76213"
]

results = phone_book_manager(queries)
for result in results:
    print(result)
