#!/usr/bin/env python

# -------------------------------------------------------------------------------
# Author :     Sumedh Vilas Datar
# Name:        check_true_false
# Purpose:     Main entry into logic program. Reads input files, creates
#              base, tests statement, and generates result file.
#
# Created:     10/12/2017
# Last Edited: 10/21/2017
# Notes:         
#            *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so I put it in a list, which
#               is passed by reference.
#              *Written to be Python 2.4 compliant for omega.uta.edu
# -------------------------------------------------------------------------------

import sys
from logical_expression import *
def main(argv):
    argv = ["Check","a1.txt","b1.txt","c1.txt"]
    if len(argv) != 4:
        print('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0])
        sys.exit(0)

    # Read wumpus rules file
    try:
        input_file = open(argv[1], 'rb')
    except:
        print('failed to open file %s' % argv[1])
        sys.exit(0)

    # Create the knowledge base with wumpus rules
    print '\nLoading wumpus rules...'
    knowledge_base = logical_expression()
    knowledge_base.connective = ['and']
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # A mutable counter so recursive calls don't just make a copy
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Read additional knowledge base information file
    try:
        input_file = open(argv[2], 'rb')
    except:
        print('failed to open file %s' % argv[2])
        sys.exit(0)

    # Add expressions to knowledge base
    print '\nLoading additional knowledge...'
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # a mutable counter
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Verify it is a valid logical expression
    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    # I had left this line out of the original code. If things break, comment out.
    print_expression(knowledge_base, '\n',"required")

    # Read statement whose entailment we want to determine
    try:
        input_file = open(argv[3], 'rb')
    except:
        print('failed to open file %s' % argv[3])
        sys.exit(0)
    print '\nLoading statement...'
    statement = input_file.readline().rstrip('\r\n')
    input_file.close()

    # Convert statement into a logical expression and verify it is valid
    statement = read_expression(statement)
    if not valid_expression(statement):
        sys.exit('invalid statement')

    # Show us what the statement is
    print '\nChecking statement: ',
    print_expression(statement, '',"not_required")
    #print
    # for m in knowledge_base.subexpressions:
    #     print m
    # Run the statement through the inference engine
    #print "Lets print here"
    #print knowledge_base.subexpressions[1].subexpressions[1].connective
    print "Lets get the symbols"
    #symbols = []
    #cool = extract_symbols(knowledge_base)
    #print cool
    #print knowledge_base.subexpressions[0].subexpressions[0].symbol[0]
    check_true_false(knowledge_base, statement)


def extract_symbols(sentence):
    m = sentence.symbol[0]
    if sentence.symbol[0]!= '':
        print sentence.symbol[0]
    else:
        for child in sentence.subexpressions:
            extract_symbols(child)



    #sys.exit(1)


if __name__ == '__main__':
    main(sys.argv)