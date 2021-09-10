# hashcat_automator_python

This is a python program aiming to automate the dehashing process regarding multiple hashes of the same type, all originating from 
a single text file. The program retrieves each password at a one-at-a-time basis, attempts dehashing, and terminates each attempt should
it exceed an optional, user-determined deadline.

1. Requests the location of the file containing the hashes (1-hash-per-line format).
2. Requests the proper hash type code to pass to hashcat (try hashcat --help).
3. Requests the location of the wordlist to use.
4. Requests the location of the .rule to use. (Optional)
5. Requests the time-limit per hash. (Optional)
6. Requests the location to create the new outfile.

All the successfuly dehashed passwords are saved in a single outfile, in a new location provided by the user.

This program is designed as an out-of-the-box solution, and no alterations to the original code are required to achieve the 
aimed functionality.

Nonetheless, any alterations aiming to tweak/improve execution, or to achieve any fundamentally different functionality are totally
permitted, as long as the original gets proper mention.

Happy dehashing!

Made by UmbraDeorum.
