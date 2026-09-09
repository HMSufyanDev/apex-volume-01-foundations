# A set is a collection that stores unique values.
countries = {"Australia", "Canada", "UK"}

# Unique Values
leads = {
    "ABC Dental",
    "XYZ Clinic",
    "ABC Dental",
    "Smile Care",
    "XYZ Clinic"
}

print(leads)
# Conceptually, the result is:
{
    "ABC Dental",
    "XYZ Clinic",
    "Smile Care"
}

# Sets don't support indexing.

# Removing Duplicates Using a Set
leads = [
    "ABC Dental",
    "XYZ Clinic",
    "ABC Dental",
    "Smile Care",
    "XYZ Clinic"
]
unique_leads = set(leads)

print(unique_leads)

# Converting Back to a List
unique_leads = list(set(leads))
# Note: Converting to a set and back to a list should not be used when preserving original order is important.

# Set Union
agency_a = {"Web Design", "SEO", "Development"}
agency_b = {"SEO", "Marketing", "Development"}

all_services = agency_a | agency_b
print(all_services)

# {
#     "Web Design",
#     "SEO",
#     "Development",
#     "Marketing"
# }

# Alternative Syntax
all_services = agency_a.union(agency_b)

# Set Intersection
agency_a = {"Web Design", "SEO", "Development"}
agency_b = {"SEO", "Marketing", "Development"}

common_services = agency_a & agency_b
print(common_services)

"""
{
    "SEO",
    "Development"
}
"""

# Alternative Syntax
common_services = agency_a.intersection(agency_b)

# Set Difference
# Difference finds values that exist in one set but not another.
agency_a = {"Web Design", "SEO", "Development"}
agency_b = {"SEO", "Marketing", "Development"}
only_a = agency_a - agency_b
# {"Web Design"}

# Reverse Direction
only_b = agency_b - agency_a
# {"Marketing"}


