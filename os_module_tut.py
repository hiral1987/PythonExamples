import os

# print(dir(os))
# output :
# ['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT',
# 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY',
# 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK',
# 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_AddedDllDirectory', '_Environ', '__all__',
# '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_methods',
# '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_walk', '_wrap_close', 'abc', 'abort', 'access',
# 'add_dll_directory', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath',
# 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv',
# 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate',
# 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv',
# 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs',
# 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove',
# 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable',
# 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror',
# 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks',
# 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink',
# 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode', 'walk', 'write']


# Get current Working directory
# print(os.getcwd())
# output: D:\PythonProject\myFirstPythonProj


# Change directory
# os.chdir('D://')
# print(os.getcwd())
# output: D:\


# get All files & folder in directory. You can pass path parameter of which you want to get file & folder
# print(os.listdir())
# output: ['.idea', 'abstrct_base_class.py', 'access_specifier.py', 'argkw.py', 'break_continue.py', 'class2_tut.py',
# 'class_inheritance2.py', 'class_inheritance3.py', 'class_inhetitance.py', 'class_tut.py', 'class_tut3.py',
# 'comprehensions.py', 'coroutine.py', 'dec.py', 'dictionary.py', 'else_finally_in_try_except.py',
# 'else_with_for_loop.py', 'enumerate_tut.py', 'exercise7.py', 'eyes.mp3', 'filter_tut.py', 'function_caching.py',
# 'generators.py', 'global1.py', 'hir.txt', 'if.py', 'import2_tut.py', 'import2_tut2.py', 'import_tut.py',
# 'import_tut2.py', 'join_func_tut.py', 'lambda.py', 'lists.py', 'loops.py', 'main.py', 'map_tut.py', 'my_logs.txt',
# 'object_introspection.py', 'operator_overloading_and_dunder_methods.py', 'os_module_tut.py', 'physical.mp3',
# 'recursive1.py', 'reduce_tut.py', 'set.py', 'setters_and_property_decorators.py', 'short_hand.py', 'string1.py',
# 'time_module.py', 'variable.py', 'water.mp3', 'while_loop.py', '__pycache__']


# Create folder
# os.mkdir('Hi')  # This will create folder in current directory


# Create folder & subfolder
# os.makedirs('com/demo')


# Rename a file
# os.rename('hiral.txt', 'hir.txt')  # rename file
# os.rename('Hi', 'sub')  # rename folder


# Read environment variable
# print(os.environ.get('Path'))


# To join path, this helps to remove unnecessary slashes in path
# print(os.path.join('c:/', 'hir.txt'))


# To check directory or file exists or not
# print(os.path.exists('Z://'))


# To check whether path is directory or file
# os.path.isdir()
# os.path.isfile()
