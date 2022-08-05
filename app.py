from flask import Flask, render_template
import random

app = Flask(__name__)
# list of dog images
    

images = [
"https://img.freepik.com/free-photo/adorable-brown-white-basenji-dog-smiling-giving-high-five-isolated-white_346278-1657.jpg",
"https://img.freepik.com/premium-photo/golden-retriever-dog-sitting-panting_191971-7865.jpg",
"https://img.freepik.com/free-photo/beautiful-pet-portrait-dog_23-2149218450.jpg",
"https://img.freepik.com/free-photo/beagle-dog-sitting-with-white-background_53876-30186.jpg",
"https://img.freepik.com/free-photo/crazy-happy-husky-companion-dog-is-posing-cute-playful-white-grey-doggy-pet-playing-white-studio-background-concept-motion-action-movement-pets-love-looks-happy-delighted-funny_155003-33972.jpg",
"https://img.freepik.com/free-psd/portrait-happy-cardigan-welsh-corgi_53876-73961.jpg",
"https://i.ibb.co/Gs93RZf/wepik-photo-mode-202274-164653.jpg"

]

@app.route('/')

def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    