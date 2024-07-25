def num_of_variable(var):
    if isinstance(var, int):
        return var
    elif isinstance(var, str):
        return len(var)
    else:
        return None


def calculate_structure_sum(*args, i=0, sum_=0):
    if len(args) >= 1:
        element = args[0]
        if isinstance(element, list) or isinstance(element, tuple):
            if len(element) != 0:
                return calculate_structure_sum(*element, i=i, sum_=sum_)
            else:
                return calculate_structure_sum(*args[1:], i=i, sum_=sum_)
        elif isinstance(element, dict):
            return calculate_structure_sum(*list(element.keys()), *list(element.values()), i=i, sum_=sum_)
        elif isinstance(element, set):
            return calculate_structure_sum(*list(element), i=i, sum_=sum_)
        elif isinstance(element, int) or isinstance(element, str):
            if len(args) > 1:
                sum_ += num_of_variable(element)
                return calculate_structure_sum(*args[1:], i=i, sum_=sum_)
            else:
                sum_ += num_of_variable(element)
                i += 1
                if i != len(data_structure)-1:
                    return calculate_structure_sum(*data_structure[i:], i=i, sum_=sum_)
                else:
                    return sum_
    else:
        return sum_


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print("Result:", calculate_structure_sum(*data_structure))
