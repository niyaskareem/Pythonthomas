###Practice Question 1----------------------------------
#Create list of 5 veggies
veggies = ["vellarika", "kappanga", "carrot", "achinga", "mathanga"]

print("Answers to your question 1 is as below")
#Print first vegetable
print(veggies[0])

#Print last veggie
print(veggies[-1])

#Print middle 3 veggies
print(veggies[1:4])

#changing second last vegetable with Tomato
veggies[-2] = "Tomato"
print(veggies)
print("---------------------END OF ANSWER 1------------------")
###Practice question 2----------------------------------
print("Answers to your question 2 is as below")
lat_lon_1 = (1.2345,5.324234)
lat_lon_2 = (12.2323,45.44535)
lat_lon_3 = (14.2323,48.44535)
lat_lon_4 = (18.2345,55.324234)
lat_lon_5 = (28.2323,9.44535)

lat_lon_list = list(lat_lon_5)
lat_lon_list[:2] = 0,0
lat_lon_5 = tuple(lat_lon_list)
print(lat_lon_5)
print("---------------------END OF ANSWER 2------------------")
###Practice question 3----------------------------------
print("Answers to your question 3 is as below")
personal_details = {"Name" : "niyas",
                    "Age" : 25,
                    "Telephone" : 231212323,
                    "Address" : {
                        "City" : "Cochin",
                        "Landmark" : "Toyota building",
                        "POBOX" : 683104
                    }}

print(personal_details["Address"]["City"])
print("---------------------END OF ANSWER 3------------------")
###Practice question 4----------------------------------
print("Answers to your question 4 is as below")
#Created a marklist
marks = [75,85,45,65,70]

#Initializing total marks variable and fail flag
marks_sum = 0
fail = 0
#Iterating through the marks list calculating the total marks and flagging if he has secured less than 45 for any of the subject
for items in marks:
    if items < 45:
        fail = 1
    else:
        marks_sum = marks_sum + items
#Finding the average of his marks
marks_avg = marks_sum/len(marks)

#If he has secured less 45 for any subject, then it means he failed else he will fall into either Distinction or passed category
if fail == 1:
    print("Failed Miserably")
else:
    if marks_avg > 75:
        print("Distinction")
    else:
        print("Passed")

print("---------------------END OF ANSWER 4------------------")