# Getting Started With Machine Learning

## Why machine learning and how it works?
- Machine learning is a subfield of artificial intelligence that involves the development of algorithms and statistical models that enable computers to learn and improve from experience without being explicitly programmed. The primary goal of machine learning is to develop models that can automatically analyze large amounts of data, identify patterns, and make predictions or decisions based on the data. Machine learning is used in a wide range of applications, including image recognition, natural language processing, recommendation systems, fraud detection, and autonomous vehicles.

- Machine learning works by training models on data, typically through a process called supervised learning, unsupervised learning, or reinforcement learning. In supervised learning, the model is trained on labeled data, where the correct answers are already known. The model then learns to generalize from the training data to make predictions on new, unseen data. In unsupervised learning, the model is trained on unlabeled data, and the goal is to identify patterns or clusters within the data. Reinforcement learning involves the use of rewards and punishments to train a model to make decisions and take actions that maximize its cumulative reward over time. Once a machine learning model is trained, it can be used to make predictions or decisions on new, unseen data. The model's performance can be evaluated using various metrics, such as accuracy, precision, recall, and F1 score, to determine how well it generalizes to new data.

## Where do we use machine learning?

Machine learning is used in a wide range of applications in different industries. Some of the common areas where machine learning is used include:

- Image and speech recognition: Machine learning is used in image and speech recognition applications, such as face recognition, object detection, and speech-to-text conversion.

- Natural Language Processing (NLP): Machine learning is used in NLP applications, such as sentiment analysis, language translation, chatbots, and voice assistants.

- Fraud detection: Machine learning is used to detect fraudulent activities in financial transactions, such as credit card fraud, insurance fraud, and identity theft.

- Recommendation systems: Machine learning is used in recommendation systems, such as those used by e-commerce websites, music and movie streaming services, and social media platforms, to suggest products or content based on a user's preferences.

- Healthcare: Machine learning is used in healthcare applications, such as disease diagnosis, drug discovery, and medical image analysis.

- Autonomous vehicles: Machine learning is used in autonomous vehicle technology, such as self-driving cars, to analyze sensor data and make real-time decisions.

- Predictive maintenance: Machine learning is used in predictive maintenance applications, such as detecting equipment failures before they occur, reducing downtime and maintenance costs.

These are just a few examples of the many applications of machine learning in different industries. As the technology advances, we can expect to see even more innovative use cases for machine learning in the future.

## Categorization of Machine Learning algorithms

### Supervised Learning
- In this algorithm there is a dependent variable which needs to be calculated using independent variables.
- Repititive training process untill desired accuracy is achieved

### Unsupervised Learning
- We don't have target or estimation to be predicted
- Used for clustering into various groups
- No definite output, instead focus is on categorization

### Reinforcement Learning
- Take specific decision based on situation
- Usually the machine is exposed to an unknown environment and it learns from there. This contnuous approach is like humans, trial and error.
- Machine learns from experience, hopefully best knowledge and apply that in business logics

## Preprocessing Steps:

- Creation of Independent and Dependent Matric
```
# Basic practice to keep Indepent matrix in X (capital)
X = df.iloc[:,:-1].values
```
```
# Basic practice to keep depent matrix in y (small)
y = df.iloc[:, 3].values
```

- Handling null values (Either by removing NaN records or filling it with mean, median, etc)
```
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.NaN, strategy="mean")
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
```

- Handling Categorical data (e.g. Yes, No)
```
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

column_transformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
X = np.array(column_transformer.fit_transform(X), dtype = np.float64)

```

- Preparing Training and Test dataset
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

- Feature scaling (if required) Data may be required to be scaled in order to handle large data difference
```
from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()

X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)
```

## Machine Learning Algorithms

### Linear regression

- Training the model
```
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
```

- Prediction using the model
```
predictor = regressor.predict(X_test)
```

- Analysing the predictions
```
plt.scatter(X_train, y_train, label="Original Dataset", color="blue")
plt.plot(X_train, regressor.predict(X_train), label="Predictions", color="red")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Linear regression analysis")
plt.legend()
```


