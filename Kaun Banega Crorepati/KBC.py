# --- WELCOME TO KAUN BANEGA CROREPATI ---

# List of all questions, options, and correct answers
Questions=[['Which of these vehicles in India usually has only 3 wheels?','motorbike','Bus','truck','auto rickshaw','d'],
           ['which of the following contains both letters and numbers?','Aadhaar uid','mobile number','Pin Code','Pan','d'],
           ['Which word will come in the blank space in “Ab pachtay hote kya, jab _____ chug gayi khet”?','Cat','Squirrel','Bird','Spider','c'],
           ['Which of these clothes is worn on the upper part of your body?','Lungi','dhoti','salwar','shirt','d'],
           ['Whose signature will be seen on the Indian currency note of 500 rupees?','Vice President','RBI Governor','Finance Minister','Chief Minister','b'],
           ['The Chief Minister of Punjab, Bhagwant Mann was earlier famous for which of these professions?','pilot','policeman','comedian','chef','c'],
           ['In which city is the ISRO Headquarters, Antriksh Bhavan located?','Bangalore','Hyderabad','New Delhi','Thiruvananthapuram','a'],
           ['In the Mahabharata, who appointed Karna as the king of Anga?','Arjun','Duryodhana','Sri Krishna','Dhritarashtra','b'],
           ['The Western Ghats does not pass through which of these states?','Goa','Tamil Nadu','West Bengal','Gujarat','c'],
           ['Every year in the month of December, Tansen Samaroh is organized in which district?','Ajmer','Jodhpur','Gwalior','Indore','c'],
           ['Renowned artist Sudarshan Patnaik is famous for his artworks made of which material?','Fruit','marble','Sand','Rice','c'],
           ['In the 1930s, which of the following was the name of a series of conferences organized by the British to discuss reforms in India?','round table','boardroom','square table','Triangular','a'],
           ['Which sport is seen in the logo of Odisha Tourism, which has a deep connection with Odisha?','Cricket','Field hockey','Football','Wrestling','b'],
           ['Which was the first mountain peak above 8,000 metres in height, to be summited by humans?','Annapurna','Lhotse','Kangchenjunga','Makalu','a'],
           ['Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?','Cathay Cinema Hall','Fort Canning Park ','National University of Singapore','National Gallery of Singapore','a'],
           ['What was the title of the thesis that Dr B R Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?','The wants and Means of India ','The Problem of the Rupee','National Dividend of India',' The Law and Lawyers','b'],
           ['Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk? ','Asanga','Nagasena ','Mahadharmarakshita ','Dharmaraksita','b']]

# List of prize money corresponding to each question level
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]
money=0
Wrong_answer=True

# Loop through each question
for i in range(len(Questions)):
    while True:
        # Display the current question and options
        print(f'''Question for Rs.{levels[i]} is:
              {Questions[i][0]}\n''')
        print(f'''          Give answer in range(a-d) or press q to quit.    
              a. {Questions[i][1]}         b. {Questions[i][2]}
              c. {Questions[i][3]}         d. {Questions[i][4]}\n''')
        j=input()
        # Validate if the user input is within the expected range
        if j not in ['a','b','c','d','q']:
            print("Enter valid option from range(a-d) or press q to quit")
            continue
        # If correct answer
        if(j==Questions[i][-1]):
            print(f"Hurray you won {levels[i]}\n")
            money=levels[i]
            # If the user wins the final prize
            if(money==70000000):
                print("Congratulations You Won The Game")
            break  
        # If player chooses to quit        
        elif(j=='q'):
            print(f'Congratulations you won {levels[i-1]}')
            break
         # If wrong answer given
        else:
            # Provide minimum guaranteed prize money based on level
            if (money>=10000 and money<320000):
                print('Better luck next time you Won Rs.10000')
                Wrong_answer=False
            elif (money>=320000):
                print('Better luck next time you Won Rs.320000')
                Wrong_answer=False
            else:
                print('Better luck next time you Won Rs.0')
                Wrong_answer=False
            break 
    # Check if player chose to quit or answered incorrectly    
    if j=='q':
        break 
    elif (Wrong_answer==False):
        break
# Game End Message
print("The Game Ends")