package pspunit1;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;

public class Ejemplo3 {
public static void main(String[] args) throws IOException {
	
	//En primer lugar mostramos donde nos encontramos 
	String w= System.getProperty("user.dir");
	System.out.println("Mi ruta es: "+w);
	//Creamos el ojeto File con el directorio donde está Ejemplo2.class
	File directorio=new File(".\\bin");
	//Si hay un package el nombre del .class es package.clase
	ProcessBuilder pb=new ProcessBuilder("java","pspunit1.Ejemplo2");
	
	pb.directory(directorio);
	
	System.out.printf("El directorio de trabajo es: %s%n ",pb.directory());
	Process p=pb.start();
	
	InputStream is=p.getInputStream();
	int c;
	while((c=is.read())!=-1) {
		System.out.print((char)c);
		
	}
	is.close();
	
}
}
