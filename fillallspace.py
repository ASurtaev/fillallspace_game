import PySimpleGUI as sg
import gameplay as gameplay

def mainMenu():
	sg.theme('Purple')
	levels_pool = [str(i) for i in range(1, 31)]

	main_layout = [[sg.Button(str(i), size = (2, 2)) for i in range(row, row+10)] for row in range(1,30,10)]
	main_layout.append([sg.Button('Exit', size = (85,2))])

	main_window = sg.Window('Fill All Space!', main_layout)

	while True:
		event, values = main_window.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		if event in levels_pool:
			gameplay.startLevel(int(event))

	main_window.close()	

if __name__=='__main__':
	mainMenu()