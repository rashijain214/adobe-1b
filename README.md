# Challenge 1b: Multi-Collection PDF Analysis

## Overview

An advanced PDF analysis solution designed to process multiple document collections and extract contextually relevant content based on defined personas and use cases. This system is built for scalability, modularity, and adaptability across diverse domains where extracting targeted insights from large PDF datasets is critical.


##  Features

-  **Multi-Collection Handling**: Efficiently ingests and manages multiple sets of PDFs.
-  **Persona-Based Filtering**: Extracts content aligned with user-defined personas and specific roles.
-  **Use-Case Driven Parsing**: Prioritizes and highlights information relevant to selected scenarios or objectives.
-  **Extensible Pipeline**: Modular design enables plugging in custom NLP models, heuristics, or filters.
-  **Summarization & Insights**: Generates concise summaries and key insights for each persona-use-case pair.


##  Tech Stack

- **Language**: Python 3.x
- **Libraries**: PyMuPDF / PyTorch / Sentence Transformers / Hugging Face / scikit-learn

## Project File Structure
```
adobe-1b/
├── Collection_1/                  #  Travel Planning
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
├── Collection_2/                  #  Adobe Acrobat Learning
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
├── Collection_3/                  #  Recipe Collection
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
```

    
## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```


## Docker Image Instructions
#### Build the Docker image
```
sudo docker build -t challenge-analyzer:latest .
> Note: The `sudo` prefix may be required on personal systems, but is not necessary in Adobe's evaluation environment.

```

#### Run analysis (replace Collection_2 with Collection_1, Collection_3, or Collection_4)
```
sudo docker run --rm \
  -v $(pwd)/Collection_2:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  challenge-analyzer:latest \
  --collection /app/input
> Note: The `sudo` prefix may be required on personal systems, but is not necessary in Adobe's evaluation environment.Can run without sudo too

```

## Run Locally (Without Docker)
Run the analysis script locally(Replace Collection_1 with Collection_2, Collection_3, or Collection_4 as needed)
```
python main.py --collection Collection_1
```

## Input/Output Format
#### Input JSON Structure
```
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

#### Output JSON Structure
```
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```



### Files
**1. extractor.py — PDF Text + Title Extraction**

Purpose: Extracts text and title information from each page of PDFs.

Key Functions:

    extract_text_from_pdfs(pdf_dir, input_documents):

        Loops through PDFs and reads each page using PyMuPDF.

        Extracts both:

            Full text content.

            Titles (determined heuristically based on font size, boldness, position, etc.).

        Returns a list of pages, each with:

            "document", "page_number", "text", "title".

    find_best_title(text_spans):

        Heuristically finds the most likely section/page title from text spans on a page.

**2. chunker.py — Text Chunking**

Purpose: Splits extracted page text into smaller, more manageable chunks for later ranking.

Functions:

    chunk_text(pages):

        Splits each page's text into sentence-based blocks.

        Keeps chunks over 100 characters.

    chunk_text_advanced(pages):

        Smarter chunking by splitting text into paragraphs.

        Ensures each chunk is under ~1000 characters.

        Handles long sections with (Part 1), (Part 2), etc.

**3. ranker.py — Relevance Ranking**

Purpose: Ranks text chunks or sections by how relevant they are to a job description or task.

Functions:

    rank_chunks(chunks, job_description, persona, job_to_be_done):

        Ranks individual chunks using TF-IDF + cosine similarity.

        Takes into account the persona’s role and task context.

        Boosts relevance for pages early in the document.

        Returns:

            top_chunks: Top 5 most relevant.

            refined_texts: Cleaned summaries (first ~800 characters, trimmed to full sentence).

    rank_chunks_with_sections(chunks, job_description):

        Instead of individual chunks, ranks aggregated sections by title + document.

        Scores combined text per section.

        Same TF-IDF-based approach.

    trim_to_sentence(text, limit=800):

        Ensures returned summaries don’t cut off mid-sentence, respecting character limit.

    normalize_scores(scores):

        Normalizes similarity scores for fair comparison.

**4. builder.py — Final Output JSON Builder**

Purpose: Packages everything into a structured JSON format.

Function:

    build_output_json(...):

        Takes in:

            Metadata (input_documents, persona, job_to_be_done, timestamp).

            ranked_sections: Top-ranked chunks or sections.

            refined_texts: Trimmed relevant content.

        Returns:

            metadata block.

            extracted_sections: Document/Title/Page/Rank.

            subsection_analysis: Refined, short summaries of top sections.

 #### End-to-End Pipeline
- extractor.py: Reads PDFs → gets pages with text and title.
 - chunker.py: Breaks pages into smaller chunks.
 - ranker.py: Scores and ranks chunks by relevance to the job/task.
 - builder.py: Assembles everything into final output JSON.

