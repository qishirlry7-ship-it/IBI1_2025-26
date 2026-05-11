class food_item:
    def __init__(self, name, calories, protein, carbohydrates, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat

def nutrition_report(food_list):
    total_calories = 0
    total_protein = 0
    total_carbohydrates = 0
    total_fat = 0

    for item in food_list:
        total_calories = total_calories + item.calories
        total_protein = total_protein + item.protein
        total_carbohydrates = total_carbohydrates + item.carbohydrates
        total_fat = total_fat + item.fat

    print('Total calories:', total_calories)
    print('Total protein:', total_protein, 'g')
    print('Total carbohydrates:', total_carbohydrates, 'g')
    print('Total fat:', total_fat, 'g')

    if total_calories > 2500:
        print('Warning: calorie intake is more than 2500 calories')

    if total_fat > 90:
        print('Warning: fat intake is more than 90 g')

apple = food_item('apple', 60, 0.3, 15, 0.5)
noodles = food_item('noodles', 450, 12, 80, 8)
burger = food_item('burger', 800, 35, 50, 45)
milk = food_item('milk', 150, 8, 12, 5)

food = [apple, noodles, burger, milk]

nutrition_report(food)
