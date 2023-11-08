def singleton(_class):
    """
    Wraps a class definition, ensuring that Class() constructor calls
    will instantiate an instance only once, to which all subsequent
    calls to Class() will refer.

    ```
    @singleton
    class MyClass():
        def __init__(self, ...):
            ...

    a = MyClass()  # Instantiates MyClass
    b = MyClass()  # Re-uses existing instantiation

    a == b  # true
    ```
    """
    instances = {}

    def get(*args, **kwargs):
        if _class not in instances:
            instances[_class] = _class(*args, **kwargs)

        return instances[_class]

    return get
