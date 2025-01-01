from flask import Flask, render_template, request, jsonify
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Data storage
location_counts = {}
category_counts = {}

# Function to update counts
def update_counts(selected_location, selected_category):
    global location_counts, category_counts
    if selected_location:
        location_counts[selected_location] = location_counts.get(selected_location, 0) + 1
    if selected_category:
        category_counts[selected_category] = category_counts.get(selected_category, 0) + 1

# Route for the chatbot page
@app.route("/")
def index():
    return render_template("index.html")

# API route for chatbot communication
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"response": "I didn't understand that. Can you clarify?"})

    # Bot's logic
    if "event" in user_message.lower():
        response = "Here are some event categories:\n1. Music\n2. Sports\n3. Tech\n4. Art\n5. Food\nEnter the number of the event you're interested in:"
    elif user_message.isdigit():
        categories = ["Music", "Sports", "Tech", "Art", "Food"]
        selected_category = categories[int(user_message) - 1] if int(user_message) <= len(categories) else None
        if selected_category:
            update_counts("Sample Location", selected_category)  # Update counts with sample location
            response = f"You selected {selected_category}. Thank you!"
        else:
            response = "Invalid selection. Please enter a number between 1 and 5."
    else:
        response = "I'm here to help you find events! Mention 'event' to start."

    return jsonify({"response": response})

# Route to generate graphs
@app.route("/graphs", methods=["GET"])
def generate_graphs():
    global location_counts, category_counts

    # Top 5 locations graph
    locations = sorted(location_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    loc_names, loc_values = zip(*locations) if locations else ([], [])
    plt.bar(loc_names, loc_values, color="skyblue")
    plt.title("Top 5 Searched Locations")
    plt.xlabel("Location")
    plt.ylabel("Count")
    plt.savefig("static/location_graph.png")
    plt.close()

    # Top 5 categories graph
    categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    cat_names, cat_values = zip(*categories) if categories else ([], [])
    plt.bar(cat_names, cat_values, color="orange")
    plt.title("Top 5 Searched Categories")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("static/category_graph.png")
    plt.close()

    return jsonify({"message": "Graphs updated successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
