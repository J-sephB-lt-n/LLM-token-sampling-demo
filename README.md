```bash
echo "OPENAI_API_BASE_URL='your api base url'" >> .env
echo "OPENAI_API_KEY='your api key'" >> .env
uv run fastapi dev backend.py --port 6969 # then navigate to http://localhost:6969
```

Here is the original prompt which I gave the model to create this application:

````
Write me a single page web application using just html, css and javascript.
I want the application to do the following:
1. User adds system prompt text into a form and user prompt text into another form. 
2. User must also provide model_name (text)
3. User must also specify max_tokens and top_logprobs (non-negative integers)
4. The "submit prompt" button only works once all user inputs have been provided and are valid.
5. User prompt is submitted to LLM server (which uses the OpenAI api spec). See the LLM server code below:
```python
{{ contents of backend.py here }}
```
6. Show the API response code and status to the user (as a popup)
7. Show the model content (LLM text response) to the user. When the user hovers over one of the TOKENS (not words) in the LLM response (get the tokens from the logprobs output), show the distribution of token probabilities for that word (i.e. what that token could have been), illustrating with color and bar graph the relative probabilities of each token. The probability color should scale evenly through the scale red (0 probability) to yellow (50% probability) to green (100% probability). Normalise the probabilities to sum to 100 over the token probabilities available.
````
```
