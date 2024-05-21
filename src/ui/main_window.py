from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox

class MainWindow(QMainWindow):
    def __init__(self, generators):
        super().__init__()

        self.generators = generators

        self.setWindowTitle("Code Generator")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # 添加生成器选择框
        self.generator_layout = QHBoxLayout()
        self.layout.addLayout(self.generator_layout)

        self.generator_label = QLabel("Select Generator:")
        self.generator_layout.addWidget(self.generator_label)

        self.generator_combo_box = QComboBox()
        self.generator_combo_box.addItems(self.generators.keys())
        self.generator_layout.addWidget(self.generator_combo_box)

        # 添加参数输入框
        self.input_layout = QHBoxLayout()
        self.layout.addLayout(self.input_layout)

        self.name_label = QLabel("Name:")
        self.input_layout.addWidget(self.name_label)

        self.name_line_edit = QLineEdit()
        self.input_layout.addWidget(self.name_line_edit)

        # 添加生成按钮
        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_code)
        self.layout.addWidget(self.generate_button)

        # 添加代码显示框
        self.code_text_edit = QTextEdit()
        self.layout.addWidget(self.code_text_edit)

    def generate_code(self):
        generator_name = self.generator_combo_box.currentText()
        name = self.name_line_edit.text()
        generator = self.generators[generator_name]

        # 调用选择的生成器生成代码
        code = generator(name)
        self.code_text_edit.setPlainText(code)
