import validators
import analyzer
import formatting
import generators
import scoring

# 1. User Input & Generators
password = validators.get_valid_password()
analysis_id = generators.generate_analysis_id()
current_date = generators.get_current_date()

# 2. Analyze Features
has_numbers = analyzer.has_number(password)
has_lowercases = analyzer.has_lowercase(password)
has_uppercases = analyzer.has_uppercase(password)
has_special = analyzer.has_special_character(password)
password_length = analyzer.get_password_length(password)

# 3. Calculate Score, Strength, and Recommendations
score = scoring.calculate_security_score(
    has_numbers, has_lowercases, has_uppercases, has_special, password_length
)
strength = scoring.get_password_strength(score)
recommendations = scoring.get_recommendations(
    has_numbers, has_lowercases, has_uppercases, has_special, password_length
)

# 4. Print Structured Output
print(formatting.format_header(analysis_id, current_date))
print(formatting.format_password_analysis(password_length))
print(formatting.format_security_checks(has_uppercases, has_lowercases, has_numbers, has_special, password_length))
print(formatting.format_score_summary(score, strength))
print(formatting.format_recommendations(recommendations))