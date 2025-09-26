# CrewAI Documentation Generator

A powerful AI-powered documentation generator built with CrewAI that automatically creates professional README.md files for your projects. Simply describe your project idea, and let our expert technical writer agent craft comprehensive documentation tailored to your needs.

## Description

This project leverages CrewAI's multi-agent framework to automate the creation of high-quality project documentation. The system uses a specialized technical writer agent powered by Google's Gemini AI model to generate well-structured README.md files based on your project description. Whether you're starting a new project or need to improve existing documentation, this tool helps you create professional, comprehensive documentation with minimal effort.

## Key Features

- **AI-Powered Documentation**: Uses Google Gemini AI to generate contextually appropriate documentation
- **Interactive Project Input**: Simple command-line interface to describe your project
- **Professional Structure**: Automatically creates well-formatted README.md files with standard sections
- **Environment Validation**: Built-in .env file testing to ensure proper API key configuration
- **Flexible Output**: Generates both detailed README content and concise project descriptions
- **CrewAI Integration**: Leverages CrewAI's agent framework for reliable, structured AI workflows

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Google API key for Gemini AI access
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

3. Create a `.env` file in the project root and add your API key:
```bash
echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
```

4. Test your environment setup:
```bash
python test.py
```

### Usage

1. Run the documentation generator:
```bash
python agent.py
```

2. When prompted, describe your project in detail. Include:
   - Main purpose and functionality
   - Key features and capabilities
   - Target audience
   - Any specific requirements or technologies

3. The agent will generate a complete README.md file and save it to your project directory.

## Project Structure

```
crew-ai/
├── agent.py                 # Main CrewAI agent implementation
├── test.py                  # Environment validation script
├── single_agent_report.md   # Sample AI-generated content
├── README.md               # This documentation file
```

## Configuration

The project uses Google's Gemini AI model (`gemini-p2.5-ro`) with the following default settings:
- Temperature: 0.7 (balanced creativity and consistency)
- Model: gemini-p2.5-ro
- API Key: Loaded from .env file

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- Bug fixes
- Feature enhancements
- Documentation improvements
- Additional AI model integrations

## License

This project is open source and available under the [MIT License](LICENSE).
