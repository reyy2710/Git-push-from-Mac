import statistics

def calculate_statistics():
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    
    mean = statistics.mean(numbers)
    variance = statistics.variance(numbers)
    std_dev = statistics.stdev(numbers)

    print(f"Mean: {mean:.2f}")
    print(f"Variance: {variance:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")

calculate_statistics()
