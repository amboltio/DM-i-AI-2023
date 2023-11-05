def render(file: str, **kwargs) -> str:
    '''Renders a template file with placeholders of {{kwarg}} form with the provided value.'''
    try:
        with open(file, encoding="utf8") as fp:
            contents = fp.read()

            for key, value in kwargs.items():
                contents = contents.replace(f'{{{{{key}}}}}', str(value))

            return contents
    except Exception as e:
        print(e)