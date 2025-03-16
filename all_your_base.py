def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError("Bases must be at least 2.")

    #Convertir a base decimal
    valor_decimal = 0
    i = len(digits) - 1
    print(i)
    for numero in digits:
        if numero < 0 or numero >= input_base:
            raise ValueError("All digits must be valid for the input base.")
        valor_decimal += numero * (input_base ** i)
        i -= 1
    
    print(valor_decimal)

    #Convertir a base deseada
    output_digit = []
    num_list = list(str(valor_decimal))

    # for numero in num_list:
    #     output_digit.append(int(numero) % output_base)
    # return output_digit

    while valor_decimal > 0:
        output_digits.append(valor_decimal % output_base)
        valor_decimal //= output_base

    return output_digit



print(rebase(2, [1,0,1,0,1,0], 10))# [1]
