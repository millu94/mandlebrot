import timeit

# Generic test function: simple loop with addition
def test_function():
    x = 0
    for _ in range(262144):  # 262,144 iterations
        x += 1

# Measure execution time
execution_time = timeit.timeit(test_function, number=1)  # Run once
average_time_per_iteration = execution_time / 262144

print(execution_time, average_time_per_iteration)