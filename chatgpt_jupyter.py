# import the required libraries
import requests
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler

# define the URL for the ChatGPT API
chatgpt_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# define a new handler class that extends IPythonHandler
class ErrorHandler(IPythonHandler):
    def write_error(self, status_code, **kwargs):
        # call the parent write_error method
        super(ErrorHandler, self).write_error(status_code, **kwargs)
        
        # extract the error message from the kwargs
        message = kwargs['exc_info'][1].args[0]
        
        # define the payload for the ChatGPT API
        payload = {
            "prompt": f"Error: {message}",
            "max_tokens": 60,
            "temperature": 0.5,
            "n": 1,
            "stop": "\n"
        }
        
        # make a request to the ChatGPT API
        headers  = {"Authorization": "Bearer YOUR_API_KEY_HERE"}
        response = requests.post(chatgpt_url, headers=headers, json=payload)
        response.raise_for_status()
        
        # extract the response text from the JSON response
        text = response.json()['choices'][0]['text']
        
        # write the ChatGPT response to the output
        self.write(f"\nChatGPT: {text}\n")

# define a function that adds the error handler to the notebook interface
def load_jupyter_server_extension(nbapp):
    web_app  = nbapp.web_app
    base_url = web_app.settings['base_url']
    endpoint = url_path_join(base_url, 'api', 'errors')
    web_app.add_handlers('.*', [(endpoint, ErrorHandler)])
