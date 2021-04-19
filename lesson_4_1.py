


# Modify this function to return a list of strings as defined above
def list_benefits():
    """Initializes a list of strings"""
    list_of_benefits = ["More organized code", "More readable code", "Easier code reuse",
                        "Allowing programmers to share and connect code together"]
    return list_of_benefits



# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    """Adds an extra string"""
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    """prints first 4 members of the list of strings"""
    list_of_benefits = list_benefits()

    print(build_sentence(list_of_benefits[0]))
    print(build_sentence(list_of_benefits[1]))
    print(build_sentence(list_of_benefits[2]))
    print(build_sentence(list_of_benefits[3]))


name_the_benefits_of_functions()