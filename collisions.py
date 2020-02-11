import random

def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1

            else:
                # We found collision
                break

    print(f"{buckets} buckets, {tries} hashes before collision. {tries / buckets * 100:.1f}%")

# how_many_before_collision(32, 10)

def longest_linked_list(keys, buckets, loops=10):
    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"Longest linked list chain for {key} keys in {buckets} buckets (Load factor: {keys / buckets:2f}: {largest_n}")

longest_linked_list(16, 16, 10)