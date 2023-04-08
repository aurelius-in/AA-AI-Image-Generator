### DCGAN for Generating Fish, Hands, and Faces

#### Novel DCGAN: 

My DCGAN is novel in several ways.

1. I implemented a new architecture that includes multiple discriminators and generators, where each discriminator and generator focuses on a particular subset of the data (in this case, tropical fish, human hands, and human faces). This approach allowed me to generate high-quality images for each subset, as opposed to trying to generate all three subsets with a single discriminator and generator.

2. I utilized a novel loss function that combines several different components, including adversarial loss, reconstruction loss, and feature matching loss. This allowed me to generate images that not only look realistic but also capture the underlying structure and features of the target data.

3. I decided to narrow my dataset to images of tropical fish, human hands, and human faces for several reasons. 

* These subsets represent a diverse range of visual characteristics, including complex textures, shapes, and colors. 
* Each subset poses unique challenges for image generation, which provides an interesting and challenging task for the DCGAN to solve.

##### Tropical Fish
Generating images of tropical fish was the easiest task, as they have relatively consistent visual features and patterns that are repeated across different fish species.  Subjectively, it is easier to be satisfied by results, but objectively it is harder to define accuracy. 

##### Human Faces
Human faces were more challenging due to their high degree of variability in terms of features, expressions, and lighting conditions. 

##### Human Hands
Finally, human hands were the most difficult to generate convincingly due to their intricate structure and subtle movements that are difficult to capture accurately.
