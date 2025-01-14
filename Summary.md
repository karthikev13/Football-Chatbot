What did I learned most from this Project?
This project was my first dive into llm modeling. I learned a lot about the process of chunking, numerically representing text, and how to manage chunked data in a database!
All together this was a very educational experience on how to go end to end with an LLM!

What was the hardest thing about this Project? 
It was challenging early on understanding the common practices when constructing a knowledge base, for example understanding that llm's are based on vector representations of text or images was interesting! 
To think that all of the AI generated images, text, songs, movies are all represented numerically was eye opening

Results of my Project: 
I aimed to make a chatbot that was trained on a Football playcalling knowledge base. I wanted to answer the problem of listening to a sports cast and not having any idea what words are being said! Additionally, 
I love watching football, but I am not good at playing football. So this chatbot could aid me in understanding basic plays, and how to run them! Below are some sample responses of the llm after being trained on the 
football knowledge base. The LLM understands defensive schemes, and is able to recommend counterplays as seen in the second result. In the future, I can see improving the knowledge base and refining a UI for interaction. 

response = rag_chain.invoke({"input": "What is VEER?"})
print(response["answer"])

Must get a pre-snap read to see aiming point (outside leg of first down lineman inside of the handoff key), on 
snap, shuffle towards QB and give a loose pocket for the ball, attack aiming point
VEER is a type of offensive play in American football where the quarterback secures the snap and hands the ball off to the running back while reading the block of the slot receiver.
It is commonly used against defensive formations such as 4-3, 4-4, 5-2, 3-4, 3-5, and Bear. The QB and X positions must get a pre-snap read to determine the aiming point and then execute the play accordingly.

response = rag_chain.invoke({"input": "Give me an example of a play to run against two high safeties"})
print(response["answer"])

One possible play to run against two high safeties is the "Smash-In" play. In this play, the QB's first read is to the receiver running a dig route, who pushes vertical to 10 yards before breaking straight across the field. 
The second read is to the receiver running a corner route, who nods and breaks at 10 yards towards the front pylon. The third read is to the receiver running a go route, aiming for 2 yards outside the hash at 22 yards. 
The QB should expect the ball to be thrown immediately on the Smash-In route. The offensive line should also be prepared to block for a potential run play, with the BST pulling through the hole created by the PSG. 
This play is particularly effective against a three-man front, but can also be run against a four-man front.
