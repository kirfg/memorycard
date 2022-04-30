from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel,QVBoxLayout, QMessageBox,QHBoxLayout,QRadioButton,QGroupBox,QButtonGroup
from random import shuffle, randint
class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3  


question_list=[]
q1 = Question('Государственный язык Португалии', 'Португальский', 'Английский', 'Испанский', 'Французкий')
q= Question('почему в росии холодно', 'да', 'нет','возможно','хочу')
q2 = Question('кто такой Кузко', 'император', 'лорд злыдень', 'тут и там', 'да')

question_list.append(q)
question_list.append(q1)
question_list.append(q2)
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.move(900,70)
main_win.resize(400,200)

question = QLabel('Какой национальности не существует?')
btn_answer1= QRadioButton('Энцы')
btn_answer2= QRadioButton('Смурфы')
btn_answer3= QRadioButton('Чулымцы')
btn_answer4= QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)
qbox = QGroupBox('Варианты ответов')

answer= QPushButton('Ответить')

v_2 = QHBoxLayout()
v_2.addWidget(btn_answer1)
v_2.addWidget(btn_answer3)
v_3 = QHBoxLayout()
v_3.addWidget(btn_answer2)
v_3.addWidget(btn_answer4)

v_4 = QVBoxLayout()
v_4.addWidget(qbox)
v_5=QVBoxLayout()
v_5.addLayout(v_3)
v_5.addLayout(v_2)

qbox.setLayout(v_5)

ans_qbox = QGroupBox('Результат теста')
a=QLabel('Правильно/Неправильно')
b=QLabel("Правильный ответ")
v_6=QVBoxLayout()
v_6.addWidget(a)
v_6.addWidget(b)
ans_qbox.setLayout(v_6)
ans_qbox.hide()


v_1 = QVBoxLayout()
v_1.addWidget(question)
v_1.addLayout(v_4)
v_1.addWidget(ans_qbox)
v_1.addWidget(answer)






def show_question():
    answer.setText('Ответить')
    ans_qbox.hide()
    qbox.show()
    RadioGroup.setExclusive(False)    
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    answer.setText('Следующий вопрос')
    ans_qbox.show()
    qbox.hide()
    


answers =[btn_answer1, btn_answer2, btn_answer3, btn_answer4]





def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    b.setText(q.right_answer)
    show_question()


def show_correct(res):
    a.setText(res)
    show_result()


def next_question():
    main_win.total +=1
    print('Статистика' '\n -Всего вопросов:' +str(main_win.total), '\n -Правильных ответов:' +str(main_win.score) )

    cur_question= randint(0, len(question_list) - 1)
    
    q = question_list[cur_question]
    ask(q)
    
def click_OK():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score +=1 
        print('Статистика' '\n -Всего вопросов:' +str(main_win.total), '\n -Правильных ответов:' +str(main_win.score) )
        print('Рейтинг:' +str(main_win.score/main_win.total*100))
    else:
        show_correct('Неправильно!')
        print('Неверно')
        print('Рейтинг:' +str(main_win.score/main_win.total*100))

       
        

        



main_win.score = 0
main_win.total = 0
answer.clicked.connect(click_OK)
next_question()


main_win.setLayout(v_1)

main_win.show()
app.exec_()




