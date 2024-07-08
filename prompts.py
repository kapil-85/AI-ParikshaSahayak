import logging

logger = logging.getLogger(__name__)


SYSTEM_PROMPTS = {
    "Default": {
        "role": "system",
        "content": """
        You are a New Generation AI based School Teacher who is expert in school subjects. 
        Your job is to generate questions and answers basis user query of the User. 
        Generate as many questions as asked by the User. 
        If complexity is not specified, generate a mix of easy, moderate and hard questions for the asked Topic and Subject. 
        Format the questions in a clear and organized manner. 
        Ensure that the questions assess both basic understanding and higher-order 
        thinking skills. Generate the questions always and generate answers only when asked in User's query.
        """
    },
}


initialise_prompt =''' You are a New Generation AI based School Teacher for class 1 to class 12 for Madhya Pradesh School Education Board, India. Answer in a clear and organized manner.
Respond to User's query from provided text or document only, Don't take help from the internet.
                    '''
initialise_prompt2 =''' File Selection and Processing:

"Please select a file from the list to begin."
"Choose a document to process and generate questions from."
User Interaction:

"Ask a question related to the selected document."
"Enter your query or topic of interest to generate responses."
Output Generation:

"Generating questions based on the selected document."
"Preparing responses and generating interactive content."
Functional Choices:

"Select complexity level: Easy or Difficult."
"Choose the type of questions: Short, Long, MCQ, Fill in the Blanks, or True and False."
Language and Response:

"Specify the language mode for responses: English or English and Hindi."
"Select the mode of questions: Only Questions or Questions with Answers."
Feedback and Download Options:


"""
                    '''

filter_prompt2 = """
For the following user query, first analyze whether it is related to {} books/chapters.
If the query is related then Based on the context answer the user query else return message "This is beyond my capabilites, please ask another question."

User Query - {}

"""

# format_prompt=""" Format the response in proper question format and shuffule the questions.Remember to keep all the information as it is. Response - {}"""

# format_prompt=""" Format the response and provide only questions in both the language which are there in response and shuffle the response and consider following constraints,
# 1. number of questions - {}
# 2. type of questions - {}
# 3. Topic name - {} 

# provide exact number of questions as per provided
# convert the mathematical expressions in Latex form.
# Remember to keep all the information as it is. Response - {}"""

# format_prompt="""Response which is given is in dictionary format . Please convert these into proper question paper format 
# Restrict the response to {} number of questions and reorder the questions.

# Shuffle the order of questions

# Keep the mathematical expressions in LaTex format 
# Remember to keep all the information as it is. Response - {}
# """

# format_prompt="""From the context Provide the summary in tabular format of Response {} contain following parameters
#     1. Topics name
#     2. Total Number of Questions
#     3. Type of Questions

#     Provide the Topic names and Type of Questions in proper tabular format 
#     Also mention the total number of questions and class at the end 
# """

format_prompt="""format and regenerate the Response {}"""


aiformat_prompt="""From the context Provide the brief summary in tabular format of Response {} contain following 
    1. Chapter names
    2. Description of each topic

    provide the response in tabular format . Only include Chapter names and Description
    Also mention the subject at the end 
"""

latex_prompt="""format the response {} into python list.
    
    Remember to keep all the information as it is
    """

ai_prompt="""Based on the context, generate only questions considering following constraints,
             1. number of questions  - {}
             2. mode of questions - {}
             3. type of questions - {} 
             Generate questions according to Madhya Pradesh Board Education School
             Response is to be generated in both english and Hindi,first generate in english then in Hindi
             number of questions is metioned zero then show message please add the number question,
             after number of questions mentioned then start the generating questions and answer.
             and if you are generating Answers also, Answer start in a new line and Generate questions according to Madhya Pradesh School Education Board
             generate the all types of question and answer,and please insure the question and answer based on topic or text.
             Remember to keep all the information as it is. Response - {}


"""

ai_topic_prompt="""Based on the context, generate only questions considering following constraints,
    1. topic of questions  - {}
    2. number of questions - {} 
    3. mode of questions - {}
    4. type of questions - {}
    5. Level of questions - {}
    Response is to be generated in both english and Hindi,first generate in english then in Hindi,
    and if you are generating Answers also, Answer it in a new line and Generate questions according to Madhya Pradesh School Education Board,
    number of questions is metioned zero then show message please add the number question,
    after number of questions mentioned then start the generating questions and answers.
    generate the all types of question and answer,and please insure the question and answer based on topic or text.
"""
ai_topic_prompt1="""Based on the context, generate only questions considering following constraints,
                    make sure the question and answer only generate from the selected document only
    1. text - {}             
    2. topic_name - {}
    3. number of questions - {}
    4. mode of questions - {}
    5. type of questions - {}
    6. Level of questions - {}
    questions and answers should be started from new line.
    Response is to be generated in both english and Hindi,first generate in english then in Hindi.
    If Answers are being generated, always start the Answer in a new line.
    If the Topic is not present in the selected Document, don't provide any questions or answers and rather write "This topic is not present in Book" & then list all the topics which are present in the uploaded document in tabular format and call this list "Topics available"
    
"""
ai_topic_prompt_questions="""Based on the context, extract only questions
Remember to keep all the information as it is. Response - {}
"""

mcq_test_prompt = """
        Based on the context generate terminologies and key terms
        first generate terminologies then generate key terms
        generate the response in both english and Hindi, first generate in english then in Hindi
        Remember to keep all the information as it is. Response-{}    
"""

key_term_prompt = """
        Based on the context generate key terms
        Remember to keep all the information as it is. Response-{}    
        
          
    """

learn_outcome_prompt = """
        Based on the context generate learning outcomes
        generate the response in both english and Hindi, first generate in english then in Hindi
        Remember to keep all the information as it is. Response-{} 
             
    """

student_prompt = """Based on query {} generate response from context {}
                    make sure generate response should be generated from uploaded document only.

"""

master_prompt = """
Level of questions : This is the depth of the questions the teacher wants to generate. A low depth will cover the basics, and generalizations while a high depth will cover the specifics, details, unfamiliar, complex, and side cases. The lowest depth level is Easy, and the highest is Complex.

Do not discuss about the context you have recieved and do not mention you are unable to access or read any documents 

Easy : Covers basics questions with simple definitions and brief explanations, suitable for beginners or quick overviews.
Difficult : Provides expert and complex questions .

if type of questions is Short Questions then generate questions according to 1 marks and 2 marks from given context
if type of questions is Long Questions then generate questions according to 3,4,5 marks from given context

You have been provided the Context/Subject/Chapter/Book 
Based on the context, generate {} considering following constraints,
    1. Level of questions - {}
   
    3. number of questions  - {}
    4. type of questions - {}
after all the selected these thing than generate the question and answer according to selected document file only.
If topic name is not provided then based on context generate {} from books/chapters/Subject 

if Level of questions is Yes then categorise the Response as Easy or Difficult 

if topic name is not from context then mention this topic name is out of context

Remember to generate questions according to Madhya Pradesh School Education Board
Remember to keep all the information as it is. Response - {}
Remember to not discuss about the context you have recieved and do not mention you are unable to access or read any documents 

"""

lang_prompt = """ Translate the below response to {} language . 
Remember to keep all the information as it is. Response - {}
"""
