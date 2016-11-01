def data_type(data): #this code passes all tests on andelab
    # test for string
    if isinstance(data, str):
        return len(data)

    # test for boolean
    elif isinstance(data, bool):
        return True

    # test for small and large integer
    elif isinstance(data, int):
        if (data <= 100):
            return 'less than 100'
        else:return 'more than 100'

    # test for small and large lists
    elif isinstance(data, list):
        if len(data) < 3:
            return None
        else:
            return len(data)

    else: return 'no value'

val = {'name':'edwin', 'gender':'male'}
print data_type(val)

