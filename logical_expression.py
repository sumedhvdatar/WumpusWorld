#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 07/22/2013
# Notes:       *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from copy import copy


#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos

all_symbols = []
truth_table = []
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []


def print_expression(expression, separator,identifier):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print '\nINVALID\n'

    elif expression.symbol[0]: # If it is a base case (symbol)
        all_symbols.append(expression.symbol[0])
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '',identifier)
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
            read_subexpressions(input_string, counter, result.subexpressions)
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break
    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print '\nUnexpected end of input.\n'
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            subexpressions.append(expression)


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# End of ported code
#-------------------------------------------------------------------------------

# Add all your functions here
def check_true_false(knowledge_base, statement):
	#your code goes here
    print '\nYour code goes here\n'
    value_for_entails = tt_entails(knowledge_base,statement)
    print "This is for positive alpha"
    print value_for_entails
    #print "This is for not tt entails"
    negation_alpha = logical_expression()
    negation_alpha.connective = ['not']
    negation_alpha.subexpressions = statement
    value_for_not_entails = tt_entails(knowledge_base,negation_alpha)
    print "This is for negation Alpha"
    print value_for_not_entails
    if value_for_entails == True and value_for_not_entails != True:
        print "It is definitely true"
    elif value_for_entails != True and value_for_not_entails == True:
        print "It is definitely false"
    elif value_for_not_entails != True and value_for_entails != True:
        print "It is possibly true,possibly false"
    elif value_for_entails == True and value_for_not_entails == True:
        print "It is both true and false"


    #for m in truth_table:
    #    print m


def tt_entails(knowledge_base,alpha):
    #new_list = []
    symbols = []
    model = {}
    #print all_symbols
    for i in all_symbols:
        #check = i.split("|")
        if i not in symbols:
            symbols.append(i)
            #knowledge_base.symbol.append(i.split("|")[0])
    #knowledge_base.subexpressions.subexpressions.symbol[0]
    return tt_check_all(knowledge_base,symbols,alpha,model)


def tt_check_all(knowledge_base,symbols,alpha,model):
    #print symbols
    if not symbols:
        #print "We generated the model"
        #print model
        truth_table.append(model)
        if pl_true(knowledge_base,model):
            print "This is the model"
            print model
            print pl_true(knowledge_base,model)
            #print pl_true(knowledge_base,model)
            result = pl_true(alpha, model)
            #assert result in (True, False)
            return result
        else:
            print "This is for else"
            print model
            print pl_true(knowledge_base,model)
            return True
    else:
        #print model
        symbol_to_be_removed, rest = symbols[0], symbols[1:]
        #rest = symbols
        model_true = extend(model,symbol_to_be_removed,True)
        model_false = extend(model,symbol_to_be_removed,False)
        #return tt_check_all(knowledge_base,rest,alpha,extend(model,symbol_to_be_removed,True)) and tt_check_all(knowledge_base,rest,alpha,extend(model,symbol_to_be_removed,False))
        o1 = tt_check_all(knowledge_base, rest, alpha,model_true)
        o2 = tt_check_all(knowledge_base, rest, alpha,model_false)
        return o1 and o2
def pl_true(sentence,model):

    m = sentence.symbol[0]
    if sentence.symbol[0] != '':
        #print "final"
        #print model
        return model[sentence.symbol[0]]
    elif sentence.connective[0].lower() == "and":
        for child in sentence.subexpressions:
            #print child.subexpressions.symbol[0]
            if pl_true(child, model) == False:
                return False
        return True

    elif sentence.connective[0].lower() == "or":
        for child in sentence.subexpressions:
            # print child.subexpressions.symbol[0]
            if pl_true(child, model) == True:
                return True
        return False

    elif sentence.connective[0].lower() == "if":
        left_child = sentence.subexpressions[0]
        right_child = sentence.subexpressions[1]
        #print pl_true(left_child,model)
        #print pl_true(right_child,model)
        if pl_true(left_child, model) == True and pl_true(right_child,model) == False:
            return False
        return True

    elif sentence.connective[0].lower() == "iff":
        left_child = sentence.subexpressions[0]
        right_child = sentence.subexpressions[1]
        #print "for iff"
        #print pl_true(left_child, model)
        #print pl_true(right_child, model)
        if pl_true(left_child, model) == pl_true(right_child, model):
            return True
        return False


    elif sentence.connective[0].lower() == "not":
        #for child in sentence.subexpressions:
        #child = sentence.subexpressions.symbol[0]
        #check_symbol = sentence.subexpressions[0].symbol[0]
        #result = None
        if hasattr(sentence.subexpressions,'__len__'):
            child = sentence.subexpressions[0]
            if pl_true(child, model) == True:
                return False
            else:
                #result =  True
                return True
        else:
            child = sentence.subexpressions
            if pl_true(child, model) == False:
                return True
            elif pl_true(child,model) == True:
                return False

    elif sentence.connective[0].lower() == "xor":
        number_of_symbols = 0
        for child in sentence.subexpressions:
            # print child.subexpressions.symbol[0]
            #print "for xor"
            #print pl_true(child,model)
            if pl_true(child, model) == True:
                number_of_symbols = number_of_symbols + 1
        if number_of_symbols == 1:
            return True
        else:
            return False

def extend(model, var, val):
    """Copy the substitution s and extend it by setting var to val; return copy."""
    s2 = model.copy()
    s2[var] = val
    return s2


def read_rules_file(input_file):
    input_file = open(input_file, 'rb')
    for line in input_file:
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # A mutable counter so recursive calls don't just make a copy
        subexpression = valid_expression(line.rstrip('\r\n'))
    input_file.close()
