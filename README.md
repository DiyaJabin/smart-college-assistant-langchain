# Smart College Assistant using LangChain Tool Calling Agent

Smart College Assistant is an AI-powered terminal-based assistant built using Python, LangChain, and Ollama.
The assistant understands student-related queries and automatically invokes the appropriate tool to provide accurate responses.

This project was created as part of my IBM Professional Agentic AI course assignment.

## Features

* Attendance percentage calculator
* Exam eligibility checker
* Result, average marks, grade, and pass/fail calculator
* Fee balance calculator
* Library fine calculator
* Hostel fee calculator
* Student information lookup using Student ID
* Multi-tool query handling
* Interactive terminal-based assistant
* Verbose agent execution to show tool-calling steps

## Tech Stack

* Python
* LangChain
* LangChain Classic Agents
* LangChain Ollama
* Ollama
* Llama 3.2

## Project Structure

```text
smart-college-assistant/
│
├── main.py          # Runs the agent and terminal interface
├── tools.py         # Contains all LangChain tools
├── prompt.py        # Contains the ChatPromptTemplate
├── students.py      # Contains student data dictionary
└── README.md        # Project documentation
```

## Tools Implemented

### 1. Attendance Calculator

Calculates attendance percentage and checks exam eligibility.

Rule:

```text
Attendance >= 75% → Eligible for Exam
Attendance < 75%  → Not Eligible for Exam
```

### 2. Result Calculator

Calculates average marks, grade, and pass/fail status from 5 subject marks.

Grade rules:

```text
Average >= 90 → A
75–89         → B
60–74         → C
< 60          → D
```

Pass rule:

```text
Average >= 50 → Pass
Average < 50  → Fail
```

### 3. Fee Balance Calculator

Calculates pending fee amount.

```text
Pending Fee = Total Course Fee - Amount Paid
```

### 4. Library Fine Calculator

Calculates fine for delayed book returns.

```text
Fine = ₹5 × Number of Delayed Days
```

### 5. Hostel Fee Calculator

Calculates total hostel fee.

```text
Total Hostel Fee = Monthly Hostel Fee × Number of Months Stayed
```

### 6. Student Information Tool

Retrieves student details from a Python dictionary using Student ID.

## Sample Queries

```text
I attended 72 classes out of 90. Am I eligible for exams?
```

```text
My marks are 95, 90, 88, 91 and 87. What is my grade?
```

```text
My course fee is 50000 and I have paid 35000. How much fee is pending?
```

```text
I returned a library book 8 days late. What is the fine amount?
```

```text
Hostel fee is 6000 per month and I stayed for 5 months. Calculate my hostel fee.
```

```text
Give me all the details of the student with student ID 24BCE1172.
```

## Multi-Tool Example

```text
I attended 80 classes out of 100.
My marks are 90, 85, 88, 92 and 95.
My course fee is 60000 and I paid 45000.

Provide:
1. Attendance Status
2. Grade
3. Pending Fee
```

The agent automatically invokes multiple tools and provides a consolidated response.

## Installation

Install the required packages:

```bash
pip install langchain langchain-ollama langchain-classic
```

Pull the Ollama model:

```bash
ollama pull llama3.2
```

## How to Run

Start the application:

```bash
python main.py
```

Then enter your query in the terminal.

## Example Output

```text
Entering new AgentExecutor chain...

Invoking: `library_fine_calculator` with `{'delayed_days': 8}`

Library Fine: ₹40

Finished chain.

The fine amount for returning a library book 8 days late is ₹40.
```

## Learning Outcome

Through this project, I learned how to:

* Create LangChain tools using the `@tool` decorator
* Use `ChatPromptTemplate`
* Build a tool-calling agent with `create_tool_calling_agent`
* Execute an agent using `AgentExecutor`
* Use `verbose=True` to understand tool-calling flow
* Handle both single-tool and multi-tool user queries
* Organize an Agentic AI project into multiple Python files

## Future Improvements

* Add Streamlit or Flask UI
* Store student data in a database
* Add better validation for user inputs
* Improve response formatting
* Add more student services such as scholarship eligibility and timetable lookup
