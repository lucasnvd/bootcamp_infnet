def fahrenheit_to_celsius(*temperatures):
    def compute(value):
        return (value-32) * (5/9)

    return map(compute, temperatures)


temperatures = list(fahrenheit_to_celsius(32, 45, 56, 67, 90))
print(temperatures)
