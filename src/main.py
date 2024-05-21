import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from generators.cpp_class_generator import generate_cpp_class
from generators.cmake_generator import generate_cmake
from generators.c_function_generator import code_generate

def main():
    generators = {
        "C++ Class": generate_cpp_class,
        "CMake": generate_cmake,
        "C Function": code_generate,  # 添加 C 函数代码生成器
    }

    app = QApplication(sys.argv)
    window = MainWindow(generators)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
