# CSV Normalizer

Normalizes CSVs according to [this spec](http://github.com/anybodys/kmd-csvnormalizer/blob/master/ProblemSpec.md).

Note: Project name is prefixed with the developer's name to avoid conflicts with other implementations.

## To Install and Run

Requirements
- Ubuntu 16.04 (Probably other unix-based systems would work.)
- Python 3.6. (Probably any python3.2+ would work.)

1. Install: `pip install git://git@github.com/anybodys/kmd-csvnormalizer.git`. You may want to run this with `sudo -H`.
1. Run: `cat [your input file] | kmd-csvnormalizer`


## Set Up for Development

Requirements
- Ubuntu 16.04 (Probably other unix-based systems would work.)
- Python 3.6. (Probably other pythons would work.)
- virtualenv and virtualenvwrapper. (Technically wrapper is optional, but it sure is handy!)

1. cd to where you want to work.
1. ``mkvirtualenv --python=`which python3.6` kmd-csvnormalizer``.
1. Optional but super handy: edit ~/.virtualenvwrapper/kmd-csvnormalizer/bin/postactivate to cd to your working directory. Here's a command that should work on ubuntu! ``echo "cd `pwd`" >> ~/.virtualenvs/kmd-csvnormalizer/bin/postactivate``
1. `git clone git@github.com:anybodys/kmd-csvnormalizer.git`
1. `pip install -r requirements.txt`

