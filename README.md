# Day-4-of-100
## Rock-Paper-Scissors

I will admit that I had a lot of trouble with this project. Not only did it involve a lot of concepts I have learned in the past few days such as if/else statements, f-strings, changing data types, but also it combined all that with new concepts today - lists and randomization. 

I actually had to bring out pen and paper, because for the life of me I couldn't figure out why rock wins against paper, but lost against scissors. Now the concept of lists and randomization was fairly easy to grasp, but what really troubled me was the if/else statements. The order of it really mattered, and I forgot how much so. Because I was so focused on troublshooting those statements, I failed to do the simple tasks, like changing the data types to integer. 

This was the first time I was troubleshooting code so extensively. Even after reading through the solutions and watching the video associated with this project, I stuck through till the end, and even looked up some concepts on google in case I was missing anything. 

Well, I've learned what it meant to be resilient in the world of coding, and no doubt the effort I went through today will be remembered in my future projects. It's a whole other new skill, in my opinion. I"ve also developed a habit of making comments where it made sense, it helps a lot, and I'm starting to understand what it means for your code to be readable to others. 

Like the other days, I'm going to list below what I've learned, that way in the morning, I can look back at this repository for a refresh. 

## Some things that I have known and reinforced
- the concept of randomization

## Some things that I don't remmeber learning but have a background of
- Lists and their syntax with []

## Completely New to Me 
- Random Module
  - When wanting to use the random function you need to import it
    > import random
  - Modules are created when the project gets too large. Essentailly, its tabs of code that are all related to each other (lmk if there is a better way to explain this haha)
  - There are many ways you can randomize something e.g. with or w/o float, less thans or equals to, etc. I can look it up in the literature or online.
### Usage/Examples 
  
  ```
    random_integer = random.randint(1,10)
      #random number from 1 to 10, including 1 and 10.
    random_number_0_to_1 = random.random() * 10
      #to create a decimal number from 0 to 1, 0 inclusive, and 1 non-inclusive (or in this case 10)
    random_float = random.uniform(1, 10)
      #the number is greater than a, and less than or equal to b (a,b)     
  ``` 
  ``` javascript 
    print("heads or tails?")  
    heads_or_tails = random.randint(0,1)
    if heads_or_tails == 0:
      print("Heads")
    else:
      print("Tails")
  ```

- Lists
  - syntax list[]
  - You can add multiple items and even correct parts of the lists i.e. spelling, etc.
  - the order in the list matters a lot. It is counted starting from 0 or -1.
### Usage/Examples

``` javascript
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New     York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri",       "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North     Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

    (states_of_america[1]) = "Pencilvania" #can update data or add data, in this case i changed the spelling of Pennsylvania
    states_of_america.append("Angelaland") #only adds one item to the end of the list
    states_of_america.extend(["Angelaland", "AdelineLand"]) #add multiple items
    states_of_america[0] = "Delaware"
    states_of_merica[0] = "Wonderland" #"Delaware" is replaced with "Wonderland"

```
- to randomize and recieve one result:
``` javascript
    import random

    friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

    # option 1
    print(random.choice(friends))
  
    # option 2
    index = random.randint(0, 4)
    print(friends[index])
```
- IndexErrors
  - When you try to access an item that is not in the range of the List, you will get an IndexError. 

``` javascript 
fruits = ["Cherry", "Apple", "Pear"]
print(fruits[3]) #This will be an IndexError
```
  - You can put Lists inside other Lists, this becomes something called a "Nested List" or a "2D List
``` javascript
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
```
