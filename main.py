import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

# 1. Load dataset
df = pd.read_excel("career_dataset_fixed.xlsx")

# 2. Add the clustering logic (Mapping Sub-categories to Main Categories)
def get_main_category(career):
    c = str(career).lower()
    if "ai " in c or "artificial intelligence" in c: return "Artificial Intelligence"
    if "ios" in c or "android" in c or "mobile" in c: return "Mobile App Development"
    if "cloud" in c or "aws" in c: return "Cloud Computing"
    if "cyber" in c or "security" in c: return "Cybersecurity"
    if "data" in c or "analytics" in c: return "Data Science & Analytics"
    if "devops" in c: return "DevOps"
    if "ui" in c or "ux" in c or "design" in c: return "UI/UX Design"
    if "backend" in c or "java" in c: return "Backend Development"
    if "frontend" in c or "web" in c: return "Web Development"
    return "Other"

# Generate the cluster column
df['Main_Category'] = df['Career'].apply(get_main_category)

# 3. Inputs and outputs (Target y is now the cluster, not the specific sub-career)
X = df["Skill"]
y = df["Main_Category"] 

# 4. Convert skills into numbers
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X.astype(str))

# 5. Create and Train model
model = KNeighborsClassifier(n_neighbors=5, weights='distance')
model.fit(X_vectorized, y)

print("Model Trained Successfully on Main Categories!\n")

# 6. User input
user_skill = input("Enter your skills (e.g., Python, Cloud, Mobile): ")
user_vector = vectorizer.transform([user_skill.lower()])

# 7. Predict
prediction = model.predict(user_vector)

predicted_career = prediction[0]

print("\nRecommended Main Career Category:")
print(predicted_career)

# Get careers belonging to predicted category
matching_careers = df[
    df["Career"].apply(
        lambda x: get_main_category(x) == predicted_career
    )
]["Career"].unique()

# Best role
best_role = matching_careers[0]

print("\nBest Role:")
print(best_role)

suggested_roles = []

for role in matching_careers:
    if role != best_role:
        suggested_roles.append(role)

print("\nSuggested Roles:")

for role in suggested_roles[:4]:
    print(role)