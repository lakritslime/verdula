#!/usr/bin/env python3
import os

def createfolders(cwd):
	# check if folders exist and create folders
	odds_path = os.path.join(cwd, 'odds')
	evens_path = os.path.join(cwd, 'evens')

	displaymsg = ''
	if not os.path.exists(odds_path):
		os.mkdir(odds_path)
	else:
		displaymsg += getuserinput('odds')

	if not os.path.exists(evens_path):
		os.mkdir(evens_path)
	else:
		displaymsg += getuserinput('evens')

	return displaymsg, odds_path, evens_path


def getuserinput(foldername):
	msg = ''
	while True:
		response = input("There is already a folder called '{}' in the current directory. Do you want to use it? :".format(foldername))		
		if response == 'y':
			break
		elif response == 'n':
			msg = "You have to rename the existing folder '{}' and then run the script again \n".format(foldername)
			break
		else:
			print("Your have to answer 'y' or 'n' \n")
			continue

	return msg


def movefiles():
	# get current working directory
	cwd = os.getcwd()

	# create directories
	message, odds, evens = createfolders(cwd)

	if message:
		print(message)

	if not message:
		# declare variables
		existsmsg = "A file with the name '{}' already exists in the folder '{}' so this file can't be moved."
		movedmsg = "File '{}' successfully moved."
		files_not_moved = []
		count_even = 0
		count_odd = 0

		# loop through directory
		for file in os.listdir(cwd):
			if os.path.isfile(os.path.join(cwd, file)):
				# import pdb; pdb.set_trace()
				filename, ending = file.split('.')
				lastdigit = filename[-1]

				if lastdigit.isdigit(): 

					# even numbers
					if int(lastdigit) % 2 == 0: 
						source = os.path.join(cwd, file)
						destination = os.path.join(evens, file)
						try:
							os.rename(source, destination)
							count_even += 1
							print(movedmsg.format(file))
						except FileExistsError:
							print(existsmsg.format(file, evens))
							files_not_moved.append(file)

					# odd numbers
					else:
						source = os.path.join(cwd, file)
						destination = os.path.join(odds, file)
						try:
							os.rename(source, destination)
							count_odd += 1
							print(movedmsg.format(file))
						except FileExistsError:
							print(existsmsg.format(file, odds))
							files_not_moved.append(file)


	return count_even, count_odd, files_not_moved

if __name__ == '__main__':
   
	even_count, odd_count, non_moved_list = movefiles()
	print("***** SUMMARY *****")
	print('{} files were moved to the evens-folder.'.format(even_count))
	print('{} files were moved to the odds-folder.'.format(odd_count))
	if len(non_moved_list) > 0:
		print('The following files could not be moved: ')
		for file in non_moved_list:
			print(file)