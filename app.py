import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
@st.cache
def load_data():
    # Assuming you have your cluster data in a CSV or DataFrame
    data = pd.read_csv('/content/customer_segmentation_with_clusters.csv')
    return data

# Main app code
def main():
    st.title("Customer Segmentation Interpretation")

    # Load dataset
    df = load_data()

    # Show the dataframe to the user
    st.subheader("Cluster Data")
    st.write(df)

    # Show insights for each cluster
    st.subheader("Cluster Interpretation")

    # Write interpretation based on the average values you have
    cluster_interpretations = {
        0: "Older customers with medium income & moderate spending. Might be retired or in a stable phase of life.",
        1: "High-income, mid-aged customers who spend a lot. Likely professionals with premium shopping preferences.",
        2: "Young, low-income, but impulsive spenders. Likely students or entry-level workers.",
        3: "Young adults with balanced income and moderate spending habits. Likely in the early stages of their careers.",
        4: "Older, high-income customers who spend very little. Likely careful buyers or minimalists."
    }

    # Display interpretation for each cluster
    for cluster, interpretation in cluster_interpretations.items():
        st.write(f"**Cluster {cluster}:** {interpretation}")

    # Scatter plot to visualize clusters
    st.subheader("Cluster Visualization")
    fig, ax = plt.subplots()  # Create a figure and axis
    sns.scatterplot(x='Age', y='Annual Income (k$)', hue='Cluster', data=df, palette='Set2', ax=ax)
    ax.set_title("Customer Segments by Age vs. Income")
    st.pyplot(fig)  # Pass the figure object

    # Another plot for Spending Score
    st.subheader("Spending Score Visualization")
    fig, ax = plt.subplots()  # Create a new figure and axis
    sns.scatterplot(x='Age', y='Spending Score (1-100)', hue='Cluster', data=df, palette='Set2', ax=ax)
    ax.set_title("Customer Segments by Age vs. Spending Score")
    st.pyplot(fig)  # Pass the figure object

if __name__ == "__main__":
    main()
