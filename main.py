# main.py

import argparse
import os
import json
import datetime

from app.extractor import extract_text_from_pdfs
from app.chunker import chunk_text
from app.ranker import rank_chunks
from app.builder import build_output_json


def main(collection_path):
    input_path = os.path.join(collection_path, 'challenge1b_input.json')
    output_path = os.path.join(collection_path, 'challenge1b_output.json')
    pdf_folder = os.path.join(collection_path, 'PDFs')

    # Load input JSON
    with open(input_path, 'r') as f:
        input_data = json.load(f)

    try:
        documents_info = input_data['documents']
        input_documents = [doc['filename'] for doc in documents_info]
        persona = input_data['persona']  # <-- pass the whole dict
        job_to_be_done = input_data['job_to_be_done']  # <-- pass the whole dict
    except KeyError as e:
        raise ValueError(f"❌ Missing expected key in input JSON: {e}")

    job_description = f"{persona}: {job_to_be_done}"

    print("🔍 Extracting text from PDFs...")
    extracted_data = extract_text_from_pdfs(pdf_folder, input_documents)
    print("✂️ Chunking text...")
    chunks = chunk_text(extracted_data)

    # Inject section titles into text to increase matching score
    for chunk in chunks:
        if chunk.get("title"):
            chunk["text"] = f"{chunk['title']}. {chunk['text']}"

    print("📊 Ranking chunks...")
    job_description = f"The role is: {persona}. The goal is to: {job_to_be_done}"
    ranked_chunks, refined_chunks = rank_chunks(chunks, job_description, persona, job_to_be_done)


    print("🛠️ Building output JSON...")
    output_json = build_output_json(
        input_documents=input_documents,
        persona=persona,
        job_to_be_done=job_to_be_done,
        ranked_sections=ranked_chunks,
        refined_texts=refined_chunks,
        timestamp=datetime.datetime.now().isoformat()
    )

    with open(output_path, 'w') as f:
        json.dump(output_json, f, indent=2)

    print(f"✅ Output written to {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--collection', type=str, required=True, help='Path to collection folder')
    args = parser.parse_args()
    main(args.collection)
