# ArrayPack

With this project we wanted to create a simple way to manipulate arrays
objects. In order to have the maximum number of array-like object, we
had to organise modules in a package named arrayPack.

## Getting Started

To use the pack simply put it in the same folder of the script which you
want to use the package in.


### Prerequisites

You just need python 3.6 or 2.7 installed on your pc.

### Installing

_We are working on setup.py in order to make this package available to
all system scripts but, currently, you have to follow these instructions._

After you put the package folder in the same directory of the script you
can import its modules using import comand:

```python
import arrayPack as ar
```

OR you can import single modules:

```python
from arrayPack import generic as arr
from arrayPack.sorting import sortAndSearch as sort
from arrayPack.stack import stack as st
```

Then to call a class or a function type the alias of the module:

```python
stack1 = st.Stack("i")
```

For the documentation go to the [wiki](https://github.com/Saverio11/pythonArray-simplified/wiki)
of the repository.

## Built With

* [Python 3.6.3](https://www.python.org/) - The programming language used
* [Pycharm Community Edition](https://www.jetbrains.com/pycharm/) - Python IDE

## Authors

* **Saverio Custodi** - *ArrayPack* - [Saverio11](https://github.com/Saverio11)


## License

This project is licensed under the GPL License

## Acknowledgments

* Inspired by: Emilio Ugo Giuffrida
