def reverse_string(s):
    """Retorna a string passada como parâmetro invertida."""

    string_reversed = ""
    for i in range(len(s) -1, -1, -1):
        string_reversed += s[i]
    return string_reversed


if __name__ == "__main__":
    s = str(input("Digite algo: "))
    print(reverse_string(s))




