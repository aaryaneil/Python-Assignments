def for_loops_dict_comprehension(a,b):
    for_output = {}
    dict_output = {}

    for i in range(len(a)):
        for_output[a[i]] = b[i]

    dict_output = {a[i]:b[i] for i in range(len(a))}

    print(f"Answer using for loop: {for_output}")
    print(f"Answer using dictionary comprehension: {dict_output}")

a=["Bob", "Sam", "Neal"]
b=["Physics", "Biology", "Maths"]

for_loops_dict_comprehension(a,b)