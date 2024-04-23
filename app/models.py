"""
Dictionary of modelName-endpoint key-value pairs
"""
endpoints = {
    "gpt-3.5-turbo":"https://api.openai.com/v1/chat/completions",
    "gpt-4":"https://api.openai.com/v1/chat/completions",
    "claude-2.1":"https://api.anthropic.com/v1/complete",
    "open-mistral-7b":"https://api.mistral.ai/v1/models/chat/completions",
    "mistral-small":"https://api.mistral.ai/v1/models/chat/completions", 
    "mistral-medium":"https://api.mistral.ai/v1/models/chat/completions",
}

authHeaders = {
    "gpt-3.5-turbo":"Authorization",
    "gpt-4":"Authorization",
    "claude-2.1":"x-api-key",
    "open-mistral-7b":"Authorization",
    "mistral-small":"Authorization", 
    "mistral-medium":"Authorization",
}