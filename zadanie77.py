import math
from collections import Counter

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def vigenere_encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha() and char.isupper():
            shift = alphabet.index(key[key_index % key_length])
            new_char = alphabet[(alphabet.index(char) + shift) % 26]
            encrypted_text.append(new_char)
            key_index += 1
        else:
            encrypted_text.append(char)

    return ''.join(encrypted_text), math.ceil(len(text) / key_length)

def vigenere_decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = []
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha() and char.isupper():
            shift = alphabet.index(key[key_index % key_length])
            new_char = alphabet[(alphabet.index(char) - shift) % 26]
            decrypted_text.append(new_char)
            key_index += 1
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

def letter_frequencies(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = Counter(char for char in text if char in alphabet)
    return {letter: counter.get(letter, 0) for letter in alphabet}

def coincidence_index(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = sum(1 for char in text if char in alphabet)
    frequencies = letter_frequencies(text)
    numerator = sum(f * (f - 1) for f in frequencies.values())
    denominator = n * (n - 1) if n > 1 else 1
    return numerator / denominator

def estimate_key_length(text):
    kappa = coincidence_index(text)
    return round(0.0285 / (0.0385 - kappa), 2)

def main():
    source_text = read_file("dokad.txt")
    key_1 = "LUBIMYCZYTAC"
    encrypted_text, key_repeats = vigenere_encrypt(source_text, key_1)

    encrypted_text_2, key_2 = read_file("szyfr.txt").splitlines()
    decrypted_text = vigenere_decrypt(encrypted_text_2, key_2)

    frequencies = letter_frequencies(encrypted_text_2)
    estimated_key_length = estimate_key_length(encrypted_text_2)
    actual_key_length = len(key_2)

    results = []
    results.append("77.1")
    results.append(f"Liczba powtórzeń klucza: {key_repeats}")
    results.append(f"Zaszyfrowany tekst: {encrypted_text}")
    results.append("\n77.2")
    results.append(f"Odszyfrowany tekst: {decrypted_text}")
    results.append("\n77.3")
    results.append("Częstotliwości liter:")
    for letter, count in frequencies.items():
        results.append(f"{letter}: {count}")
    results.append(f"Szacunkowa długość klucza: {estimated_key_length}")
    results.append(f"Dokładna długość klucza: {actual_key_length}")

    write_file("Vigenere_wyniki.txt", '\n'.join(results))

if __name__ == "__main__":
    main()