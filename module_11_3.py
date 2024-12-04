def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not attr.startswith('__') and not callable(getattr(obj, attr))]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if method.startswith('__') or callable(getattr(obj, method))]

    # Получаем модуль, к которому принадлежит объект
    obj_module = obj.__module__ if hasattr(obj, '__module__') else 'N/A'

    # Собираем информацию в словарь
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }

    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)