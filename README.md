# python-template
Template repository for new python projects

## Getting Started

1. Initialize new conda environment
```
conda env create -f <projectname>.yml
```

2. Install required libraries

```
pip install -r requirements.txt
```

3. Install pre-commit hooks

```
pre-commit install
```

4. Create a file called `apiKeys.json` file in the `secrets` directory with the following structure:
```
{
    "openai": {
        "api_key": "<your-key>"
    },
    "anthropic": {
        "api_key": "<your-key>"
    },
    ...
}
```


## Running the code

add your instructions...
