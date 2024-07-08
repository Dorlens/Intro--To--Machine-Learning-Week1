"Dorlens - Assignment: As#4 - ML Knowledge Check"
 


"""Create a BMI ( Body Mass Index) calculator. BMI is body_weight (measured in pounds ) adds on 703, further divided by the square of the square of person's height (measured in inches). 
For example, John weighs 200 pounds, stands at 6 feet. His BMI would be (200 X 703) / (72^2) ≈ 27.14
The program would ask for 3 things for each person:
1) name
2) weight
3) height
Note: most of the persons would stand X feet Y inches. Before you compute the BMI, you need to convert the height to 'inches'
Finally, output that person's BMI. """



name = input("What's your name? ")
weight = float(input("How much you weigh in pounds? "))
feet = int(input("What's your height in feet? "))
inches = int(input("whats your reminding inches? "))

height = feet * 12 + inches # converted feet to inches 

bmi = (weight * 703) / (height **2) # body mass index 

print(f"{name} weighs {weight} pounds and stands at {feet} feet {inches} inches her BMI would be {bmi}")