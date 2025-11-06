# task to do


- 1 build a pipeline to bring it to railway or aws 
- 2 add data files and convert to enbeddings 
- 3 pass enbeddings to webhook 
- 3 research if use mcp calendar or custom
- 4 connect to postgress to save appointments and clients history



### How to run 

# build image
docker build -t chatbot_rag:local .

# run with port mapping (host port 8000 -> container port 8000)
docker run --rm -p 8000:8000 --name chatbot_rag_local chatbot_rag:local