import validators

pro_name = validators.get_project_name()
cli_bud = validators.get_positive_int("Enter your client bughe: ")
est_hours = validators.get_non_negative_float("Enter Estimated hours: ")
platform_per = validators.get_valid_percentage()
other = validators.get_non_negative_float("Enter otehr expenses: ")

print(pro_name)
print(cli_bud)
print(est_hours)
print(platform_per)
print(other)
