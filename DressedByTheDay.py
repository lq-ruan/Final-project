#Enter the corresponding warmth and emoji for each cloth
clothes_warmth= {
    "T-shirt": 2,
    "Sweater": 5,
    "Jacket": 8,
    "Coat": 10,
    "Scarf": 3,
    "Shorts": 1,
    "Jeans": 3,
    "Thermal Pants": 6}

clothes_emoji = {
    "T-shirt": "👕",
    "Sweater": "🧥",
    "Jacket": "🥼",
    "Coat": "🧥",
    "Scarf": "🧣",
    "Shorts": "🩳",
    "Jeans": "👖",
    "Thermal Pants": "🧦"
}

def get_feels_like(temp: float, windy:bool, rainy:bool):
    if windy and rainy:
        return temp-4
    elif rainy or windy:
        return temp-2
    else:
        return temp

def generate_outfit(items):
    outfit = []

    # 1-item
    for i in range(len(items)):
        outfit.append([items[i]])

    # 2-item combos
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            outfit.append([items[i], items[j]])

    # 3-item combos
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            for k in range(j + 1, len(items)):
                outfit.append([items[i], items[j], items[k]])

    return outfit


# Outfit recommendation
def recommend_clothes(clothes_warmth, temp, feels_like_target):
    warmth_needed = feels_like_target - temp
    best_combo = None
    closest_total = None

    items = list(clothes_warmth)
    all_combos = generate_outfit(items)

    for combo in all_combos:
        total = sum(clothes_warmth[item] for item in combo)
        if total <= warmth_needed and (closest_total is None or total > closest_total):
            closest_total = total
            best_combo = combo

    if best_combo is None:
        return []
    else:
        return best_combo, closest_total


# Describe the outfit
def describe_outfit(combo, weather):
    introduction = f"📸 Picture this: it's a {weather} day, and you're heading out in style."

    details = " "
    for item in combo:
        emoji = clothes_emoji[item]
        details += f"{emoji} Wearing your {item.lower()}\n"

    ending = ("✨ You'll look great and stay perfectly comfortable all day.")

    return f"{introduction}\n{details}\n\n{ending}"


# ------------------------------
# Main program - Interaction with the users
def main():
    print("👚 Welcome to the Comfort Temperature Dressing Assistant!")
    print("🌦️ We'll help you dress just right to enjoy a warm and comfortable winter day in Sydney (around 0°C to 25°C).")

    print("\n🌡️ Let’s start with today’s temperature.")
    while True:
        try:
            current_temp = float(input("What’s the temperature outside today? (°C): "))
            if 0 <= current_temp <= 25:
                break
            else:
                print("Hmm, that doesn’t seem quite right. Please enter a number between 0°C and 25°C.")
        except ValueError:
            print("Oops! That’s not a number. Let’s try again！")

    print("\n💨 Is there a breeze today?")
    while True:
            wind_input = input("Is it windy today? (yes/no): ").strip().lower()
            if wind_input == "yes":
                windy = True
                break
            elif wind_input == "no":
                windy = False
                break
            else:
                print("Just type 'yes' or 'no', no pressure!")

    print("\n🌧️Let’s check the sky...")
    while True:
            rain_input = input("Is it raining today? (yes/no): ").strip().lower()
            if rain_input == "yes":
                rainy = True
                break
            elif rain_input == "no":
                rainy = False
                break
            else:
                print("Just type 'yes' or 'no', no pressure!")


    default_comfort = 26
    print("\n🌡️Let’s find your comfort zone...")
    while True:
        user_input = input(f"What's your comfort temperature? (default: {default_comfort}): ").strip()
 