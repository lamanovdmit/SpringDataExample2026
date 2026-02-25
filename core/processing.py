"""
Модуль для обработки данных
"""

def process_data(data: str) -> str:
    """
    Преобразует входную строку в верхний регистр
    
    Args:
        data: Входная строка для обработки
        
    Returns:
        Строка в верхнем регистре
    """
    return data.upper()


def process_data_lower(data: str) -> str:
    """
    Преобразует входную строку в нижний регистр
    
    Args:
        data: Входная строка для обработки
        
    Returns:
        Строка в нижнем регистре
    """
    return data.lower()


def get_data_length(data: str) -> int:
    """
    Возвращает длину строки
    
    Args:
        data: Входная строка
        
    Returns:
        Длина строки
    """
    return len(data)


if __name__ == "__main__":
    # Тестирование модуля при прямом запуске
    test_string = "Test String"
    print(f"Original: {test_string}")
    print(f"Upper: {process_data(test_string)}")
    print(f"Lower: {process_data_lower(test_string)}")
    print(f"Length: {get_data_length(test_string)}")