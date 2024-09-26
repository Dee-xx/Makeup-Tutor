def recommend_makeup(skin_tone):
    recommendations = {
        "fair": "Try pastel colors or soft pinks.",
        "medium": "Warm tones like coral or peach work well.",
        "dark": "Deep shades like burgundy or plum are great choices."
    }
    return recommendations.get(skin_tone.lower(), "Please enter a valid skin tone.")

user_skin_tone = input("Enter your skin tone (fair, medium, dark): ")
print(recommend_makeup(user_skin_tone))
