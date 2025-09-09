import streamlit as st
from collections import Counter
import heapq
import matplotlib.pyplot as plt


# Huffman Coding solver
def huffman_coding_solver():
    st.write("Huffman Coding Algorithm")

    # Input: Get the text from the user
    text = st.text_area("Enter the text to encode and decode", "example text")

    if st.button("Encode and Decode"):
        # Generate Huffman Tree and codes
        huffman_tree, huffman_codes = huffman_encoding(text)
        encoded_text = ''.join([huffman_codes[char] for char in text])

        st.write(f"Huffman Codes: {huffman_codes}")
        st.write(f"Encoded Text: {encoded_text}")

        # Decode the encoded text
        decoded_text = huffman_decoding(encoded_text, huffman_tree)
        st.write(f"Decoded Text: {decoded_text}")

        # Visualize Huffman Tree
        st.write("Huffman Tree Visualization")
        visualize_huffman_tree(huffman_tree)


# Build Huffman Tree and generate codes
def huffman_encoding(text):
    # Frequency dictionary for characters
    frequency = Counter(text)

    # Create a priority queue (min-heap) to store the Huffman tree nodes
    heap = [[weight, [char, ""]] for char, weight in frequency.items()]
    heapq.heapify(heap)

    # Build the Huffman Tree
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_tree = heap[0]

    # Generate Huffman codes
    huffman_codes = {char: code for char, code in huffman_tree[1:]}

    return huffman_tree, huffman_codes


# Decode the encoded text
def huffman_decoding(encoded_text, huffman_tree):
    huffman_dict = {code: char for char, code in huffman_tree[1:]}

    decoded_text = ''
    current_code = ''

    for bit in encoded_text:
        current_code += bit
        if current_code in huffman_dict:
            decoded_text += huffman_dict[current_code]
            current_code = ''

    return decoded_text


# Visualize Huffman Tree
def visualize_huffman_tree(huffman_tree):
    labels = {}
    for node in huffman_tree[1:]:
        labels[node[0]] = node[1]

    # Plot tree as a dictionary (for simplicity)
    fig, ax = plt.subplots()
    ax.bar(labels.keys(), [len(code) for code in labels.values()], color='skyblue')
    ax.set_ylabel("Code Length")
    ax.set_title("Huffman Codes Length by Character")
    st.pyplot(fig)
