from random import choice

breakfast = ['porridge', 'crumpets', 'bagel', 'jam on toast', 'marmite on toast', 'cereal']
lunch = ['sandwich', 'leftovers', 'cous cous']
dinner = ['spaghetti bolognese', 'salad', 'sticky tofu', 'lasagna', 'curry', 'burger', 'pad thai', 'quiche', 'nut roast', 'tacos', 'falafel wraps', 'pizza', 'pesto pasta', 'chicken and chips', 'roast aubergine']

print("Hello and welcome to the Meal Decider! Are you looking for breakfast, lunch or dinner?")

meal_type = input()

if meal_type == "breakfast":
    print(choice(breakfast))
    print("Thank you for using the Meal Decider! Come again soon :-)")

if meal_type == "lunch":
    print(choice(lunch))
    print("Thank you for using the Meal Decider! Come again soon :-)")

if meal_type == "dinner":
    print (choice(dinner))
    print("Thank you for using the Meal Decider! Come again soon :-)")


else:
    print("I don't recognise that meal type! Please choose breakfast, lunch or dinner")
