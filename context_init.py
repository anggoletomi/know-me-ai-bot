from config import *

def create_context():
    """
    Dynamically create a context string for the chatbot based on variables in config.py.
    Handles all variables starting with 'OWNER_', including user-defined ones.
    Skips variables that are missing, empty, or incorrectly formatted.
    """
    # Default prompt
    context = ASSISTANT_PROMPT if 'ASSISTANT_PROMPT' in globals() and ASSISTANT_PROMPT else (
        "Always respond in a formal tone, be very welcoming, and provide helpful answers. "
    )

    preferred_name = OWNER_NICK_NAME if 'OWNER_NICK_NAME' in globals() and OWNER_NICK_NAME else OWNER_FULL_NAME

    context += f"The owner prefers to be called {preferred_name}. You should always refer to them as {preferred_name} during conversations. "

    # Add specific sections with prompts
    if 'OWNER_FULL_NAME' in globals() and OWNER_FULL_NAME:
        context += f"You are a professional virtual assistant created to assist with questions about {OWNER_FULL_NAME}. "

    if 'OWNER_NICK_NAME' in globals() and OWNER_NICK_NAME:
        context += f"{OWNER_FULL_NAME} is also known by {OWNER_NICK_NAME} as the nickname. "

    if 'OWNER_SUMMARY' in globals() and OWNER_SUMMARY:
        context += f"You need to remember key information about {OWNER_FULL_NAME} or {OWNER_NICK_NAME}, here is the summary : {OWNER_SUMMARY}. "

    if 'OWNER_BIO' in globals() and OWNER_BIO:
        context += f"{OWNER_BIO}. "

    if 'OWNER_LINKEDIN' in globals() and OWNER_LINKEDIN:
        context += f"LinkedIn profile: {OWNER_LINKEDIN}. "

    if 'OWNER_WEBSITE' in globals() and OWNER_WEBSITE:
        context += f"Portfolio/Website: {OWNER_WEBSITE}. "

    if 'OWNER_EDUCATION' in globals() and isinstance(OWNER_EDUCATION, list) and OWNER_EDUCATION:
        context += "Educational Background: " + " ".join(OWNER_EDUCATION) + " "

    if 'OWNER_CERTIFICATIONS' in globals() and isinstance(OWNER_CERTIFICATIONS, list) and OWNER_CERTIFICATIONS:
        context += "Certifications: " + " ".join(OWNER_CERTIFICATIONS) + " "

    if 'OWNER_EXPERIENCE' in globals() and isinstance(OWNER_EXPERIENCE, list) and OWNER_EXPERIENCE:
        context += "Professional Experience: " + " ".join(OWNER_EXPERIENCE) + " "

    if 'OWNER_SPECIALIZATION' in globals() and isinstance(OWNER_SPECIALIZATION, list) and OWNER_SPECIALIZATION:
        context += f"Specialization: {', '.join(OWNER_SPECIALIZATION)}. "

    if 'OWNER_HARD_SKILLS' in globals() and isinstance(OWNER_HARD_SKILLS, list) and OWNER_HARD_SKILLS:
        context += f"Hard Skills: {', '.join(OWNER_HARD_SKILLS)}. "

    if 'OWNER_SOFT_SKILLS' in globals() and isinstance(OWNER_SOFT_SKILLS, list) and OWNER_SOFT_SKILLS:
        context += f"Soft Skills: {', '.join(OWNER_SOFT_SKILLS)}. "

    if 'OWNER_LANGUAGES' in globals() and isinstance(OWNER_LANGUAGES, list) and OWNER_LANGUAGES:
        context += f"Languages spoken: {', '.join(OWNER_LANGUAGES)}. "

    # Dynamically include other 'OWNER_*' variables
    for var_name, var_value in globals().items():
        if var_name.startswith("OWNER_") and var_name not in [
            "OWNER_FULL_NAME", "OWNER_NICK_NAME", "OWNER_BIO", "OWNER_LINKEDIN", "OWNER_WEBSITE",
            "OWNER_EDUCATION", "OWNER_CERTIFICATIONS", "OWNER_EXPERIENCE", "OWNER_SPECIALIZATION",
            "OWNER_HARD_SKILLS", "OWNER_SOFT_SKILLS", "OWNER_LANGUAGES"
        ]:
            # Format and include custom fields
            if isinstance(var_value, list) and var_value:
                context += f"{var_name.replace('OWNER_', '').replace('_', ' ').title()}: {', '.join(var_value)}. "
            elif isinstance(var_value, str) and var_value.strip():
                context += f"{var_name.replace('OWNER_', '').replace('_', ' ').title()}: {var_value}. "

    return context

if __name__ == "__main__":
    context = create_context()
    print(context)