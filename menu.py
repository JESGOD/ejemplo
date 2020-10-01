from calculadora import Calculadora


class Menu:

    def Iniciar_menu(self):

        opcion = 0
        self.calculadora1 = Calculadora()


        while opcion != 5:

            print("\n  por favor ingrese una opcion: \n")
            print("          1: sumar \n"
                  "          2: restar \n"
                  "          3: multiplicar \n"
                  "          4: dividir \n"
                  "          5: salir \n")
            try:

                opcion = int(input())
                if opcion == 1:
                    self.calculadora1.suma()
                elif opcion == 2:
                    self.calculadora1.resta()

                elif opcion == 3:
                    self.calculadora1.producto()
                else:
                    if opcion == 4:
                        self.calculadora1.division()
            except ValueError:
                print("\n**********opcion invalida**********\n")
