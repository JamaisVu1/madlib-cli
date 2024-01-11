# ChatGPT was a big help

import os, re

def read_template(template_file):
    try:
        with open(template_file, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {template_file}")
    
def parse_template(template):
    parts = tuple(re.findall(r'{(.*?)}', template))
    stripped_template = re.sub(r'{[^}]*}', '{}', template)
    return stripped_template.strip(), parts
     
     
def merge(template, user_inputs):
    return template.format(*user_inputs)


def print_welcome_message():
    print("Welcome to Madlibs! ")
    
def get_user_inputs(placeholders):
    user_inputs = {}
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder.lower()}: ")
        user_inputs[placeholder] = user_input
    return [user_inputs[placeholder] for placeholder in placeholders]

def save_to_file(completed_madlib, output_file):
    with open(output_file, 'w') as file:
        file.write(completed_madlib)

def main():
    print_welcome_message()

   
    template_file = 'assets/madlib_template.txt'  
    try:
        template = read_template(template_file)
        stripped_template, placeholders = parse_template(template)
    except FileNotFoundError as e:
        print(e)
        return

   
    user_inputs = get_user_inputs(placeholders)

   
    completed_madlib = merge(stripped_template, user_inputs)

   
    print("\nCompleted Madlib:\n")
    print(completed_madlib)

   
    output_file = 'completed_madlib.txt'
    save_to_file(completed_madlib, output_file)

    print(f"\nCompleted Madlib saved to '{output_file}'.")

if __name__ == "__main__":
    main()