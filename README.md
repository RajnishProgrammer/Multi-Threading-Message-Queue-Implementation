# Multi-Threaded Priority Message Queue Implementation

This project implements a multi-threaded priority message queue system in Python. It allows multiple threads to send messages to each other with varying priorities and performs simple actions upon receiving messages using a thread pool.

## Table of Contents

1. [Introduction](#introduction)
2. [Architecture Overview](#architecture-overview)
3. [Implementation Details](#implementation-details)
4. [Instructions](#instructions)
5. [Test Cases](#test-cases)
6. [Open Points](#open-points)
7. [Summary of Design and Coding Concepts](#summary-of-design-and-coding-concepts)

## Introduction

In this project, we have implemented a priority message queue data structure and a thread pool. The priority message queue supports operations such as enqueue, dequeue, peek, and empty check, while the thread pool manages concurrent task execution.

## Architecture Overview

The architecture consists of the following components:
- **PriorityMessageQueue**: Implements the priority message queue using Python's `PriorityQueue` and provides thread-safe operations.
- **ThreadPool**: Implements the thread pool using `ThreadPoolExecutor` for concurrent task execution.
- **ReceiverThread**: Represents a thread that receives messages, enqueues them into the message queue, and performs actions using the thread pool.

## Implementation Details

- **PriorityMessageQueue**: Utilizes Python's `queue.PriorityQueue` with locking mechanisms to ensure thread safety.
- **ThreadPool**: Utilizes Python's `concurrent.futures.ThreadPoolExecutor` for managing a pool of threads.
- **ReceiverThread**: Subclass of Python's `threading.Thread`, receives messages, enqueues them, and performs actions concurrently using the thread pool.

## Instructions

To run the program:
1. Ensure you have Python installed on your system.
2. Clone the repository or download the source code.
3. Navigate to the directory containing the source code.
4. Run the `Main.py` file using Python.
``` python Main.py ```

## Test Cases

Test cases can be added to verify the functionality of the priority message queue, thread pool, and message sending/receiving mechanism. Ensure to cover edge cases and scenarios with varying priorities.

## Open Points

- Enhance error handling and logging for better debugging.
- Implement more advanced message processing logic.
- Explore optimizations for performance improvements.

## Summary of Design and Coding Concepts

- Utilized object-oriented programming principles for modular design.
- Ensured thread safety using locking mechanisms in the priority message queue.
- Implemented concurrent task execution using a thread pool.
- Followed best practices for documentation, code readability, and maintainability.

