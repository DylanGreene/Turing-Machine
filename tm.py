#!/usr/bin/python

# Imports
# =============================================================================

import getopt
import sys
import os

# Global variables
# =============================================================================

PROGRAM_NAME    = os.path.basename(sys.argv[0])
MAX_TRANSITIONS = 200
DEF_FILE        = ''
IN_FILE         = ''

# Functions

def error(message, exit_code = 1):
    print >>sys.stderr, message
    sys.exit(exit_code)

def usage(exit_code = 0):
    error('''Usage: {} [ -n MAX_TRANSITIONS ] TM_DEF_FILE TEST_FILE

    Options:

        -n MAX_TRANSITIONS - Set the max number of transitions
        -h Show this help message'''
        .format(PROGRAM_NAME, exit_code))

# Parse command line arguments
# =============================================================================

try:
    options, arguments = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    error(e)

for option, value in options:
    if option == '-h':
        usage(0)
    elif option == '-n': # Option for setting max number of transitions
        MAX_TRANSITIONS = value
    else:
        usage(1)

if len(arguments) < 2 or len(arguments) > 2:
    usage(1)
else:
    DEF_FILE = arguments[0]
    IN_FILE = arguments[1]

# Main Execution
# =============================================================================

# Open the TM defition file and load its contents
with open(DEF_FILE) as f:
    definition_lines = f.readlines()
# Strip the trailing whitespace from each line in the def file
for i in range(len(definition_lines)):
    definition_lines[i] = definition_lines[i].rstrip()

# Print the machine name
print definition_lines[0]
# Parse the two alphabets
alphabet = definition_lines[1].split(",")
tape_alphabet = definition_lines[2].split(",")
# Include the alphabet and _ in the tape_alphabet
for symbol in alphabet:
    tape_alphabet.append(symbol)
tape_alphabet.append("_")
# Parse the rest of the machine defition
states = definition_lines[3].split(",")
start_state = definition_lines[4]
accept_state = definition_lines[5]
reject_state = definition_lines[6]
rules = definition_lines[7:]
# Print the rules with associated rule number
rule_n = 0
for rule in rules:
    rule_n = rule_n + 1
    print "{}: {}".format(rule_n, rule)
print

# Print the name of the test file
print "Test File: {}".format(IN_FILE)
# Open the FA test file and load its contents
with open(IN_FILE) as f:
    input_lines = f.readlines()
# Strip the trailing whitespace from each line in the test file
for i in range(len(input_lines)):
    input_lines[i] = input_lines[i].rstrip()

# Loop over each of the test strings
for line in input_lines:
    print "Tape: {}".format(line) # Print the test string
    tape = list(line) # Split the test string up
    tape_index = 0
    next_state = start_state
    step = 1
    print "1@0#|{}|{}".format(start_state, "".join(tape))
    # Continue moving on the tape until an invalid symbol or reached max #
    while tape[tape_index] in tape_alphabet and step < MAX_TRANSITIONS:
        curr_state = next_state
        next_state = None
        step = step + 1
        rule_n = 0
        # Loop over the rules to find one given current state and symbol
        for rule in rules:
            rule = rule.split(",")
            rule_n = rule_n + 1
            # If a transition has been found
            if curr_state == rule[0]:
                if tape[tape_index] == (rule[1].split("|"))[0]:
                    # Update the TM variables
                    next_state = (rule[1].split("|"))[1]
                    tape[tape_index] = rule[2]
                    move = rule[3]
                    if move == "R":
                        tape_index = tape_index + 1
                        if tape_index == len(tape):
                            tape.append("_")
                    elif move == "L":
                        if not tape_index == 0:
                            tape_index = tape_index - 1
                    else:
                        error("Invalid tape move direction")
                    # Print the output in the configuration like format
                    try:
                        i = tape.index("_")
                    except ValueError:
                        i = len(tape)
                    print "{}@{}#{}|{}|{}".format(step, tape_index,
                        "".join(tape[0:tape_index]), next_state, "".join(tape[tape_index:i]))
                    break
        if next_state is None or next_state == reject_state:
            next_state = reject_state
            break
        elif next_state == accept_state:
            break

    # Print the final tape at the end
    try:
        i = tape.index("_")
    except ValueError:
        i = len(tape)
    if next_state == accept_state:
        print "Accepted: {}".format("".join(tape[:i]))
    elif next_state == reject_state:
        print "Rejected: {}".format("".join(tape[:i]))
    else:
        print "Error: {}".format("".join(tape[:i]))
