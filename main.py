import time
from functools import reduce
from statistics import mean


# Exercise 1
def exercise1(the_data):
    mapped_data = list(map(lambda x: len(x), the_data))
    reduced_data = reduce(lambda n, m: n if n > m else m, mapped_data)
    print(reduced_data)


# Exercise 2
def square(x):
    return x ** 2


def exercise2(the_data):
    print(f"For the list of #: {len(the_data)}")
    data = []
    addition = 0
    # using loop
    start_time = time.perf_counter()
    for x in the_data:
        data.append(square(x))
    addition = sum(data)
    end_time = time.perf_counter()
    elapsed_time_loop = (end_time - start_time) * 1000
    print(f"\tTime for loop:\t\t\t\t{elapsed_time_loop}\t\t\t The sum: {addition}")
    data.clear()

    # using list comprehensive
    start_time = time.perf_counter()
    data = [x ** 2 for x in the_data]
    addition = sum(data)
    end_time = time.perf_counter()
    elapsed_time_comprehensive = (end_time - start_time) * 1000
    print(f"\tTime for comprehensive:\t\t{elapsed_time_comprehensive}\t\t\t The sum: {addition}")
    data.clear()

    # using mapping
    start_time = time.perf_counter()
    mapping_data = list(map(square, the_data))
    reduced_data = reduce(lambda n, m: n + m, mapping_data)
    end_time = time.perf_counter()
    elapsed_time_mapping = (end_time - start_time) * 1000

    print(f"\tTime for mapping:\t\t\t{elapsed_time_mapping}\t\t\t The sum: {reduced_data}")

    print("*" * 15)


# Exercise 3
def exercise3(the_data):
    mapped_data = list(map(lambda x: (x - mean(the_data)) ** 2, the_data))
    reduced_data = reduce(lambda x, m: x + m, mapped_data)
    final_answer = square(reduced_data / len(the_data))
    print("*********** Exercise 3 ***********")
    print("Answer: ", final_answer)


# Exercise 4
def reducer(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value

    return merged_dict


def exercise4(file_path):
    word_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            word_list.extend([word.lower() for word in words])

    mapped_data = list(map(lambda x: {x: 1}, word_list))
    reduced_data = reduce(reducer, mapped_data)
    print(reduced_data)


if __name__ == '__main__':
    # -------------------------------- Exercise 1 --------------------------------
    # data1 = [
    #     "Hello, World!",
    #     "The Second line",
    #     "Hi There!",
    #     "This should be the longest",
    # ]
    #
    # exercise1(data1)

    # -------------------------------- Exercise 2 --------------------------------
    # data21 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # data22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 100
    # data23 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 1000
    # data24 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10000
    #
    # exercise2(data21)
    # exercise2(data22)
    # exercise2(data23)
    # exercise2(data24)

    # -------------------------------- exercise 3 --------------------------------
    # data3 = [random.randint(1, 100) for _ in range(5000)]
    # exercise3(data3)

    # -------------------------------- exercise 4 --------------------------------
    data4 = './data.txt'
    exercise4(data4)

    # End of main function
    print("Done")
