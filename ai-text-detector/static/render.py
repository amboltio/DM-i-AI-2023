

def render(file: str, **kwargs) -> str:
    '''Renders a template file with placeholders of {{kwarg}} form with the provided value.'''

    with open(file) as fp:
        contents = fp.read()

        for key, value in kwargs.items():
            contents = contents.replace(f'{{{{{key}}}}}', str(value))

        return contents
