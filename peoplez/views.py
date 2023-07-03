from django.shortcuts import render
from .models import *
from dotenv import load_dotenv
import os
import openai
import random

load_dotenv()
openai.api_key = os.getenv('API_KEY')  # chatgtp api key


# Create your views here.

# user profile
def user_profile(request):
    return render(request, 'peoplez/user.html')


# about the time machine
def time_machine(request):
    about_data = Introduction.objects.all()

    context = {
        'about': about_data,
    }

    return render(request, 'peoplez/community.html', context)


# traveling to alternate universe
def inside(request):
    # character options
    characters = ['Goku', 'Gohan', 'Piccolo', 'Vegeta', 'Krillin', 'Bulma',
                  'Frieza', 'Trunks', 'Tien', 'Goten', 'Android 17', 'Android 18', 'Majin Buu',
                  'Mr. Satan']

    # scenario options
    scenarios = ["wakes up one morning and has been transported back in time to the year 1910",
                 "is stranded on a deserted island with only a volleyball as their companion",
                 "wins a free trip to space, but during the journey, the spaceship malfunctions, and is left adrift in the cosmos",
                 "suddenly gains the ability to talk to animals, but quickly realizes that they're not very friendly or intelligent",
                 "is the only person left on Earth after Lord Beerus wipes out all human life",
                 "is a detective tasked with solving a string of bizarre murders that all seem to be connected to a mysterious, underground society",
                 "discovers that using the dragonballs leads to the creation of a powerful dragon warrior race",
                 "is a famous musician who suddenly loses their hearing and must find a way to cope and continue creating music",
                 "competes in a cooking competition judged by the Great Saiyaman",
                 "discover's Yamcha's fear of women is magically amplified, causing him to run away from every female he encounters",
                 "enters a dance competition to save a town from a curse",
                 "must recruit other Z fighters to play basketball against a group of aliens who have come to destroy Earth",
                 "becomes trapped in a video game and must beat all the levels to escape",
                 " accidentally eats some bad sushi and experiences hallucinations"
                 ]

    # chat gtp messages will be stored here
    messages = [

        {"role": "system",
         "content": "You are a kind helpful assistant"}
    ]

    random_character = random.choice(characters)  # selecting random character
    random_scenario = random.choice(scenarios)  # selecting random scenario

    message = f"Write a short story where in an alternate universe {random_character} from the dragonball franchise; {random_scenario}"

    # if there is a message we append the new message from the user (you)
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # chat gtp response
    reply = chat.choices[0].message.content

    # dalle images
    images = openai.Image.create(prompt=f"digital art of {random_character} from a weird dragonball universe",
                                 n=3,
                                 size="1024x1024"
                                 )

    image1 = images['data'][0]
    final_1 = image1['url']

    image2 = images['data'][1]
    final_2 = image2['url']

    image3 = images['data'][2]
    final_3 = image3['url']

    # create new story
    new_story = StoryTime(description=reply, image1=final_1, image2=final_2, image3=final_3)

    context = {
        'story': new_story,
        'image1': final_1,
        'image2': final_2,
        'image3': final_3
    }

    return render(request, 'peoplez/inside.html', context)


# this view will be triggered if the user chooses to save the time machine story
def save_timeline(request):
    pass

