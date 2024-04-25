# Danesh_Amooz
#### Video Demo: <https://aparat.com/v/NpM7k>
#### Description:
we have three functions named main, check_correct_args, select_house. We import the csv,sys library before defining the functions.
in the check_correct_args function, we define three main conditions for the input:
1) if len(sys.argv) was less than 3, print a message (Too few command-line arguments) for us
2) if len(sys.argv) was more than 3, print a message (Too many command-line arguments) for us.
3) if the csv extension was not in sys.argv[1] or if the csv extension was not in the sys.argv[2] file, print the message (Not CSV files)
and in the select_house function, we defined these items:
1) if the input char in courage, loyalty, adventure which was located in danesh.csv file, return the Gryffindor value.
2) Otherwise, if the input char was in dedication, patience, honesty, return Hufflepuff fv value.
3) Otherwise, if the input char was in wisdom, creativity, perfectionism, return Ravenclaw fv value.
4) Otherwise, if the input char was in ambition, competitive, leadership, return Slytherin fv value.
5) Otherwise, it will return (No House).
now the select_grade function:
1) We define a variable called age that subtracts the input year from 2022
2) Then we define a variable named grade, which subtracts age from 5
3) And then we sum the value of word Grade with str grade
And the main function:
1) First, we open the check_correct_args function here and then define a list called data
2) We put an error handler in the Try section by opening sys.argv[1], which is like a csvfile.
3) We define a variable called khandan in which we import with csv, write the dictreader method and put the csvfile in it.
4) For the khan variable that is in khandan: add the khan variable from the data list of the append method
5) In the execpt error management section, we set the FileNotFoundError error to print the Could't read CSV file error.
6) We define an empty list called khoroj, and then for each khan we have in the data, we have a variable called house that we can access with the select_house function through the khan variable of the characteristic object.
7) The next line is the same as before. We define a variable named grade and through the select_grade function we call the khan variable so that birthdate is listed.
8) Now we want to add name, house, grade in the list called khoroj through append method. We only add name with khan
9) By opening sys.argv[2] like a file, we define a variable called Nevis, which uses the csv package that we imported before to sort the fields based on name, house and grade with the dictwriter method.In the next line, we give the fields to the dictionary with the Nevis variable to the writerow method
10) For each khan variable that is in khoroj: do the same as line 23, only with the difference that we put the khan variable in the list
At the end of our Python code, we call main as always