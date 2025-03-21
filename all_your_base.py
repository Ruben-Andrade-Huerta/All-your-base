def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Convertir a base decimal
    valor_decimal = 0
    i = len(digits) - 1
    for numero in digits:
        if numero < 0 or numero >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        valor_decimal += numero * (input_base ** i)
        i -= 1

    # Caso especial para valor_decimal == 0
    if valor_decimal == 0:
        return [0]

    # Convertir a base deseada
    output_digit = []
    while valor_decimal > 0:
        output_digit.append(valor_decimal % output_base)
        valor_decimal //= output_base  
    return output_digit[::-1]
