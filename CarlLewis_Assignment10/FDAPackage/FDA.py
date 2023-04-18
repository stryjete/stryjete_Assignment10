#Name: Carl Lewis (Luke Brooks, Tatianna Stryjewski, and Matthew Martin)
#email: stryjete@mail.uc.edu
#Assignment Title: Assignment 06
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Using JSON and API
#Citations: https://fdc.nal.usda.gov/api-guide.html
#Anything else that's relevant: The API is the different types of cheese
# registered with the FDA
#FDA.py

def iterate_dictionary(myDictionary):
    for k, v in myDictionary.items():
        print ("key is " + str(type(k)) + ", value is " + str(type(v)))
        if isinstance(v, dict):
            iterate_dictionary(v)
        else:
            print("{0} : {1}".format(k, v))
            if (isinstance(v, list)):
                for vv in v:
                    if (isinstance(vv, dict)):
                        iterate_dictionary(vv)