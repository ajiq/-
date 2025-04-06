#!/usr/bin/env python3

import sys
import base64

def encode_b64(input_text: str) -> None:
    """
    Кодируетзаданный текст в Base64 и выводит результат.
    Завершает выполнение с кодом 0 при успехе.
    """
    encoded_bytes = base64.b64encode(input_text.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    print(encoded_str)
    sys.exit(0)


def decode_b64(input_text: str) -> None:
    """
    Декодирует заданную строку Base64.
    - Если строка корректна, выводит результат и завершает с кодом 0.
    - Если некорректна, завершает выполнение с кодом 1.
    """
    try:
        decoded_bytes = base64.b64decode(input_text, validate=True)
        decoded_str = decoded_bytes.decode("utf-8", errors="replace")
        print(decoded_str)
        sys.exit(0)
    except Exception:
        sys.exit(1)


def main():
    """
    Простая управляющая функция, которая определяет,
    выполнять кодирование или декодирование.

    Использование:
      script.py encode "текст"
      script.py decode "YmFzZTY0"
    """
    if len(sys.argv) < 3:
        print("Использование: script.py <encode|decode> <текст>")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    input_text = sys.argv[2]

    if mode == "encode":
        encode_b64(input_text)
    elif mode == "decode":
        decode_b64(input_text)
    else:
        print("Неизвестный режим. Используйте 'encode' или 'decode'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
