# u/brOSKI

u/brOSKI is a chat bot that attempts to help Berkeley students with everything Cal while trained to sound like the average r/berkeley enjoyer. We accomplish
with a dual pronged approach. In order to get the "sound" of a funny berkeley student, I trained LLaMA 2 13b on the r/berkeley subreddit using the together.ai
API, and in order to get the knowledge and accuracy of a Cal advisor, LeonShams ustilized prompt engineering and LLama 2 13b to currate our data based on class
information, teacher biographies and enrollment information. This way our model could give helpful information to the user. pranavdo implemented the front end,
which displays a user interface that interacts with the backend to call LLama 2 12b. 

u/brOSKI is finetuned with the help of together.ai, which offers a very easy to use API to train and deploy the model. Unfortunately, the API does not yet support
your finetuned models to be used with your local code. So unless you are signed into my account, you cannot YET talk to the finetunened u/brOSKI. Nonetheless,
there will be some pictures provided below of some of the funny answers u/brOSKI gave after chating with it for about 10 minutes.

This program was built during CalHacks 2023 so it has only been in development for about 48 hours (as of 10/29/2023). Considering the extremely
short time frame, we are extremely happy with the results of our model. All of the code that we used during those 48 hours are provided here
in this github. Stay tuned, because we have future visions of expanding the model even more!

# Here are some images of just the finetuned model, no contextual analysis is ran here.
*Finetuned chat bot, the "brO" side of u/brOSKI*

<img width="746" alt="im a person" src="https://github.com/m0zzaR/CalCompanion/assets/83364878/cdcdf748-7517-4181-88c4-651cba1fac68">
<img width="767" alt="are you a berkeley student" src="https://github.com/m0zzaR/CalCompanion/assets/83364878/f7aa96f2-e459-4b09-9d21-566bc57a7689">
<img width="763" alt="paulin" src="https://github.com/m0zzaR/CalCompanion/assets/83364878/a8af1df9-3c25-48f3-9cf9-9d33b89d80b1">
<img width="737" alt="whats the meaning of life" src="https://github.com/m0zzaR/CalCompanion/assets/83364878/d2564557-7e91-401a-966b-d13705ca0646">

The data we used for this model was about 3500 lines of r/berkeley posts from 2023 formated in Q&A style. Where the title
and body are the "question" and the most upvoted comment is the "answer". The model is trained for 6 epochs. There
is MUCH MUCH room for improvement here considering our biggest limiting factor was finding and downloading data
within the CalHacks time frame. 
-Note: The data that we curated removes personal user information.

# Guide for running context chat bot into a localHost*
*Context analysis chat bot, the "u/OSKI" side of u/brOSKI*

You need to use your own together.ai API Key to run this program. 
requirements
```
pip install together
pip install flask
pip install flask_cors
```

Step 1> while inside ./CalCompanion run
```
python api.py
```
Step 2> open up the index.html fine

Step 3> Chat away!
