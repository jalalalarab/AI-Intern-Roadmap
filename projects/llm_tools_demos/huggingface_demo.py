from transformers import pipeline

classifier = pipeline("sentiment-analysis")

results = classifier([
    "I love building AI projects, this is amazing!",
    "This install took forever and I'm frustrated.",
    "FastAPI makes building APIs really straightforward."
])

for text, result in zip(["Text 1", "Text 2", "Text 3"], results):
    print(f"{text}: {result['label']} (confidence: {result['score']:.2f})")