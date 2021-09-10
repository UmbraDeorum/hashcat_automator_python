#!/usr/bin/python3

'''
This is a python program aiming to automate the dehashing process regarding multiple hashes of the same type, all originating from 
a single text file. The program retrieves each password at a one-at-a-time basis, attempts dehashing, and terminates each attempt should
it exceed an optional, user-determined deadline.

All the successfuly dehashed passwords are saved in a single outfile, in a new location provided by the user.

This program is designed as an out-of-the-box solution, and no alterations to the original code are required to achieve the 
aimed functionality.

Nonetheless, any alterations aiming to tweak/improve execution, or to achieve any fundamentally different functionality are totally
permitted, as long as the original gets its respectful credit.

Happy dehashing!

Made by UmbraDeorum.

'''
import os
import subprocess
import multiprocessing

dehashed = []
n = 0

def exiting(dehashed, n):
    if n!=0 and dehashed!=[]:
        print("\n\nProcess completed or terminated by user.")
        percentage = 100*len(dehashed)/n
        print(f"Succesfully dehashed {len(dehashed)} ({percentage}%) password hashes!")
        if percentage > 50:
            print("Well done! Same luck next time!\n\n")
        else:
            print("Bye!\n\n")
    else:
        print('\n\nProgram was terminated before it could make any progress.\nBye!\n\n')
try:

    def dehashing(hash_type, hash, words, ruleset):
        subprocess.run(f'hashcat --force --status -O -o cracked.tmp -a 0 -m {hash_type} {hash} {words} -r {ruleset}', shell=True)

    file_loc = str(input("Insert the location of the file containing the hashes: ")).strip()
    my_file = open(file_loc, "r")
    hash_list = my_file.readlines() # Generate list of hashes from provided file
    hash_type = str(input("Insert the proper hash type code to pass to hashcat: ")).strip()
    words = str(input("Insert the location of the wordlist you want to use: ")).strip()
    ruleset = str(input("Insert the location of the .rule you want to use: ")).strip()
    timer = int(input("Insert the time limit (seconds) per hash. \"0\" stands for no time limit: "))
    outfile = str(input("Insert the location of the outfile: ")).strip()

    for hash in hash_list:
        n+=1
        hash = hash.replace("\n","") # Generate ready-to-crack hash

        if __name__ == '__main__':
            proc = multiprocessing.Process(target=dehashing, name='dehashing', args=(hash_type, hash, words, ruleset,))
            # Initiate new dehashing attempt
            proc.start()
            # Wait maximum requested seconds per hash
            if timer!=0:
                proc.join(timer)
            else:
                proc.join()
            # Then terminate dehashing
            if proc.is_alive():
                print('Attempt exceeded the 15 minute deadline. Killing...')
                proc.terminate()
                # Cleanup after kill
                proc.join()
                subprocess.run('pkill hashcat', shell=True)

        if os.path.isfile('./cracked.tmp'): 		    # If file exists, then dehashing attempt was successful
            dehash = subprocess.check_output('cat cracked.tmp') # Retrieve cracked hash
            dehashed.append(dehash) 			    # Save in the dehashed passowrds' list
            os.system('rm cracked.tmp')			    # Remove latest dehashed password
            if os.path.isfile(outfile):	 		    # Check if outfile already exists
                os.system(f'rm {outfile}')		    # Remove if True

       	# By recreating the outfile after each successful attempt, the user can interrupt the program at any time without losing progress.

            with open(outfile, 'w') as f:
                for dehash in dehashed:
                    f.write("%s\n" % dehash)		    # Generate new oufile
    exiting(dehashed, n)

# Prapared for the case of user interrupting the program

except KeyboardInterrupt:
    exiting(dehashed, n)
