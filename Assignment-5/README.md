# Maths for Machine Learning
**Author:** Velayutham Augustheesan  
**Date:** [Add date here]

## Overview
This assignment covers probability, statistics, and Python programming applications. The tasks include theoretical probability calculations, normal and exponential distributions, Bayesian inference, binomial distributions, and practical Python implementations such as triangular distributions, random number generation, image blending, and linear algebra computations.

---

## Problem Coverage
- **Problems 7, 12, 13, 14, 15** are covered in the notebook: `assignment_05_velayutham_augustheesan_maths.ipynb`.
- **Problems 1, 2, 3, 4, 5, 6, 8, 9, 10, 11** are covered in the Word file: `assignment_05_velayutham_augustheesan_maths`.

---

## Problem Descriptions

### **Problem 1: Network Collision Probability**
- **Scenario:** 10 devices share a channel; each attempts to send with 20% probability.  
- **Goal:** Find the probability that there is **no collision** in a given time slot.

### **Problem 2: Password Probability**
- **Scenario:** 8-character password using `[a-z, A-Z, 0-9]` with repetition allowed.  
- **Goal:** Probability that the password contains **at least one digit**.

### **Problem 3: Software Bug Probabilities**
- **Scenario:** Module A and B have probabilities of bugs: P(A)=0.15, P(B)=0.10, P(A∩B)=0.03.  
- **Goal:** 
  - (a) P(A|B)  
  - (b) P(B|Aᶜ)

### **Problem 4: Robot Sensor Bayes Theorem**
- **Scenario:** Sensor detects obstacles with 95% true positive and 2% false positive; obstacles present 10% of time.  
- **Goal:** Probability obstacle is truly present given the sensor triggers.

### **Problem 5: Spam Detection**
- **Scenario:** Spam probability 10%, "money" keyword appears 80% in spam, 5% in non-spam.  
- **Goal:** Probability that an email is spam given it contains "money".

### **Problem 6: Rare Disease Diagnosis**
- **Scenario:** Disease prevalence 1/10,000, test has 99% true positive and 0.5% false positive.  
- **Goal:** Probability a person actually has the disease given a positive test.

### **Problem 7: Microchip Defects (Binomial Distribution)**
- **Scenario:** 500 chips, defect probability 0.02, sample of 20 with replacement.  
- **Goal:** 
  - (a) Probability exactly 3 defects  
  - (b) Probability at least 2 defects

### **Problem 8: Exponential Failure Time**
- **Scenario:** Component failure time ~ Exp(λ) with mean 500 hours.  
- **Goal:** 
  - (a) Probability it lasts 400–600 hours  
  - (b) Probability it lasts another 250 hours after 300 hours

### **Problem 9: Sensor Noise (Normal Distribution)**
- **Scenario:** Noise ~ N(0, 0.5).  
- **Goal:** 
  - (a) P(-0.2 ≤ X ≤ 0.3)  
  - (b) Probability reading is an "outlier" (>1.5σ)

### **Problem 10: Network Latency**
- **Scenario:** Latency ~ N(μ=150, σ=20 ms).  
- **Goal:** 
  - (a) P(X>180 ms)  
  - (b) Latency threshold for 90% of packets  
  - (c) Probability of critical latency (>2.5σ)

### **Problem 11: Component Lifespan**
- **Scenario:** Lifespan ~ N(μ=2500, σ=300).  
- **Goal:** 
  - (a) Percentage ≥2000 hours  
  - (b) Warranty period such that 1% fail before it  
  - (c) Expected components between 2200–2800 hours in batch of 10,000

### **Problem 12: Triangular Distribution Class**
- **Goal:** Implement `TriangularDistribution` class with methods:  
  - `pdf(x)`  
  - `cdf(x)`  
  - `plot_pdf()`  
  - `plot_cdf()`  
  - `get_probability(x1, x2)`  
- **Requirement:** Handle edge cases `a=c` or `b=c` gracefully.

### **Problem 13: Random Number Generation**
- **Goal:** Implement `rand7()` using only `rand5()`, ensuring uniform probability.

### **Problem 14: Image Blending**
- **Scenario:** Two 10×10 grayscale images.  
- **Goal:** Implement `blend_images(image_A, image_B, weight_A, weight_B)` for weighted average blending, keeping pixel values in [0, 255].

### **Problem 15: Eigenvalues and Eigenvectors**
- **Goal:** Compute eigenvalues and eigenvectors of given matrices using `numpy.linalg.eig`.

---

## Python Modules and Libraries Used
- `numpy` – numerical computations, linear algebra, random numbers  
- `scipy.stats` – binomial, normal, exponential distributions  
- `matplotlib.pyplot` – plotting PDF and CDF, image visualization  

---

## Notes
- All probability problems assume **independence** where applicable.  
- Bayes’ theorem and conditional probability were applied in Problems 4–6.  
- Code includes **error handling**, **type hints**, and **edge case considerations**.  
- Triangular and uniform random number problems demonstrate custom class and algorithm implementation.  

---

## How to Run
1. Open the notebook `assignment_05_velayutham_augustheesan_maths.ipynb` in **Google Colab** or **Jupyter Notebook**.  
2. Run cells sequentially to observe outputs.  
3. Plots will be displayed inline.  
4. The Word file `assignment_05_velayutham_augustheesan_maths` contains solutions and explanations for theoretical problems.

---

## Author
**Velayutham Augustheesan**