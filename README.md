![testing diagram](test1.drawio.svg)

# Task Queue with Priority and Resource Limits

This Python implementation provides a task queue that allows you to manage tasks based on their priority and required resources. It uses the heap data structure to efficiently organize and access tasks. The code has been designed to handle thousands of tasks with different priorities and resource requirements. To simulate a Max Heap using Python's heapq, priorities are stored as negative values.

## Implementation Details

### Classes

#### Resources
- `Resources` class represents the resources required for each task.
- It includes slots for `ram`, `cpu_cores`, and `gpu_count`.
- You can create instances of `Resources` to specify the resources required by each task.

#### Task
- `Task` class represents individual tasks to be added to the task queue.
- It includes slots for `id`, `priority`, `resources`, `content`, and `result`.
- The `id` uniquely identifies each task, while `priority` defines the task's importance.
- `resources` holds the required resources, and `content` contains the task description.
- `result` can store the outcome of task processing.

#### TaskQueue
- `TaskQueue` class manages the queue of tasks and their processing.
- It uses Python's heapq to implement a priority queue with a Max Heap behavior.
- The `add_task` method adds tasks to the queue based on their priority.
- The `get_task` method retrieves the highest priority task that can be processed with available resources.

### Unit Tests

A set of unit tests is provided to demonstrate the operation of the task queue. These tests ensure the correctness of the implementation and showcase how tasks are selected based on available resources.
`python test_priority_queue.py`

## Time and Space Complexity

The time complexity for the `get_task` method is O(n log n) for the `add_task` it is O (log n). The space complexity is O(n), where n represents the number of tasks in the queue.

## Credits

This implementation was developed by Armen Ghahramanyan within a one-hour time deadline.
