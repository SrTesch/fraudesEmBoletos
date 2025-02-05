import re

def validate_boleto_number(boleto: str) -> bool:
    """ Validates if the boleto number follows the standart pattern. """
    pattern = r"^\d{47}$" #Boletos usually have 47 digits
    return bool(re.match(pattern, boleto))

if __name__ == "__main__":
    boleto = "00190500954014481606906809350314337370000000100"
    print(f"Boleto valid? {validate_boleto_number(boleto)}")