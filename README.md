# Supermarket Purchase Analysis

Interactive web application for analyzing supermarket purchase data, built with Streamlit.

**Live Demo:** [https://supermarketpurchaseanalysis.streamlit.app/](https://supermarketpurchaseanalysis.streamlit.app/)

[Русская версия](README_RU.md)

## Features

- Interactive visualization of purchase patterns and trends
- Filter by product category, payment method, and customer type
- Sales analytics and revenue insights
- Payment method distribution analysis
- Modern and responsive UI

## Quick Start

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/supermarket-analysis.git
cd supermarket-analysis

# Install dependencies
pip install -r requirements.txt 

# Generate sample data
python generate_data.py

# Run the application
streamlit run app.py
```

### Docker

```bash
# Build the image
docker build -t supermarket-analysis .

# Run the container
docker run -p 8501:8501 supermarket-analysis
```

Open your browser at `http://localhost:8501`

## Project Structure

```
.
├── app.py                     # Main Streamlit application
├── generate_data.py           # Sample data generator
├── supermarket_data.xlsx      # Generated data file
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
└── .streamlit/
    └── config.toml            # Streamlit settings
```

## Technologies

- **Python 3.11+**
- **Streamlit** - Web interface
- **Pandas** - Data manipulation
- **Plotly** - Interactive charts
- **OpenPyXL** - Excel file handling

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
