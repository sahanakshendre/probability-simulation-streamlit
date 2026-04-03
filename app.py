import streamlit as st
import random
import matplotlib.pyplot as plt

st.title("🎲 Probability Simulator App")

# Select experiment
experiment = st.selectbox("Choose Experiment", ["Coin Toss", "Dice Roll"])

# Number of trials
trials = st.slider("Number of Trials", 10, 1000, 100)

results = []

# Simulation
if st.button("Run Simulation"):

    if experiment == "Coin Toss":
        for _ in range(trials):
            results.append(random.choice(["Heads", "Tails"]))

        labels = ["Heads", "Tails"]
        counts = [results.count("Heads"), results.count("Tails")]

        theoretical = [0.5, 0.5]

    else:
        for _ in range(trials):
            results.append(random.randint(1, 6))

        labels = [1, 2, 3, 4, 5, 6]
        counts = [results.count(i) for i in labels]

        theoretical = [1/6] * 6

    # Show results
    st.write("### Frequency")
    for l, c in zip(labels, counts):
        st.write(f"{l}: {c}")

    # Experimental probability
    st.write("### Experimental Probability")
    exp_prob = [c / trials for c in counts]

    for l, p in zip(labels, exp_prob):
        st.write(f"{l}: {p:.2f}")

    # Theoretical probability
    st.write("### Theoretical Probability")
    for l, t in zip(labels, theoretical):
        st.write(f"{l}: {t:.2f}")

    # Graph
    st.write("### 📊 Visualization")

    fig, ax = plt.subplots()
    ax.bar([str(i) for i in labels], exp_prob)
    st.pyplot(fig)