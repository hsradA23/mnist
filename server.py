from fastapi import FastAPI
import torch
from torch import nn
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from json import dumps

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()

        self.clf = nn.Sequential(
            nn.Conv2d(in_channels=1,out_channels=32,kernel_size=6, bias=False), # 28-4+1 = 25
            nn.BatchNorm2d(num_features=32),
            nn.Conv2d(in_channels=32,out_channels=16,kernel_size=5, bias=False), #25-4+1 = 22
            nn.BatchNorm2d(num_features=16),
            nn.Conv2d(in_channels=16,out_channels=8,kernel_size=4, bias=False),
            nn.BatchNorm2d(num_features=8),
            nn.Flatten(),
            nn.Linear(2048,1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024,512),
            nn.LeakyReLU(0.2),
            nn.Linear(512,10),     
        )

    def forward(self, x):
        return nn.functional.softmax(self.clf(x))
    
    
clf = Classifier()
clf.load_state_dict(torch.load('model.pt'))


@app.post("/items/")
async def create_items(items: List[int]):
    arr = torch.FloatTensor(items)
    arr = arr.view(1, 1, 28,28)
    arr = map(lambda x: round(x,4) ,clf(arr).tolist()[0])
    return {"message": dumps(list(arr))}

@app.get("/")
async def root():
    return {"message": "Hello World"}