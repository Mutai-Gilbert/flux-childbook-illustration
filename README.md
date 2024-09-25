# flux-childbook-illustration
# Flux Childbook Illustration Generator

This project allows you to generate visually striking images using the `samsa-ai/flux-childbook-illustration` model from the Replicate API. The generated images are based on a user-provided prompt and are ideal for creating fantasy storybook illustrations with a cheerful tone, specifically in a style reminiscent of Pixar animation.

## Features
- Generates cartoonish illustrations suitable for children's storybooks (ages 2-5)
- Allows custom prompts to describe the scene and style
- Downloads and saves the generated image locally
- Ensures the image is free from textual elements

## Prerequisites
To run this project, you need:
1. Python 3.x installed on your system.
2. A Replicate API token, which you can get from [Replicate](https://replicate.com/).
3. Required Python libraries:
    - `replicate`
    - `requests`
    - `os`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flux-childbook-illustration-generator.git
   cd flux-childbook-illustration-generator

2. Install the required Python libraries:
    ```bash
    pip install replicate requests

3. Set up your environment: Replace the placeholder API token with your actual Replicate API token inside the script:
   ```bash
   REPLICATE_API_TOKEN = "your_replicate_api_token"
