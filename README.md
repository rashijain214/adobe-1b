# Challenge 1b: Multi-Collection PDF Analysis

## Overview

An advanced PDF analysis solution designed to process multiple document collections and extract contextually relevant content based on defined personas and use cases. This system is built for scalability, modularity, and adaptability across diverse domains where extracting targeted insights from large PDF datasets is critical.


## 🔧 Features

- 📁 **Multi-Collection Handling**: Efficiently ingests and manages multiple sets of PDFs.
- 🧠 **Persona-Based Filtering**: Extracts content aligned with user-defined personas and specific roles.
- 🔍 **Use-Case Driven Parsing**: Prioritizes and highlights information relevant to selected scenarios or objectives.
- ⚙️ **Extensible Pipeline**: Modular design enables plugging in custom NLP models, heuristics, or filters.
- 📊 **Summarization & Insights**: Generates concise summaries and key insights for each persona-use-case pair.


## 🛠 Tech Stack

- **Language**: Python 3.x
- **Libraries**: PyMuPDF / PyTorch / Sentence Transformers / Hugging Face / scikit-learn

## Project File Structure
```
adobe-1b/
├── Collection_1/                  # 🧳 Travel Planning
│   ├── PDFs/
│   │   ├── South of France - Cities.pdf
│   │   ├── South of France - Cuisine.pdf
│   │   ├── South of France - History.pdf
│   │   ├── South of France - Restaurants and Hotels.pdf
│   │   ├── South of France - Things to Do.pdf
│   │   ├── South of France - Tips and Tricks.pdf
│   │   └── South of France - Traditions and Culture.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection_2/                  # 📘 Adobe Acrobat Learning
│   ├── PDFs/
│   │   ├── Learn Acrobat - Create and Convert_1.pdf
│   │   ├── Learn Acrobat - Create and Convert_2.pdf
│   │   ├── Learn Acrobat - Edit_1.pdf
│   │   ├── Learn Acrobat - Edit_2.pdf
│   │   ├── Learn Acrobat - Export_1.pdf
│   │   ├── Learn Acrobat - Export_2.pdf
│   │   ├── Learn Acrobat - Fill and Sign.pdf
│   │   ├── Learn Acrobat - Generative AI_1.pdf
│   │   ├── Learn Acrobat - Generative AI_2.pdf
│   │   ├── Learn Acrobat - Request e-signatures_1.pdf
│   │   ├── Learn Acrobat - Request e-signatures_2.pdf
│   │   ├── Learn Acrobat - Share_1.pdf
│   │   ├── Learn Acrobat - Share_2.pdf
│   │   ├── Test Your Acrobat Exporting Skills.pdf
│   │   └── The Ultimate PDF Sharing Checklist.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection_3/                  # 🍽️ Recipe Collection
│   ├── PDFs/
│   │   ├── Breakfast Ideas.pdf
│   │   ├── Dinner Ideas - Mains_1.pdf
│   │   ├── Dinner Ideas - Mains_2.pdf
│   │   ├── Dinner Ideas - Mains_3.pdf
│   │   ├── Dinner Ideas - Sides_1.pdf
│   │   ├── Dinner Ideas - Sides_2.pdf
│   │   ├── Dinner Ideas - Sides_3.pdf
│   │   ├── Dinner Ideas - Sides_4.pdf
│   │   └── Lunch Ideas.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Dockerfile                     # For containerization
├── README.md                      # Project overview
├── app/
│   ├── __init__.py
│   ├── builder.py
│   ├── chunker.py
│   ├── extractor.py
│   └── ranker.py
├── main.py                        # Main script entry
└── requirements.txt               # Python dependencies


    
## 🚀 Installation

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
