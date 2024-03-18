# This code implements a simple file system simulation using Python classes 
# (File, Directory, Stack and FileSystem). The first 3 classes represents characteristics of the file,
# directory and data struture in the file system, and the FileSystem class provides basic file system operations 
# such as listing files and directories (ls), creating directories (mkdir), changing the current directory (cd), 
# and creating files (touch). The script also includes a basic command-line interface that allows users 
# to interact with the simulated file system. It runs a loop where the user can input commands, 
# and the program responds accordingly until the user types "exit" to quit the simulation.

# The file class supports how files are displayed in the file system
class File:
    def __init__(self, name, content=""):
        self.name = name
        self.content = content

    def __str__(self):
        return f"File: {self.name}"

# The directory class supports the creation of files and directories 
class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.contents = []
        self.parent = parent

    def create_file(self, file):
        self.contents.append(file)

    def create_dir(self, dir):
        dir.parent = self
        self.contents.append(dir)

    def search_file(self, file_name):
        for item in self.contents:
            if isinstance(item, File) and item.name == file_name:
                return item
        return None

    def search_dir(self, dir_name):
        for item in self.contents:
            if isinstance(item, Directory) and item.name == dir_name:
                return item
        return None

    def __str__(self):
        return f"Directory: {self.name}"

# This is stack data structure that is used to create instances that can be used 
# to traverse back to previous directory and print the current directory
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# The filesystem class incorporates all the other classes to ensure proper 
# functionality of the program
class FileSystem:
    def __init__(self):
        self.root = Directory("root")
        self.current_dir = self.root
        self.dir_stack = Stack()

    def ls(self):
        for item in self.current_dir.contents:
            print(item)

    def pwd(self):
        path_stack = Stack()
        temp_dir = self.current_dir

        while temp_dir != self.root:
            path_stack.push(temp_dir.name)
            temp_dir = temp_dir.parent

        path_stack.push("root")

        path = "/".join(reversed(path_stack.items))
        print("Current Directory:", path)

    def mkdir(self, dir_name):
        new_dir = Directory(dir_name)
        self.current_dir.create_dir(new_dir)

    def cd(self, dest):
        if dest == "..":
            self.cd_up()
        else:
            new_dir = self.current_dir.search_dir(dest)
            if new_dir:
                self.current_dir = new_dir
            else:
                print(f"Directory '{dest}' not found.")

    def cd_up(self):
        if self.dir_stack:
            self.current_dir = self.dir_stack.pop()
        else:
            print("You are currently in the root directory.")
        if self.current_dir is None:
            self.current_dir = self.root

    def touch(self, file_name):
        new_file = File(file_name)
        self.current_dir.create_file(new_file)

# This main method runs the program and provides user with an interface to interract with file system
if __name__ == "__main__":
    fs = FileSystem()
    while True:
        command = input("$ ").lower().split()
        if command[0] == "exit":
            break
        elif command[0] == "ls":
            fs.ls()
        elif command[0] == "pwd":
            fs.pwd()
        elif command[0] == "mkdir":
            fs.mkdir(command[1])
        elif command[0] == "cd":
            fs.cd(command[1])
        elif command[0] == "touch":
            fs.touch(command[1])
        else:
            print("Invalid command")