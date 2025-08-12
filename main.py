questions = [
    ["Which language was used in making Facebook?", "Python", "French", "Javascript", "Java", 4],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Who is known as the father of the computer?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Which gas do plants absorb from the atmosphere?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["Who wrote the Indian national anthem?", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Mahatma Gandhi", "Sarojini Naidu", 1],
    ["What is the largest ocean in the world?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["In which year did India gain independence?", "1942", "1945", "1947", "1950", 3],
    ["Which is the smallest prime number?", "1", "2", "3", "5", 2],
    ["Who is known as the Missile Man of India?", "Dr. A.P.J. Abdul Kalam", "Vikram Sarabhai", "Homi Bhabha", "Rakesh Sharma", 1],
    ["Which is the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 2]
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0

for i in range(len(questions)):
    question = questions[i]
    print(f"\nQuestion for ₹{levels[i]}")
    print(question[0])
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}")
    
    ans = int(input("Enter the Answer (1-4): "))
    
    if ans == question[-1]:
        print(f"✅ Correct answer! You have won ₹{levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
        elif i < 4:
            money = levels[i]
        elif 4 < i < 9:
            money = levels[i]
    else:
        print(f"❌ Wrong Answer! You take home ₹{money}")
        break

else:
    print(f"🎉 Congratulations! You have completed the game and won ₹{levels[-1]}")
