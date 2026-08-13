# Simple AI-style Example
# Rule-based decision system

weather = input("Enter weather (sunny/rainy): ").lower()

if weather == "sunny":
    print("Recommendation: You can go outside.")
elif weather == "rainy":
    print("Recommendation: Carry an umbrella.")
else:
    print("Recommendation: Weather information not recognized.")
