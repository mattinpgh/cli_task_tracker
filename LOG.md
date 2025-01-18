# Log/Diary:

## Day One, January 15th, 2025
* Created basic structure. Made scratchpad.py to start learning argparse
* Working through [the argparse tutorial](https://docs.python.org/3/howto/argparse.html) in the official python docs
* Next steps: 
  * finish [the argparse tutorial](https://docs.python.org/3/howto/argparse.html)
  * work through [Real Python's argparse lesson](https://realpython.com/command-line-interfaces-python-argparse/)
  * work through [Creating and packaging command-line tools](https://packaging.python.org/en/latest/guides/creating-command-line-tools/)

## Day Two, January 16th, 2025
* Completed working through [the argparse tutorial](https://docs.python.org/3/howto/argparse.html)
* Started working through [Real Python's argparse lesson](https://realpython.com/command-line-interfaces-python-argparse/)
  * Made it to [Creating a CLI with `argparse`](https://realpython.com/command-line-interfaces-python-argparse/#creating-a-cli-with-argparse)
    * Detoured to read about the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser) object
    * Started reading the [`.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method. Made it to [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction)


**Reflection**: starting to get a handle on how `argparse` works. I still have a lot to read through and a lot to work 
with, but knowing generally what these programs do is making me a little more confident. I know I'm also really weak 
on file handling, so once I finish working through these tutorials, that's where I'm going to head. 

## Day Three, January 18th, 2025
* Took a break yesterday, picked back up with the docs:
  * Finished add_argument, though I admittedly skimmed the last few parameters.
  * This is really meaty: (in parse_args()) `"Convert argument strings to objects and assign them as attributes of the namespace. Return the populated namespace."`
  * Finished the docs with the Namespace object
* Back to the Real Python tutorial
  * Adding `pathlib` to my reading list. I don't know if it's important to this project, but I've seen it too many times to not read it now
  * Interesting flow =>
    * Create an ArgumentParser object (`parser = ArgumentParser()`)
    * Add arguments to the ArgumentParser - argparse recognizes `positional arguments` and `optional arguments`
      * **Positional**: `add_argument("x")` or `add_argument("path")`
      * **Optional**: `add_argument("-l", "-long", action="store_true")`
    * Call the parse_args() method on the parser, getting a Namespace object `args = parser.parse_args()`
    * The Namespace object contains the arguments passed to the parser
    * Access the namespace objects with dot notation on args:
      * If you have `add_argument("path")`, you access that with `args.path`
* Finished the tutorial up through `Creating Command-Line Interfaces with Python's argparse.` Got enough additional reading in the meantime to drive me crazy.


# Running List of Future Reading

* pathlib
* [Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/)
* [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/)
* [Model-View-Controller (MVC) in Python Web Apps: Explained With Lego](https://realpython.com/lego-model-view-controller-python/)
* [Getting Started with Testing in Python](https://realpython.com/python-testing/)