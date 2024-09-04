from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)

@app.route('/')
def homepage():
    """Render a form with fields based on the story's prompts."""
    prompts = story.prompts
    return render_template('form.html', prompts=prompts)

@app.route('/story', methods=['POST'])
def generate_story():
    """Generate and display the story based on user input."""
    answers = {prompt: request.form[prompt] for prompt in story.prompts}
    story_text = story.generate(answers)
    return render_template('story.html', story=story_text)

if __name__ == '__main__':
    app.run(debug=True)