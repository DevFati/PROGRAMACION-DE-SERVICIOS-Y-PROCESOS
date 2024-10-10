package pspunit1;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;

public class Ejemplo5 {
public static void main(String[] args) throws IOException {
	
	File directorio=new File(".\\bin");
	
	ProcessBuilder pb=new ProcessBuilder("java","pspunit1.EjemploLectura");
	pb.directory(directorio);
	String w=System.getProperty("user.dir");
	System.out.println("Mi ruta es: "+w);
	Process p=pb.start();
	
	//Escritura
	OutputStream os=p.getOutputStream();
	os.write("Hola Fatima\n".getBytes());
	os.flush();
	
	//LEER STREAM DE ERRORES 
	try {
		InputStream er=p.getErrorStream();
		BufferedReader brer=new BufferedReader(new InputStreamReader(er));
		String liner=null;
		
		while((liner=brer.readLine())!=null) {
			System.out.println("ERROR>"+liner);
		}
	}catch(IOException ioe) {
		ioe.printStackTrace();
	}
	
	
	
	//LEER STREAM DE ENTRADA 
	
	try {
		InputStream er=p.getInputStream();
		BufferedReader brer=new BufferedReader(new InputStreamReader(er));
		String liner=null;
		
		while((liner=brer.readLine())!=null) {
			System.out.println("BIEEEEEEEEEEEEEEN!>"+liner);
		
	}
	}catch(

	IOException ioe)
	{
		ioe.printStackTrace();
	}

}}
