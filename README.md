# AI News Research Agent

An intelligent AI-powered news research tool built with CrewAI that automatically finds and summarizes the top 3 most significant AI news stories from the past week. Using Google Gemini AI and web search capabilities, this agent delivers concise, well-formatted reports on the latest developments in artificial intelligence.

## Description

This project leverages CrewAI's single-agent framework to automate AI news research and reporting. The system uses a specialized AI news researcher agent powered by Google's Gemini AI model and SerperDev search tool to find, analyze, and summarize the most impactful AI news stories. Perfect for staying up-to-date with the rapidly evolving AI landscape without manually scouring multiple news sources.

## Key Features

- **Automated News Research**: Uses web search to find the most recent and significant AI news
- **AI-Powered Analysis**: Google Gemini AI analyzes and summarizes news content
- **Weekly Focus**: Specifically targets news from the past week for relevance
- **Structured Output**: Generates well-formatted reports with clear titles and summaries
- **File Export**: Automatically saves reports to `single_agent_report.md`
- **Real-time Search**: Uses SerperDev API for current web search capabilities

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Google API key for Gemini AI access
- SerperDev API key for web search
- pipr (for dependency management)

### Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd crew-ai
```

2. Install dependencies using pipr:
```bash
pipr install
```

3. Create a `.env` file in the project root and add your API keys:
```bash
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
echo "SERPER_API_KEY=your_serper_api_key_here" >> .env
```

4. Test your environment setup:
```bash
python test.py
```

### Usage

1. Run the AI news research agent:
```bash
python agent.py
```

2. The agent will automatically:
   - Search for the top 3 most significant AI news stories from the past week
   - Analyze and summarize each story
   - Generate a formatted report
   - Save the report to `single_agent_report.md`

3. View the generated report in the terminal output or open `single_agent_report.md`

## Project Structure

```
crew-ai/
├── agent.py                 # Main CrewAI agent implementation
├── test.py                  # Environment validation script
├── single_agent_report.md   # Generated AI news report
├── README.md               # This documentation file
└── .env                    # Environment variables (create this)
```

## Configuration

The project uses:
- **AI Model**: Google Gemini 2.5 Flash (`gemini-2.5-flash`)
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Search Tool**: SerperDev API for web search
- **API Keys**: Loaded from .env file

## Sample Output

The agent generates reports with:
- A clear title for each news story
- Concise paragraph summaries
- Focus on the most significant developments
- Professional formatting suitable for sharing

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature enhancements
- Additional news sources or search strategies
- Report formatting improvements

## License

This project is open source and available under the [MIT License](LICENSE).
