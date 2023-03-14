- Create and activate vritual environment

  - python -m venv gptenv/
  - source gptenv/bin/activate
  - Run pip install -r requirements.txt

- Now install "ffmpeg" module

  - Windows: https://phoenixnap.com/kb/ffmpeg-windows
  - MAC: brew install ffmpeg

- Now put your Open AI API key in config.py file
- Now run python harvis.py and open the link in browser(gradio is taking care of this UI thingy)

- Can also use Docker to run this application together instead of virtualenv
- To run the containers, simply navigate to the directory containing the docker-compose.yml file and run the following command:
- docker-compose up
- This will start both containers and output their logs to the console. To stop the containers, use the Ctrl-C key combination.

Sarath Vadlamannati ;)
