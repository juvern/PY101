buffer1 = ['ace', 'louis', 'kyon', 'maple', 'lemon']
buffer2 = ['ace', 'louis', 'kyon', 'maple', 'lemon']

# Mutates the original list
def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    print(buffer)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Creates a new list and assigns
def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    print(buffer)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


print(add_to_rolling_buffer1(buffer1, 3, 'maverick'))
print(add_to_rolling_buffer2(buffer2, 3, 'maverick'))

