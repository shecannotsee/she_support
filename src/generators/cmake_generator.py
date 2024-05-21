import textwrap

def generate_cmake(project_name):
    code = textwrap.dedent(f'''
        cmake_minimum_required(VERSION 3.10)

        # set the project name
        project({project_name})

        # specify the C++ standard
        set(CMAKE_CXX_STANDARD 11)
        set(CMAKE_CXX_STANDARD_REQUIRED True)

        # add the executable
        add_executable({project_name} main.cpp)
    ''')
    return code

