"""
AUTHOR: liicodex
Date: 31 July 2024
Reason: This is to intergrate with the brandbot
"""

# REQUIRED MODULES
import openai

# INITIALIZING PROGRAM
apiKey = None
openai.api_key = apiKey

# LOGIC FUNCTIONS

# Function to process text file and get output
def processTextFile(inputFile, prompt, outputFile):
    with open(inputFile, "r") as file:
        fileText = file.read()

    # Generating ouput using OpenAI API
    response = openai.Completion.create(
        engine = "davinci", # Curie--content/chatbot + Babbage--classification, sentiment, data + Ada--chatbots, live updates
        prompt = prompt +  "\n\n" + fileText,
        max_tokens = 2048,
        temperature = 0.6,
        top_p = 1
    )

    # Generated Output
    output = response.choices[0].text
    # print(ouput)

    # Save output to a file


# MAIN FUNCTION

if __name__ == '_main_':
    inputFile = None
    prompt = None
    output = None
    main()