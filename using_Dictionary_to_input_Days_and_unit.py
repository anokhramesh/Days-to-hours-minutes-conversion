# In this Program- we will convert Days to Hours or Minutes.
# So user can input two parameters in this format-1:hours or 1:minutes.
def days_to_units(num_of_days,conversion_unit):#function for conversion.
    if conversion_unit == "hours":# if user input is days and hours-apply this formula.
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit =="minutes":# if user input is days and minute-apply this formula. 
        return f"{num_of_days} days are {num_of_days *24*60} minutes"
    else:
        return "unsupported unit"    #if user input is none of the above value print-unsupported unit.
def validate_and_execute():#function for validating the calculation.
    try:
        user_input_number =int(days_and_unit_dictionary["days"])#only convert if user input is a positive value.
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)#print the calculated value.
        elif user_input_number == 0:#if user input is a 0,print the below message.
            print("You Entered  0,Please enter a valid positive number")
        else:#if user input is a negative number-print the below message.
            print("You Entered a negative number,Not Possible conversion")
    except ValueError:#if user input is a float value or string or character-print the belo message.
        print("Your input is not a valid number")
user_input =""# created a variable name user_input.
while user_input != "exit":#continue loop untill the user typed a string -exit.
    user_input =input("Enter number of Days and unit(1:hours/minutes)\n")# num of days : unit(hour or minutes)
    days_and_unit = user_input.split(":")# splitting the user input to two parts with seperate a column.
    days_and_unit_dictionary ={"days":days_and_unit[0],"unit":days_and_unit[1]}#assigning the days and unit to days_and_unit_dictionary variable.
    #print(days_and_unit_dictionary)#print the values of-days_and_unit_dictionary variable.
    #print(type(days_and_unit_dictionary))#print the type of-days_and_unit_dictionary variable.
    validate_and_execute()# calling the validate_and_execute function.