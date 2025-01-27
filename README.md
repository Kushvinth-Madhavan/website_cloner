# Website Cloner

A Python-based tool that creates a local copy of websites by recursively downloading and saving HTML pages while maintaining the original site structure. This tool is perfect for creating offline backups of websites or for educational purposes.

## Features

- Recursive website crawling
- Maintains original website structure
- Handles relative and absolute URLs
- Domain-restricted crawling (only clones pages from the same domain)
- Automatic directory structure creation
- Link rewriting for offline browsing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kushvinth-madhavan/website-cloner.git
cd website-cloner
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python website_cloner.py
```

When prompted, enter the website URL you want to clone (including http:// or https://). For example:
```
Enter the website URL to clone (e.g., https://example.com): https://example.com
```

The cloned website will be saved in the `cloned_website` directory, maintaining the original site structure.

## Project Structure

```
website-cloner/
├── README.md
├── requirements.txt
├── website_cloner.py
└── cloned_website/         # Generated directory for cloned sites
    └── example.com/       # Example of cloned website directory
```

## Code Structure

- `website_cloner.py`: Main script containing all the functionality
  - `clone_website()`: Main function that handles the recursive cloning process
  - `save_html()`: Handles saving HTML content and rewriting links
  - `is_valid_url()`: Validates URLs and ensures they're within the same domain

## Requirements

See `requirements.txt` for the full list of dependencies:
- beautifulsoup4>=4.9.3
- requests>=2.25.1

## Limitations

- Only clones HTML pages and their structure
- Does not download assets (images, CSS, JS files)
- Limited to single domain crawling
- Basic error handling
- May not handle all edge cases in URL structures

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Please ensure you have permission to clone any website you target with this tool. Respect robots.txt and website terms of service. This tool is intended for educational purposes and creating authorized backups only.
