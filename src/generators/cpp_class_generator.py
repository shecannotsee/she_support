import textwrap

def generate_cpp_class(class_name):
    code = textwrap.dedent(f'''
        class {class_name} {{
         public:
          // copy:off
          {class_name}(const {class_name}&) = delete;
          {class_name}& operator=(const {class_name}&) = delete;
          // move:off
          {class_name}({class_name}&&) = delete;
          {class_name}& operator=({class_name}&&) = delete;
          // destructors
          ~{class_name}() = default;
          // constructors
          {class_name}() = default;
        
         private:
          // data
         public:
          // interface
        
        }};
    ''')
    return code
