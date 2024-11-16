import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

os.getenv("GROK_API_KEY")

class Chain:
    def __init__(self):
        self.llm =  ChatGroq (
    groq_api_key = os.getenv("GROK_API_KEY"),
    model="llama-3.1-70b-versatile",
    temperature=0, max_tokens=None, timeout=None, max_retries=2,)

def extract_jobs(self,cleaned_text):
    prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the following keys: role, 'experience, 'skills' and 'description.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE) :
        """
    )
    chain_extract = prompt_extract | self.llm
    res = chain_extract.invoke(input={'page_data': cleaned_text})
    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(res.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res if isinstance(res, list) else [res]

def write_mail(self, job, links):
            prompt_email = PromptTemplate.from_template(
                    """
                    ### SCRAPED TEXT FROM WEBSITE:
                    {page_data}
                    ### INSTRUCTION:
                    The scraped text is from the career's page of a website.
                    Your job is to extract the job postings and return them in JSON format containing the following keys: role, 'experience, 'skills' and 'description.
                    Only return the valid JSON.
                    ### VALID JSON (NO PREAMBLE) :
                    """
                )
            chain_email = prompt_email | self.llm
            res = chain_email.invoke({"job_description": str(job), "link_list": links})
            return res.content

if __name__ == "__main__":
    print(os.getenv("GROK_API_KEY"))