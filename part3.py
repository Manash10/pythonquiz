def convertSalary(salary, country):
    conversion_rates = {
        #conversion rates
        "Canada": 1.0,
        "USA": 1.18,
        "Cambodia": 4847.38,
        "United Kingdom": 0.91
    }
    
    if country not in conversion_rates:
        print("Error: Invalid Country Input")
        return None
    
    converted_salary = salary / conversion_rates[country]
    return converted_salary
#main program
def main():
    salary = float(input("Please enter your salary in Germany: "))
    country = input("Enter the country you want to migrate to: ")
    
    converted_salary = convertSalary(salary, country)
    
    if converted_salary is not None:
        average_salaries = {
            "Canada": 64000,
            "USA": 56516,
            "Cambodia": 5649856,
            "United Kingdom": 35423
        }
        
        currency_name = ""
        
        if country == "Canada":
            currency_name = "CAD"
        elif country == "USA":
            currency_name = "USD"
        elif country == "Cambodia":
            currency_name = "Cambodian riel"
        elif country == "United Kingdom":
            currency_name = "Pound Sterling"
        
        if converted_salary > average_salaries[country]:
            print("You will be rich in {} with a salary of {} {}".format(country, int(converted_salary), currency_name))
        else:
            print("You will be poor in {} with a salary of {} {}".format(country, int(converted_salary), currency_name))

main()
