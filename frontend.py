# Install Gradio if not already installed
!pip install gradio --quiet

import gradio as gr
from PIL import Image

# Load your logo image
logo = Image.open("/content/drive/MyDrive/across_hackathon_data/ROOTSlogo.png")

# Backend logic — Replace this with real processing
def recommend_resources(topic, num_keywords, num_authors, num_refs):
    # Word count validation
    words = topic.strip().split()
    if len(words) > 20:
        return "Please limit your topic description to 20 words or fewer."

    # Dummy results — Replace with actual analysis
    keywords = [f"Keyword {i+1}" for i in range(num_keywords)]
    authors = [f"Author {i+1}" for i in range(num_authors)]
    references = [f"Reference {i+1}" for i in range(num_refs)]

    # Format output
    output = (
        "Recommended Keywords:\n" + "\n".join(f"- {k}" for k in keywords) + "\n\n" +
        "Recommended Authors:\n" + "\n".join(f"- {a}" for a in authors) + "\n\n" +
        "Recommended References:\n" + "\n".join(f"- {r}" for r in references)
    )
    return output

def append_text(existing_text, new_text):
    # Füge den neuen Text ans Ende des bestehenden Texts an
    return existing_text + "\n" + new_text

# Create the Gradio interface
with gr.Blocks(title="ROOTS: Research Orientation and Overview Tool for Starters") as demo:
    with gr.Row():
        gr.Image(value=logo, label="ROOTS Logo", show_label=False, interactive=False)

    gr.Markdown("""
    # ROOTS: Research Orientation and Overview Tool for Starters  
    Use this tool to get a quick orientation into a research topic through recommended keywords, authors, and references.
    """)

    with gr.Row():
        topic_input = gr.Textbox(
            label="Topics you would like to know more about (max 20 words)",
            placeholder="e.g., applications of machine learning in climate modeling",
            lines=2
        )

    with gr.Row():
        num_keywords = gr.Slider(1, 20, value=10, step=1, label="How many related keywords do you want me to recommend?")
        num_authors = gr.Slider(1, 10, value=5, step=1, label="How many authors active in this field should I recommend?")
        num_refs = gr.Slider(1, 10, value=5, step=1, label="How many references should I recommend?")

    submit_btn = gr.Button("Submit")
    output = gr.Textbox(label="Recommendations", lines=15, interactive=False)
    #output = append_text(output, out)

    submit_btn.click(
        fn=recommend_resources,
        inputs=[topic_input, num_keywords, num_authors, num_refs],
        outputs=output
    )

demo.launch()