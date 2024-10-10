package pspunit1;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;

public class Ejemplo4 {
public static void main(String[] args) throws IOException {
	
	Process p=new ProcessBuilder("CMD","/C","DATE").start();
	
	//Escritura: Enviar la nueva fecha a date
	
	OutputStream os=p.getOutputStream();
	os.write("06/15/2018".getBytes());
	os.flush();
	
	//Lectura: Obtener la salida de Date
	
	InputStream is=p.getInputStream();
	int c;
	while((c=is.read())!=-1) {
		System.out.println((char)c);
	}
	is.close();
	
	int exitVal;
	
	try {
		exitVal=p.waitFor();
		System.out.println("Valor de salida: "+exitVal);
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
}
}
