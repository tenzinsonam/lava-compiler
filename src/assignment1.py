import ply.lex as lex
from myLexer import MyLexer
import argparse
import os.path

def getTestFileName():
    argParser = argparse.ArgumentParser(description='Provide the filename which is to be lexed')
    argParser.add_argument('filename', type=str, help="filename to be parsed")
    args = argParser.parse_args()
    return args.filename

def iterateOverToken():
    if os.path.exists(filename):
        fs = open(filename, 'r')
        data = fs.read()
        lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok: break
            print(tok)
        fs.close()
    else:
        print("File Does Not Exists ...")



if __name__ == "__main__":
    tokens = MyLexer.tokens
    lexer = lex.lex(module=MyLexer())    ## observation :: if I set optimise argument to 1 then it is not able to parse the strings

    filename = getTestFileName()
    iterateOverToken()
