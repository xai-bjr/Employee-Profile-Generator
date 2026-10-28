"""
Employee Profile & Data Management System
Author: GitHub Portfolio Project
Description: Demonstrates interactive user inputs, string manipulation, 
type casting, error handling, string slicing, and modern f-string formatting.
"""

def generate_employee_profile():
    print("=" * 55)
    print("         WELCOME TO THE EMPLOYEE PROFILE GENERATOR")
    print("=" * 55)
    
    # 1. Interactive Inputs with basic cleaning (.strip() and .capitalize())
    first_name = input("Enter first name: ").strip().capitalize()
    last_name = input("Enter last name: ").strip().capitalize()
    full_name = f"{first_name} {last_name}"
    
    street_address = input("Enter street address: ").strip()
    apartment = input("Enter apartment/suite (optional, press Enter to skip): ").strip()
    
    # Conditional formatting for address
    if apartment:
        address = f"{street_address}, {apartment}"
    else:
        address = street_address
        
    # Numeric inputs with error handling (try-except blocks)
    while True:
        try:
            employee_age = int(input("Enter employee age: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer for age.")
            
    while True:
        try:
            experience_years = int(input("Enter years of experience: "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer for experience.")
            
    position = input("Enter position/title (e.g., Data Analyst): ").strip().title()
    
    while True:
        try:
            salary = float(input("Enter annual salary ($): "))
            break
        except ValueError:
            print("❌ Invalid input. Please enter a valid number for salary.")
            
    # 2. Processed Information Strings
    employee_info = f"{full_name} is {employee_age} years old."
    experience_info = f"Experience: {experience_years} years"
    
    # Professional formatted ID Badge layout using f-strings
    employee_card = (
        f"┌{'─' * 51}┐\n"
        f"│ BADGE: {full_name:<43} │\n"
        f"├{'─' * 51}┤\n"
        f"│ Position: {position:<17} │ Age: {employee_age:<16} │\n"
        f"│ Salary: ${salary:<15,.2f} │ Exp: {experience_years} yrs{' ' * 13}│\n"
        f"└{'─' * 51}┘"
    )
    
    # 3. Dynamic Employee Code & Slicing Demonstration
    # Generates a code like: DAT-2026-JD-001 based on inputs
    dept_prefix = position[:3].upper() if len(position) >= 3 else "GEN"
    current_year = "2026"
    initials = f"{first_name[0]}{last_name[0]}"
    employee_code = f"{dept_prefix}-{current_year}-{initials}-001"
    
    # String Slicing breakdown
    department = employee_code[0:3]
    year_code = employee_code[4:8]
    extracted_initials = employee_code[9:11]
    
    # 4. Displaying Final Clean Output
    print("\n" + "=" * 55)
    print("                  GENERATED REPORT")
    print("=" * 55)
    print(f"• {employee_info}")
    print(f"• {experience_info}")
    print(f"• Address: {address}")
    print(f"\n{employee_card}\n")
    
    print("--- String Slicing & Code Breakdown ---")
    print(f"Generated Employee Code : {employee_code}")
    print(f"-> Extracted Department : {department}")
    print(f"-> Extracted Year Code  : {year_code}")
    print(f"-> Extracted Initials   : {extracted_initials}")
    print("=" * 55)

# Entry point of the script
if __name__ == "__main__":
    generate_employee_profile()
