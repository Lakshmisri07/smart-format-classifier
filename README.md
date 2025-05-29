 SMART-FORMAT-CLASSIFIER 
 
  Smart Format Classifier is a modular, multi-agent AI system designed to intelligently process and classify input data in PDF, JSON, or Email (text) formats. By automatically detecting both the format and intent of incoming content, it ensures accurate routing to specialized agents for further processing. This solution addresses real-world challenges in document understanding and automation by maintaining contextual memory for traceability and multi-stage workflows.

Key Features:

Format & Intent Classification: Automatically detects the format (PDF, JSON, Email) and identifies the intent such as Invoice, RFQ, Complaint, or Regulation using a central Classifier Agent.
Agent-Based Processing: Inputs are routed to specialized agents—JSON Agent for structured data and Email Agent for text-based content—ensuring context-specific handling.
Contextual Memory: A shared memory module retains key details such as sender, topic, extracted fields, timestamps, and conversation IDs, enabling seamless information chaining across agents.

Technical Overview:

Programming Language: Built using Python to leverage modular and AI-driven capabilities.
LLM Integration: Supports integration with OpenAI or open-source LLMs for intent detection and field extraction.
Memory Management: Incorporates Redis, SQLite, or an in-memory store to maintain shared context accessible across agents.
Modular Agents: Includes Classifier Agent, JSON Agent, and Email Agent, each responsible for specific input types and workflows.

## folder Structur
smart-format-classifier
|
|-agents
| 
|--classifier_agent.py
      
--email_agent.py
  
--json_agent.py
  
--pdf_agent.py

-data
      
--input
     
---sample_email.txt
  
---sample_invoice.json
   
---sample_invoice.pdf 
   
--output
  
---logs.json
   
---sample_screenshot.png
   
-memory
  
--shared_memory.db
   
-utils
  
--file_loader.py
   
-README.md
   
-demo.mp4
  
-main.py
  
-requirements.txt

## Sample Input Files

sample_invoice.pdf: A PDF file representing an invoice document.  
sample_request.json: A JSON file simulating a structured request like an RFQ.  
sample_email.txt: Plain text email content demonstrating typical email input.

## Sample Output Screenshots

sample_screenshot.png: Screenshot showing the system output in the console or logs during processing.

## Demo Video
Watch the demo here:https://drive.google.com/file/d/1uonjDEVX-ZjW6U1bapqQK6ba8TNR-uiY/view?usp=drive_link

Conclusion:
Smart Format Classifier provides a scalable and intelligent framework for processing diverse input types in automated workflows. By combining modular agent-based design with a shared memory context, it enables accurate format and intent classification, efficient data routing, and traceable multi-agent collaboration. The system is ideal for use cases in business automation, document processing, and AI-driven communication management.
