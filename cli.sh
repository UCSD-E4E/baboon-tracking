#!/bin/bash

# Check to see if pyenv is on the path.
pyenv --version > /dev/null
if [ $? -ne 0 ]
then
    # Install pyenv if not found.
    curl https://pyenv.run | bash
fi

# Check to see if pyenv has been added to the path.
cat ~/.bashrc | grep 'export PATH="~/.pyenv/bin:$PATH"' > /dev/null
if [ $? -ne 0 ]
then
    # Add pyenv to your path.
    echo 'export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
    
    # Source the changes so that we can get our new path.
    source ~/.bashrc
fi

PYTHON_VERSION=3.8.3

# Ensure Python is installed
pyenv versions | grep $PYTHON_VERSION > /dev/null
if [ $? -ne 0 ]
then
    # Install Python
    pyenv install $PYTHON_VERSION
fi
pyenv local $PYTHON_VERSION

python ./cli.py $@