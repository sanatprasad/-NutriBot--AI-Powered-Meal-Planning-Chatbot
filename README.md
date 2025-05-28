# Mealify: Your Personalized Meal Planning Assistant

Mealify is a serverless chatbot application built on AWS that simplifies meal planning by creating personalized 7-day meal plans tailored to your dietary preferences and goals. Harnessing the capabilities of AWS services, Mealify provides an efficient and convenient solution for planning your meals.

![Meal-Planner](https://github.com/Divyam-Pandit/AWS-Projects/assets/100858214/4d4d0ebb-0a2f-4fd3-8db7-5430cd87698a)

## Features

* **Conversational Interface:** Interact with Mealify through an intuitive chatbot built with AWS Lex. Simply convey your preferences and goals, and Mealify will generate a personalized meal plan just for you.
* **Personalized Meal Plans:** Receive 7 days of delicious and nutritious meals based on your dietary needs and restrictions (e.g., vegan, vegetarian, gluten-free).
* **Flexible and Scalable:** Mealify's serverless architecture ensures scalability and reliability, capable of handling any number of users.
* **Cloud-based and Secure:** All data is securely stored on the AWS cloud, ensuring protection and accessibility.

## Technology Stack

* **AWS Lex:** Chatbot platform for building conversational interfaces.
* **AWS S3:** Static website hosting for the Mealify interface.
* **Kommunicate:** Chat widget integration for a seamless user experience.
* **AWS Bedrock:** Powerful tool for generating personalized meal plans.
* **AWS Lambda:** Serverless function for data manipulation and communication between Lex and Bedrock.
* **CloudWatch Logs:** Monitoring and troubleshooting for the Lambda function.

## How it Works

1. **Interact with the Mealify chatbot:** Share your dietary preferences and goals.
2. **AWS Lex collects user input:** Passes the information to the Lambda function.
3. **Lambda function fetches data from Lex:** Prepares and sends it to AWS Bedrock.
4. **AWS Bedrock generates meal plan:** Creates a 7-day plan based on user input.
5. **Lambda function receives meal plan:** Formats and returns it to Lex.
6. **Mealify chatbot presents the plan:** Displays the personalized meal plan to the user.

## Getting Started

1. Visit the Mealify website and access the chatbot.
2. Answer the chatbot's questions about your dietary preferences and goals.
3. Once you submit your information, Mealify will generate a personalized 7-day meal plan.
4. Enjoy delicious and nutritious meals tailored just for you!

## Future Developments

* Integration with external food delivery services.
* Expansion to additional languages and dietary options.
* Personalized recipe recommendations.

## About Mealify

This project is a demonstration of the power of serverless architecture and cloud services to create innovative and user-friendly applications. We believe that Mealify can help people make healthy and informed choices about their meals, promoting a better and more balanced lifestyle.
