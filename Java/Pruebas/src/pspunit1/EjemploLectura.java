package pspunit1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//Lee una cadena desde la entrada estándar y la visualiza 
public class EjemploLectura {

	public static void main(String[] args) {
		
		//Bytes 
		InputStreamReader in=new InputStreamReader(System.in);
		//Caracteres 
		BufferedReader br=new BufferedReader(in);
		String texto;
		
		
		try {
			System.out.println("Introduce una cadena: ");
			texto=br.readLine();
			System.out.println("La cadena escrita es: "+texto);
			in.close();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}
}
