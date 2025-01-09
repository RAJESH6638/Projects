# Cold Email Generator  

This project is a Cold Email Generator that automates the creation of personalized cold emails based on job descriptions provided through a URL. It extracts data from a company's career page, parses the content, matches the skills, and generates an email in response to the job posting. Currently, it is designed for individual use.  

---

## Table of Contents  
- [About](#about)  
- [Getting Started](#getting-started)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Features](#features)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)  

---

## About  
The Cold Email Generator uses a Groq API and LangChain to analyze job descriptions from a URL. By parsing the content and matching predefined skills, it automatically drafts a personalized email that you can send to recruiters.  

---

## Getting Started  
Follow the instructions below to set up the Cold Email Generator on your local machine.

---

## Prerequisites  
Ensure the following tools are installed:  
- Python 3.7+  
- Streamlit for deployment  
- PyCharm Community Edition for development  
- Groq API key  

You also need the following Python libraries:  
- `streamlit`  
- `pandas`  
- `chromadb`  
- `langchain_groq`  
- `langchain_core`  
- `dotenv`  

---

## Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/RAJESH6638/cold-email-generator.git  

# Cold Email Generator

## Installation

1. Navigate to the project directory:

   ```bash
   cd cold-email-generator
   
2. Install the required dependencies:

   ```bash
      pip install -r requirements.txt

3. Set up your Groq API key:
   Create a .env file in the root directory and add the following:

   ```bash
      GROK_API_KEY=your_groq_api_key_here  
---

1. Usage
   Run the app:

   ```bash
      streamlit run main.py  

2. Enter the URL of the job description you want to parse. For example, use a link like this:

   ```text
      https://aexp.eightfold.ai/careers/job/26707639?hl=en  

3. Click "Submit" to get a cold email generated based on the job description.

## Features

- **Job Description Parsing**: Extracts relevant data from job postings on company career pages.
- **Skill Matching**: Matches predefined skills with the job description.
- **Email Generation**: Automatically generates a personalized email for job applications.
- **Streamlit Deployment**: Easily accessible web interface for personal use.

## Contributing

This project is for individual use, but contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions, feedback, or suggestions, please contact:  
Rajesh Singh  
- GitHub: [RAJESH6638](https://github.com/RAJESH6638)  
- LinkedIn: [Rajesh Singh](https://www.linkedin.com/in/rajesh-singh/)
- Email: [Rajesh Singh](writetorajesh1214@gmail.com)
 
