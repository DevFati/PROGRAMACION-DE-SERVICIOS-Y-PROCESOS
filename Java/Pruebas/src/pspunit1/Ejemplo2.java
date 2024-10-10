package pspunit1;

import java.io.IOException;
import java.io.InputStream;


public class Ejemplo2 {

	public static void main(String[] args) throws IOException {
		//se ejecuta el cmd y luego finaliza
		
		Process p =new ProcessBuilder("CMD","/C","DIR").start();
		
		//Mostramos caracter a caracter la salida generda por DIR 
		
		//Leemos lo que el comando escribió en la consola 
		InputStream is=p.getInputStream();
		int c;
		
		while((c=is.read())!=-1) {
			System.out.print((char)c);
			
			
		}
		
		is.close();
		
		//Comrobación de error 0 bien y -1 mal 
		int exitVal;
		
		//Recoge la salida de System.exit()
		
		try {
			exitVal=p.waitFor();
			System.out.println("Valor de salida: "+exitVal);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		
	}
}
