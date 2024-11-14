def introspection_info(obj):
    obj_type = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]

    module_name = obj.__class__.__module__

    extra_info = {}
    if isinstance(obj, (int, float, complex)):
        extra_info['is_integer'] = isinstance(obj, int)
        extra_info['is_floating_point'] = isinstance(obj, float)
    elif isinstance(obj, str):
        extra_info['length'] = len(obj)
        extra_info['is_numeric'] = obj.isnumeric()
    elif isinstance(obj, list):
        extra_info['length'] = len(obj)
        extra_info['is_empty'] = not obj

    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module_name,
        'extra_info': extra_info
    }


number_info = introspection_info(42)
print(number_info)


class SampleClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"


sample_object = SampleClass("Alice", 30)
sample_object_info = introspection_info(sample_object)
print(sample_object_info)
