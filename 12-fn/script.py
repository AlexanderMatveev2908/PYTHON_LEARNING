from typing import Any, Optional

def multi_args(*args: Any) -> None:
    for x in args:
        print(f'-> {x}')



multi_args(1,2,3,4)

def multi_named(*args: Optional[Any], **kwargs: Any) -> None:
    print(kwargs)
    for k,v in kwargs.items():
        print(f'{k} => {v}')


multi_named(name='john', job= 'skater')