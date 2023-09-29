while True:
    midScore = int(input("Midterm score: "))
    finalScore = int(input("Final score: "))
    projectPoint = int(input("Project points: "))
    
    if midScore > 40 or finalScore > 40 or projectPoint > 20:
        print("Error: Over points.")
        break
    else:
        total = midScore+finalScore+projectPoint
        if total >= 90:
            grade = "A"
        elif total >= 80:
            grade = "B"
        elif total >= 70:
            grade = "C"
        elif total >= 60:
            grade = "D"
        else:
            grade = "F"
            
    print(f"Total score: {total} point")
    print(f"You got grade: {grade}.")

    continued = str(input("Do you want to continue?, press 'y' to continue or 'n' to stop: "))
    if continued == "y":
        pass
    else:
        exit()