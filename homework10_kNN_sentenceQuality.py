# name 1:
# name 2:
# name 3:


dataset = [
    {"sentence": "The breathtaking sunset painted the sky with hues of orange, pink, and purple, casting a serene ambiance over the tranquil beach.", "quality": 1},
    {"sentence": "The cat sat lazily on the windowsill, watching the world outside with a curious gaze.", "quality": 0},
    {"sentence": "I like pizza. It is tasty.", "quality": -1},
    {"sentence": "The orchestra played a symphony that filled the concert hall with enchanting melodies.", "quality": 1},
    {"sentence": "The rain fell gently, creating a soothing rhythm on the roof.", "quality": 1},
    {"sentence": "The book was filled with intricate plots and well-developed characters.", "quality": 1},
    {"sentence": "The traffic jam stretched for miles, causing frustration among commuters.", "quality": -1},
    {"sentence": "The movie was predictable and lacked depth.", "quality": -1},
    {"sentence": "The restaurant served bland food with poor presentation.", "quality": -1},
    {"sentence": "The sunrise over the mountains was a breathtaking sight to behold.", "quality": 1},
    {"sentence": "The children laughed and played in the park, enjoying the warm sunshine.", "quality": 1},
    {"sentence": "The novel kept me on the edge of my seat with its suspenseful plot twists.", "quality": 1},
    {"sentence": "The breathtaking sunset painted the sky with hues of orange, pink, and purple, casting a serene ambiance over the tranquil beach.", "quality": 1},
    {"sentence": "The cat sat lazily on the windowsill, watching the world outside with a curious gaze.", "quality": 0},
    {"sentence": "I like pizza. It is tasty.", "quality": -1},
    {"sentence": "The orchestra played a symphony that filled the concert hall with enchanting melodies.", "quality": 1},
    {"sentence": "The rain fell gently, creating a soothing rhythm on the roof.", "quality": 1},
    {"sentence": "The book was filled with intricate plots and well-developed characters.", "quality": 1},
    {"sentence": "The traffic jam stretched for miles, causing frustration among commuters.", "quality": -1},
    {"sentence": "The movie was predictable and lacked depth.", "quality": -1},
    {"sentence": "The restaurant served bland food with poor presentation.", "quality": -1},
    {"sentence": "The sunrise over the mountains was a breathtaking sight to behold.", "quality": 1},
    {"sentence": "The children laughed and played in the park, enjoying the warm sunshine.", "quality": 1},
    {"sentence": "The novel kept me on the edge of my seat with its suspenseful plot twists.", "quality": 1},
    {"sentence": "The breathtaking view from the top of the mountain left me speechless.", "quality": 1},
    {"sentence": "The puppy wagged its tail happily as it played with its favorite toy.", "quality": 1},
    {"sentence": "The delicious aroma of freshly baked cookies filled the kitchen.", "quality": 1},
    {"sentence": "The lecture was informative, but it felt a bit too long.", "quality": 0},
    {"sentence": "The new painting in the gallery caught everyone's attention with its vibrant colors.", "quality": 1},
    {"sentence": "The traffic on the highway was moving smoothly, with no delays in sight.", "quality": 0},
    {"sentence": "The performance at the theater received rave reviews from critics.", "quality": 1},
    {"sentence": "The quiet, peaceful atmosphere of the countryside was a welcome change from the city.", "quality": 1},
    {"sentence": "The coffee shop was cozy and inviting, perfect for a relaxing afternoon.", "quality": 1},
    {"sentence": "The rainy weather put a damper on our outdoor plans.", "quality": -1},
    {"sentence": "The abandoned house looked spooky, with broken windows and overgrown weeds.", "quality": -1},
    {"sentence": "The birthday party was a huge success, with laughter and joy filling the air.", "quality": 1},
    {"sentence": "The intricate design of the cathedral's stained glass windows was truly remarkable.", "quality": 1},
    {"sentence": "The train arrived at the station right on time, much to the relief of the waiting passengers.", "quality": 1},
    {"sentence": "The company's new product received mixed reviews from consumers.", "quality": 0},
    {"sentence": "The hike through the forest was challenging but rewarding, with stunning views along the way.", "quality": 1},
    {"sentence": "The exam was difficult, but I managed to pass with flying colors.", "quality": 1},
    {"sentence": "The ocean waves crashed against the shore, creating a soothing sound.", "quality": 1},
    {"sentence": "The museum exhibit featured a diverse collection of artwork from around the world.", "quality": 1},
    {"sentence": "The conversation with my friend was enlightening, and I learned a lot from it.", "quality": 1},
    {"sentence": "The city skyline at night was a breathtaking sight, with twinkling lights as far as the eye could see.", "quality": 1},
    {"sentence": "The abandoned factory was eerie, with shadows dancing in the moonlight.", "quality": -1},
    {"sentence": "The soccer game was intense, with both teams giving it their all until the very end.", "quality": 1},
    {"sentence": "The snowfall blanketed the city in white, creating a picturesque scene.", "quality": 1},
    {"sentence": "The dance performance was mesmerizing, with graceful movements and intricate choreography.", "quality": 1},
    {"sentence": "The road trip was long but enjoyable, with plenty of stops along the way to take in the scenery.", "quality": 1},
    {"sentence": "The abandoned shipwreck on the beach was a haunting reminder of the past.", "quality": -1},
    {"sentence": "The sunset was absolutely stunning, painting the sky with vibrant shades of red and orange.", "quality": 1},
    {"sentence": "The dog barked loudly, chasing after the playful squirrels in the park.", "quality": 1},
    {"sentence": "I enjoyed the concert last night. The music was fantastic!", "quality": 1},
    {"sentence": "The movie theater was packed, and the film received a standing ovation at the end.", "quality": 1},
    {"sentence": "The food at the new restaurant was exquisite, bursting with flavors.", "quality": 1},
    {"sentence": "The novel I read was captivating, and I couldn't put it down until I finished it.", "quality": 1},
    {"sentence": "The traffic jam was unbearable, making me late for work.", "quality": -1},
    {"sentence": "The service at the restaurant was terrible. I waited over an hour for my food.", "quality": -1},
    {"sentence": "The movie I watched last night was boring. I fell asleep halfway through.", "quality": -1},
    {"sentence": "The book I picked up was poorly written, with no engaging plot.", "quality": -1},
    {"sentence": "The rainstorm flooded the streets, causing chaos and delays.", "quality": -1},
    {"sentence": "The children's playground was dirty and poorly maintained.", "quality": -1},
    {"sentence": "DATA 233 is a wonderful class and I really like it because I have always love computing data.", "quality": 1},
{"sentence": "The product is exceptionally durable and long-lasting.", "quality": 1},
    {"sentence": "Their customer service is responsive and helpful.", "quality": 1},
    {"sentence": "The design is innovative and user-friendly.", "quality": 1},
    {"sentence": "The company's reputation for quality is outstanding.", "quality": 1},
    {"sentence": "The price is reasonable for the value provided.", "quality": 0},
    {"sentence": "The craftsmanship is top-notch and meticulous.", "quality": 1},
    {"sentence": "The material used is of superior quality.", "quality": 1},
    {"sentence": "The performance exceeds expectations.", "quality": 1},
    {"sentence": "The brand is synonymous with excellence.", "quality": 1},
    {"sentence": "The reliability of the product is commendable.", "quality": 1},
    {"sentence": "The accuracy of the information provided is impressive.", "quality": 1},
    {"sentence": "The efficiency of the service is remarkable.", "quality": 1},
    {"sentence": "The packaging is well-designed and secure.", "quality": 1},
    {"sentence": "The functionality of the product is flawless.", "quality": 1},
    {"sentence": "The experience of using the product/service is seamless.", "quality": 1},
    {"sentence": "The taste of the food is exquisite.", "quality": 1},
    {"sentence": "The comfort provided is unparalleled.", "quality": 1},
    {"sentence": "The speed of delivery is swift and punctual.", "quality": 1},
    {"sentence": "The support offered is comprehensive and thorough.", "quality": 1},
    {"sentence": "The technology utilized is cutting-edge.", "quality": 1},
    {"sentence": "The cleanliness of the facility is impeccable.", "quality": 1},
    {"sentence": "The presentation of the product is elegant and refined.", "quality": 1},
    {"sentence": "The ease of use is exceptional.", "quality": 1},
    {"sentence": "The variety of options available is extensive.", "quality": 1},
    {"sentence": "The professionalism of the staff is exemplary.", "quality": 1},
    {"sentence": "The safety measures in place are thorough and effective.", "quality": 1},
    {"sentence": "The ambiance of the environment is inviting.", "quality": 1},
    {"sentence": "The customization options are diverse and flexible.", "quality": 1},
    {"sentence": "The accuracy of the measurements is precise.", "quality": 1},
    {"sentence": "The flavor profile is rich and satisfying.", "quality": 1},
    {"sentence": "The energy efficiency of the appliance is commendable.", "quality": 1},
    {"sentence": "The transparency in pricing is appreciated.", "quality": 1},
    {"sentence": "The accessibility of the service is convenient.", "quality": 1},
    {"sentence": "The user interface is intuitive and user-friendly.", "quality": 1},
    {"sentence": "The warranty offered is generous and reliable.", "quality": 1},
    {"sentence": "The freshness of the ingredients is evident.", "quality": 1},
    {"sentence": "The adaptability of the product is impressive.", "quality": 1},
    {"sentence": "The educational content provided is informative and engaging.", "quality": 1},
    {"sentence": "The aesthetics of the design are pleasing.", "quality": 1},
    {"sentence": "The sound quality is crisp and clear.", "quality": 1},
    {"sentence": "The environmental sustainability practices are commendable.", "quality": 1},
    {"sentence": "The nutritional value of the food is high.", "quality": 1},
    {"sentence": "The response time is quick and efficient.", "quality": 1},
    {"sentence": "The scent of the product is pleasant.", "quality": 1},
    {"sentence": "The style of the product is trendy and fashionable.", "quality": 1},
    {"sentence": "The instructions provided are clear and concise.", "quality": 1},
    {"sentence": "The warranty coverage is extensive.", "quality": 1},
    {"sentence": "The level of customer care is exceptional.", "quality": 1},
    {"sentence": "The speed of service is impressive.", "quality": 1},
    {"sentence": "The accuracy of the product description is high.", "quality": 1},
    {"sentence": "The design aesthetics are modern and sleek.", "quality": 1},
    {"sentence": "The product's longevity is commendable.", "quality": 1},
    {"sentence": "The efficiency of the manufacturing process is high.", "quality": 1},
    {"sentence": "The nutritional information provided is accurate.", "quality": 1},
    {"sentence": "The user experience is smooth and enjoyable.", "quality": 1},
    {"sentence": "The product's versatility is impressive.", "quality": 1},
    {"sentence": "The quality control measures are stringent.", "quality": 1},
    {"sentence": "The reliability of the service is commendable.", "quality": 1},
    {"sentence": "The convenience of the product is appreciated.", "quality": 1},
    {"sentence": "The aesthetic appeal is attractive.", "quality": 1},
    {"sentence": "The responsiveness of the customer support is commendable.", "quality": 1},
    {"sentence": "The flavor profile is diverse and satisfying.", "quality": 1},
    {"sentence": "The sound quality is clear and crisp.", "quality": 1},
    {"sentence": "The environmental sustainability practices are commendable.", "quality": 1},
    {"sentence": "The nutritional value of the food is high.", "quality": 1},
    {"sentence": "The breathtaking view from the top of the mountain left me speechless.", "quality": 1},
    {"sentence": "The puppy wagged its tail happily as it played with its favorite toy.", "quality": 1},
    {"sentence": "The delicious aroma of freshly baked cookies filled the kitchen.", "quality": 1},
    {"sentence": "The lecture was informative, but it felt a bit too long.", "quality": 0},
    {"sentence": "The new painting in the gallery caught everyone's attention with its vibrant colors.", "quality": 1},
    {"sentence": "The traffic on the highway was moving smoothly, with no delays in sight.", "quality": 0},
    {"sentence": "The performance at the theater received rave reviews from critics.", "quality": 1},
    {"sentence": "The quiet, peaceful atmosphere of the countryside was a welcome change from the city.", "quality": 1},
    {"sentence": "The coffee shop was cozy and inviting, perfect for a relaxing afternoon.", "quality": 1},
    {"sentence": "The rainy weather put a damper on our outdoor plans.", "quality": -1},
    {"sentence": "The abandoned house looked spooky, with broken windows and overgrown weeds.", "quality": -1},
    {"sentence": "The traffic jam stretched for miles, causing frustration among commuters.", "quality": -1},
    {"sentence": "The movie was predictable and lacked depth.", "quality": -1},
    {"sentence": "The restaurant served bland food with poor presentation.", "quality": -1},
    {"sentence": "The rainy weather put a damper on our outdoor plans.", "quality": -1},
    {"sentence": "The abandoned house looked spooky, with broken windows and overgrown weeds.", "quality": -1},
    {"sentence": "The traffic jam was unbearable, making me late for work.", "quality": -1},
    {"sentence": "The service at the restaurant was terrible. I waited over an hour for my food.", "quality": -1},
    {"sentence": "The movie I watched last night was boring. I fell asleep halfway through.", "quality": -1},
    {"sentence": "The book I picked up was poorly written, with no engaging plot.", "quality": -1},
    {"sentence": "The rainstorm flooded the streets, causing chaos and delays.", "quality": -1},
    {"sentence": "The children's playground was dirty and poorly maintained.", "quality": -1},
    {"sentence": "The abandoned factory was eerie, with shadows dancing in the moonlight.", "quality": -1},
    {"sentence": "The abandoned shipwreck on the beach was a haunting reminder of the past.", "quality": -1},
    {"sentence": "The traffic on the highway was moving smoothly, with no delays in sight.", "quality": 0},
    {"sentence": "The lecture was informative, but it felt a bit too long.", "quality": 0},
    {"sentence": "The company's new product received mixed reviews from consumers.", "quality": 0},
    {"sentence": "The hike through the forest was challenging but rewarding, with stunning views along the way.", "quality": 1},
    {"sentence": "The exam was difficult, but I managed to pass with flying colors.", "quality": 1},
    {"sentence": "The ocean waves crashed against the shore, creating a soothing sound.", "quality": 1},
    {"sentence": "The museum exhibit featured a diverse collection of artwork from around the world.", "quality": 1},
    {"sentence": "The conversation with my friend was enlightening, and I learned a lot from it.", "quality": 1},
    {"sentence": "The city skyline at night was a breathtaking sight, with twinkling lights as far as the eye could see.", "quality": 1},
    {"sentence": "The soccer game was intense, with both teams giving it their all until the very end.", "quality": 1},
    {"sentence": "The snowfall blanketed the city in white, creating a picturesque scene.", "quality": 1},
    {"sentence": "The dance performance was mesmerizing, with graceful movements and intricate choreography.", "quality": 1},
    {"sentence": "The road trip was long but enjoyable, with plenty of stops along the way to take in the scenery.", "quality": 1},
    {"sentence": "The birthday party was a huge success, with laughter and joy filling the air.", "quality": 1},
    {"sentence": "The intricate design of the cathedral's stained glass windows was truly remarkable.", "quality": 1},
    {"sentence": "The train arrived at the station right on time, much to the relief of the waiting passengers.", "quality": 1},
    {"sentence": "The new painting in the gallery caught everyone's attention with its vibrant colors.", "quality": 1},
    {"sentence": "The performance at the theater received rave reviews from critics.", "quality": 1},
    {"sentence": "The quiet, peaceful atmosphere of the countryside was a welcome change from the city.", "quality": 1},
    {"sentence": "The coffee shop was cozy and inviting, perfect for a relaxing afternoon.", "quality": 1},
    {"sentence": "The soccer game was intense, with both teams giving it their all until the very end.", "quality": 1},
    {"sentence": "The abandoned house looked spooky, with broken windows and overgrown weeds.", "quality": -1},
    {"sentence": "The abandoned factory was eerie, with shadows dancing in the moonlight.", "quality": -1},
    {"sentence": "The abandoned shipwreck on the beach was a haunting reminder of the past.", "quality": -1},
    {"sentence": "The traffic on the highway was moving smoothly, with no delays in sight.", "quality": 0},
    {"sentence": "The lecture was informative, but it felt a bit too long.", "quality": 0},
    {"sentence": "The company's new product received mixed reviews from consumers.", "quality": 0},
    {"sentence": "The hike through the forest was challenging but rewarding, with stunning views along the way.", "quality": 1},
    {"sentence": "The exam was difficult, but I managed to pass with flying colors.", "quality": 1},
    {"sentence": "The ocean waves crashed against the shore, creating a soothing sound.", "quality": 1},
    {"sentence": "The museum exhibit featured a diverse collection of artwork from around the world.", "quality": 1},
    {"sentence": "The conversation with my friend was enlightening, and I learned a lot from it.", "quality": 1},
    {"sentence": "The city skyline at night was a breathtaking sight, with twinkling lights as far as the eye could see.","quality": 1},
    {"sentence": "The soccer game was intense, with both teams giving it their all until the very end.", "quality": 1},
    {"sentence": "The snowfall blanketed the city in white, creating a picturesque scene.", "quality": 1},
    {"sentence": "The dance performance was mesmerizing, with graceful movements and intricate choreography.", "quality": 1},
    {"sentence": "The road trip was long but enjoyable, with plenty of stops along the way to take in the scenery.", "quality": 1},
    {"sentence": "The birthday party was a huge success, with laughter and joy filling the air.", "quality": 1},
    {"sentence": "The intricate design of the cathedral's stained glass windows was truly remarkable.", "quality": 1},
    {"sentence": "The train arrived at the station right on time, much to the relief of the waiting passengers.", "quality": 1},
    {"sentence": "The new painting in the gallery caught everyone's attention with its vibrant colors.", "quality": 1},
    {"sentence": "The performance at the theater received rave reviews from critics.", "quality": 1},
    {"sentence": "The quiet, peaceful atmosphere of the countryside was a welcome change from the city.", "quality": 1},
    {"sentence": "The coffee shop was cozy and inviting, perfect for a relaxing afternoon.", "quality": 1},
    {"sentence": "The soccer game was intense, with both teams giving it their all until the very end.", "quality": 1}
]
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class kNNsentenceQuality():
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.kNN_model = KNeighborsClassifier(n_neighbors=3)

    def trainkNN(self, X_train, y_train):
        X_train_transformed = self.vectorizer.fit_transform(X_train)
        y_train = np.array(y_train)
        self.kNN_model.fit(X_train_transformed, y_train)

    def Quality_kNN(self, sentences):
        X_test_transformed = self.vectorizer.transform(sentences)
        predictions = self.kNN_model.predict(X_test_transformed)
        return predictions


sentences = [data['sentence'] for data in dataset]
labels = [data['quality'] for data in dataset]

X_train, X_test, y_train, y_test = train_test_split(sentences, labels, test_size=0.1, random_state=42)

# Initialize kNNsentenceQuality object
obj = kNNsentenceQuality()
obj.trainkNN(X_train, y_train)

new_sentences = ["The sunrise over the mountains was a breathtaking sight to behold.",
                 "The movie was not as good as I expected.",
                 "DATA 233 is a wonderful class and I really like it because I have always love computing data."]
quality = obj.Quality_kNN(new_sentences)
print("Predicted Quality:", quality)
