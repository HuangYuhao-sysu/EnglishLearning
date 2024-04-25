#!/usr/bin/env python3

Sentences = {
'1 tea':[
    "Studies have shown that tea has various benefits for people.",
    "It makes them more alert, improves their memory and concentration, and offers many other benefits.",
    "I know some people in their 70s and 80s who are in great health, most of whom are avid tea drinkers."
    ],
'2 spring':[
    "I really enjoy the mild, breezy weather of spring.",
    "The gentle spring breeze and mild temperatures make outdoor activities very enjoyable.",
    "It's a time when everything seems to come alive."
    ],
'3 gift':[
    "In our fast-paced world, giving gifts is still a big deal.",
    "Whether it's for birthdays, holidays, or just to show appreciation, it's a tradition that brings people together.",
    "I recently got a potted plant from a friend, which keeps reminding me of her affection and presence in my life."
    ],
'4 family and friends':[
    "I'm aiming to make more time for my family and friends.",
    "Life can often get busy, and it's easy to neglect the people who mean the most to us.",
    "I plan to schedule regular get-togethers and make an effort to stay in touch with my loved ones."
    ],
'5 films':[
    "When it comes to films, I have a pretty diverse taste.",
    "However, I would say that I particularly enjoy two main genres, dramas and science fiction",
    "Both dramas and science fiction provide me with an escape from reality.",
    ],
'6 introverts':[
    "Introverts often prefer quiet and solitary environments.",
    "They enjoy reflecting on their own ideas, and are often good at tasks that require concentration and focus.",
    "This can be an asset in fields like writing, programming, or research, where deep thinking is key.",
    ],
'7 AI':[
    "While artificial intelligence is certainly transforming the job market, it's not going to completely eliminate the human workers.",
    "AI can take over some of the routine work, freeing up humans to focus on more complex and critical tasks.",
    "Many jobs require human qualities like empathy, critical-thinking and problem-solving, which AI is still far from replicating.",
    ],
'8 pandemic':[
    "During the pandemic, I had to adapt to online learning, which presented some challenges.",
    "Staying focused and motivated while learning remotely is difficult, but I managed to overcome these obstacles.",
    "I believe online learning will continue to evolve and become more effective in the future.",
    ],
'9 dream':[
    "My dream is to become a published author, sharing my stories and ideas with the world.",
    "I'm working hard to achieve this dream by writing regularly, and seeking feedback from others.",
    "I recently finished my first draft of a novel, and I'm really proud.",
    ],
'10 social media':[
    "Social media has become a powerful tool for connecting with people from all over the world.",
    "I use social media to share my experiences, learn new things, and connect with like-minded individuals.",
    "However, it's important to use it responsibly, avoiding its potential pitfalls such as addiction and misinformation.",
    ],
'11 cinema':[
    "Cinema has always fascinated me, it offers a unique way of experiencing stories and emotions.",
    "I remember watching my first film as a child, and being transported into a whole new world.",
    "Cinema is magical because it deeply affects our hearts and minds. Some movies can leave a lasting impression on us.",
    ],
'12 perseverance':[
    "I've learned that perseverance is key to overcoming challenges and achieving my goals.",
    "When faced with difficulties, I remind myself that perseverance will eventually lead to success.",
    "The sense of accomplishment I feel after persevering through a challenge is incredibly rewarding.",
    ],
'13 diet':[
    "I follow a balanced diet, incorporating a variety of fruits, vegetables and whole grains into my meals.",
    "I enjoy trying new cuisines and exploring different flavors from around the world.",
    "I believe that healthy eating habits are crucial form maintaining good health and well-being.",
    ],
'14 running':[
    "Running is a solitary yet rejuvenating activity.",
    "It's a great way to stay fit and healthy. I enjoy the sense of accomplishment after a long run.",
    "Running clears my mind and helps me unwind after a stressful day. It's become a regular part of my daily routine.",
    ],
'15 traveling':[
    "My most memorable travel experience was hiking through the Swiss Alps, surrounded by breathtaking scenery.",
    "Traveling has taught me to appreciate diverse cultures and ways of life.",
    "I always look forward to future travels, as they provide me with priceless life experiences and memories.",
    ],
'16 living area':[
    "There have been more high-rise buildings in my neighborhood, making the area much denser than before.",
    "Some cafes have opened up in a few of those buildings.",
    "I'm really happy with the construction of an outdoor gym, where I work out regularly.",
    ],
'17 save money':[
    "I save money by setting a budget and sticking to it, which helps me avoid unnecessary expenses.",
    "Shopping around for the best deals and using coupons helps me save money on daily purchases.",
    "I also save by investing in long-term financial products, allowing my money to grow over time."
    ],
'18 living house':[
    "I live in a cozy apartment located in the heart of the city.",
    "It's a two bedroom unit with a small balcony that overlooks a busy street.",
    "I used to live in a detached house in a quiet suburban neighborhood, which had a garden where I could relax and unwind.",
    ],
'19 a recent change':[
    "I've undergone a positive change in my health recently. I've started focusing on exercise and diet.",
    "A recent medical check up make me realize the need for action.",
    "I've been exercising regularly, choosing healthier food options, and maintaining a good sleep schedule.",
    ],
'20 a skill':[
    "I was bored one day and decided to pick up a guitar that had been lying around in my house for years.",
    "I downloaded some tutorials and started practising every day.",
    "With practices and persistence, I gradually got better, and Within a few months, I could play some simple songs.",
    ],
'21 friendships':[
    "Friendships are incredibly important in live.",
    "They provide support, companionship, and a sense of belonging.",
    "My friends are like an extended family to me, and I cherish the bond we share.",
    ],
'22 journaling':[
    "Journaling is a valuable tool for mental wellbeing in this fast-paced world.",
    "Putting pen to paper allows you to express yourself freely and helps manage stress, anxiety, and even sadness",
    "Jotting down ideas and thoughts can help you think of innovative solutions to challenges.",
    ],
'23 city life':[
    "I love the buzz of city life. There's always something to do and new places to explore.",
    "My favorite part of city life is the variety of restaurants and cafes.",
    "I love trying new cuisines and meeting with people from different cultures.",
    ],
'24 environment':[
    "I'm very concerned about the environmental issues and try to live a sustainable lifestyle.",
    "Recycling is a habit that I've adopted to reduce waste and help the environment.",
    "I think everyone has a responsibility to protect our planet. We need to work together to create a more sustainable future.",
    ],
'25 t-shirts':[
    "I wear t-shirts on a daily basis as they are my go-to choice for casual attire.",
    "Wether I'm running errands, meeting friends or lounging at home, a comfortable t-shirt is always my first choice.",
    "I'm currently on the lookout for new t-shirts to refresh my wardrobe.",
    ],
'26 more bicycle':[
    "For me, the most convenient form of transportation is the bicycle.",
    "It's easy to park, doesn't require fuel, and allows me to get some exercise at the same time.",
    "of course, It's not always the suitable for long distances and bad weather, but it's ideal for most days.",
    ],
'27 ambitions':[
    "One of my ambitions is becoming a polyglot over the next ten years.",
    "To realize this goal, I plan to use language learning apps, and travel to practice in real life situations.",
    "Being multilingual is a gateway to global opportunities and fosters a deeper understanding of the world.",
    ],
'28 sport':[
    "I think it's crucial for children to do sport.",
    "It helps them stay fit and learn the importance of discipline and hard work.",
    "My favorite sport was swimming. I loved the feeling of being in the water and the challenge of improving my techniques.",
    ],
'29 advertisement dislike':[
    "This ad popped up on my screen repeatedly while I was scrolling through my social media feed.",
    "It was a video advertisement promoting a fast food chain, showcasing their greasy burgers and fries.",
    "I felt like the ad was stalking me, which made me feel very uncomfortable.",
    ],
'30 spare time':[
    "In my spare time, I like to go hiking and biking in the mountains.",
    "I recently joined a mountain biking club and we meet on a particular trail every Sunday morning and ride together.",
    "It's a great workout and a good way for me to meet new friends.",
    ],
'31 talk about Allen':[
    "Allen loves trying out new recipes and making tasty dishes from all over the world.",
    "He's especially good at grilling, his steaks and burgers are amazing.",
    "he believes that food has a special way of bringing people together and creating awesome memories.",
    ],
}


import random

keys = list(Sentences.keys())
random.shuffle(keys)  # Randomly shuffle the keys
remaining = len(keys)

for key in keys:
    print(key)  # Print the current key
    print("Remaining topic: " + str(remaining))
    remaining = remaining - 1
    input("Press Enter to show the sentences...")  # Wait for Enter key press
    print("\n---\n")  # Print a separator after each key's sentences
    for sentence in Sentences[key]:
        print(sentence)  # Print each sentence
    print("\n---\n")  # Print a separator after each key's sentences

print("All sentences reviewed!")