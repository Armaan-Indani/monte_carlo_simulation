import numpy as np

# Define conditional probabilities
P_Aptitude = 0.8
P_Coding = 0.5
P_Good_Grades_given_Aptitude_Coding = {
    (True, True): 0.9,
    (True, False): 0.7,
    (False, True): 0.6,
    (False, False): 0.3,
}
P_Job_given_Good_grades = {True: 0.8, False: 0.2}
P_Startup_given_Good_grades = {True: 0.7, False: 0.3}


# Monte Carlo Simulation
def monte_carlo_simulation(num_samples=10000):
    count_aptitude = 0
    count_coding = 0

    count_good_grades = 0
    count_good_grades_and_aptitude = 0
    count_good_grades_and_coding = 0
    count_good_grades_and_aptitude_and_coding = 0
    count_job = 0
    count_job_and_good_grades = 0
    count_startup = 0
    count_startup_and_good_grades = 0

    count_job_and_aptitude = 0
    count_job_and_coding = 0
    count_startup_and_aptitude = 0
    count_startup_and_coding = 0

    for i in range(num_samples):
        # Sample aptitude
        aptitude = np.random.rand() < P_Aptitude

        # Sample coding skills
        coding = np.random.rand() < P_Coding

        # Sample good grades given the apt and coding
        good_grades = (
            np.random.rand() < P_Good_Grades_given_Aptitude_Coding[(aptitude, coding)]
        )

        # Sample job given grades
        job = np.random.rand() < P_Job_given_Good_grades[good_grades]

        # Sample startup given grades
        startup = np.random.rand() < P_Startup_given_Good_grades[good_grades]

        # Accumuate the counts
        if aptitude:
            count_aptitude += 1
            if good_grades:
                count_good_grades_and_aptitude += 1
            if job:
                count_job_and_aptitude += 1
            if startup:
                count_startup_and_aptitude += 1

        if coding:
            count_coding += 1
            if good_grades:
                count_good_grades_and_coding += 1
            if job:
                count_job_and_coding += 1
            if startup:
                count_startup_and_coding += 1

        if aptitude and coding and good_grades:
            count_good_grades_and_aptitude_and_coding += 1

        if good_grades:
            count_good_grades += 1

            if job:
                count_job_and_good_grades += 1

            if startup:
                count_startup_and_good_grades += 1

        if job:
            count_job += 1

        if startup:
            count_startup += 1

    # Probabilities:
    print("P(Good grades = True) =", count_good_grades / num_samples)
    print("P(Job = True) =", count_job / num_samples)
    print("P(Startup = True) =", count_startup / num_samples)
    print()
    if(count_good_grades > 0):
        print("P(Aptitude = True | Good_grades = True) =", count_good_grades_and_aptitude / count_good_grades)
        print("P(Coding = True | Good_grades = True) =", count_good_grades_and_coding / count_good_grades)
    else:
        print("P(Aptitude = True | Good_grades = True) =", 0)
        print("P(Coding = True | Good_grades = True) =", 0)
    print()

    if(count_job > 0):
        print("P(Good_grades = True | Job = True) =", count_job_and_good_grades / count_job)
    else:
        print("P(Good_grades = True | Job = True) =", 0)
    
    if(count_startup > 0):
        print("P(Good_grades = True | Startup = True) =", count_startup_and_good_grades / count_startup)
    else:
        print("P(Good_grades = True | Startup = True) =", 0)
    print()

    if(count_job > 0):
        print("P(Aptitude = True | Job = True) =", count_job_and_aptitude / count_job)
        print("P(Coding = True | Job = True) =", count_job_and_coding / count_job)
    else:
        print("P(Aptitude = True | Job = True) =", 0)
        print("P(Coding = True | Job = True) =", 0)
        
    if(count_startup > 0):
        print("P(Aptitude = True | Startup = True) =", count_startup_and_aptitude / count_startup)
        print("P(Coding = True | Startup = True) =", count_startup_and_coding / count_startup)
    else:
        print("P(Aptitude = True | Startup = True) =", 0)
        print("P(Coding = True | Startup = True) =", 0)
    print()
    print("---")

monte_carlo_simulation(1)
monte_carlo_simulation(10)
monte_carlo_simulation(100)
monte_carlo_simulation(1000)
monte_carlo_simulation(10000)
monte_carlo_simulation(100000)
