from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print(products)



# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences_set = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }
    converted_products.append(converted_product)




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)





# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    matches = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        matches.append({'name': product['name'], 'match_count': match_count})

    matches.sort(key=lambda x: x['match_count'], reverse=True)
    return matches



# TODO: Step 7 - Call your function and print the results
print("Recommended Products:")
recommendations = recommend_products(converted_products, customer_preferences_set)
for recommendation in recommendations:
    print(f"- {recommendation['name']}: {recommendation['match_count']} matches")


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
# I used different core Python operations and loops to have matching products based 
#on preferences according to the user. I used a list to store the customer's preferences'
#and converted the list to remove duplicate preferences. the i also converted the product 
#tages into sets to allow for faster comparisons. 

#For the count_matches function, I used a set interaction to find both what the customer and product
#both have in common. I used len() to count the number of matching tags. 
#Then I also used recommended_products function
#to sort the products by their match counts.

#If the product catalog had 1,000 or more products, the program can take more time to process. 
#This is because it would to go through every product. A way I could improve the program
#is by using a database or find an efficient way to store and search for the product. I can also make 
# sure the products are converted into a set only once. This will be more efficient because it won't 
#require repeatedly converting the product tags into sets for every recommendation.