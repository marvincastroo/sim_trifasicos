"""
Estructuras de Datos Abstractas y Algoritmos para Ingeniería
IE - 0217
Proyecto Simulador de circuitos trifásicos

Marvin Castro Castro C01884
Lorena Solis Extteny B97657
"""
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import numpy as np
#import matlab.engine
import matplotlib.pyplot as plt
import pandas as pd
import calculos as ca


# Inicialización Tkinter
root = Tk()
root.title("Simulador Trif.")
root.geometry("225x150")

# Inicialización etiquetas
index_list = [1, 2, 3]
index_status = Label(root, text="1", bd=1, relief=SUNKEN, anchor=CENTER)
status = Label(root, text="1", bd=1, relief=SUNKEN, anchor=CENTER)
load_quantity = Message(root, text="Seleccione cantidad de cargas:")
display_quantity = Message(root, text="Cantidad de cargas a simular")
blank = Label(root, text="    ", bd=1)

# Acomodar etiquetas
load_quantity.grid(row=1, column=0)
blank.grid(row=1, column=1)
display_quantity.grid(row=2, column=0)

"""
Función que permite cambiar el numero de cargas a +1
(ahora obsoleta)
"""
def forward(index_list):
  global button_forward
  global button_back
  global status

  button_forward = Button(root, text=">>", command=lambda: forward(index_list+1))
  button_back = Button(root, text="<<", command=lambda: back(index_list - 1))
  status = Label(root, text=str(index_list), bd=1, relief=SUNKEN, anchor=CENTER)

  if index_list == 3:
    button_forward = Button(root, text=">>", state=DISABLED)

  button_forward.grid(row=1, column=4)
  button_back.grid(row=1, column=2)
  status.grid(row=2, column=2, columnspan=3, sticky=W + E)
  return index_list

"""
Función que cambia el numero de cargas a -1
(ahora obsoleta)
"""
def back(index_list):
  global button_forward
  global button_back
  global status

  button_forward = Button(root, text=">>", command=lambda: forward(index_list + 1))
  button_back = Button(root, text="<<", command=lambda: back(index_list - 1))

  if index_list == 1:
    button_back = Button(root, text="<<", state=DISABLED)

  status = Label(root, text=str(index_list), bd=1, relief=SUNKEN,anchor=CENTER)
  status.grid(row=2, column=2, columnspan=3, sticky=W + E)
  button_back.grid(row=1, column=2)
  button_forward.grid(row=1, column=4)
  return index_list

"""
Funcion llamada al presionar el botón "OK"
Llama a la clase One_Load
"""
def sender():
  global status
  a = status.cget("text")
  b = int(a)
  if b == 1:
    c = One_Load(root)
  pass

# Inicializacion Botones
button_back = Button(root, text = "<<", command=back, state=DISABLED )
button_exit = Button(root, text = "OK", command=sender)
button_forward = Button(root, text = ">>", command=lambda:forward(2), state=DISABLED)
# Acomodar botones
button_back.grid(row=1, column=2)
button_exit.grid(row=1, column=3)
button_forward.grid(row=1, column=4, pady=10)
index_status.grid(row=2, column=2, columnspan=3, sticky=W+E)


"""
Interfaz principal
"""
class One_Load:

  img_1load = ImageTk.PhotoImage(Image.open("textures//star.jpg"))
  img_2load = ImageTk.PhotoImage(Image.open("textures//delta.jpg"))
  img_3load = ImageTk.PhotoImage(Image.open("textures//star_grounded.jpg"))
  Generador_frame = LabelFrame(root, text="generadores")
  """
  Constructor
  Inicializacion de todos los widgets
  Acomodar widgets
  """
  def __init__(self, master):
    global img_1load
    global Generador_frame
    frame = Frame(master)

    # Se crea ventana "top"
    self.top = Toplevel()
    self.top.title("One_load")

    # Creacion del frame con los widgets del generador
    self.Generador_frame = LabelFrame(self.top, text="Generadores", labelanchor="n")
    self.Generador_frame.grid(row=1, column=1)

    # Etiquetas magnitud de los generadores
    self.generator_magA_label = Label(self.Generador_frame, text="Fase A:")
    self.generator_magB_label = Label(self.Generador_frame, text="Fase B:")
    self.generator_magC_label = Label(self.Generador_frame, text="Fase C:")

    # Entradas de datos de los generadores
    self.entry_genA = Entry(self.Generador_frame, width=5)
    self.entry_genB = Entry(self.Generador_frame, width=5)
    self.entry_genC = Entry(self.Generador_frame, width=5)

    self.blank_space = Label(self.Generador_frame, text="  ")

    # Etiquetas de las fases de los generadores
    self.generator_phaseA_label = Label(self.Generador_frame, text="Ang(AN)")
    self.generator_phaseB_label = Label(self.Generador_frame, text="Ang(BN)")
    self.generator_phaseC_label = Label(self.Generador_frame, text="Ang(CN)")

    # Entrada de las fases de los generadores
    # Establecer ángulos de fase por defecto
    self.entry_genA_phase = Entry(self.Generador_frame, width=5)
    self.entry_genA_phase.insert(END, 0)
    self.entry_genB_phase = Entry(self.Generador_frame, width=5)
    self.entry_genB_phase.insert(END, -120)
    self.entry_genC_phase = Entry(self.Generador_frame, width=5)
    self.entry_genC_phase.insert(END, -240)

    # Creacion de frame para la Carga 1
    self.Load1_frame = LabelFrame(self.top, text="Carga 1", labelanchor="n")
    self.Load1_frame.grid(row=1, column=2)

    # Etiquetas para la Carga 1
    self.Load1A_label = Label(self.Load1_frame, text="Fase A:")
    self.Load1B_label = Label(self.Load1_frame, text="Fase B:")
    self.Load1C_label = Label(self.Load1_frame, text="Fase C:")

    # Entradas para valores de la Carga 1
    self.entry_Load1A = Entry(self.Load1_frame, width=8)
    self.entry_Load1B = Entry(self.Load1_frame, width=8)
    self.entry_Load1C = Entry(self.Load1_frame, width=8)

    self.blank_space2 = Label(self.Load1_frame, text="  ")
    self.blank_space2.grid(row=3, column=3)
    self.blank_space2.grid(row=4, column=3)
    self.blank_space2.grid(row=5, column=3)

    self.var = IntVar()
    self.var.set(1)

    """
     Seleccion: Topologia de estrella o delta por medio de RadioButtons
       IntVar == 1: Circuito con topologia en estrella
       IntVar == 2: Circuito con topologia en delta
    """
    self.radio_star = Radiobutton(self.Load1_frame, text="Estrella", variable=self.var, value=1, command=self.change_to_star)
    self.radio_delta = Radiobutton(self.Load1_frame, text="Delta", variable=self.var, value=2, command=self.change_to_delta)
    self.radio_delta.deselect()
    # self.current_topology = 1 cuando es estrella
    self.current_topology = 1

    """
    Casilla de verificación:
        Balanceo de las fases de la Carga 1
    """
    self.balanced_State = IntVar()
    self.balanced_Checkbox = Checkbutton(self.Load1_frame, text="Carga Balanceada",
                                         variable=self.balanced_State, onvalue=1, offvalue=0, command=self.check_balanced)
    self.balanced_Checkbox.deselect()

    """
    Casilla de verificación:
        Balanceo de las fases de la Carga 1
    """
    self.neutral_State = IntVar()
    self.neutral_Checkbox = Checkbutton(self.Load1_frame, text="Linea de neutro",
                                         variable=self.neutral_State, onvalue=1, offvalue=0, command=self.check_neutral)
    self.neutral_Checkbox.deselect()

    """
    Botón RUN:
        llama la funcion self.get_values que se encarga de empezar la simulación
    """
    self.RUN_button = Button(self.top, text="Simular",padx=30, pady=30, command=self.get_values)

    # Cargar imagenes
    self.img_3load_label = Label(self.top, image=self.img_3load)
    self.img_2load_label = Label(self.top, image=self.img_2load)
    self.img_1load_label = Label(self.top, image=self.img_1load)
    self.img_1load_label.grid(row=0, column=1, columnspan=22)

    """
    Diccionario con localizacion de todos los widgets. 
    """
    self.widgets = {
      # Generadores
      self.generator_magA_label: {"row": 3, "column": 0},
      self.generator_magB_label: {"row": 4, "column": 0},
      self.generator_magC_label: {"row": 5, "column": 0},
      # Entrada generadores
      self.entry_genA: {"row": 3, "column": 2},
      self.entry_genB: {"row": 4, "column": 2},
      self.entry_genC: {"row": 5, "column": 2},
      # Espacios en blanco
      self.blank_space: {"row": 3, "column": 3},
      self.blank_space: {"row": 4, "column": 3},
      self.blank_space: {"row": 5, "column": 3},
      # Fase de generadores
      self.generator_phaseA_label: {"row": 3, "column": 4},
      self.generator_phaseB_label: {"row": 4, "column": 4},
      self.generator_phaseC_label: {"row": 5, "column": 4},
      # Entrada de fase de generadores
      self.entry_genA_phase: {"row": 3, "column": 5},
      self.entry_genB_phase: {"row": 4, "column": 5},
      self.entry_genC_phase: {"row": 5, "column": 5},
      # Etiquetas de Carga 1
      self.Load1A_label: {"row": 3, "column": 0},
      self.Load1B_label: {"row": 4, "column": 0},
      self.Load1C_label: {"row": 5, "column": 0},
      # Entradas de la Carga 1
      self.entry_Load1A: {"row": 3, "column": 2},
      self.entry_Load1B: {"row": 4, "column": 2},
      self.entry_Load1C: {"row": 5, "column": 2},
      # Espacios en blanco
      self.blank_space2: {"row": 3, "column": 3},
      self.blank_space2: {"row": 4, "column": 3},
      self.blank_space2: {"row": 5, "column": 3},
      # Botones de radio
      self.radio_star: {"row": 3, "column": 4, "rowspan": 2},
      self.radio_delta: {"row": 5, "column": 4, "rowspan": 2},
      # Casillas de verificacion
      self.balanced_Checkbox: {"row": 3, "column": 5, "rowspan": 2},
      self.neutral_Checkbox: {"row": 5, "column": 5, "rowspan": 2},
      # Boton Correr
      self.RUN_button: {"row": 1, "column": 3},

    }
    for key, value in self.widgets.items():
      key.grid(value)

  """
  Funcion accionada al presionar el boton de radio "Estrella" 
  Cambia la imagen del circuito a uno en topologia estrella
  cambia el valor de la variable self.current_topology = 1
  """
  def change_to_star(self):
    self.img_2load_label.grid_forget()
    self.img_1load_label.grid(row=0, column=1, columnspan=22)
    self.current_topology = 1
    #print(self.current_topology)

  """
  Funcion accionada al presionar el boton de radio "Delta" 
  Cambia la imagen del circuito a uno en topologia Delta
  cambia el valor de la variable self.current_topology = 2
  """
  def change_to_delta(self):
    self.img_1load_label.grid_forget()
    self.img_2load_label.grid(row=0, column=1, columnspan=22)
    self.current_topology = 2

  """
  Funcion que globaliza las variables del generador y la carga
  Solo se acciona si self.correct_values() es cierto
  """
  def get_values(self):
    condition = self.correct_values()
    if condition == True:
      # creo que hay mejores formas de acceder a estas
      # variables sin tener que hacerlo global, pero bueno
      global V_genA
      global V_genB
      global V_genC
      global V_genA_phase
      global V_genB_phase
      global V_genC_phase
      global Load1A
      global Load1B
      global Load1C
      global current_topology
      global state

      V_genA = self.entry_genA.get()
      V_genB = self.entry_genB.get()
      V_genC = self.entry_genC.get()
      V_genA_phase = self.entry_genA_phase.get()
      V_genB_phase = self.entry_genB_phase.get()
      V_genC_phase = self.entry_genC_phase.get()
      Load1A = self.entry_Load1A.get()
      Load1B = self.entry_Load1B.get()
      Load1C = self.entry_Load1C.get()
      current_topology = self.current_topology
      state = self.neutral_State.get()

      access_values()

  """
  Funcion accionada al marcar la casilla de balanceo
  Hace las entradas de la Fase B, C, iguales a la de la Fase A.
  """
  def check_balanced(self):
    state = self.balanced_State.get()
    if state == 1:
      load = self.entry_Load1A.get()
      try:
        this = complex(load)
        self.entry_Load1B.delete(0, END)
        self.entry_Load1C.delete(0, END)
        self.entry_Load1B.insert(END, load)
        self.entry_Load1C.insert(END, load)
      except:
        pass

    elif state == 0:
      self.entry_Load1B.delete(0, END)
      self.entry_Load1C.delete(0, END)

  """
  Funcion que se acciona al marcar la casilla del neutro
  Si el circuito es estrella, verificar si la casilla está marcada
  Si esta marcada, cambiar circuito estrella con neutro.
  """
  def check_neutral(self):
    if self.current_topology != 2:
      state = self.neutral_State.get()
      if state == 1:
        self.img_1load_label.grid_forget()
        self.img_3load_label.grid(row=0, column=1, columnspan=22)

      elif state == 0:
        self.img_3load_label.grid_forget()
        self.img_1load_label.grid(row=0, column=1, columnspan=22)
    else:
      pass

  """
  Funcion que verifica la validez de los datos
  Es decir, que sean complejos o floats. 
  """
  def correct_values(self):
    voltage_genA = self.entry_genA.get()
    voltage_genB = self.entry_genB.get()
    voltage_genC = self.entry_genC.get()
    phase_genA = self.entry_genA_phase.get()
    phase_genB = self.entry_genB_phase.get()
    phase_genC = self.entry_genC_phase.get()
    condition = 0
    try:
      voltage_genA = float(voltage_genA)
      voltage_genB = float(voltage_genB)
      voltage_genC = float(voltage_genC)
      condition = condition + 1

    except:
      response = messagebox.showerror("Error", "Por favor ingrese "
                                               "únicamente valores numéricos")
    try:
      phase_genA = complex(phase_genA)
      phase_genB = complex(phase_genB)
      phase_genC = complex(phase_genC)
      condition = condition + 1

    except:
      response = messagebox.showerror("Error", "Por favor ingrese "
                                               "únicamente valores numéricos")
    if condition == 2:
      return True
    else:
      return False


"""
Funcion que recoge las variables desde la GUI, importa a MATLAB y realiza 
los calculos aritmeticos
"""
def access_values():
  global V_genA
  global V_genB
  global V_genC
  global V_genA_phase
  global V_genB_phase
  global V_genC_phase
  global Load1A
  global Load1B
  global Load1C
  global current_topology
  global state


  Load1A = complex(Load1A)
  Load1B = complex(Load1B)
  Load1C = complex(Load1C)

  voltages = [V_genA, V_genB, V_genC]
  phases = [V_genA_phase, V_genB_phase, V_genC_phase]
  n = -1

  # Union de la magnitud y la fase de la tension
  for v in voltages:

    n += 1
    v_real = (float(v)) * np.cos(float(phases[n])*np.pi/180)
    v_imag = (float(v)) * np.sin(float(phases[n])*np.pi/180)*1j
    result = (v_real + v_imag)
    voltages[n] = complex(result)

  V_generatorA = voltages[0]
  V_generatorB = voltages[1]
  V_generatorC = voltages[2]

  Load1A = complex(Load1A)
  Load1B = complex(Load1B)
  Load1C = complex(Load1C)

  # IF: topologia = estrella, neutro desactivado
  if current_topology == 1 and state == 0:
    output = ca.star(Load1A, Load1B, Load1C, V_generatorA, V_generatorB, V_generatorC)

  # IF: topologia = delta
  elif current_topology == 2:
    output = ca.delta(Load1A, Load1B, Load1C, V_generatorA, V_generatorB, V_generatorC)
    In = (0.0, 0.0)

  # IF: topologia = estrella, neutro activado
  elif current_topology == 1 and state == 1:
    output = ca.star_grounded(Load1A, Load1B, Load1C, V_generatorA, V_generatorB, V_generatorC)


  VnN = rect2pol(output[0])
  Van = rect2pol(output[1])
  Vbn = rect2pol(output[2])
  Vcn = rect2pol(output[3])
  Ia = rect2pol(output[4])
  Ib = rect2pol(output[5])
  Ic = rect2pol(output[6])
  try:
    In = rect2pol(output[7])
  except:
    pass

  #Tuple formatting, mostrar un solo decimal
  VnN = tuple([float("{0:.1f}".format(n)) for n in VnN])
  Van = tuple([float("{0:.1f}".format(n)) for n in Van])
  Vbn = tuple([float("{0:.1f}".format(n)) for n in Vbn])
  Vcn = tuple([float("{0:.1f}".format(n)) for n in Vcn])
  Ia = tuple([float("{0:.1f}".format(n)) for n in Ia])
  Ib = tuple([float("{0:.1f}".format(n)) for n in Ib])
  Ic = tuple([float("{0:.1f}".format(n)) for n in Ic])
  try:
    In = tuple([float("{0:.1f}".format(n)) for n in In])
  except:
    pass

  print("tension VnN:", VnN)
  print("tension Van", Van)
  print("tension Vbn", Vbn)
  print("tension Vcn", Vcn)
  print("corriente Ia", Ia)
  print("corriente Ib", Ib)
  print("corriente Ic", Ic)
  try:
    print("corriente In", In)
  except:
    pass

  """
  Graficacion de resultados con uso de matplotlib
  """
  # Variables - Frecuencia 60 Hz
  x = np.linspace(0, 0.05, 100)
  f = 60
  omega = 2 * np.pi * f

  # Ondas de la tension para la Carga 1
  wave_Van = Van[0] * np.cos(omega * x + np.deg2rad(Van[1]))
  wave_Vbn = Vbn[0] * np.cos(omega * x + np.deg2rad(Vbn[1]))
  wave_Vcn = Vcn[0] * np.cos(omega * x + np.deg2rad(Vcn[1]))
  wave_Vnn = VnN[0] * np.cos(omega * x + np.deg2rad(VnN[1]))

  plt.plot(x, wave_Van, label='V_an')
  plt.plot(x, wave_Vbn, label='V_bn')
  plt.plot(x, wave_Vcn, label='V_cn')
  plt.plot(x, wave_Vnn, label='V_nN')
  plt.xlabel('Tiempo (s)')
  plt.ylabel('Tension (V)')
  plt.legend()
  plt.show()

  # Ondas de la corriente para la Carga 1
  wave_Ia = Ia[0] * np.cos(omega * x + np.deg2rad(Ia[1]))
  wave_Ib = Ib[0] * np.cos(omega * x + np.deg2rad(Ib[1]))
  wave_Ic = Ic[0] * np.cos(omega * x + np.deg2rad(Ic[1]))
  wave_In = In[0] * np.cos(omega * x + np.deg2rad(In[1]))


  plt.plot(x, wave_Ia, label='Ia')
  plt.plot(x, wave_Ib, label='Ib')
  plt.plot(x, wave_Ic, label='Ic')
  plt.plot(x, wave_In, label='In')
  plt.xlabel('Tiempo (s)')
  plt.ylabel('Corriente (A)')
  plt.legend()
  plt.show()

  # Diccionario para presentar la informacion por medio de un dataframe
  d = {'Generador(V)': [V_genA, V_genB, V_genC], 'Fase Generador ': [V_genA_phase, V_genB_phase, V_genC_phase],
          'Corriente (A)':["Ia = " + str(Ia), "Ib = " + str(Ib), "Ic = " + str(Ic)],
       'Tension (V)':["Van = " + str(Van), "Vbn = " + str(Vbn), "Vcn = " + str(Vcn)]}

  fig, ax = plt.subplots()
  fig.patch.set_visible(False)
  ax.axis('off')
  ax.axis('tight')
  df = pd.DataFrame(data=d)
  df.round(2)

  # Inicializacion de tabla con uso de matplotlib
  the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
  the_table.auto_set_font_size(False)
  the_table.set_fontsize(6)
  the_table.scale(1.5, 1.5)
  fig.tight_layout()

  plt.show()

def rect2pol(z):
  mag = np.abs(z)
  rads = np.angle(z)
  degs = np.rad2deg(rads)
  return mag, degs

root.mainloop()

