Engineer

↓

Incident Assistant

↓

Workflow

↓

Prompt Builder

↓

LLM Client

↓

Output Parser

↓

Incident Report


## Why should Prompt Builder NOT directly call GPT?
Because in a good architecture, we should have segregation of responsibilities. Hence , prompt builder is just building the prompt which can be utilized by multiple LLM clients. This gives us flexibility to change the client without extesive change in how we are building the prompt.