# hashcat_automator_python

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
