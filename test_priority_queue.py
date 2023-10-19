import unittest
from priority_queue import TaskQueue, Task, Resources

class TestTaskQueue(unittest.TestCase):
    def setUp(self):
        # Set up the task queue and tasks for each test
        self.queue = TaskQueue()
        self.task1 = Task(id=1, priority=3, resources=Resources(4, 2, 1), content="Task 1", result="Result 1")
        self.task2 = Task(id=2, priority=2, resources=Resources(2, 1, 0), content="Task 2", result="Result 2")
        self.task3 = Task(id=3, priority=5, resources=Resources(8, 4, 2), content="Task 3", result="Result 3")

    def test_task_selection(self):
        self.queue.add_task(self.task1)
        self.queue.add_task(self.task2)
        self.queue.add_task(self.task3)

        available_resources = Resources(6, 3, 1)

        # Get the highest priority task that can be processed with available resources
        selected_task = self.queue.get_task(available_resources)
        self.assertEqual(selected_task.id, 1)  # Task 1 has the highest priority and can be processed
        available_resources = Resources(2, 1, 0)
    
        # Get the highest priority task that can be processed with available resources
        selected_task = self.queue.get_task(available_resources)
        self.assertEqual(selected_task.id, 2)  # Task 2 has the highest priority and can be processed

        available_resources = Resources(10, 5, 3)
    
        # Get the highest priority task that can be processed with available resources
        selected_task = self.queue.get_task(available_resources)
        self.assertEqual(selected_task.id, 3)  # Task 3 has the highest priority and can be processed

        available_resources = Resources(1, 1, 1)
    
        # No task can be processed with the available resources
        selected_task = self.queue.get_task(available_resources)
        self.assertIsNone(selected_task)

if __name__ == "__main__":
    unittest.main()
