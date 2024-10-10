package pspunit1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class EjemploError {
public static void main(String[] args) throws IOException {
	//Se ejecuta el cmd y luego finaliza 
	
	Process p=new ProcessBuilder("CMD","/C","DIRR").start();
	
	//Mostramos caracter a caracter la salida generada por DIR
	
	//Leemos lo que el comando escribió en la consola
	InputStream is=p.getInputStream();
	
	int c;
	
	while((c=is.read())!=-1) {
		System.out.print((char)c);
		
	}
	is.close();
	
	
	//Comprobación de error 0 bien y -1 mal
	int exitVal;
	
	try {
		//recoge la salida de Syste.exit()
		exitVal=p.waitFor();
		System.out.println("Valor de salida: "+exitVal);
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
	InputStream er=p.getErrorStream();
	BufferedReader brer=new BufferedReader(new InputStreamReader(er));
	String liner=null;
	
	while((liner=brer.readLine())!=null) {
		System.out.println("ERROR>"+liner);
	}
	
}
}
