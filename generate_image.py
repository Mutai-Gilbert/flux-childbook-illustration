import os
import requests
import replicate

# Load the environment variables from the .env file
load_dotenv()

# Replace with your Replicate API token from the .env file
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

# Set the model you want to use
MODEL_NAME = "samsa-ai/flux-childbook-illustration"
VERSION_ID = "cc3beea6ddc39416cf121390b476b1a8802ca47db03fb97306ef6c25f38f60a2"  # Specific version ID

# Initialize the Replicate client
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

def generate_image(prompt):
    # Generate the image using replicate.run()
    output = client.run(f"{MODEL_NAME}:{VERSION_ID}", input={"prompt": prompt})

    # Save the image
    image_url = output[0]  # Assuming the model returns a list of image URLs
    image_data = requests.get(image_url).content

    # Ensure the directory exists
    output_dir = "kids_books"
    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, "output_image.png")

    with open(output_file, "wb") as f:
        f.write(image_data)

    print(f"Image saved to {output_file}")

if __name__ == "__main__":
    prompt = """
    Create a visually striking image in the style of animated Pixar for a fantasy story with a cheerful tone.

    Composition: Ground level shot.

    Set in an enchanted forest. The scene should reflect the themes and elements from the story. The following is the contents to the page: “A magical tree sprouted golden leaves that glowed under the sunlight”; of the book “The Golden Forest”.

    Important: Ensure the image is free from any textual elements, and the style is consistent across all pages.

    Cartoonish, and suitable for young children aged 2-5 years old. Ensure that there are no characters in the image that you generate.

    Instructions: No text in the image; focus on vivid, imaginative visuals.

    Image of an enchanted forest with major objects or landmarks visualized based on location. The atmosphere should feel cheerful, the time of day is based on the contents to the page. Follow the style consistently; the theme is Pixar (like the movies).
    """
    generate_image(prompt)
