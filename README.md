# THE OSI MODEL INTERACTIVE

An interactive, self-hosted visualization of the OSI Model built with Python Flask and CSS Grid.

## Features
- 7-layer 3D stacked "database" design with a custom blue color fade
- Smooth, accordion-style expand/collapse animation (no JavaScript height calculations needed)
- Interactive info card explaining the OSI Model
- Fully responsive and clean UI
- Dynamic rendering using Jinja2 templates

## How It Works
1. The Python backend (`app.py`) holds a dictionary with all the OSI layer data (names and descriptions).
2. Flask uses **Jinja2** to pass this data to the HTML template.
3. A simple Jinja loop `{% for layer in layers %}` generates the 7 layer cards automatically.
4. CSS Grid (`grid-template-rows: 0fr` to `1fr`) handles the smooth opening and closing animation.
5. A tiny bit of JavaScript toggles the `.active` class when you click a card.

## Usage

terminal:

pip install flask
python app.py



Then open your browser at: http://localhost:5000/ and click on the layers to explore!
