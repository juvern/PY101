def first():
    return {
        'prop1': "hi there",
    }

# return None as there due to the indent
def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())