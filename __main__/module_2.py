import module_1

# you can get the main of the other module by typing
# module_1.main()


# but, when a file gets imported to another one 
# it's __name__ value is changed to the name of the file.
# In this case, the __main__ which was the old __name__ return
# will be module_1. Nevertheless module_2 __name__ remains
# as __main__

print(f'module_2 - __name__: {__name__}')