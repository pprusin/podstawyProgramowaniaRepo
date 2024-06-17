import unittest
import threading

def increment_shared_counter(counter_dict, key, iterations):
    for _ in range(iterations):
        counter_dict[key] += 1

class TestMultiThreading(unittest.TestCase):
    def test_increment_shared_counter(self):
        iterations = 1000
        num_threads = 10
        shared_counter = {'count': 0}
        threads = []

        for _ in range(num_threads):
            thread = threading.Thread(target=increment_shared_counter, args=(shared_counter, 'count', iterations))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        expected_value = iterations * num_threads
        self.assertEqual(shared_counter['count'], expected_value)

if __name__ == '__main__':
    unittest.main()
