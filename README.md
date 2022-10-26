# pylib-challenge

Python Library Challenges

## Initial setup

Run `./init.sh` in terminal for basic setup.

To use virtual envrironment, run `pipenv shell` and when you wish to exit from it, run `exit`. Recommended is to keep one environment for each challenge.

To install new libraries inside this environment, run `pipenv install <library_name>`. For example, `pipenv install request`.

While you are inside the shell, run `python main.py` for importing the module to check your own code.

## How to complete challenge

1. Fork Repo
2. Run `./init.sh`
3. Open challenge directory and add code to the module
4. Run `./test_code.sh`. Fix any errors. If no error, coverage report must give 100% result
5. You are done

The command `./test_code.sh` inside each challange folder is used to verify if you have completed challenge successfully. The `main.py` file can be run to check the code runing inside a main function.

You are only allowed to change files other than `test_code.sh` file and files in `test` folder inside each challenge folder.

## Challenge 0 : Sample module

This is sample module written for reference. Do not edit this folder.

## Challenge 1 : Simple file based json database module

Create a simple database by using a file to store in json format.

## Challenge 2 : YAML to Dictionary parsing module

Create a module to parse a Yaml file to python dictionary.

#### References

- https://yaml.org/spec/1.2.2/
- https://docs.fileformat.com/programming/yaml/
