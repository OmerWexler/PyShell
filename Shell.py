import os
import getpass
import subprocess

class Shell:
    def __init__(self):
        self.local_commands = {
            'set': self._set_, 
            'get': self._get_,
            'restart': self._restart_,
            'cd': self._cd_, 
            'exit': self._exit_}

        self._restart_(None)
        self.is_running = True
        self.original_local_path = os.path.join(os.getcwd(), 'local_path')
        

    def _restart_(self, args):
        self.local_variables = {
            'prompt': self.build_prompt(),
        }


    def init_shell(self):
        while self.is_running:
            cmd = input(self.local_variables['prompt'])
            
            proccess = cmd.split(' ')[0].lower()
            args = cmd.split(' ')[1:]
            self._execute_command_(proccess, args, None)

    
    def _execute_command_(self, proccess, args, stdin_overwrite):
            try:
                output = self._execute_local_(proccess, args)
                if output:
                    return output
                
                output = self._execute_from_path_(self.original_local_path, proccess, args, stdin_overwrite)
                if output:
                    return output

                output = self._execute_from_path_(os.getcwd(), proccess, args, stdin_overwrite)
                if output:
                    return output
                
                output = self._execute_extenal_(proccess, args)
                if output:
                    return output

                print('Command not found.')
            except Exception as e:
                print(e)


    def _execute_local_(self, command, args):
        if command in self.local_commands.keys():
            args_string = ''

            for arg in args:
                args_string += arg + ' '
            
            self.local_commands[command](args)
            return True
        
        return False


    def _execute_from_path_(self, path, command, args: list, stdin_overwrite):
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                if file.split('.')[0] == command:
                    
                    redirect_file = None
                    redirect_proccess = None
                    redirect_proccess_args = None
                    
                    args_string = ''

                    for i in range(0, len(args)):
                        if args[i] == '>':
                            redirect_file = args[i + 1]
                            break
                        elif args[i] == '|':
                            redirect_proccess = args[i + 1]
                            redirect_proccess_args = args[i + 2:]
                            break
                        else:
                            args_string += args[i] + ' '

                    if file.endswith('.py'): 
                        cmd = f'python {os.path.join(path, file)} {args_string}'
                    else:
                        cmd = f'{os.path.join(path, file)} {args_string}'
                        
                    if not redirect_file == None:
                        ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=stdin_overwrite)
                        self._output_to_file_(ps, redirect_file)
                    elif not redirect_proccess == None:
                        ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=stdin_overwrite)
                        self._execute_command_(redirect_proccess, redirect_proccess_args, ps.stdout)
                    else:
                        ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=stdin_overwrite)
                        self._output_to_console_(ps)

                    return ps
                            
        return False


    def _output_to_console_(self, proccess):
        while proccess.poll() == None:
            print(proccess.stdout.readline().decode(), end='')
        print(proccess.stdout.read().decode(), end='')


    def _output_to_file_(self, proccess, file):
        output = b''
        with open(file, 'wb') as file:
            while proccess.poll() == None:
                output += proccess.stdout.readline()
            output += proccess.stdout.read()
            file.write(output)


    def _execute_extenal_(self, command, args):
        for path in os.environ['PATH'].split(';'):
            try:
                output = self._execute_from_path_(path, command, args, redirect)
                if output:
                    return output

            except:
                pass
        return False


    def _set_(self, args):
        if args[0] in self.local_variables.keys():
            self.local_variables[args[0]] = args[1]
        else:
            print(f'{args[0]} not found in local variables.')
            print('Available variables: ')

            for key in self.local_variables.keys():
                print(key)


    def _get_(self, args):
        if args[0] in self.local_variables.keys():
            print(self.local_variables[args[0]])
        else:
            print(f'{args[0]} not found in local variables.')
            print('Available variables: ')

            for key in self.local_variables.keys():
                print(key)

    
    def build_prompt(self):
        return 'Hello ' + getpass.getuser() + ', ' + os.getcwd() + '> '


    def _exit_(self, args):
        self.is_running = False


    def _cd_(self, args):
        os.chdir(args[0])
        self.local_variables['prompt'] = self.build_prompt()


if __name__ == '__main__':
    shell = Shell()
    shell.init_shell()