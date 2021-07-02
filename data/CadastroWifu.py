from PyQt5  import uic,QtWidgets

def main_fun () :
    # Pegando texto dos campos
    nome = formulario.lname.text()
    tags = formulario.ltags.text() 
    descricao = formulario.ldescribe.text()
    radialB = [formulario.rf,formulario.rm,formulario.rcatAnime,formulario.rcatManga,formulario.rcatVtube,
        formulario.rcatFilme,formulario.rcatCantor,formulario.rcatGame]
    for v in radialB  :
        v.isChecked() == True and print(v.text()+" é verdadeiro") or (v.text()+" é falso")






app=QtWidgets.QApplication([])
formulario = uic.loadUi("cadastro-wifu.ui")
formulario.bsubmit.clicked.connect(main_fun)  

formulario.show()
app.exec()



