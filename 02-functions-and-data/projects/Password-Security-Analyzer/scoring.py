def calculate_security_score(has_numbers, has_lowercases, has_uppercases, has_special, password_length) -> int:
    score = 0
    if password_length >= 8:
        score += 20
    if password_length >= 12:
        score += 10
    if has_uppercases:
        score += 15
    if has_lowercases:
        score += 15
    if has_numbers:
        score += 15
    if has_special:
        score += 15
    if password_length >= 16:
        score += 10

    return score



def get_password_strength(score) -> str:
    if 0 <= score < 40:
        return "Very Weak"
    elif 40 <= score < 60:
        return "Weak"
    elif 60 <= score < 75:
        return "Moderate"
    elif 75 <= score < 90:
        return "Strong"
    elif 90 <= score <= 100:
        return "Excellent"
    

def get_recommendations(has_numbers, has_lowercases, has_uppercases, has_special, password_length) -> list[str]:
    recommendations = []

    if password_length < 8:
        recommendations.append("Increase length to at least 8 characters.")

    elif password_length < 12:
        recommendations.append("Increase length to 12+ characters for better protection.")

    elif password_length < 16:
        recommendations.append("Increase length to 16+ characters for better protection.")

    if not has_uppercases:
        recommendations.append("Add at least one uppercase letter (A-Z).")

    if not has_lowercases:
        recommendations.append("Add at least one lowercase letter (a-z).")

    if not has_numbers:
        recommendations.append("Add at least one number (0-9).")

    if not has_special:
        recommendations.append("Add at least one special character (!@#$%^&*).")

    if not recommendations:
        recommendations.append("Great job! Your password meets all basic security criteria.")

    return recommendations
