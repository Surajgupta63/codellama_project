# CodeSuraj AI Chatbot with Gradio Frontend  
![Python](https://img.shields.io/badge/Python-3.x-blue) ![Gradio](https://img.shields.io/badge/Gradio-frontend-orange) ![API](https://img.shields.io/badge/API-localhost-green)  

This project implements a simple AI chatbot using **Gradio** as the frontend, which interacts with a locally hosted API to generate contextual AI-based responses. The chatbot maintains conversation history for context-aware replies.

---

## Features  
- 🎯 **API Integration:** Connects to a backend API endpoint to send user prompts and retrieve AI-generated responses.  
- 💬 **Contextual Conversations:** Maintains chat history to enhance interaction with contextual replies.  
- 🖥️ **Gradio Interface:** Provides an interactive, user-friendly input/output interface.  

---

## Installation  

Follow these steps to set up and run the chatbot on your local machine:  

### 1. Clone the Repository  
```bash  
git clone <repository-url>  
cd <repository-directory>  
```  

### 2. Install Dependencies  
Ensure Python is installed, then run:  
```bash  
pip install requests gradio  
```  

### 3. Run the Application  
Make sure your local API server is running (default: `http://localhost:11434`). Then, launch the chatbot interface by running:  
```bash  
python app.py  
```  

---

## How It Works  

1. **Input a Prompt:** The user inputs a message in the Gradio interface.  
2. **API Call:** The `generate_response()` function sends the input and chat history to the API endpoint: `http://localhost:11434/api/generate`.  
3. **Response Handling:** The API processes the request and returns the AI-generated reply.  
4. **Conversation Continuation:** The reply is displayed, and chat history is updated for maintaining context.  

---

## Code Overview  

### API Setup  
```python  
url = "http://localhost:11434/api/generate"  
header = {'Content-Type': 'application/json'}  
```  

### Chatbot Logic  
```python  
def generate_response(prompt):  
    history.append(prompt)  
    final_prompt = '\n'.join(history)  
    data = {'model': 'CodeSuraj', 'prompt': final_prompt, 'stream': False}  
    response = requests.post(url=url, headers=header, data=json.dumps(data))  
```  

### Gradio Interface  
```python  
interface = gd.Interface(  
    fn=generate_response,  
    inputs=gd.Textbox(lines=4, placeholder="Enter your prompt"),  
    outputs=gd.Textbox(lines=4, type='text')  
)  
interface.launch()  
```  

---

## File Structure  
```
.  
├── app.py          # Main script with API requests and Gradio interface  
├── README.md       # Project documentation (this file)  
└── requirements.txt (optional)  # If you want to list dependencies  
```  

---

## Customization  

- **API Endpoint:** Modify the `url` variable in the script to point to your custom API endpoint.  
- **Gradio Layout:** Adjust the text box size, lines, or other input/output features as needed.  

---

## Dependencies  

- Python 3.x  
- `requests`  
- `gradio`  

You can also create a `requirements.txt` file using:  
```bash  
pip freeze > requirements.txt  
```  

---

## License  

This project is open-source and free to use. Feel free to modify and improve it to suit your needs.  

---

## Contributions  
Contributions are welcome! If you encounter any issues or want to add features, feel free to fork the repository and submit a pull request.  

---

For any questions, suggestions, or contributions, feel free to create an issue or submit a pull request!

