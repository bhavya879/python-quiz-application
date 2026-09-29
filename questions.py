def return_questions():
    questions = [
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. func", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["A. input()", "B. print()", "C. output()", "D. display()"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store whole numbers?",
        "options": ["A. float", "B. int", "C. str", "D. bool"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store decimal numbers?",
        "options": ["A. float", "B. int", "C. bool", "D. list"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which function is used to get user input?",
        "options": ["A. get()", "B. read()", "C. input()", "D. scan()"],
        "answer": "C"
    },
    {
        "question": "Which data type stores text values?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. //", "C. **", "D. %"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for floor division?",
        "options": ["A. /", "B. //", "C. %", "D. **"],
        "answer": "B"
    },
    {
        "question": "What is the output of print(10 % 3)?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 0"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used for conditional execution?",
        "options": ["A. when", "B. if", "C. check", "D. switch"],
        "answer": "B"
    },
    {
        "question": "Which keyword is executed when an if condition is false?",
        "options": ["A. default", "B. otherwise", "C. else", "D. except"],
        "answer": "C"
    },
    {
        "question": "Which loop iterates over a sequence?",
        "options": ["A. repeat", "B. loop", "C. for", "D. until"],
        "answer": "C"
    },
    {
        "question": "Which loop continues until a condition becomes false?",
        "options": ["A. for", "B. while", "C. repeat", "D. do"],
        "answer": "B"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": ["A. ()", "B. {}", "C. []", "D. <>"],
        "answer": "C"
    },
    {
        "question": "Which brackets are used to create a tuple?",
        "options": ["A. {}", "B. []", "C. <>", "D. ()"],
        "answer": "D"
    },
    {
        "question": "Which brackets are used to create a dictionary?",
        "options": ["A. []", "B. {}", "C. ()", "D. <>"],
        "answer": "B"
    },
    {
        "question": "Which data type stores only True or False values?",
        "options": ["A. int", "B. float", "C. bool", "D. str"],
        "answer": "C"
    },
    {
        "question": "Which function returns the length of a list?",
        "options": ["A. count()", "B. len()", "C. size()", "D. total()"],
        "answer": "B"
    },
    {
        "question": "Which keyword immediately exits a loop?",
        "options": ["A. stop", "B. continue", "C. pass", "D. break"],
        "answer": "D"
    },
    {
        "question": "Which keyword skips the current iteration of a loop?",
        "options": ["A. continue", "B. break", "C. stop", "D. next"],
        "answer": "A"
    },
    {
        "question": "Which keyword does nothing and acts as a placeholder?",
        "options": ["A. break", "B. continue", "C. pass", "D. skip"],
        "answer": "C"
    },
    {
        "question": "Which method adds an element to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insert()", "D. extend()"],
        "answer": "B"
    },
    {
        "question": "Which method removes the last item from a list?",
        "options": ["A. delete()", "B. remove()", "C. pop()", "D. clear()"],
        "answer": "C"
    },
    {
        "question": "Which method sorts a list in ascending order?",
        "options": ["A. arrange()", "B. order()", "C. sort()", "D. sortedlist()"],
        "answer": "C"
    },
    {
        "question": "What is the index of the first element in a list?",
        "options": ["A. 1", "B. -1", "C. 0", "D. Depends on list"],
        "answer": "C"
    },
    {
        "question": "Which method converts a string to uppercase?",
        "options": ["A. upper()", "B. capitalize()", "C. title()", "D. large()"],
        "answer": "A"
    },
    {
        "question": "Which method converts a string to lowercase?",
        "options": ["A. down()", "B. lower()", "C. small()", "D. casefold()"],
        "answer": "B"
    },
    {
        "question": "Which operator is used to check equality?",
        "options": ["A. =", "B. !=", "C. ==", "D. >="],
        "answer": "C"
    },
    {
        "question": "Which operator is used to assign a value?",
        "options": ["A. =", "B. ==", "C. :=", "D. !="],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to import a module?",
        "options": ["A. include", "B. require", "C. import", "D. using"],
        "answer": "C"
    },
    {
        "question": "Which built-in function returns the data type of an object?",
        "options": ["A. datatype()", "B. type()", "C. typeof()", "D. class()"],
        "answer": "B"
    },
    {
        "question": "Which module is commonly used for random number generation?",
        "options": ["A. math", "B. random", "C. numbers", "D. randint"],
        "answer": "B"
    },
    {
        "question": "Which function returns the absolute value of a number?",
        "options": ["A. mod()", "B. abs()", "C. absolute()", "D. fabs()"],
        "answer": "B"
    },
    {
        "question": "What will len('Python') return?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Which method removes all items from a list?",
        "options": ["A. delete()", "B. remove()", "C. clear()", "D. empty()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to create a class?",
        "options": ["A. object", "B. define", "C. class", "D. struct"],
        "answer": "C"
    },
    {
        "question": "Which special method acts as a constructor in Python classes?",
        "options": ["A. __start__", "B. __main__", "C. __init__", "D. __create__"],
        "answer": "C"
    },
    {
        "question": "Which keyword refers to the current object inside a class?",
        "options": ["A. self", "B. this", "C. object", "D. current"],
        "answer": "A"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": ["A. catch", "B. error", "C. try", "D. handle"],
        "answer": "C"
    },
    {
        "question": "Which block executes if an exception occurs?",
        "options": ["A. finally", "B. except", "C. catch", "D. try"],
        "answer": "B"
    },
    {
        "question": "Which block always executes after try-except?",
        "options": ["A. else", "B. final", "C. except", "D. finally"],
        "answer": "D"
    },
    {
        "question": "Which file mode is used to read a file?",
        "options": ["A. r", "B. w", "C. a", "D. x"],
        "answer": "A"
    },
    {
        "question": "Which file mode is used to write a file?",
        "options": ["A. r", "B. a", "C. w", "D. rw"],
        "answer": "C"
    },
    {
        "question": "Which file mode appends data to an existing file?",
        "options": ["A. r", "B. w", "C. x", "D. a"],
        "answer": "D"
    },
    {
        "question": "Which function opens a file in Python?",
        "options": ["A. file()", "B. open()", "C. read()", "D. fopen()"],
        "answer": "B"
    },
    {
        "question": "Which module is used for mathematical functions like sqrt()?",
        "options": ["A. random", "B. math", "C. statistics", "D. calc"],
        "answer": "B"
    },
    {
        "question": "What is the output type of input()?",
        "options": ["A. int", "B. float", "C. bool", "D. str"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to return a value from a function?",
        "options": ["A. output", "B. return", "C. yield", "D. print"],
        "answer": "B"
    },
    {
        "question": "Which built-in function converts a string to an integer?",
        "options": ["A. str()", "B. float()", "C. int()", "D. integer()"],
        "answer": "C"
    }
    ]
    return questions


