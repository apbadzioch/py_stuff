"""
OPENAI API CODING WITH PYTHON
OpenAI Python API: Recipe Blog
As a new food blogger looking to create the next big culinary hub for your readers, get ready to transform your coding skills into a flavorful experience!
In this project, you’ll build a recipe generator that provides tailored recipe recommendations by providing the model with context about the user’s dietary preferences, ingredients on hand, and cuisine favorites. You’ll practice prompt engineering to format the model output recipes in the best format for your blog.
Let’s get cooking!

Tasks:
Setting Up the Environment
1.
Start the project by importing the OpenAI class from the openai module.
2.
Create an instance of the OpenAI class and assign it to a variable named client.
Create a User Profile
3.
Create a dictionary named user_profile with no entries in it.
4.
Update the previously defined dictionary user_profile by adding a new key-value pair. The key should be "dietary_restrictions" and the value should be a string listing the user’s dietary restrictions.
The restrictions can be separated by commas or written in any other format that clearly specifies the various restrictions.
5.
Add to the user_profile dictionary by inserting a new key-value pair. Assign the key "cuisine_preferences" and set its value to a string that indicates the user’s favorite cuisines.
Format this list with commas or any other clear way to denote the different preferences.
6.
Finish updating the user_profile dictionary by adding a key called "ingredients_available". The value for this key should be a string listing the ingredients the user has on hand.
The list can be separated by commas or written in a format that clearly outlines the various ingredients available to the user.
Prepare the Prompts
7.
Create a dictionary called system_prompt which will define the instructions for the AI. This dictionary should instruct the AI to generate HTML code for a recipe blog that takes into account specific dietary restrictions, chosen cuisine type, and a provided list of ingredients.
Ensure that the dictionary includes a key named "role" with the value "system", and another key named "content" where the value is the instruction string for the AI.
Example Prompt
8.
Create a string variable named user_content1 that begins the user prompt. This string should start with a sentence indicating your intention to create a recipe blog post. Then, proceed to include the relevant data from the user_profile dictionary, making sure to specify what each piece of data from user_profile represents.
For example, the string should clearly label the dietary restrictions, cuisine preferences, and available ingredients as provided in the user_profile.
Example Prompt
9.
Construct a string called user_content2 to continue shaping the user prompt. This string should outline the structure of a blog post, including requests for specific elements such as the title, description, ingredients, and instructions.
Within this string, you have the option to include examples illustrating the preferred format for listing ingredients and instructions, guiding the AI on how to present these sections effectively.
Example Prompt
10.
Construct a string with the name user_content3 that establishes certain limitations for the recipe creation. This string should specify that:
o	the recipes must be made using only the ingredients listed in the user_profile
o	the AI’s output should be limited to a single blog post
o	the recipe instructions should not exceed six steps.
These constraints will guide the AI in generating content that adheres to the given parameters.
Example Prompt
11.
Define a dictionary named user_prompt that will hold the instructions for the AI. This dictionary should include a key "role" with the value "user".
Additionally, add another key "content" where the value is a concatenation of the strings user_content1, user_content2, and user_content3.
When combining these strings, ensure you use appropriate punctuation and spacing to distinguish each part clearly. You may use the newline character "\n" to insert a line break between each string, which will help maintain a readable and organized format for the prompt.
Make the Chat Completion
12.
Utilize the client variable to initiate a chat completion. Pass the following keyword arguments to the function:
o	Assign the model keyword argument a value of either "gpt-3.5-turbo" or "gpt-4-turbo-preview", depending on which model you want to use.
o	For the messages keyword argument, provide a list that contains the dictionary system_prompt as its first item, followed by the dictionary user_prompt as the second item.
Assign the return value of the chat completion to a variable called response.
13.
Output the chat completion reply content to the terminal.
14.
The result of this process should be HTML code that is prepared for review and can then be published on a website.
Employing generative AI for automating such tasks significantly streamlines the content creation workflow, making it more efficient for producing various types of content.
"""


# import openai class
# from openai import OpenAI

# create instance named client
# client = OpenAI()

# create empty dictionary
user_profile = {}
user_profile['dietary_restrictions'] = ['peanut, shellfish']
user_profile['cuisine_preferences'] = ['italian, mexican']
user_profile['ingredients_available'] = ['beef, chicken, polenta']

# create a dictionary for instructions called system_prompt
system_prompt = {
    'role': 'system',
    'content': 'Generate an HTML code for a recipe blog that considers dietary restrictions, cuisine type, and ingredients.'
}

# string variable that begins the user prompt
user_content1 = f'''I want to create a recipe blog post. Here are my dietary restrictions:
{user_profile['dietary_restrictions']}. My cuisine preferences are: {user_profile['cuisine_preferences']}.
The ingredients I have available are: {user_profile['ingredients_available']}.'''

user_content2 = "Please provide a blog post with a title description, ingredients, and instructions. Format the ingredients and instructions as follows: Ingredients should be bulleted and instructions should be numbered."

user_content3 = "The recipe must use only the listed ingredients and should result ina single blog post with instructions not exceeding six steps."

user_prompt = {
    "role": "user",
    "content": user_content1 + "\n" + user_content2 + "\n" + user_content3
}

response = client.chat.completion.create(
    model = "gpt-3.5-turbo",
    messages = [system_prompt, user_prompt]
)

print(response.choices[0].message.content)