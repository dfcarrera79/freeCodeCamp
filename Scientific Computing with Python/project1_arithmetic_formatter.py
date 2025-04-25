## Build an Arithmetic Formatter Project

def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_numbers = []
    bottom_numbers = []
    operators = []
    dashes = []
    results = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        num1, op, num2 = parts
        
        # Check for valid operator
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers contain only digits
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Check if numbers have more than four digits
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        operators.append(op)
        
        # Determine the length of the longest number in the problem
        max_length = max(len(num1), len(num2))
        
        # Format the top number (right-aligned with space for operator)
        top_numbers.append(num1.rjust(max_length + 2))
        
        # Format the bottom number (operator + space + number)
        bottom_numbers.append(op + ' ' + num2.rjust(max_length))
        
        # Create the dashes line
        dashes.append('-' * (max_length + 2))
        
        # Calculate result if needed
        if show_answers:
            if op == '+':
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            results.append(result.rjust(max_length + 2))
    
    # Build each line of the output
    top_line = '    '.join(top_numbers)
    bottom_line = '    '.join(bottom_numbers)
    dashes_line = '    '.join(dashes)
    
    arranged_problems = [top_line, bottom_line, dashes_line]
    
    # Add results if needed
    if show_answers:
        results_line = '    '.join(results)
        arranged_problems.append(results_line)
    
    return '\n'.join(arranged_problems)

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')