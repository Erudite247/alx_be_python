#!/bash/bin
# Ask the user to input the current weather
<<<<<<< HEAD
current_weather = input("What's the weather like today? (sunny/rainy/cold):  ").lower()

# Clothing Recommendations
if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
=======
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

>>>>>>> 2faa3f79e1e196ff4e545271d0b97b0c1ba5d59d
