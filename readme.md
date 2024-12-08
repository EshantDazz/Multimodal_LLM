# Image Analysis with Llama Vision

A streamlined application for image analysis using Llama Vision model through Groq's API. This project combines the power of LangChain, Streamlit, and Llama's vision capabilities to provide intelligent image analysis.

## 🚀 Features

- Image upload and processing
- Base64 image encoding
- Automated file management with unique identifiers
- Asynchronous operations for better performance
- Integration with Groq's Llama Vision model
- Clean temporary file handling
- Interactive Streamlit interface

## 📋 Prerequisites

- Python 3.8+
- Groq API access
- Required Python packages (see requirements.txt)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `myenv/.env` file with your Groq API credentials:
```
GROQ_API_KEY=your_api_key_here
```

## 🏗️ Project Structure

```
.
├── main.py              # Main application logic
├── utils.py            # Utility functions for file handling
├── requirements.txt    # Project dependencies
├── myenv/             # Environment variables
│   └── .env          # API keys and configurations
└── images/           # Directory for temporary image storage
```

## 💻 Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Upload an image through the web interface
3. Enter your prompt for image analysis
4. View the AI-generated response

## 🔧 Core Components

### Image Processing (utils.py)
- `save_uploaded_file()`: Handles image uploads with unique identifiers
- `delete_image()`: Cleans up temporary files
- `encode_image()`: Converts images to base64 format

### AI Integration (main.py)
- Implements LangChain for structured AI interactions
- Utilizes Groq's Llama Vision model for image analysis
- Manages asynchronous operations for better performance

## 📝 API Reference

### return_ai_response
```python
async def return_ai_response(base64_image: str, prompt: str) -> str | list[str | dict]
```
Processes an image and returns AI analysis based on the provided prompt.

### save_uploaded_file
```python
async def save_uploaded_file(uploaded_file) -> str
```
Saves uploaded files with unique identifiers and returns the filepath.

## 🔒 Security Notes

- Automatically cleans up temporary files
- Secure handling of API credentials through environment variables
- Input validation for uploaded files

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## ⚠️ Important Notes

- Ensure proper API key configuration before running
- Monitor image storage to prevent disk space issues
- Consider implementing rate limiting for production use