# CheckSumr

A user-friendly desktop application for file hash verification and generation. CheckSumr provides an intuitive GUI to verify file integrity and generate cryptographic hashes using multiple algorithms.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

## Features

- **Hash Verification**: Verify file integrity by comparing against known hash values
- **Hash Generation**: Generate cryptographic hashes for any file
- **Multiple Algorithms**: Support for MD5, SHA-1, SHA-224, SHA-256, SHA3-256, SHA-384, SHA3-384, SHA-512, and SHA3-512
- **Auto-Detection**: Automatically detects hash algorithm based on hash length
- **User-Friendly GUI**: Clean and intuitive interface built with Tkinter
- **Memory Efficient**: Processes large files using chunked reading
- **Copy to Clipboard**: Easily copy generated hashes

## Screenshots

The application features:
- File selection browser
- Hash verification with visual feedback
- Multiple hash algorithm selection
- Generated hash display with copy functionality

## Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/CheckSumr.git
cd CheckSumr
```

2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install Tkinter if not available:
   - **Ubuntu/Debian**: `sudo apt-get install python3-tk`
   - **Fedora**: `sudo dnf install python3-tkinter`
   - **macOS**: Included with Python from python.org
   - **Windows**: Included with Python installer

## Usage

### Running the Application

```bash
python Main.py
```

### Verifying a File Hash

1. Click **Browse** to select a file
2. Enter the known hash value in the "Hash Verification" section
3. Click **Verify Hash**
4. The application will automatically detect the hash algorithm and verify the file

### Generating a File Hash

1. Click **Browse** to select a file
2. Select the desired hash algorithm from the dropdown menu
3. Click **Generate Hash**
4. The hash will be displayed in the output area
5. Click **Copy to Clipboard** to copy the hash

## Supported Hash Algorithms

| Algorithm | Hash Length | Use Case |
|-----------|-------------|----------|
| MD5 | 32 characters | Legacy support (not recommended for security) |
| SHA-1 | 40 characters | Legacy support (not recommended for security) |
| SHA-224 | 56 characters | Moderate security |
| SHA-256 | 64 characters | Standard security (recommended) |
| SHA3-256 | 64 characters | Modern security standard |
| SHA-384 | 96 characters | High security |
| SHA3-384 | 96 characters | Modern high security |
| SHA-512 | 128 characters | Maximum security |
| SHA3-512 | 128 characters | Modern maximum security |

## Project Structure

```
CheckSumr/
├── Main.py           # Application entry point
├── GUI.py            # Tkinter GUI implementation
├── Hashing.py        # Core hashing and verification logic
├── requirements.txt  # Project dependencies
├── README.md         # Project documentation
└── LICENSE           # License file
```

## API Usage

You can also use the `Hashing` class programmatically:

```python
from Hashing import Hashing

# Verify a file hash (auto-run mode)
verifier = Hashing('/path/to/file', 'expected_hash_value', auto_run=True)
print(verifier.result)  # True if hash matches, False otherwise

# Generate a hash
generator = Hashing('/path/to/file', '', auto_run=False)
md5_hash = generator.gen_hash('md5')
sha256_hash = generator.gen_hash('sha256')
print(f"MD5: {md5_hash}")
print(f"SHA256: {sha256_hash}")
```

## Contributing

Contributions are welcome! Here's how you can help:

### Looking for Frontend Developers

I fully authorize you to improve the GUI and make pull requests. I will merge them with the main branch.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Improvement

- Enhanced UI/UX design
- Dark mode support
- Drag-and-drop file selection
- Batch file processing
- Progress bar for large files
- File hash comparison feature
- Export hash results to file
- Additional hash algorithms

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's standard library
- GUI powered by Tkinter
- Hashing powered by hashlib

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute improvements via pull requests

---

**Note**: MD5 and SHA-1 are considered cryptographically broken and should not be used for security-critical applications. Use SHA-256 or SHA3-256 for modern security requirements.
