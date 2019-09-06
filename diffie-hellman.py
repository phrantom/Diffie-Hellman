from Crypto.Util.number import getPrime
from random import randint
""""
 Sistema de intercambio de claves de cifrado Diffie-Hellman

 autores: 	Whitfield Diffie
			Martin Hellman

 Se emplea generalmente como medio para acordar claves simetricas 
 que seran empleadas para el cifrado de una sesion 
 (establecer clave de sesion).
"""

print ("""
#########################################################################################	
#                                                                                       #        
#                                  GENERADOR DE CLAVES                                  #
#                                   DIFFIE - HELLMAN                                    #
#                                                                                       #
#########################################################################################
             """)


generador = 2 							# Este es el generador 
nroPrimo = getPrime(1024) 				# asignamos un nro primo

print ("Generador :", +generador)
print ("Nro primo : ", + nroPrimo)

# estos nros privados son aleatorios mayor 0 y menores que el el numero primo generado
a = randint(nroPrimo/2,nroPrimo-1)		# nro privado para el usuario a,
b = randint(nroPrimo/2,nroPrimo-1)		# nro privado para el usuario b

# nro publico, este numero se comparten entre cada uno
A = pow(generador,a,nroPrimo) 	# generador ** a % nroPrimo
B = pow(generador,b,nroPrimo) 	# generador ** b % nroPrimo


#SHARED SECRET 	
S_A = pow(B,a,nroPrimo)		# la funcion pow estaria realizando :  B ** a % nroPrimo 
S_B = pow(A,b,nroPrimo)		# la funcion pow estaria realizando :  A ** b % nroPrimo

assert(S_A == S_B)

print ("\nNro publico de A : ",+ A)
print ("Nro publico de B : ", + B) 

print ("\nShared secret A: ", + S_A)
print ("Shared secret B: ", + S_B)

"""

Paso 1) El usuario "a" le tiene que enviar al usuario "b":

		"generador", "nroPrimo" y "A" (nro publico)

Paso 2) El usuario "b" le envia al usuario "a":
		
		"B" (nro publico)

Paso 3) Cada uno calcula el shared secret y obtienen la misma llave :-D

	
"""