class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        window = []
        num = 0
        for item, counts in range(sum(counter.values())):
            print(counter[item])
        return sum(counter.values())