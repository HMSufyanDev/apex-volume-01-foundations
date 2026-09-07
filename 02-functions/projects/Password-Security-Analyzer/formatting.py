
def format_header(analysis_id: str, date: str) -> str:
    border = "=" * 50
    return f"""{border}
            PASSWORD SECURITY ANALYZER
{border}

Analysis ID: {analysis_id}
Date: {date}"""


def format_password_analysis(password_length: int) -> str:
    divider = "-" * 50
    return f"""
PASSWORD ANALYSIS
{divider}

Password Length: {password_length} characters"""


def format_security_checks(has_upper: bool, has_lower: bool, has_num: bool, has_spec: bool, length: int) -> str:
    divider = "-" * 50
    
    # Checkmarks and crosses
    check = "✓"
    cross = "✗"
    
    # Format each individual check line
    upper_str = f"{check if has_upper else cross} Contains uppercase letters"
    lower_str = f"{check if has_lower else cross} Contains lowercase letters"
    num_str = f"{check if has_num else cross} Contains numbers"
    spec_str = f"{check if has_spec else cross} Contains special characters"
    length_str = f"{check if length >= 12 else cross} Password should be at least 12 characters"
    
    return f"""
SECURITY CHECKS

{upper_str}
{lower_str}
{num_str}
{spec_str}
{length_str}

{divider}"""


def format_score_summary(score: int, strength: str) -> str:
    divider = "-" * 50
    return f"""
SECURITY SCORE: {score}/100

PASSWORD STRENGTH: {strength.upper()}

{divider}"""


def format_recommendations(recommendations: list[str]) -> str:
    border = "=" * 50
    
    if not recommendations:
        recs_text = "• Great job! No security recommendations at this time."
    else:
        recs_text = "\n".join(f"• {rec}" for rec in recommendations)
        
    return f"""
RECOMMENDATIONS

{recs_text}

{border}"""