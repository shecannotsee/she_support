import textwrap
import re

def param_parse(param):
    param_list_str = param.split()
    if len(param_list_str) > 0:
        param_name = param_list_str[-1]
        param_type = " ".join(param_list_str[:-1])
        if param_name[0] == "*":
            param_type += "*"
            param_name = param_name[1:]
        return param_type, param_name
    else:
        return "", ""

def parse_c_function(c_function_string):
    function_return = ""
    function_name = ""
    match = re.search(r'[^()]+(?=\()', c_function_string)
    if match:
        function_return_name = match.group()
        function_return_name = function_return_name.split()
        function_return = function_return_name[0]
        function_name = function_return_name[1]
        if function_name[0] == "*":
            function_return += "*"
            function_name = function_name[1:]
    else:
        print("parse c function error")
        return None

    param_info_list = []
    match = re.search(r'\((.*?)\)', c_function_string)
    if match:
        param_info = match.group(1).split(',')
        for param in param_info:
            param_info_list.append(param_parse(param))
    else:
        print("parse c function error")
        return None

    return {
        'function_name': function_name,
        'function_return': function_return,
        'function_params': param_info_list
    }

def code_generate(c_function):
    function_info = parse_c_function(c_function)
    function_name = function_info['function_name']
    function_return = function_info['function_return']
    function_param = ", ".join([f"{param_type} {param_name}" for param_type, param_name in function_info['function_params']])
    function_name_list = ", ".join([param_name for _, param_name in function_info['function_params']])

    code = textwrap.dedent(f'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/* global mock set */
static bool mock_{function_name} = false;
constexpr int mock_{function_name}_errno = 1;
enum class {function_name}_case_des : int {{
    ret_1,
}};
static {function_name}_case_des {function_name}_case = {function_name}_case_des::ret_1;
/* {function_name} mock set */
typedef {function_return} (*{function_name}_func_t)({function_param});
/* The real function address function */
{function_name}_func_t {function_name}_func = reinterpret_cast<{function_name}_func_t>(dlsym(RTLD_NEXT,"{function_name}"));
/* {function_name} mock */
extern "C" {function_return} {function_name}({function_param}) {{
  if (mock_{function_name}) {{
    if ({function_name}_case == {function_name}_case_des::ret_1) {{
      return {function_return}{{}};
    }} else if ( 1 ) {{
      return {function_return}{{}};
    }} else {{  
      return {function_return}{{}};
    }}
  }} else {{
    return {function_name}_func({function_name_list});
  }}
}}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    ''')
    return code
