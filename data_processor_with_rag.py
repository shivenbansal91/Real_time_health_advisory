import pandas as pd
import json
import time

def load_knowledge_base(file_name="knowledge_base.json"):
    """
    Load the knowledge base containing health tips.
    """
    with open(file_name, "r") as file:
        return json.load(file)

def generate_recommendation(row, knowledge_base):
    """
    Generate a recommendation based on health metrics using the knowledge base.
    """
    if row["heart_rate"] > 140:
        return knowledge_base["high_heart_rate"]
    elif row["spo2"] < 95:
        return knowledge_base["low_spo2"]
    elif row["steps"] > 10000:
        return knowledge_base["high_steps"]
    else:
        return knowledge_base["normal"]

def process_data(input_file="health_data.csv", output_file="processed_health_data.csv"):
    """
    Processes health data in real-time and generates RAG-based recommendations.
    """
    # Load the knowledge base
    knowledge_base = load_knowledge_base()

    # Initialize the output file with headers if it doesn't exist
    pd.DataFrame(columns=["timestamp", "heart_rate", "steps", "spo2", "calories", "recommendation"]).to_csv(output_file, index=False)

    last_row = 0  # Track the last processed row

    while True:
        try:
            # Load the input data
            data = pd.read_csv(input_file)

            # Process only new rows
            if len(data) > last_row:
                new_data = data.iloc[last_row:]

                # Add recommendations using RAG
                new_data["recommendation"] = new_data.apply(lambda row: generate_recommendation(row, knowledge_base), axis=1)

                # Append processed rows to the output file
                new_data.to_csv(output_file, mode="a", header=False, index=False)
                print(f"Processed {len(new_data)} new rows.")

                # Update the last processed row
                last_row = len(data)
            else:
                print("No new data found. Waiting for updates...")
                break

            time.sleep(2)  # Wait before rechecking for new data

        except FileNotFoundError:
            print(f"Input file '{input_file}' not found. Please ensure it exists.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    process_data()
