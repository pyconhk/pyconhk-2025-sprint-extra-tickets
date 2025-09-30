# PyCon HK 2025 Sprint Day - The Ticket Challenge 🎟️

Welcome, developer! We're excited you're interested in joining our **Sprint Day at PyCon HK 2025**. Due to overwhelming demand, our initial tickets are gone. However, we've reserved a special batch for those who can demonstrate their Python prowess by solving this challenge.

This isn't just a challenge—it's **your ticket** to the event. By solving the puzzle and submitting a valid "ticket signature" and create a Pull Request, you'll prove your skills and secure your place in line for a spot at the Sprints.

The tickets will be distributed to those **who successfully get their solutions merged into the repository**. The earlier you submit, the better your chances of getting a ticket!

---

## 🚀 The Mission: Forge Your Ticket

Your mission is to create a valid ticket signature with the provided `registration.py` script. The script requires you to input your **Order ID** (please never input your **ticket id**!) from Eventbrite, and a private key path (which you will need to find the password to unzip the `locked_key.zip`!) to generate a Base64-encoded signature.

This signature is your "proof-of-work," and submitting it correctly is how you claim your spot.

## 🏁 How to Play: A Step-by-Step Guide

### Step 1: Fork the Repository

At the top-right of this page on GitHub, click the **"Fork"** button. This will create a personal copy of this repository under your own GitHub account.

![Fork Button Location](https://docs.github.com/assets/cb-13835/images/help/repository/fork-button.png)

### Step 2: Clone Your Fork

Now, clone **your forked repository** (not the original one) to your local machine.

```bash
# Replace <YOUR_GITHUB_USERNAME> with your actual username
git clone https://github.com/<your github username>/pyconhk-2025-sprint-extra-tickets.git
cd pyconhk-2025-sprint-extra-tickets
```

### Step 3: Install Dependencies

Make sure you have Python 3.8+ installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### Step 4: Find the Password in our Discord Channel

Join our [Discord channel](https://bit.ly/pyconhk) and look for the `#sprint` channel. The password to unzip the `locked_key.zip` file is hidden somewhere in the channel. It might be in a pinned message, a bot message, or even a reply to another message.

Once you find the password, unzip the file:

```bash
unzip locked_key.zip
```

Or if you are on Windows, just right-click the file and select "Extract All...".

### Step 5: Solve the Puzzle

Now, it's time to solve the puzzle and generate your ticket signature.

Run the `registration.py` script with your **Order ID** (not your Ticket ID!) and the path to the private key you just extracted.

```bash
python registration.py --order-id <your order id> --key-path <path/to/private_key.pem>
```

> For example: `python registration.py --order-id 13298822263 --key-path ./private_key.pem`

**Important:** Please never ever share your **ticket id** to anyone, including in your PR. Once it is leaked, you risk losing your ticket.

---

## 🚩 How to Claim Your Sprint Day Ticket

Submission is done by opening a Pull Request (PR).

1.  **Create a New Branch:**
    ```bash
    git checkout -b submission/<your order id>
    ```

    > For example, if your order ID is `13298822263`, your branch name should be `submission/13298822263`.

2.  **Commit and Push:**
    ```bash
    git add tickets/
    git commit -m "Claim sprint ticket: <your order id>"
    git push -u origin submission/<your order id>
    ```

3.  **Open a Pull Request** on GitHub to the `main` branch. An automated system will immediately check your signature.

*   A **green checkmark ✅** means your submission is valid and you've reserved your spot **in the queue**! Please note that you are **guaranteed a ticket only if your PR is merged**.

*   A **red cross ❌** means the verification failed. Close the PR, debug your solution, and try again.

**Tickets are allocated on a first-come, first-served basis for valid PRs. Good luck, and we can't wait to see you at the Sprints!**
