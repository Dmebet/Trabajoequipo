def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    prev_val = 0
    for i in range(len(s) - 1, -1, -1):
        val = roman_dict[s[i]]
        if val < prev_val:
            num -= val
        else:
            num += val
        prev_val = val
    return num

num_romano = input("Introduce un número romano uwu: ")
num_entero = roman_to_int(num_romano)
print("El número romano", num_romano, "es igual a :D", num_entero)