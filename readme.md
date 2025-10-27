# task to do


- 1 build a pipe to bring it to railway or aws 
- 1 add ngrok  or an alternative 
- 2 add service url to twilio
- 3 test webhook



### How to run 

# build image
docker build -t chatbot_rag:local .

# run with port mapping (host port 8000 -> container port 8000)
docker run --rm -p 8000:8000 --name chatbot_rag_local chatbot_rag:local