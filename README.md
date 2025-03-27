# Document Chunking and Azure Cognitive Search Uploader

## Project Overview

This application provides a robust solution for document chunking and uploading to Azure Cognitive Search, designed to help you process and index large documents efficiently.

## Features

- PDF text extraction
- Recursive text splitting
- Azure Cognitive Search integration
- Containerized deployment
- Environment-based configuration

## Prerequisites

- Docker
- Docker Compose
- Azure Subscription
- Azure OpenAI Service
- Azure Cognitive Search Service

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:chaitanyadevle/document-chunking-service.git
cd document-chunking-service
```

### 2. Configuration

1. Copy the `.env.sample` to `.env`
2. Fill in your Azure service credentials:

```bash
cp .env.sample .env
nano .env  # or use your preferred text editor
```

#### Required Environment Variables

- `AI_SEARCH_INDEX_NAME`: Your Azure Search Index Name
- `AI_SEARCH_INDEX_ENDPOINT`: Your Azure Cognitive Search service endpoint
- `AZURE_API_KEY`: Your Azure Cognitive Search admin key

### 3. Build and Run

```bash
docker-compose up --build
```

## Project Structure

```
.
├── app
│   ├── azure_search_uploader.py   # Azure Search upload logic
│   ├── main.py                    # Main application entry point
│   ├── pdf_text_extractor.py      # PDF text extraction utility
│   └── recursive_text_splitter.py # Document chunking logic
├── Media
│   └── document.pdf # Put your pdf document in this folder
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Development

### Local Development

1. Create a virtual environment
2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### Running Tests

*Tests not implemented yet. Contributions welcome!*

## Security

- Never commit `.env` file to version control
- Rotate API keys regularly
- Use least-privilege principles when creating service credentials

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Troubleshooting

- Ensure all environment variables are correctly set
- Verify Azure service credentials
- Check Docker and Docker Compose versions

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - chaitanyadevale11@gmail.com

Project Link: [https://github.com/chaitanyadevle/document-chunking-service](https://github.com/chaitanyadevle/document-chunking-service)
