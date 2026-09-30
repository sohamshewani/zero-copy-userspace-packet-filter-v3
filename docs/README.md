# Zero Copy User Space Packet Filter

## Overview

This project implements a zero-copy user space packet filter using Python. The architecture consists of a core module for handling packet filtering logic, a ring buffer manager for efficient data storage and retrieval, and a sliding window flow control mechanism to ensure data integrity. Packets are processed in userspace, leveraging Python's efficient memory management capabilities.

## Files

- `include/types.py`: Defines packet types.
- `include/errors.py`: Defines custom error classes.
- `include/ring_buffer.py`: Implements a ring buffer for data storage and retrieval.
- `include/sliding_window.py`: Implements a sliding window flow control mechanism.
- `include/packet_filter.py`: Implements packet filtering logic.
- `src/ring_buffer_manager.py`: Manages the ring buffer.
- `src/packet_filter_engine.py`: The core engine for packet filtering.
- `src/main.py`: Main application entry point.
- `Makefile`: Build and test the application.
- `tests/test_ring_buffer.py`: Unit tests for the ring buffer.
- `tests/test_sliding_window.py`: Unit tests for the sliding window.
- `tests/test_packet_filter.py`: Unit tests for the packet filter.
- `tests/test_integration.py`: Integration tests for the entire system.

## Usage

1. Build the project using `make all`.
2. Run the tests using `make tests`.
3. Run the application using `python3 main.py`.
