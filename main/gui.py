import PySimpleGUI as sg
from bitarray import bitarray

import algorithm as al
import fileops

MODE = "e"
INPUT = "k"

sg.theme('Dark')

col1_a = [[sg.Radio("Input from keyboard", "source", key='kb', enable_events=True, default=True)],
          [sg.Radio("Input from file", "source", key='file', enable_events=True)]]

col1_b = [[sg.Radio("Encryption", "mode", key='en', enable_events=True, default=True)],
          [sg.Radio("Decryption", "mode", key='de', enable_events=True)]]

col1_d = [[sg.Text('Generated key 1:'), sg.Text(key='key1_text')],
          [sg.Text('Generated key 2:'), sg.Text(key='key2_text')],
          [sg.Text('Generated key 3:'), sg.Text(key='key3_text')]]

col1_c = [[sg.Radio("Generate random keys", "keych", key='random', enable_events=True)],
          [sg.Radio("Enter custom keys (8 ascii characters long)", "keych", key='custom', enable_events=True, default=True)]]

col1 = [[sg.Text('Choose source type:'), sg.Column(col1_a)],
        [sg.Text('Choose mode:'), sg.Column(col1_b)],
        [sg.Text("Keys:"), sg.Column(col1_c)]]

col2 = [[sg.Text("Mode: Encryption", key='mode_message')],
        [sg.Text('Enter key 1:', key="key1_text"), sg.InputText(size=(None, 50), key='key1_box')],
        [sg.Text('Enter key 2:', key="key2_text"), sg.InputText(size=(None, 50), key='key2_box')],
        [sg.Text('Enter key 3:', key="key3_text"), sg.InputText(size=(None, 50), key='key3_box')],
        [sg.HSeparator()],
        [sg.Text('Enter input text:', key='input_text'), sg.InputText(key='input_value')],
        [sg.Text('', key='result_message')],
        [sg.Text('Result:', key='output_text'), sg.InputText(key='output_value')],
        [sg.Button('Process')]]

layout = [[sg.Text('Triple DES encryption and decryption')],
          [sg.Column(col1), sg.VSeparator(), sg.Column(col2)],
          [sg.Button('Exit')]]

window = sg.Window('Cryptography', layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "kb":
        window.Element('input_text').update(value='Enter input text:')
        window.Element('output_text').update(value='Result:')
        INPUT = "k"
    if event == "file":
        window.Element('input_text').update(value='Enter input file path:')
        window.Element('output_text').update(value='Enter output file path:')
        input_file_path = values['input_value']
        output_file_path = values['output_value']
        INPUT = "f"
    if event == "en":
        window.Element('mode_message').update(value='Mode: Encryption')
        MODE = 'e'
    if event == "de":
        window.Element('mode_message').update(value='Mode: Decryption')
        MODE = 'd'
    if event == "random":
        window.Element('key1_text').update(value='Generated key 1:')
        window.Element('key2_text').update(value='Generated key 2:')
        window.Element('key3_text').update(value='Generated key 3:')
        keys = al.random_keys()
        window.Element('key1_box').update(value=keys[0])
        window.Element('key2_box').update(value=keys[1])
        window.Element('key3_box').update(value=keys[2])
    if event == "custom":
        window.Element('key1_text').update(value='Enter key 1:')
        window.Element('key2_text').update(value='Enter key 2:')
        window.Element('key3_text').update(value='Enter key 3:')
        window.Element('key1_box').update(value="")
        window.Element('key2_box').update(value="")
        window.Element('key3_box').update(value="")
    if event == "Process":
        input_box = values['input_value']
        output_box = values['output_value']
        keys = list()
        for i in range(3):
            keys.append(values['key'+str(i+1)+'_box'])

        print(keys)
        if INPUT == 'f':
            if MODE == 'e':
                fileops.encode_from_file(input_box, output_box, keys)
            else:
                fileops.decode_from_file(input_box, output_box, keys)
        else:
            if MODE == 'e':
                processed = al.triple_des_encryption(input_box, keys[0], keys[1], keys[2]).to01()
                #processed = al.triple_des_encryption("1 2 3 4 5 6 7 8", keys[0], keys[1], keys[2]).to01()

            else:
                processed = al.triple_des_decryption(bitarray(input_box), keys[0], keys[1], keys[2])
            window.Element('output_value').update(value=processed)


window.close()
