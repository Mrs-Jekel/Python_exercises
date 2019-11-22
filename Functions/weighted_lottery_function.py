#ability to create a function heading generator and takes in a title and heading type
def heading_generator(title, heading_type):                 # create the function heading generator-takes in a title and heading type
      return f'<h{heading_type}>{title}</h{heading_type}>'  # return a formatted string start off by saying <h say heading type> returns a string of <h1>
                                                            # inside of there pass in the title then pass in </h and the heading type and close it off

print(heading_generator('Greetings!', '1'))                 # then print out the heading generator with Greetings and 1 (h1 tag)
print(heading_generator('I am in a title', '3'))            # then print out the heading generator with I am in a title and 3 (h3 tag)
///////////////////////////////////////////////////////
From Benjamin Nicklaus to Everyone:  04:26 PM
import numpy as np               # import numpy library

def weighted_lottery(weights):   # create a function weighted lottery and takes in weights
    container_list = []          # create a container list to keep track of weights

    for (name, weight) in weights.items():     # for the get key and value name and weight in weights items(gives ability to loop through KVP)
        for _ in range(weight):                # nested loop for counter -for _ (variable not used) in range weight
            container_list.append(name)        # container list and append the name(builds the list)

    return np.random.choice(container_list)    # call np and then say random.chioce (pulls out random sample)
"""
#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))
"""
other_weights = {                              
    'green': 1,                                
    'yellow': 2,                               
    'red': 3
}

print(weighted_lottery(other_weights))   
