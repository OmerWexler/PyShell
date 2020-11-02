tab = '    '
print('\'1.set <LOCAL_VAR> <VALUE>\' - change the value of a local shell variable.')
print(tab + '<LOCAL_VAR> - variable name.')
print(tab + '<VALUE> - new variable value.\n')

print('\'2.get <LOCAL_VAR>\' - get the value of a local shell variable.')
print(tab + '<LOCAL_VAR> - variable name.\n')

print('\'3.restart\' - resets all shell variables to default values.\n')

print('\'4.cd <NEW_DIR>\' - change the current working directory.')
print(tab + '<NEW_DIR> - the new local directory.\n')

print('\'5.exit\' - leave shell.\n')

print('\'6.ls <DIR>\' - list all the contents of a directory.')
print(tab + '<DIR> - the dir to list.\n')

print('\'7.hexdump <FILE>\' - dump a file into stout (in hex format).')
print(tab + '<FILE> - the file to dump.\n')

print('\'8.to_hex\' - echos all input in hex.\n')

print('\'9.to_hex\' - translates and echos all input from hex.\n')