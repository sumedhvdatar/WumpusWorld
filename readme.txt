NAME : Sumedh Vilas Datar
-------------------------------------------------------------------------------------------------------------------------------------------------------------
PROGRAMMING LANGUAGE : Python (2.7 , compatible with omega )
-------------------------------------------------------------------------------------------------------------------------------------------------------------
CODE STRUCTURE : 

The folder assignment_5_Sumedh_Vilas_Datar_1001365726 contains two python files called check_true_false.py and logical_expression.py and one file for rules. 
Inside assignment_folder there is another folder named WumpusWorldSlower which has the files which has just plain implementation of tt_entails algorithm.

check_true_false.py conatins the code related to extraction of data and reading the text files which are given as input.

logical_expression.py has all the contents related to the tt_entails algorithm.

wumpus_rules.txt : This has all the rules of the game.

Inoreder to reduce the computational time, I have also implemented the algorithm to reduce the model by checking for those symbols which are single ie either
they have a positive single symbol or not of the single symbol. The algorithm will cut down on unnecessary truth table building and knowledge base building.This will make
the program run faster and give output within a short time.

Implementation on the reduction of computational time :

Read each file and store all the information of single symbols and their respective boolean value in a hashmap as a key value pair. 

Before sending symbols to tt_entails make sure that the symbols are modified. The symbols are modified by checking with the hashmap and for those symbols which have a boolean 
value, they are assigned a flag and appended into the symbol list

The symbol list is now sent to the tt entails algorithm and the symbol with a flag will have only one recursive call with the respective boolean function. this will reduce the 
computational time
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
RUNNING THE PROGRAM

$python check_true_false.py $wumpus_rules.txt $additional_information_file.txt $statement.txt

The output of the program is a result.txt file which has the final output.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
