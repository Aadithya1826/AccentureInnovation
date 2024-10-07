from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__,static_folder="C:/Users/aadit/OneDrive/Desktop/AccentureInnovation/static")

genai.configure(api_key="AIzaSyARkA1YAG-wxAi0gQCLVNZ4wmT3mS0k46E")
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_scene_description(crime_scene_data):
    prompt = f"""
    Based on the following crime scene data:
    {crime_scene_data}
    Please generate a detailed and vivid description of how the crime might have unfolded. Include sensory details, character emotions, and possible actions.
    """
    response = model.generate_content(prompt)
    return response.text


def generate_crime_novel(chapter_title, scene_description, previous_chapters=""):
    prompt = f"""
    You are writing a crime novel titled 'The Shadows of Midnight'. The title of the current chapter is '{chapter_title}'.
    
    Based on the following scene description:
    {scene_description}
    
    Previous chapters: {previous_chapters}

    Write the next chapter of the novel. Focus on character interactions, dialogue, and the suspense of the crime.
    """
    response = model.generate_content(prompt)
    return response.text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    crime_scene_data = request.form['crime_scene_data']
    chapter_title = request.form['chapter_title']
    
    # Generate the scene description
    scene_description = generate_scene_description(crime_scene_data)
    
    # Generate the crime novel chapter
    novel_chapter = generate_crime_novel(chapter_title, scene_description)
    
    return jsonify({
        'scene_description': scene_description,
        'novel_chapter': novel_chapter
    })


if __name__ == '__main__':
    app.run(debug=True)
