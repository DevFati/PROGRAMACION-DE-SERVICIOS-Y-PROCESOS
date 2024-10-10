package pspunit1;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Ejemplo6 {
public static void main(String[] args) {
	 
	ProcessBuilder test=new ProcessBuilder();
	//environment devuelve las variables de entorno
	Map entorno=test.environment();
	System.out.println("Variables de entorno: ");
	System.out.println(entorno);
	
	test=new ProcessBuilder("java","Hola","Fatima");
	//Command devuelve los argumentos del proceso test
	List l=test.command();
	Iterator iter=l.iterator();
	System.out.println("Los argumentos del comando son: ");
	
	while(iter.hasNext()) {
		System.out.println(iter.next());
	}
	
	//command con parámetros define un nuevo proceso y sus argumentos 
	test.command("CMD","/C","DIR");
	
	try {
		Process p=test.start();
		//Leemos lo que el comando escribió en la consola. 
		InputStream is=p.getInputStream();
		int c;
		while((c=is.read())!=-1) {
			System.out.println((char)c);
		}
		is.close();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	
	
	
}
}
