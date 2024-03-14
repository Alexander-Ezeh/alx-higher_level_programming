#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(a, b))

# import dis

# def magic_calculation(a, b):
#     from magic_calculation_102 import add, sub

#     if a < b:
#         c = add(a, b)
#         for i in range(4, 6):
#             c = add(c, i)
#         return c
#     else:
#         return sub(a, b)

# # Uncomment the following lines to see the bytecode of the function
# # dis.dis(magic_calculation)
