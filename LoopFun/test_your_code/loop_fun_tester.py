import subprocess

def run_test(input_data, test_case_number):
    # Start the student's script as a subprocess
    process = subprocess.Popen(['python', 'loop_fun_student.py'],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    # Send the test input data and get the output
    output, errors = process.communicate(input=input_data)

    # Build the output string for this test case
    test_output = f"Test Case {test_case_number}:\n"
    test_output += f"Input: {input_data.replace('\\n', ' ')}\n"
    test_output += "Output:\n"
    test_output += output
    test_output += "--------\n"

    return test_output

# Initialize an empty string to collect all outputs
all_outputs = ""

# Define your test cases
test_cases = [
    "5\n10\n",  # Normal Case
    "3\n6\n",   # Edge Case: Lower Bound on Height
    "5\n20\n",  # Edge Case: Upper Bound on Width
    "2\n6\n15\n",  # Invalid Height and Valid Width
    "4\n4\n12\n",   # Invalid Width and Valid Height
]

# Run each test case and collect outputs
for i, test_input in enumerate(test_cases, start=1):
    all_outputs += run_test(test_input, i)

# Overwrite the file with all the outputs from this run of the tester
with open('student_output.txt', 'w') as file:
    file.write(all_outputs)
