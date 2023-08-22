import heapq

class MaxFiveQueue:
    def __init__(self):
        self.queue = []

    def push(self, value):
        heapq.heappush(self.queue, value)
        if len(self.queue) > 5:
            heapq.heappop(self.queue)

    def get_max_five(self):
        return sorted(self.queue, reverse=True)

# Создаем объект
max_five_queue = MaxFiveQueue()

# Добавляем элементы
max_five_queue.push(10)
max_five_queue.push(5)
max_five_queue.push(15)
max_five_queue.push(3)
max_five_queue.push(12)
max_five_queue.push(20)
max_five_queue.push(8)

# Получаем пять самых больших элементов
max_elements = max_five_queue.get_max_five()
print(max_elements)
