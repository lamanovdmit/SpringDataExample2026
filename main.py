from core.processing import process_data, process_data_lower, get_data_length

def main():
    input_data = "Hello, Laboratory Work!"
    
    result_upper = process_data(input_data)
    result_lower = process_data_lower(input_data)
    data_length = get_data_length(input_data)
    
    print("=" * 50)
    print(f"Исходная строка: {input_data}")
    print(f"Длина строки: {data_length}")
    print(f"Верхний регистр: {result_upper}")
    print(f"Нижний регистр: {result_lower}")
    print("=" * 50)

if __name__ == "__main__":
    main()