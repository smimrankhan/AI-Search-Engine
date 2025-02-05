# Xarvis - AI Search Engine

Xarvis is an AI-powered search engine built with Streamlit and LangChain, capable of retrieving information from the web using multiple sources like Wikipedia, Arxiv, and DuckDuckGo. It leverages OpenAI's GPT-3.5 Turbo model to process and respond intelligently to user queries.

## Features
- **AI-powered search**: Uses OpenAI's GPT-3.5 Turbo for intelligent responses.
- **Multiple data sources**: Retrieves information from Wikipedia, Arxiv, and DuckDuckGo.
- **Interactive chat interface**: Provides a user-friendly chat experience with real-time responses.
- **Secure API key input**: Users can input their API key through a sidebar.

## Technologies Used
- **Streamlit**: For building the web-based interface.
- **LangChain**: For handling AI-powered search and tool integration.
- **OpenAI GPT-3.5 Turbo**: The LLM used for generating responses.
- **Wikipedia API**: Retrieves relevant information from Wikipedia.
- **Arxiv API**: Fetches scientific articles from Arxiv.
- **DuckDuckGo Search API**: Performs web searches for relevant information.
- **dotenv**: Manages environment variables securely.

## Installation
Follow these steps to set up Xarvis on your local machine:

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/xarvis-ai-search.git
   ```
2. Navigate to the project directory:
   ```sh
   cd xarvis-ai-search
   ```
3. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Create a `.env` file and add your OpenAI API key:
   ```sh
   OPEN_API_KEY=your_openai_api_key
   ```

## Usage
Run the application using the following command:
```sh
streamlit run xarvis.py
```

### How to Use
1. Open the app in your browser after running Streamlit.
2. Enter your OpenAI API key in the sidebar.
3. Start chatting by entering a query in the chat input.
4. The AI will fetch information from various sources and provide an intelligent response.

## Troubleshooting
- Ensure all required dependencies are installed.
- Verify that the `.env` file contains a valid OpenAI API key.
- Restart the app if you encounter errors.

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License
This project is licensed under the MIT License.

## Author
**SM Imran Khan Biky**

---

Explore knowledge efficiently with Xarvis! 🚀