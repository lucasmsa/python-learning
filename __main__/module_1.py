# when python runs a  file, it sets some special variables
# __name__ is one of them
def main():
    print(f'module_1 - __name__: {__name__}')


# the module_2 will never pass that if
# because it sees __name__ of module_1 as module_1 not
# __main__
# sometimes you'll only want to run some part
# of the code when the file is being
# imported and other ones directly from the 
if __name__ == '__main__':
    main()
else:
    print("you're in the second module")