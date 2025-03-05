import json
from selection import filter_data
from projection import project_data
from transformation import generate_mapping, extract_themes
from output import write_output

def main():
    # Load the input data with UTF-8 encoding
    with open("assignment_sample_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # User inputs
    use_filters = input("Do you want to apply filters? (yes/no): ").strip().lower() == "yes"
    extract_themes_flag = input("Do you want to extract themes of conversation? (yes/no): ").strip().lower() == "yes"

    if use_filters:
        # Example filters
        #filters = {"review_star_rating": "4"}
        #filters = {"user_info.age_group": "25-34", "review_star_rating": "4"}
        #filters = {"content": "Nice"}

        filters_input = input("Enter filters as key=value pairs separated by commas (e.g., review_star_rating=4,user_info.age_group=25-34): ")
        filters = {pair.split("=")[0].strip(): pair.split("=")[1].strip() for pair in filters_input.split(",") if "=" in pair}

        # Filter data
        filtered_data = filter_data(data, filters)

        # Project relevant fields
        fields = ["content", "review_star_rating", "user_info"]
        projected_data = project_data(filtered_data, fields)
        
        # Generate standardized schema mapping
        platform_schema = "Amazon: review_star_rating -> rating; Reddit: karma -> upvotes"
        mapping = generate_mapping(platform_schema)

        # Write filtered output to a file
        write_output({"filtered_data": projected_data, "schema_mapping": mapping}, "filtered_output.json")
        print("Filtered data and schema mapping saved to 'filtered_output.json'.")

    if extract_themes_flag:
        # Topic for theme extraction
        topic = input("Enter the topic for theme extraction (e.g., 'skin', 'hair'): ").strip()

        # Extract themes
        themes = extract_themes(data, topic)

        # Save themes to a file
        write_output({"themes": themes}, "themes_output.json")
        print("Themes of conversation saved to 'themes_output.json'.")

if __name__ == "__main__":
    main()