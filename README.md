# ROOTS

![ROOTSlogo](https://github.com/user-attachments/assets/48c7d6c4-9d07-4e30-911d-389fcdda253e)

ROOTS - Research Orientation and Overview Tool for Starters, is an AI-powered tool that helps beginners explore academic fields by recommending foundational papers, key authors, and essential keywords to build a strong understanding from the ground up.

ROOTS is developed by the team MuT in the context of the 1st [ACROSS](https://www.across-alliance.eu/) Hackaton on AI-based tools for metrics in educations, STEM and social sciences.

Team members (in alphabetical order)
- Daniel Trommler, Professorship for Humans and Technology, TU Chemnitz
- Ferenc Rósza, Professorship for Humans and Technology, TU Chemnitz
- Giuseppe Sanseverino, Professorship for Humans and Technology, TU Chemnitz
- Lena Marcella Nischwitz, Professorship for Humans and Technology, TU Chemnitz

## Introduction

Navigating a new academic field can be overwhelming especially for beginners unfamiliar with key terminology, foundational authors, or landmark publications. Traditional search engines and academic databases assume the user already knows what to look for, creating a barrier for early-stage researchers, students, or those exploring interdisciplinary topics.

### The Problem

The volume of scientific literature is growing exponentially, making it harder than ever to identify relevant and foundational work. Existing solutions often fall short:
1. Search engines (e.g. Google Scholar) rely on predefined sections like titles, keywords, and authors, thus limiting depth and missing contextual cues.
2. Example-based tools (e.g. NotebookLM) require the user to already possess a representative paper, which beginners usually don’t have.

In short, current systems either expect too much from beginner users and the output might be overwhelming.

### Our Solution: ROOTS

ROOTS is an AI-powered recommender system that helps beginners find their footing in any academic domain with minimal input.

Unlike traditional systems, ROOTS leverages Generative AI to analyze not only the structured metadata (titles, keywords, etc.) but also deeper semantic cues across abstracts. This allows for context-aware recommendations even if the user starts with just a broad phrase, a vague interest, or a general topic.

With ROOTS, users can:
- Receive paper recommendations without needing to know specific keywords.
- Discover foundational authors and works in a new field.
- Save time and avoid time-consuming manual searches.
- Build a clearer understanding of a domain from the ground up.

### Who Is ROOTS For

ROOTS is designed to target:
- New graduate students or undergraduates entering research.
- Researchers switching to a new discipline.
- Educators designing reading lists for introductory topics.
- Anyone curious and overwhelmed by scientific literature.

### Why ROOTS Matters

As publication rates continue to rise rapidly and research becomes more interconnected, tools like ROOTS will be crucial in democratizing access to scientific knowledge—making research more approachable, inclusive, and efficient for all levels of expertise.
ROOTS output can also be used as input for other AI-powered scientific assistans such as [Notebook LM](https://notebooklm.google/), or [Research Rabbit](https://www.researchrabbit.ai/). Thus representing a useful add-on to already existing tools. 

## How ROOTS Works

### Interface Design

Gradio is used to design the frontend. The inputs and outputs of the webapp are reported in the following flowchart:

![ROOTS_Miro_final](https://github.com/user-attachments/assets/aa6a3c72-f9eb-4951-ada1-c50ac35632a9)

The Image below shows a screen capture of the UI.

<img width="644" alt="Picture1" src="https://github.com/user-attachments/assets/cb97ea9a-09d0-4a27-afbc-5b251e51c549" />

A demo of the UI is available (only as temporary link) here: [Link](https://f40a73ab41374fc9a6.gradio.live/)

### System implementation

- Search string is given directly to an embedding model, which tokenize the query and calculates an embedding.

- Calculation of the cosine similarity between the search string embedding and all document embeddings.

- Output of the top hits with the highest similarity.

## Limitations

- Slow calculation of the similarity between the search string embedding and all document embeddings à Parallel computation is faster.

- Better data structure for a good internal data management.

- GPU usage for Hugging Face.

- Memory optimization (e.g. for DataFrames).

# Code

Developed [backend](backend.py) and [frontend](frontend.py) codes are shared in this repository.  

Please note that the two are standlaone codes. Due to time constraint our team was not able to have a full implementation. Also, the backend still needs refinements to work as described above.

