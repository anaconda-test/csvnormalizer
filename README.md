# CSV Normalizer

Normalizes CSVs according to [this spec](http://github.com/anybodys/csvnormalizer/blob/master/ProblemSpec.md).


## To Install and Run

Requirements
- Ubuntu 16.04 (Probably other unix-based systems would work.)
- Python 3.6. (Probably any python3.2+ would work.)

1. Install: `pip install git+ssh://git@github.com/anybodys/csvnormalizer.git`.
   - If you don't have ssh setup for GitHub, try `pip install https://github.com/anybodys/csvnormalizer.git`. But first, I strongly encourage you to [set up ssh](https://help.github.com/articles/connecting-to-github-with-ssh/)!
   - Note: You may need the `--user` flag.
1. Run: `cat [your input file] | kmd-csvnormalizer`. Note: Package name is prefixed with the developer's name to avoid conflicts with other implementations.


## Set Up for Development

Requirements
- Ubuntu 16.04 (Probably other unix-based systems would work.)
- Python 3.6. (Probably other pythons would work.)
- virtualenv and virtualenvwrapper. (Technically wrapper is optional, but it sure is handy!)

1. cd to where you want to work.
1. ``mkvirtualenv --python=`which python3.6` csvnormalizer``.
1. Optional but super handy: edit ~/.virtualenvwrapper/csvnormalizer/bin/postactivate to cd to your working directory. Here's a command that should work on ubuntu! ``echo "cd `pwd`" >> ~/.virtualenvs/csvnormalizer/bin/postactivate``
1. `git clone git@github.com:anybodys/csvnormalizer.git`
1. `pip install -r requirements.txt`

