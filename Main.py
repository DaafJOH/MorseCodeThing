import tkinter, random, random_word

MORSE = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----",
}

ALPHABET = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

class MainWindow:
    def __init__(self, master) -> None:
        self.MainTitle = tkinter.Label(master, text="Learn Morse code!")
        self.MainTitle.pack()
        self.AlphabetButton = tkinter.Button(master, text="Learn the alphabet", command=self.Alphabet)
        self.AlphabetButton.pack()
        self.DecodeButton = tkinter.Button(master, text="Learn to decode", command=self.Decode)
        self.DecodeButton.pack()
        self.EncodeButton = tkinter.Button(master, text="Learn to encode", command=self.Encode)
        self.EncodeButton.pack()

    def Alphabet(self):
        self.Aroot = tkinter.Tk()
        self.AWindow = AlphabetWindow(self.Aroot)

    def Decode(self):
        self.Droot = tkinter.Tk()
        self.DWindow = DecodeWindow(self.Droot)

    def Encode(self):
        pass

class AlphabetWindow:
    def __init__(self, master) -> None:
        self.MainTitle = tkinter.Label(master, text="Learn the alphabet")
        self.MainTitle.pack()
        self.QuestionLabel = tkinter.Label(master, text="", font=("Arial", 48))
        self.QuestionLabel.pack()
        self.AwnserLabel = tkinter.Label(master, text="", font=("Arial", 24))
        self.AwnserLabel.pack()
        self.SubmitButton = tkinter.Button(master, text="Awnser", command=self.Awnser)
        self.SubmitButton.pack()
        self.SwitchButton = tkinter.Button(master, text="Encode", command=self.Switch)
        self.SwitchButton.pack()

        self.Encode = True
        self.AwnserButton = True

        self.MakeLetter()

    def MakeLetter(self):
        self.Letter = random.choice(ALPHABET)
        if self.Encode: self.QuestionLabel.config(text=self.Letter)
        else: self.QuestionLabel.config(text=MORSE[self.Letter])

    def Awnser(self):
        if self.AwnserButton:
            if self.Encode: self.AwnserLabel.config(text=MORSE[self.Letter])
            else: self.AwnserLabel.config(text=self.Letter)
            self.SubmitButton.config(text="Next")
            self.AwnserButton = False
        else:
            self.MakeLetter()
            self.AwnserLabel.config(text="")
            self.AwnserButton = True
            self.SubmitButton.config(text="Awnser")

    def Switch(self):
        self.Encode = not self.Encode
        if self.Encode: self.SwitchButton.config(text="Encode")
        else: self.SwitchButton.config(text="Decode")
        self.MakeLetter()
        self.AwnserButton = True

class DecodeWindow:
    def __init__(self, master) -> None:
        self.MainTitle = tkinter.Label(master, text="Learn to decode")
        self.MainTitle.pack()
        self.PlayButton = tkinter.Button(master, text="Play", command=self.Play)
        self.PlayButton.pack()
        self.AwnserLabel = tkinter.Label(master, text="")
        self.AwnserLabel.pack()
        self.AwnserButton = tkinter.Button(master, text="Awnser", command=self.Awnser)
        self.AwnserButton.pack()
        self.SpeedLabel = tkinter.Label(master, text="Playback speed in DPS")
        self.SpeedLabel.pack()
        self.SpeedSlider = tkinter.Scale(master, from_=1, to=15, orient=tkinter.HORIZONTAL)
        self.SpeedSlider.pack()
        self.LengthLabel = tkinter.Label(master, text="Word length")
        self.LengthLabel.pack()
        self.LengthSlider = tkinter.Scale(master, from_=3, to=10, orient=tkinter.HORIZONTAL)
        self.LengthSlider.pack()

        self.WORDS = random_word.RandomWords()

    def MakeWord(self, length):
        self.Word = self.WORDS.get_random_word(minLength=length, maxLength=length)
        print(self.Word)

    def Play(self):
        pass

    def Awnser(self):
        self.MakeWord(5)

root = tkinter.Tk()
Window = MainWindow(root)
root.mainloop()