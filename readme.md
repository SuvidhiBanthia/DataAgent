**Documentation**
=========================

**1\. Project Overview**
------------------------

This project focuses on analyzing consumer reviews and comments from multiple platforms (Amazon, Reddit, YouTube) to extract meaningful insights about skincare products. The primary objectives are:

*   **Filtering Data** : Extract relevant data based on user-defined filters.
    
*   **Theme Extraction** : Identify broad themes of conversation around specific topics

*   **Schema Mapping** : Generate standardized mappings for platform-specific schemas.
    
*   **Output Generation** : Save filtered data and extracted themes into structured JSON files.
    

The project leverages NLP techniques, including **TF-IDF vectorization** and **K-Means clustering** , to process and analyze textual data.

**2\. Data Description**
------------------------

### **2.1 Data Sources**

The dataset consists of reviews, comments, and metadata from three platforms:

1.  **Amazon Reviews** :
    
    *   Contains product reviews with attributes like **content**, **review\_star\_rating**, **user\_info**, and **product\_details**.
        
    *   Example: Reviews for skincare products like cleansers, moisturizers, and sunscreens.
        
2.  **Reddit Posts** :
    
    *   Includes discussions and comments from subreddits related to skincare.
        
    *   Example: Threads discussing skincare routines, product recommendations, and concerns.
        
3.  **YouTube Comments** :
    
    *   Contains comments from skincare-related videos.
        
    *   Example: Feedback on skincare product recommendations or tutorials.
        

### **2.2 Data Fields**

Each record in the dataset contains the following key fields:

*   **content** : Textual content of the review or comment.
    
*   **review\_star\_rating** : Rating given by the user (e.g., 1 to 5 stars).
    
*   **user\_info** : Demographic information such as **age\_group**, **gender**, and **income\_band**.
    
*   **product\_details** : Metadata about the product, including title, price, and category.
    

**3\. Implementation**
------------------------------

### **3.1 Modules**

The project is divided into the following modules:

#### **3.1.1 Selection (selection.py)**

*   **Purpose** : Filters the dataset based on user-defined criteria.
    
*   **Key Functionality** :
    
    *   **filter\_data(data, filters)**: Filters records that match the specified conditions (e.g., **review\_star\_rating=5**).
        

#### **3.1.2 Projection (projection.py)**

*   **Purpose** : Projects only the relevant fields from the filtered data.
    
*   **Key Functionality** :
    
    *   **project\_data(filtered\_data, fields)**: Extracts specific fields (e.g., **content**, **review\_star\_rating**) from the filtered records.
        

#### **3.1.3 Transformation (transformation.py)**

*   **Purpose** : Performs advanced transformations like theme extraction and schema mapping.
    
*   **Key Functionality** :
    
    *   **extract\_themes(data, topic)**:
        
        *   Uses **TF-IDF vectorization** and **K-Means clustering** to finally extract top keywords from each cluster to form coherent themes.
            
    *   **generate\_mapping(platform\_schema)**:
        
        *   Generates standardized schema mappings using the Hugging Face API.
            

#### **3.1.4 Output (output.py)**

*   **Purpose** : Writes the processed data and extracted themes to JSON files.
    
*   **Key Functionality** :
    
    *   **write\_output(data, filename)**: Saves the output data to a JSON file.
        

### **3.2 Workflow**

1.  **Input Data** : Load the dataset (**assignment\_sample\_data.json**) containing reviews, comments, and metadata.
        
2.  **Filter Data** : Apply user-defined filters (e.g., **review\_star\_rating=5**, **user\_info.age\_group=25-34**).
        
3.  **Project Relevant Fields** : Extract only the necessary fields (e.g., **content**, **review\_star\_rating**, **user\_info**).
        
4.  **Extract Themes** : Identify broad themes of conversation for a given topic (e.g., "skin").
        
5.  **Generate Schema Mapping** : Create a standardized schema mapping for platform-specific fields.
        
6.  **Save Output** : Write the filtered data and extracted themes to JSON files (**filtered\_output.json**, **themes\_output.json**).
        

**4\. Usage Instructions**
--------------------------

### **4.1 Prerequisites**

*   Python 3.x
    
*   Install required libraries: pip install -r requirements.txt 

### **4.2 Running the Script**

1.  Place the dataset (**assignment\_sample\_data.json**) in the project directory.
    
2.  Run the script: python src/main.py
    
3.  Follow the prompts (Specify whether to apply filters and/or extract themes).
        

### **4.3 Output Files**

*   **Filtered Data** : Saved as **filtered\_output.json**.
    
*   **Themes** : Saved as **themes\_output.json**.
    

**5\. Improvements**
---------------------------

1.  Can use Sentence Transformers for better semantic embeddings and integrate BERT-based models for more accurate theme labeling.
        
2.  Scalability : Optimize the code to handle larger datasets efficiently.
        

**7\. Known Limitations**
-------------------------

1.  **Static Number of Clusters** : The number of clusters (**num\_clusters**) is fixed and may need tuning for different datasets.

2. **Projection fields** : pre-defined currently, can be dynamic based on input.
        
3. **Query Analysis** : Allow user to enter natural language queries and interpret relevant filters from that to filter data.
