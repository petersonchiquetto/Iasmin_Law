# 🚀 Mini Project RAG - IAsmim_Jur

Welcome to the **Mini Project RAG - IAsmim_Jur**! This project uses **RAG (Retrieval-Augmented Generation)** with an **LLM (Large Language Model)** for semantic queries in the legal domain, based on the **Brazilian Federal Constitution**. 🧑‍⚖️📜

## 🧙‍♀️ Features

1. 🔍 **Intelligent Semantic Search**: Accurate responses based on relevant sections of the Constitution.
2. 🧹 **Text Splitting and Processing**:
   - Splits the Constitution into optimized chunks.
   - Semantic embeddings for personalized queries.
3. 📚 **Vector Memory Database**:
   - Efficient indexing for rapid information retrieval.

---

## 🛠️ Prerequisites

⚠️ Before starting, ensure the dependencies are installed:

- **Python 3.8+**
- 📦 Libraries:
  - `mrpt` ➡️ Fast nearest neighbor search
  - `vectordb2` ➡️ Vector storage and retrieval
  - `langchain` ➡️ Framework for LLM integration
  - `tf-keras` ➡️ TensorFlow < 2.16

🔧 **Installation**:
```bash
pip install git+https://github.com/vioshyvo/mrpt/
pip install vectordb2
pip install langchain
pip install --upgrade tf-keras
```

---

## 🏰 Application Architecture

### 🔢 **Data Flow**

1. **Data Collection** 🖥️:
   - The text of the Brazilian Federal Constitution is downloaded directly from a public repository [GitHub - Constitution](https://github.com/abjur/constituicao).

2. **Text Splitting and Embeddings** 🔨:
   - The text is divided into **chunks** based on the structure of chapters and subsections.
   - Embeddings are generated using a language model, enabling semantic vector representation.

3. **Indexing in Vector Memory Database** 📂:
   - Indexing uses a vector database like **Vectordb**, storing chunks with their metadata (chapter, source, etc.).

4. **Semantic Search** 🌐:
   - Users perform natural language queries.
   - The system executes a similarity search on the embeddings and returns the **top 5 most relevant results**.

### 🌐 **Core Components**

- **Data Input**: Text of the Brazilian Federal Constitution.
- **Preprocessing**:
  - Chunking (configurable size and overlap).
  - Conversion of chunks to embeddings.
- **Indexing**:
  - Vector database for efficient storage and retrieval.
- **Query and Response**:
  - Similarity search to find the most relevant chunks.

---

## 🔗 How to Use

1. **Fetch the Data**:
   The script automatically downloads the text of the Federal Constitution.

2. **Configure Text Splitting**:
   Adjust the chunk size and overlap:
   ```python
   chunk_size = 20
   chunk_overlap = 3
   ```

3. **Run Queries**:
   Test with questions like:
   ```python
   memory.search('social security rights', top_n=5)
   ```

4. 🔧 **Result**:
   The system returns the most relevant sections of the Constitution!

---

## 🎉 Extra Features

- 🔄 **Customization**: Easily adjust chunk size and search strategies.
- ⚡ **Fast and Efficient**: Built with state-of-the-art similarity search algorithms.

---

## 🤝 Contributions

💡 Have ideas for improvements? Contributions are welcome! Open an issue or submit a pull request.


<br>
This repository makes use of Local Assistant Examples as a foundational resource for implementing localized AI assistant functionalities: https://github.com/vioshyvo/mrpt/
