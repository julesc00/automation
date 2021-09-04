"""
The basic use of argparse in a script can be shown in three steps:
    1. Define the arguments that your script is going to accept, generating a new
    parser.

    2. Call the defined parser, returning an object with all of the resulting
    arguments.

    3. Use the arguments to call the entry point of your script, which will apply
    the defined behavior.

    Try to use the following general structure for your scripts:

    IMPORTS
    def main(main parameters):
        DO THINGS

    if __name__ == '__main__':
        DEFINE ARGUMENT PARSER
        PARSE ARGS
        VALIDATE OR MANIPULATE ARGS, IF NEEDED
        main(arguments)

Go to recipe_cli_step1.py
"""
