#!/bash/bin
# Ask the user to input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold):  ").lower()

#Clothing Recommendation
if weather == 'sunny':
    print('Wear a t-shirt and sunglasses.')

elif weather == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif weather == 'cold':
    print('Make sure to wear a warm coat and a scarf.')
else:
    print("Sorry, I don't have recommendations for this weather.")

