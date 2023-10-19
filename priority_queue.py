import heapq
from dataclasses import dataclass

@dataclass
class Resources:
    __slots__ = ('ram', 'cpu_cores', 'gpu_count')

    ram: int
    cpu_cores: int
    gpu_count: int

@dataclass
class Task:
    __slots__ = ('id', 'priority', 'resources', 'content', 'result')

    id: int
    priority: int
    resources: Resources
    content: str
    result: str

class TaskQueue:
    
    def __init__(self):
        self.queue = []
    
    def add_task(self, task: Task):
        """
        Add a task to the queue.
        """
        heapq.heappush(self.queue, (-task.priority, task))

    def get_task(self, available_resources: Resources) -> Task:
        """
        Get the highest priority task that can be processed with available resources.
        Returns None if no task can be processed.
        """
        back_to_queue = []
        task = None
        queue_length = len(self.queue)

        for _ in range(queue_length):
            priority, task = heapq.heappop(self.queue)
            if self.can_process(task, available_resources):
                break
            else:
                back_to_queue.append((priority, task))

        for item in back_to_queue:
            heapq.heappush(self.queue, item)

        return task

    def can_process(self, task: Task, available_resources: Resources) -> bool:
        """
        Check if a task can be processed with the available resources.
        """
        return (task.resources.ram <= available_resources.ram and
                task.resources.cpu_cores <= available_resources.cpu_cores and
                task.resources.gpu_count <= available_resources.gpu_count)
