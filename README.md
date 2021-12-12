![titleforproject](https://user-images.githubusercontent.com/66905824/145704096-6b8a4720-1101-4f3b-abc6-5255e09de4c6.jpg)

# What we wanted to do
We all are interested in cryptocurrencies so we looked for datasets on this topic. We found a [dataset](https://www.kaggle.com/odins0n/top-50-cryptocurrency-historical-prices/version/5?select=Ethereum.csv) that containted information on the top 50 coins. Each coin has its daily open price, high price, low price, volume of transactions, and change percentage. The coins we worked with were Ethereum, Bitcoin, and Solana. The overall goal of the project was to create a model that could accurately predict the daily high price of a given coin. In order to do this we used scikit to choose a good model that would give us accurate estimates. We also deployed our findings to a website using Django.

# Selection of Data
The dataset included a different CSV file for each coin. Becuase each coin was created at different times each dataset has a different number of samples. The bitcoin dataset contains 4,056 days of data, Ethereum contains 1,994 days, and Solana contains only 445 days of data. However each coin had the same feautres which are the open price, high price, low price, volume of transactions, and change percentage.
![Example image of Ethereum dataset](https://user-images.githubusercontent.com/54991313/145722618-be5a6a6c-ae72-408f-a9b0-0b5d61500d75.png)
Above you can see an example of one of our datasets. This is the ethereuem data set. (ASK ABOUT IF THEY REMOVED DATE FROM DATASET). In terms of preparing the data we did not have to change much. All of our information was numerical so it was perfect to be learned on. We also visulaized some of our data to get a better idea of what it looks like.
![eVis](https://user-images.githubusercontent.com/54991313/145723454-be62e022-ba97-4fd8-9e4a-7c8914f42a06.png)
![bVis](https://user-images.githubusercontent.com/54991313/145723491-66b72cec-0ba0-45d9-afbb-28ce7f52d300.png)

# Methods and Tools
We each wrote our notebooks in Jupyter and would push them to git using the command line. We used numpy, scikit, pandas, and matplot lib. We stored all of our code on git creating our own branches and then pushing to main once we completed our code. We all ended up using a train test split and linear regression as our model to get the best scores. The website was built using Jericho to host all of our results.

# Results
Each of us ended up creating models that were able to get relativly accurate scores. The Solana model was able to predict the scores within eight dollars
![solana data](https://user-images.githubusercontent.com/54991313/145723224-b8d9b36a-77fc-4422-acc8-3a9397311719.png)
The Ehtereum model had simillar results and was able to predict the daily high within seven dollars
![ethereum data](https://user-images.githubusercontent.com/54991313/145723274-ab7de837-0c41-4654-acb5-5097ea2faf44.png)
The Bitcoin model also preformed very well getting an accuracy percentage of 99.97%
![bitcoin data](https://user-images.githubusercontent.com/54991313/145723339-593c9eb0-02a3-45ca-b81f-49172ea19e15.png)
Overall it seems that all of our models worked very well and were able to very accurately predict the daily high of each coin.

# Discussion
We all aggred that given more time and more information we could expand on this project idea to create a bitcoin price predicted. If we could figured out a way to mine data from multipe sources such as twitter, the stock market, and other factors that influnece cryptocurrency prices we could create a model that would predict the future highs of coins. For the time that we did have we are very happy with what we created as it is able to accurately predict the high price within a couple dollars. (ASK AMEN IF HE WANTS TO TALK ABOUT WEBSITE CREATION)

# Summary
Overall this project was a very good way to learn more about machine learning and combine little bits we have learned over the semester about numpy and pandas as well. Our group was able to accurately predict the daily highs of 3 different cryptocurrencies.
