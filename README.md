## Objective 
Using gemini conductor for software development. Understand what works, what doesn't and if should be using it for my projects. It also helps me in taking inspiration while developing my own extensions and agent workflows (similar to how conductor is developed for developers)

Use case I picked up :- 
- Create a python backend that uses the Claude Agent SDK to interact with Claude AI
- Create a python frontend that consumes the backend python api 
- Create a nextjs frontend application that consumes the backend python api

## Tools  
- Used `gemini-cli` and `gemini-conductor` extension
- Used my claude code subscription for API 

## Logs 
- Step 1 : Started with first defining agent_requirements.md  
- Step 2 : Started using conductor to do a project setup (`/setup`) The conductor helped me in defining the project level context. I used the agent_requirements.md here. It helped define the overall context. 
  - `index.md`
  - `product.md`, `product-guidelines.md`, `requirements.md`, `tech-stack.md` , `workflow.md`
  - `code_styleguides/`
  - It created `tracks/` folder and `tracks.md` as the repo 
- Step 3 : Started adding tracks. using `/newTrack` 
  - Step 3.1 : Captures the requirements 
  - Step 3.2 : Captures the implementation plan
  - Step 3.2 : Develops the `spec.md` and `plan.md` files alson with `metadata.json` to track progress etc. 
- Step 4 : Started implementing the tasks using `/implement`

## Observations 
- About conductor 
   - A well designed system which works across the software development workflow. Principally very similar to BMAD method, or Github Speckit etc 
      - Clever use of developing various artifacts and system in `/conductor/` folder
      - It supports test driven and spec deriven development which is great in general. However, they sometimes add additional complexity
      - Clever use of `git` history to track changes. 
      - Can use it for brownfield projects
      - Workflow overall focusses on taking approvals and suggestions from the user in a structured way. This is great. 
      - Usage : claude-code has a better UI for asking inputs from the user 
      - Adds a manual verification step even after running automated tests. This is good thinking. 
      - Loved how interactive shell is managed within `.gemini`
- Other observations about this specific project 
   - Gemini2.5 models were sufficient for this task  
   - The agent created `python_frontend` and the tests had no knowledge of `python_backend`. Therefore it started mocking it, which is not necessary
   - The agent identified that the agent is stuck in a loop and wanted to break out of it 
   - The agent deleted the complete python_frontend folder to start afresh. 
- Other observations 

## Learnings 
- While using the agent give additional details. Also ask the agent to remember this for future by adding it in the relevant file in the '/conductor' folder. This ideally could have been built within the conductor itself.
- use `escape` actively, the agent tries to go towards a loop many times, especially while writing tests, best is to interrupt it and guide the agent as early as possible. 
- Frontend development - The frontend project can be better defined in terms of tech stack etc. 
- Frontend development - Try to add an mcp server so that the agent can run frontend tests 
- Guidelines can include things related to logging etc (Note : create your own guidelines)
- For faster development, maybe in certain case you can ask not to write tests 
- For faster development, maybe you can give explicit instructions not to first implement the backend and then make sure that while testing the frontend, the backend servers is implemented and running. 

## Future 
- The core project 
  - Support for session management 
  - The current nextjs frontend does not send the previous messages while calling the api
- Give better guidelines and support for frontend development. 
