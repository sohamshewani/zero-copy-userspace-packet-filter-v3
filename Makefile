all: tests

tests: test_ring_buffer.o test_sliding_window.o test_packet_filter.o test_integration.o
	g++ -o test_runner test_ring_buffer.o test_sliding_window.o test_packet_filter.o test_integration.o -Iinclude

test_ring_buffer.o: tests/test_ring_buffer.cpp
	g++ -c -o $@ $< -Iinclude

test_sliding_window.o: tests/test_sliding_window.cpp
	g++ -c -o $@ $< -Iinclude

test_packet_filter.o: tests/test_packet_filter.cpp
	g++ -c -o $@ $< -Iinclude

test_integration.o: tests/test_integration.cpp
	g++ -c -o $@ $< -Iinclude

include/headers: include/types.h include/errors.h include/ring_buffer.h include/sliding_window.h include/packet_filter.h
	make -C include

include/types.h:
	make -C include

include/errors.h:
	make -C include

include/ring_buffer.h:
	make -C include

include/sliding_window.h:
	make -C include

include/packet_filter.h:
	make -C include

.PHONY: tests
