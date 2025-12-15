# Distributed-System-Assignement
This repository contains a Source Code for Distributed System assignment .
# Server–Client Matrix Multiplication (Distributed Systems)

This project implements a **server–client architecture** to perform matrix multiplication using Python socket programming.  
The client sends two matrices to the server, the server performs the multiplication, and the result is sent back to the client.

This project demonstrates fundamental **distributed systems concepts** such as network communication, task offloading, and centralized computation.

---

## 👨‍🎓 Group Members
  
- **Akhrang Boro** – Roll No: 220710007010  
- **Devasish Rabha** – Roll No: 220710007022  
- **Guthal Basumatary** – Roll No: 220710007026  

---

## 🎯 Objective

To implement a client–server model where computationally intensive matrix multiplication is performed on the server, reducing client-side load and demonstrating distributed computation.

---

## 🏗️ System Architecture

- **Client**
  - Generates two square matrices
  - Sends matrices to the server over TCP
  - Receives the resulting matrix

- **Server**
  - Listens for client connections
  - Receives matrices
  - Performs matrix multiplication using NumPy
  - Sends the result back to the client

---

## 🛠️ Technologies Used

- Python 3
- NumPy
- TCP Socket Programming
- VS Code
- Git & GitHub

---
