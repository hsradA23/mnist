FROM nikolaik/python-nodejs:latest

WORKDIR /usr/src/app

RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu
RUN pip3 install numpy fastapi "uvicorn[standard]"

COPY . .
WORKDIR /usr/src/app/my-vue-app

# RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.3/install.sh | bash
# RUN nvm install node
RUN npm install


WORKDIR /usr/src/app

# CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]
ENV PORT 80000
# CMD [ "npm", "run", "dev", "--","--port", "8000", "--host"]
CMD ./run.sh