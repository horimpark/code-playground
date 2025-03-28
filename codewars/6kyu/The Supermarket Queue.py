def queue_time(customers, n):
    if n == 1:
        return sum(customers)
    if n >= len(customers):
        return max(customers)
    queue = [0] * n
    for customer in customers:
        queue[queue.index(min(queue))] += customer
    return max(queue)


if __name__ == '__main__':
    print(queue_time([5, 3, 4], 1), 12)
    print(queue_time([10, 2, 3, 3], 2), 10)
