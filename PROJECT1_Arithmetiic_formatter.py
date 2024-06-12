# PROJECT 1 - ARITHMETIC FORMATER

def convert_to_dictionary(input_data):
    transformed_data = []

    #converting each element to a dictionary with neccessary keys-values
    for data in input_data:
        if data.find('+') >= 0:
            sign = '+'
            sign_index = data.find('+')
        elif data.find('-') >= 0:
            sign = '-'
            sign_index = data.find('-')
        else:
            raise ValueError("Error: Operator must be '+' or '-'.")
        
        #extracting the two operands from the string, with no trailing spaces
        operand1 = data[0:sign_index].replace(' ', '')
        operand2 = data[sign_index+1: len(data)].replace(' ', '')

        if (not operand1.isnumeric() or not operand2.isnumeric()):
            raise ValueError("Error: Numbers must only contain digits.")
        if (len(operand1) > 4 or len(operand2) > 4):
            raise ValueError('Error: Numbers cannot be more than four digits.')
        
        #outlining properties for each problem
        if sign == '+':
            result = int(operand1) + int(operand2)
        else:
            result = int(operand1) - int(operand2)
        max_length = max(len(str(operand1)), len(str(operand2)))
        length_diff = max_length - min(len(str(operand1)), len(str(operand2)))
        line_cut = ''.join(['-']*(max_length+2))
        
        #transformed string problem into dictionary
        new_dict = {
            'operand1': operand1,
            'operand2': operand2,
            'sign' : sign,
            'result' : result,
            'max_operand_length' : max_length,
            'length_diff' : length_diff,
            'line_cut' : line_cut
        }

        transformed_data.append(new_dict)

    return transformed_data

def display_dictionary_data(dictionary_data, show_result):
    operand1_line_display = ""
    operand2_line_display = ""
    cut_line_display = ""
    result_line_display = ""
    total_display = ""

    for data in dictionary_data:

        #numerical operands display handling
        operands1_spacing = [
            "".join([" "]*data["length_diff"])+"".join([data["operand1"]]) 
            if len(data["operand1"])<data["max_operand_length"]
            else "".join([data["operand1"]])
        ]
        operands2_spacing = [
            "".join([" "]*data["length_diff"])+"".join([data["operand2"]]) 
            if len(data["operand2"])<data["max_operand_length"]
            else "".join([data["operand2"]])
        ]

        #handling display of each line : operands line, cut line and result line
        operand1_line_display += "  " + "".join(operands1_spacing) + "    "
        operand2_line_display += data["sign"] + " " + "".join(operands2_spacing) + "    "
        cut_line_display += data["line_cut"] + "    "
        result_line_display += "".join([" "*(data["max_operand_length"]+2 -len(str(data["result"])))]) +str(data["result"]) + "    "

    #removing trailing last spaces
    operand1_line_display = operand1_line_display[0:len(operand1_line_display)-4]
    operand2_line_display = operand2_line_display[0:len(operand2_line_display)-4]
    cut_line_display = cut_line_display[0: len(cut_line_display)-4]
    result_line_display = result_line_display[0: len(result_line_display)-4]

    if show_result:
        return operand1_line_display+"\n"+operand2_line_display+"\n"+cut_line_display+"\n"+result_line_display
    return operand1_line_display+"\n"+operand2_line_display+"\n"+cut_line_display+"\n"


def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
            raise ValueError('Error: Too many problems.')

    # Converting strings' array to dictionaries' array
    dictionaries = convert_to_dictionary(problems)

    # formatting all dictionary elements to required output string
    return display_dictionary_data(dictionaries, show_answers)


print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')