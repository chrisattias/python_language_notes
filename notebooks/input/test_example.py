def test_list_input():
    my_input = [1, 2, 3]  # List.
    assert sum(my_input) == 6, "Error.  Must sum to  6"

def test_tuple_input():
    my_input = (1, 2, 3)  # Tuple.
    assert sum(my_input) == 6  # AssertionError custom message is optional

def test_set_input():
    my_input = {1, 2}  # Set.
    assert sum(my_input) == 6, "Error.  Must sum to  6"
