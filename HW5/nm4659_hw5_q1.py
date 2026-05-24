from ArrayStack import ArrayStack

var_dict = {}
var_name = None
exp_str = input("-->")

while exp_str != "done()":
    operators = "+-*/"
    exp_lst = exp_str.split()
    args_stack = ArrayStack()
    equal_exp = False
    
    if "=" in exp_str:
        var_name = exp_lst[0]
        exp_lst = exp_lst[2:]
        equal_exp = True
        
    for token in exp_lst:
        if token not in operators:
            if token.isdigit():
                args_stack.push(int(token))
            else:
                args_stack.push(var_dict[token])
            
        else:
            arg2 = args_stack.pop()
            arg1 = args_stack.pop()
            if(token == '+'):
                res = arg1 + arg2
            elif(token == '-'):
                res = arg1 - arg2
            elif(token == '*'):
                res = arg1 * arg2
            elif(token == '/'):
                if(arg2 == 0):
                    raise ZeroDivisionError
                else:
                    res = arg1 / arg2
            args_stack.push(res)
    res = args_stack.pop()
    
    if equal_exp:
        var_dict[var_name] = res
        print(var_name)
    else:
        print(res)
        
    exp_str = input("-->")
