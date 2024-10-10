package pspunit1;

import java.io.IOException;

public class EjemploNotepad {

	public static void main(String[] args) throws IOException {
		
		//1º forma 
		//Process pb=new ProcessBuilder("NOTEPAD").start();
		
		//2º forma 
		ProcessBuilder pb=new ProcessBuilder("NOTEPAD");
		Process p=pb.start();
		
		
	}
}
